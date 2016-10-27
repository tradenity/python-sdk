import requests


from ..exceptions import *
from ..exceptions import errors
from token_holder import AuthTokenHolder

AUTH_TOKEN_HEADER_NAME = "X-Tradenity-Session-ID"


class HttpClient(object):
    INSTANCE = None

    def __init__(self, key, auth_token_holder):
        if key is None:
            raise ClientErrorException(message="API Key can't be None.")
        if auth_token_holder is None or not issubclass(auth_token_holder, AuthTokenHolder):
            raise ClientErrorException(message="Authentication token holder must be a subclass of AuthTokenHolder.")
        self.key = key
        self.auth_token_holder = auth_token_holder()

    def reset_session(self):
        self.auth_token_holder.reset()

    def http_op(self, op, url, data):
        kwargs = {}
        if self.auth_token_holder.token is None:
            auth = (self.key, "")
            kwargs["auth"] = auth
        else:
            headers = {AUTH_TOKEN_HEADER_NAME: self.auth_token_holder.token}
            kwargs["headers"] = headers

        print url
        if op == "GET":
            if data:
                kwargs["params"] = data
            result = requests.get(url, **kwargs)
        elif op == "POST":
            if data:
                kwargs["data"] = data
            result = requests.post(url, **kwargs)
        elif op == "PUT":
            if data:
                kwargs["data"] = data
            result = requests.put(url, **kwargs)
        elif op == "DELETE":
            result = requests.delete(url, **kwargs)
        else:
            raise ValueError("HTTP operation not supported: "+ op)

        if AUTH_TOKEN_HEADER_NAME in result.headers:
            self.auth_token_holder.token = result.headers[AUTH_TOKEN_HEADER_NAME]

        if result.status_code >= 400:
            self.handle_error(result)
        else:
            return result

    def get(self, url, data=None):
        return self.http_op("GET", url, data)

    def post(self, url, data=None):
        return self.http_op("POST", url, data)

    def put(self, url, data=None):
        return self.http_op("PUT", url, data)

    def delete(self, url):
        return self.http_op("DELETE", url, {})

    def handle_error(self, result):
        if result.status_code >= 500:
            raise ServerErrorException()
        elif result.status_code == 400:
            error = result.json()
            if error.get('errorCode') == errors.DATA_VALIDATION_ERROR_CODE:
                raise DataValidationException(error)
            elif error.get('errorCode') in [errors.INVALID_PAYMENT_ERROR_CODE, errors.GATEWAY_ERROR_ERROR_CODE, errors.REFUND_ERROR_ERROR_CODE]:
                raise PaymentErrorException(error)
            elif error.get('errorCode') in [errors.EXISTING_USERNAME_ERROR_CODE, errors.EXISTING_EMAIL_ERROR_CODE]:
                raise CustomerCreationException(error)
            elif error.get('errorCode') == errors.CART_INVALID_ITEM_ERROR_CODE:
                raise ShoppingCartException(error)
            elif error.get('errorCode') in [errors.INVENTORY_INVALID_PRODUCT_ERROR_CODE, errors.INVENTORY_NOT_AVAILABLE_PRODUCT_ERROR_CODE]:
                raise InventoryErrorException(error)
            else:
                raise RequestErrorException(error)
        elif result.status_code == 401:
            if self.auth_token_holder.token is None:
                raise AuthenticationException(result.json())
            else:
                raise SessionExpiredException(result.json())
        elif result.status_code == 403:
            raise AuthorizationException(result.json())
        elif result.status_code == 404:
            raise EntityNotFoundException(result.json())





