# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.40.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1TenantFindRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'annotations': 'dict(str, str)',
        'id': 'str',
        'name': 'str',
        'paging': 'V1Paging'
    }

    attribute_map = {
        'annotations': 'annotations',
        'id': 'id',
        'name': 'name',
        'paging': 'paging'
    }

    def __init__(self, annotations=None, id=None, name=None, paging=None):  # noqa: E501
        """V1TenantFindRequest - a model defined in Swagger"""  # noqa: E501

        self._annotations = None
        self._id = None
        self._name = None
        self._paging = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if paging is not None:
            self.paging = paging

    @property
    def annotations(self):
        """Gets the annotations of this V1TenantFindRequest.  # noqa: E501


        :return: The annotations of this V1TenantFindRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this V1TenantFindRequest.


        :param annotations: The annotations of this V1TenantFindRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def id(self):
        """Gets the id of this V1TenantFindRequest.  # noqa: E501


        :return: The id of this V1TenantFindRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1TenantFindRequest.


        :param id: The id of this V1TenantFindRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this V1TenantFindRequest.  # noqa: E501


        :return: The name of this V1TenantFindRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1TenantFindRequest.


        :param name: The name of this V1TenantFindRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def paging(self):
        """Gets the paging of this V1TenantFindRequest.  # noqa: E501


        :return: The paging of this V1TenantFindRequest.  # noqa: E501
        :rtype: V1Paging
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this V1TenantFindRequest.


        :param paging: The paging of this V1TenantFindRequest.  # noqa: E501
        :type: V1Paging
        """

        self._paging = paging

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1TenantFindRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1TenantFindRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
