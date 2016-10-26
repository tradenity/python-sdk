from tradenity.sdk.http import HttpClient, AuthTokenHolder


class Tradenity(object):
    END_POINT = 'https://api.tradenity.com/v1'
    API_KEY = None
    TOKEN_HOLDER = None
    INSTANCE = None

    @classmethod
    def initialize(cls, key=None, auth_token_holder=AuthTokenHolder):
        if cls.INSTANCE is None:
            cls.INSTANCE = HttpClient(key=key, auth_token_holder=auth_token_holder)

    @classmethod
    def get_client(cls):
        if cls.INSTANCE is None:
            cls.initialize(key=cls.API_KEY, auth_token_holder=cls.TOKEN_HOLDER)
        return cls.INSTANCE
