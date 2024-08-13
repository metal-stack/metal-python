# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.33.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.switch_api import SwitchApi  # noqa: E501
from metal_python.rest import ApiException


class TestSwitchApi(unittest.TestCase):
    """SwitchApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.switch_api.SwitchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_switch(self):
        """Test case for delete_switch

        deletes an switch and returns the deleted entity  # noqa: E501
        """
        pass

    def test_find_switch(self):
        """Test case for find_switch

        get switch by id  # noqa: E501
        """
        pass

    def test_find_switches(self):
        """Test case for find_switches

        get all switches that match given properties  # noqa: E501
        """
        pass

    def test_list_switches(self):
        """Test case for list_switches

        get all switches  # noqa: E501
        """
        pass

    def test_notify_switch(self):
        """Test case for notify_switch

        notify the metal-api about a configuration change of a switch  # noqa: E501
        """
        pass

    def test_register_switch(self):
        """Test case for register_switch

        register a switch  # noqa: E501
        """
        pass

    def test_toggle_switch_port(self):
        """Test case for toggle_switch_port

        toggles the port of the switch with a nicname to the given state  # noqa: E501
        """
        pass

    def test_update_switch(self):
        """Test case for update_switch

        updates a switch. if the switch was changed since this one was read, a conflict is returned  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
