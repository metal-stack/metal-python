# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.22.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.vpn_api import VpnApi  # noqa: E501
from metal_python.rest import ApiException


class TestVpnApi(unittest.TestCase):
    """VpnApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.vpn_api.VpnApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_vpn_auth_key(self):
        """Test case for get_vpn_auth_key

        create auth key to connect to project's VPN  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
