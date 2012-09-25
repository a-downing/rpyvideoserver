import json

import cherrypy

def rpc_enable(session_check=True, login_check=True):
    def wrapper(f):
        f.rpc_enable = True
        f.rpc_session_check = session_check
        f.rpc_login_check = login_check
        return f

    return wrapper


def rpc_return(success, data, session=None):
    if session == None:
        return json.dumps({'rpc_status': True, 'return_value': {'success': success, 'data': data}})
    else:
        return json.dumps({'rpc_status': True, 'session': session, 'return_value': {'success': success, 'data': data}})
