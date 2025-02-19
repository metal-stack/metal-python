# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.40.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.user_api import UserApi  # noqa: E501
from metal_python.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_me(self):
        """Test case for get_me

        extract the connecting user from auth header  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
