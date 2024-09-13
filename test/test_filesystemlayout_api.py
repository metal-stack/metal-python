# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.35.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.filesystemlayout_api import FilesystemlayoutApi  # noqa: E501
from metal_python.rest import ApiException


class TestFilesystemlayoutApi(unittest.TestCase):
    """FilesystemlayoutApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.filesystemlayout_api.FilesystemlayoutApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_filesystem_layout(self):
        """Test case for create_filesystem_layout

        create a filesystemlayout. if the given ID already exists a conflict is returned  # noqa: E501
        """
        pass

    def test_delete_filesystem_layout(self):
        """Test case for delete_filesystem_layout

        deletes an filesystemlayout and returns the deleted entity  # noqa: E501
        """
        pass

    def test_get_filesystem_layout(self):
        """Test case for get_filesystem_layout

        get filesystemlayout by id  # noqa: E501
        """
        pass

    def test_list_filesystem_layouts(self):
        """Test case for list_filesystem_layouts

        get all filesystemlayouts  # noqa: E501
        """
        pass

    def test_match_filesystem_layout(self):
        """Test case for match_filesystem_layout

        check if the given machine id satisfies the disk requirements of the filesystemlayout in question  # noqa: E501
        """
        pass

    def test_try_filesystem_layout(self):
        """Test case for try_filesystem_layout

        try to detect a filesystemlayout based on given size and image.  # noqa: E501
        """
        pass

    def test_update_filesystem_layout(self):
        """Test case for update_filesystem_layout

        updates a filesystemlayout. if the filesystemlayout was changed since this one was read, a conflict is returned  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
