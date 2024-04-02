# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.28.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.image_api import ImageApi  # noqa: E501
from metal_python.rest import ApiException


class TestImageApi(unittest.TestCase):
    """ImageApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.image_api.ImageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_image(self):
        """Test case for create_image

        create an image. if the given ID already exists a conflict is returned  # noqa: E501
        """
        pass

    def test_delete_image(self):
        """Test case for delete_image

        deletes an image and returns the deleted entity  # noqa: E501
        """
        pass

    def test_find_image(self):
        """Test case for find_image

        get image by id  # noqa: E501
        """
        pass

    def test_find_images(self):
        """Test case for find_images

        get all images that match given properties  # noqa: E501
        """
        pass

    def test_find_latest_image(self):
        """Test case for find_latest_image

        find latest image by id  # noqa: E501
        """
        pass

    def test_list_images(self):
        """Test case for list_images

        get all images  # noqa: E501
        """
        pass

    def test_query_images_by_id(self):
        """Test case for query_images_by_id

        query all images which match at least id  # noqa: E501
        """
        pass

    def test_update_image(self):
        """Test case for update_image

        updates an image. if the image was changed since this one was read, a conflict is returned  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
