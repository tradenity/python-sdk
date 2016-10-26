from booby import Model, fields


class ClientErrorException(Exception):
    def __init__(self, message=None, original=None):
        self.message = message
        self.original = original

    def __str__(self):
        if self.message is not None:
            return self.message
        elif self.original is not None:
            return repr(self.original)
        else:
            return "Client error."


class ServerErrorException(Exception):
    def __str__(self):
        return "Server error, please try again later, if the problem persist contact the system administrator"


class ErrorMessage(Model):
    status = fields.Integer()
    errorCode = fields.Integer()
    error = fields.String()
    timestamp = fields.String()
    message = fields.String()
    details = fields.List() # this is a dict
    fieldErrors = fields.List() # this is a dict


class RequestErrorException(Exception):
    def __init__(self, err_message):
        self.message = ErrorMessage(**err_message)

    def __str__(self):
        return "{code}: {msg}".format(code=self.errorCode, msg=self.message)


class AuthenticationException(RequestErrorException):
    pass


class AuthorizationException(RequestErrorException):
    pass


class EntityNotFoundException(RequestErrorException):
    pass


class DataValidationException(RequestErrorException):
    pass


class PaymentErrorException(RequestErrorException):
    pass


class CustomerCreationException(RequestErrorException):
    pass


class ShoppingCartException(RequestErrorException):
    pass


class InventoryErrorException(RequestErrorException):
    pass





