# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.32.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import metal_python
from metal_python.api.project_api import ProjectApi  # noqa: E501
from metal_python.rest import ApiException


class TestProjectApi(unittest.TestCase):
    """ProjectApi unit test stubs"""

    def setUp(self):
        self.api = metal_python.api.project_api.ProjectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_project(self):
        """Test case for create_project

        create a project. if the given ID already exists a conflict is returned  # noqa: E501
        """
        pass

    def test_delete_project(self):
        """Test case for delete_project

        deletes a project and returns the deleted entity  # noqa: E501
        """
        pass

    def test_find_project(self):
        """Test case for find_project

        get project by id  # noqa: E501
        """
        pass

    def test_find_projects(self):
        """Test case for find_projects

        get all projects that match given properties  # noqa: E501
        """
        pass

    def test_list_projects(self):
        """Test case for list_projects

        get all projects  # noqa: E501
        """
        pass

    def test_update_project(self):
        """Test case for update_project

        update a project. optimistic lock error can occur.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
