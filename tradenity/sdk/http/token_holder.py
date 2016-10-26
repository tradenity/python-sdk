class AuthTokenHolder(object):
    def __init__(self):
        self._token = None

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    def reset(self):
        self._token = None
