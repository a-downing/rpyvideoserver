import hashlib

import rpc_utils
from server_config import config

class RPCGeneral:
    @rpc_utils.rpc_enable(
        session_check=False,
        login_check=False
    )
    def login(self, password, **kwargs):
        session = kwargs['session']

        password_hash = hashlib.sha256(password).hexdigest()

        if password_hash != config['password_hash']:
            return rpc_utils.rpc_return(True, False)
        
        session_id = session.startSession()
        session.logIn(True)

        return rpc_utils.rpc_return(True, True, session=session_id)


    @rpc_utils.rpc_enable(
        session_check=False,
        login_check=False
    )
    def logout(self, **kwargs):
        session = kwargs['session']
        session.clear();

        return rpc_utils.rpc_return(True, None)

    @rpc_utils.rpc_enable(
        session_check=False,
        login_check=False
    )
    def status(self, **kwargs):
        session = kwargs['session']
        if session.exists() and session.loggedIn():
            return rpc_utils.rpc_return(True, True)
        else:
            return rpc_utils.rpc_return(True, False)
        