from metal_python.api_client import ApiClient
from metal_python.configuration import Configuration
from mock import MagicMock
import hmac
from hashlib import sha256
import random
from datetime import datetime


class Driver:
    HMAC_ENCODING = "utf-8"
    SALT_LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, url, bearer, hmac_key):
        if hmac_key:
            config = Configuration()
            config.host = url
            c = ApiClient(configuration=config)
            interceptor = MagicMock(wraps=c)

            def auth(*args, **kwargs):
                method = args[1]
                t = datetime.utcnow().isoformat().split(".")[0] + "Z"
                salt = self.random_string()
                msg = bytes(t, Driver.HMAC_ENCODING) + bytes(method, Driver.HMAC_ENCODING) + bytes(salt,
                                                                                                   Driver.HMAC_ENCODING)
                signature = hmac.new(key=bytes(hmac_key, Driver.HMAC_ENCODING), msg=msg, digestmod=sha256).hexdigest()

                c.set_default_header("X-Data-Salt", salt)
                c.set_default_header("X-Date", t)
                c.set_default_header("Authorization", "Metal-Admin " + signature)

                return c.call_api(*args, **kwargs)

            interceptor.call_api.side_effect = auth
            interceptor.update_params_for_auth = None

            self.client = interceptor
        elif bearer:
            raise NotImplementedError("jwt bearer token auth not yet supported")
        else:
            raise RuntimeError("either hmac_key or bearer must be provided")

    @staticmethod
    def random_string(length=24):
        return ''.join(random.choice(Driver.SALT_LETTERS) for _ in range(length))
