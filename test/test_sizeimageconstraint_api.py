# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.19.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.sizeimageconstraint_api import SizeimageconstraintApi  # noqa: E501
from metal_python.rest import ApiException


class TestSizeimageconstraintApi(unittest.TestCase):
    """SizeimageconstraintApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.sizeimageconstraint_api.SizeimageconstraintApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_size_image_constraint(self):
        """Test case for create_size_image_constraint

        create a sizeimageconstraint. if the given ID already exists a conflict is returned  # noqa: E501
        """
        pass

    def test_delete_size_image_constraint(self):
        """Test case for delete_size_image_constraint

        deletes an sizeimageconstraint and returns the deleted entity  # noqa: E501
        """
        pass

    def test_find_size_image_constraint(self):
        """Test case for find_size_image_constraint

        get sizeimageconstraint by id  # noqa: E501
        """
        pass

    def test_list_size_image_constraints(self):
        """Test case for list_size_image_constraints

        get all sizeimageconstraints  # noqa: E501
        """
        pass

    def test_try_size_image_constraint(self):
        """Test case for try_size_image_constraint

        try if the given combination of image and size is supported and possible to allocate  # noqa: E501
        """
        pass

    def test_update_size_image_constraint(self):
        """Test case for update_size_image_constraint

        updates a sizeimageconstraint. if the sizeimageconstraint was changed since this one was read, a conflict is returned  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
