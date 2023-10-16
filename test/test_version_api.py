# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.24.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.version_api import VersionApi  # noqa: E501
from metal_python.rest import ApiException


class TestVersionApi(unittest.TestCase):
    """VersionApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.version_api.VersionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_info(self):
        """Test case for info

        returns the current version information of this module  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
