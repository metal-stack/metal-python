# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.41.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.size_api import SizeApi  # noqa: E501
from metal_python.rest import ApiException


class TestSizeApi(unittest.TestCase):
    """SizeApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.size_api.SizeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_size(self):
        """Test case for create_size

        create a size. if the given ID already exists a conflict is returned  # noqa: E501
        """
        pass

    def test_create_size_reservation(self):
        """Test case for create_size_reservation

        create a size reservation. if the given ID already exists a conflict is returned  # noqa: E501
        """
        pass

    def test_delete_size(self):
        """Test case for delete_size

        deletes an size and returns the deleted entity  # noqa: E501
        """
        pass

    def test_delete_size_reservation(self):
        """Test case for delete_size_reservation

        deletes a size reservation and returns the deleted entity  # noqa: E501
        """
        pass

    def test_find_size(self):
        """Test case for find_size

        get size by id  # noqa: E501
        """
        pass

    def test_find_size_reservations(self):
        """Test case for find_size_reservations

        get all size reservations  # noqa: E501
        """
        pass

    def test_get_size_reservation(self):
        """Test case for get_size_reservation

        get size reservation by id  # noqa: E501
        """
        pass

    def test_list_size_reservations(self):
        """Test case for list_size_reservations

        get all size reservations  # noqa: E501
        """
        pass

    def test_list_sizes(self):
        """Test case for list_sizes

        get all sizes  # noqa: E501
        """
        pass

    def test_size_reservations_usage(self):
        """Test case for size_reservations_usage

        get all size reservations  # noqa: E501
        """
        pass

    def test_suggest(self):
        """Test case for suggest

        from a given machine id returns the appropriate size  # noqa: E501
        """
        pass

    def test_update_size(self):
        """Test case for update_size

        updates a size. if the size was changed since this one was read, a conflict is returned  # noqa: E501
        """
        pass

    def test_update_size_reservation(self):
        """Test case for update_size_reservation

        updates a size reservation. if the size reservation was changed since this one was read, a conflict is returned  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
