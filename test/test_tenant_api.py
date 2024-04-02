# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.28.3
    
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

    def test_create_tenant(self):
        """Test case for create_tenant

        create a tenant. if the given ID already exists a conflict is returned  # noqa: E501
        """
        pass

    def test_delete_tenant(self):
        """Test case for delete_tenant

        deletes a tenant and returns the deleted entity  # noqa: E501
        """
        pass

    def test_find_tenants(self):
        """Test case for find_tenants

        get all tenants that match given properties  # noqa: E501
        """
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

    def test_update_tenant(self):
        """Test case for update_tenant

        update a tenant. optimistic lock error can occur.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
