# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.39.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.machine_api import MachineApi  # noqa: E501
from metal_python.rest import ApiException


class TestMachineApi(unittest.TestCase):
    """MachineApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.machine_api.MachineApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_allocate_machine(self):
        """Test case for allocate_machine

        allocate a machine  # noqa: E501
        """
        pass

    def test_chassis_identify_led_off(self):
        """Test case for chassis_identify_led_off

        sends a power-off to the chassis identify LED  # noqa: E501
        """
        pass

    def test_chassis_identify_led_on(self):
        """Test case for chassis_identify_led_on

        sends a power-on to the chassis identify LED  # noqa: E501
        """
        pass

    def test_delete_machine(self):
        """Test case for delete_machine

        deletes a machine from the database  # noqa: E501
        """
        pass

    def test_find_ipmi_machine(self):
        """Test case for find_ipmi_machine

        returns a machine including the ipmi connection data  # noqa: E501
        """
        pass

    def test_find_ipmi_machines(self):
        """Test case for find_ipmi_machines

        returns machines including the ipmi connection data  # noqa: E501
        """
        pass

    def test_find_machine(self):
        """Test case for find_machine

        get machine by id  # noqa: E501
        """
        pass

    def test_find_machines(self):
        """Test case for find_machines

        find machines by multiple criteria  # noqa: E501
        """
        pass

    def test_free_machine(self):
        """Test case for free_machine

        free a machine  # noqa: E501
        """
        pass

    def test_get_machine_console_password(self):
        """Test case for get_machine_console_password

        get consolepassword for machine by id  # noqa: E501
        """
        pass

    def test_ipmi_report(self):
        """Test case for ipmi_report

        reports IPMI ip addresses leased by a management server for machines  # noqa: E501
        """
        pass

    def test_issues(self):
        """Test case for issues

        returns machine issues  # noqa: E501
        """
        pass

    def test_list_issues(self):
        """Test case for list_issues

        returns the list of issues that exist in the API  # noqa: E501
        """
        pass

    def test_list_machines(self):
        """Test case for list_machines

        get all known machines  # noqa: E501
        """
        pass

    def test_machine_bios(self):
        """Test case for machine_bios

        boots machine into BIOS  # noqa: E501
        """
        pass

    def test_machine_cycle(self):
        """Test case for machine_cycle

        sends a power cycle to the machine  # noqa: E501
        """
        pass

    def test_machine_disk(self):
        """Test case for machine_disk

        boots machine from disk  # noqa: E501
        """
        pass

    def test_machine_off(self):
        """Test case for machine_off

        sends a power-off to the machine  # noqa: E501
        """
        pass

    def test_machine_on(self):
        """Test case for machine_on

        sends a power-on to the machine  # noqa: E501
        """
        pass

    def test_machine_pxe(self):
        """Test case for machine_pxe

        boots machine from PXE  # noqa: E501
        """
        pass

    def test_machine_reset(self):
        """Test case for machine_reset

        sends a reset to the machine  # noqa: E501
        """
        pass

    def test_reinstall_machine(self):
        """Test case for reinstall_machine

        reinstall this machine  # noqa: E501
        """
        pass

    def test_set_machine_state(self):
        """Test case for set_machine_state

        set the state of a machine  # noqa: E501
        """
        pass

    def test_update_firmware(self):
        """Test case for update_firmware

        sends a firmware command to the machine  # noqa: E501
        """
        pass

    def test_update_machine(self):
        """Test case for update_machine

        updates a machine. if the machine was changed since this one was read, a conflict is returned  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
