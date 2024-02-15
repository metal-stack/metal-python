# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.27.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.ip_api import IpApi  # noqa: E501
from metal_python.rest import ApiException


class TestIpApi(unittest.TestCase):
    """IpApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.ip_api.IpApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_allocate_ip(self):
        """Test case for allocate_ip

        allocate an ip in the given network.  # noqa: E501
        """
        pass

    def test_allocate_specific_ip(self):
        """Test case for allocate_specific_ip

        allocate a specific ip in the given network.  # noqa: E501
        """
        pass

    def test_find_i_ps(self):
        """Test case for find_i_ps

        get all ips that match given properties  # noqa: E501
        """
        pass

    def test_find_ip(self):
        """Test case for find_ip

        get ip by id  # noqa: E501
        """
        pass

    def test_free_ip(self):
        """Test case for free_ip

        frees an ip  # noqa: E501
        """
        pass

    def test_free_ip_deprecated(self):
        """Test case for free_ip_deprecated

        frees an ip  # noqa: E501
        """
        pass

    def test_list_i_ps(self):
        """Test case for list_i_ps

        get all ips  # noqa: E501
        """
        pass

    def test_update_ip(self):
        """Test case for update_ip

        updates an ip. if the ip was changed since this one was read, a conflict is returned  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
