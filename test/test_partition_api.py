# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.22.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.partition_api import PartitionApi  # noqa: E501
from metal_python.rest import ApiException


class TestPartitionApi(unittest.TestCase):
    """PartitionApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.partition_api.PartitionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_partition(self):
        """Test case for create_partition

        create a Partition. if the given ID already exists a conflict is returned  # noqa: E501
        """
        pass

    def test_delete_partition(self):
        """Test case for delete_partition

        deletes a Partition and returns the deleted entity  # noqa: E501
        """
        pass

    def test_find_partition(self):
        """Test case for find_partition

        get Partition by id  # noqa: E501
        """
        pass

    def test_list_partitions(self):
        """Test case for list_partitions

        get all Partitions  # noqa: E501
        """
        pass

    def test_partition_capacity(self):
        """Test case for partition_capacity

        get partition capacity  # noqa: E501
        """
        pass

    def test_partition_capacity_compat(self):
        """Test case for partition_capacity_compat

        get partition capacity  # noqa: E501
        """
        pass

    def test_update_partition(self):
        """Test case for update_partition

        updates a Partition. if the Partition was changed since this one was read, a conflict is returned  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
