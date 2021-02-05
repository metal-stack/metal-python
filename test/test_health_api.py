# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.12.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.health_api import HealthApi  # noqa: E501
from metal_python.rest import ApiException


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.health_api.HealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_health(self):
        """Test case for health

        perform a healthcheck  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
