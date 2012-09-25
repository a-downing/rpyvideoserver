#!/usr/bin/env python2

import os
import sys
import json
import traceback
import daemon

import cherrypy

# rpyvideoserver configuration file
from server_config import config
import rpc_utils
import rpc_videoserver
import rpc_general
from sessionhandler import SessionHandler, Session

class VideoServer:
    def __init__(self):
        os.chdir(config['run_dir'])

        self.session_handler = SessionHandler()

        self.rpc_handlers = {
            'RPCVideoServer': rpc_videoserver.RPCVideoServer(),
            'RPCGeneral': rpc_general.RPCGeneral()
        }

    @cherrypy.expose
    def files(self, **keywords):
        """ handler for documents """
        content = ''

        if 'file' in keywords:
            filename = keywords['file']
            filename.replace('..', '')

            if filename.endswith('.js'):
                cherrypy.response.headers['Content-Type'] = "text/javascript"
            elif filename.endswith('.css'):
                cherrypy.response.headers['Content-Type'] = "text/css"

            with open('www/' + filename, 'r') as f:
                content = f.read()

        return content

    @cherrypy.expose
    def index(self, **keywords):
        """ handler for index """

        content = ''
        with open('www/index.html', 'r') as f:
            content = f.read()

        return content


    @cherrypy.expose
    def rpc(self, **keywords):
        """ handler for RPC requests """

        cherrypy.response.headers['Content-Type'] = "application/json"

        if 'request' in keywords:
            try:
                #print(keywords['request'])
                request = json.loads(keywords['request'])
                session_id = request['session']
                class_name = request['call']['class']
                method_name = request['call']['method']
                method_args = request['call']['args']

                if class_name in self.rpc_handlers:
                    handler = self.rpc_handlers[class_name]
                    method = getattr(handler, method_name)


                    if callable(method):
                        session = Session(self.session_handler, session_id)
                        if session.exists():
                            session.updateActivity()

                        if getattr(method, 'rpc_enable', False) == False:
                            return json.dumps({'rpc_status': False, 'rpc_fail_msg': 'Not an RPC method.'})

                        if getattr(method, 'rpc_session_check', True) == True:
                            if session.exists() == False:
                                return json.dumps({'rpc_status': False, 'rpc_fail_msg': 'Invalid session.'})

                        if getattr(method, 'rpc_login_check', True) == True:
                            if session.loggedIn() == False:
                                return josn.dumps({'rpc_status': False, 'rpc_fail_msg': 'You must be Logged in to call this RPC method.'})

                        if len(method_args) > 0:
                            return method(*method_args, **{'session' : session})
                        else:
                            return method(**{'session' : session})
            except:
                return json.dumps({'rpc_status': False, 'rpc_fail_msg': traceback.format_exc()})

def main(argc, argv):
    server_config = {
        'server.socket_host': config['http_ip'],
        'server.socket_port': config['http_port'],
    }

    cherrypy.config.update(server_config)

    if argc > 1 and argv[1] == '--daemonize':
        with daemon.DaemonContext():
            cherrypy.quickstart(VideoServer())
    else:
        cherrypy.quickstart(VideoServer())


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
    
