class AuthFailedException(Exception):
    """
    Login verification exception class
    ...
    Attributes:
        :param message : the exception detail message
        :param code : the code of response

    """

    def __init__(self, code, message="the cookie may expired"):
        self.message = message
        self.code = code
        super().__init__(self.message)

    def __str__(self):
        return f"{self.code} --> {self.message}"


class UrlISNoneException(Exception):
    """
    check whether request url is None
    ...
    Attributes:
        :param message : the exception detail message

    """

    def __init__(self, message="url is None"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


if __name__ == '__main__':
    code = 1001
    try:
        if code == 10011:
            raise AuthFailedException(code)
    except AuthFailedException as e:
        print(e)
    raise UrlISNoneException


