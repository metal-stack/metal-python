import hmac
import random
import wrapt
import os

from hashlib import sha256
from datetime import datetime

from metal_python.api_client import ApiClient
from metal_python.configuration import Configuration


class Driver:
    HMAC_BYTES_ENCODING = "utf-8"
    SALT_LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, url, bearer, hmac_key, hmac_user="Metal-Admin"):
        self.config = Configuration()
        self.config.host = url

        if os.environ.get("HTTPS_PROXY"):
            self.config.proxy = os.environ.get("HTTPS_PROXY")

        if bearer:
            self.config.api_key["Authorization"] = bearer
            self.config.api_key_prefix["Authorization"] = "Bearer"
            self.client = ApiClient(configuration=self.config)

        elif hmac_key:
            self.client = ApiClient(configuration=self.config)

            # unfortunately, the generated swagger client does not allow adding specific authorization headers
            # dynamically before a request (it only allows refreshing the auth token, but for calculating the token
            # we also need the request method, which is not passed into the refresh function callback)
            # therefore, we wrap the client and intercept the request method and add headers this way
            class RequestWrapper(wrapt.ObjectProxy):
                def __call__(self, method, u, **kwargs):
                    t = datetime.utcnow().isoformat().split(".")[0] + "Z"
                    salt = Driver.random_string()

                    key = bytes(hmac_key, Driver.HMAC_BYTES_ENCODING)
                    msg = bytes(t + method + salt, Driver.HMAC_BYTES_ENCODING)
                    signature = hmac.new(key=key, msg=msg, digestmod=sha256).hexdigest()

                    current_headers = kwargs.get("headers", dict())
                    auth_headers = {
                        "X-Data-Salt": salt,
                        "X-Date": t,
                        "Authorization": hmac_user + " " + signature,
                    }
                    kwargs["headers"] = {**current_headers, **auth_headers}

                    return self.__wrapped__(method, u, **kwargs)

            self.client.request = RequestWrapper(self.client.request)

        else:
            raise RuntimeError("either hmac_key or bearer must be provided")

    @staticmethod
    def random_string(length=24):
        return ''.join(random.choice(Driver.SALT_LETTERS) for _ in range(length))
