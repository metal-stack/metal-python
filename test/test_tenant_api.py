# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.15.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.tenant_api import TenantApi  # noqa: E501
from metal_python.rest import ApiException


class TestTenantApi(unittest.TestCase):
    """TenantApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.tenant_api.TenantApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_tenant(self):
        """Test case for get_tenant

        get tenant by id  # noqa: E501
        """
        pass

    def test_list_tenants(self):
        """Test case for list_tenants

        get all tenants  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
