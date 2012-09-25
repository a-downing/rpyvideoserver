import threading
import random
import string
import time

class SessionHandler:
    def __init__(self):
        self.sessions = {}

    def generateSessionId(self):
        while True:
            session_id = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(64))
            if session_id not in self.sessions: # just in case, will never be false
                break

        return session_id

    def startSession(self):
        lock = threading.Lock()
        lock.acquire()
        session_id = self.generateSessionId()
        self.sessions[session_id] = {'last_activity' : time.time(), 'logged_in' : False, 'data' : None}
        lock.release()
        return session_id

    def getSession(self, sess):
        if sess in self.sessions:
            return self.sessions[sess]
        else:
            return None

    def sessionExists(self, sess):
        if sess in self.sessions:
            return True
        else:
            return False

    def clearSession(self, sess):
        del self.sessions[sess]

    def updateActivity(self, sess):
        self.sessions[sess]['last_activity'] = time.time()

class Session:
    def __init__(self, handler, session_id):
        self.handler = handler
        self.session_id = session_id

    def exists(self):
        return self.handler.sessionExists(self.session_id)

    def getSessionId(self):
        return self.session_id

    def getSessionData(self):
        return self.handler.getSession(self.session_id)

    def updateActivity(self):
        self.handler.sessions[self.session_id]['last_activity'] = time.time()

    def loggedIn(self):
        if self.handler.sessions[self.session_id]['logged_in'] == True:
            return True
        else:
            return False

    def startSession(self):
        self.session_id = self.handler.startSession()
        return self.session_id

    def logIn(self, status):
        self.handler.sessions[self.session_id]['logged_in'] = status

    def clear(self):
        self.handler.clearSession(self.session_id)