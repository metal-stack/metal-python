# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.39.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.audit_api import AuditApi  # noqa: E501
from metal_python.rest import ApiException


class TestAuditApi(unittest.TestCase):
    """AuditApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.audit_api.AuditApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_audit_traces(self):
        """Test case for find_audit_traces

        find all audit traces that match given properties  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
