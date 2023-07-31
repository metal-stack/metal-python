# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.22.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.firewall_api import FirewallApi  # noqa: E501
from metal_python.rest import ApiException


class TestFirewallApi(unittest.TestCase):
    """FirewallApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.firewall_api.FirewallApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_allocate_firewall(self):
        """Test case for allocate_firewall

        allocate a firewall  # noqa: E501
        """
        pass

    def test_find_firewall(self):
        """Test case for find_firewall

        get firewall by id  # noqa: E501
        """
        pass

    def test_find_firewalls(self):
        """Test case for find_firewalls

        find firewalls by multiple criteria  # noqa: E501
        """
        pass

    def test_list_firewalls(self):
        """Test case for list_firewalls

        get all known firewalls  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
