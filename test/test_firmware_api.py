# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.21.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.firmware_api import FirmwareApi  # noqa: E501
from metal_python.rest import ApiException


class TestFirmwareApi(unittest.TestCase):
    """FirmwareApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.firmware_api.FirmwareApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_firmwares(self):
        """Test case for list_firmwares

        returns all firmwares (for a specific machine)  # noqa: E501
        """
        pass

    def test_remove_firmware(self):
        """Test case for remove_firmware

        remove given firmware  # noqa: E501
        """
        pass

    def test_upload_firmware(self):
        """Test case for upload_firmware

        upload given firmware  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
