# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.34.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1FilesystemLayoutMatchRequest(object):
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
        'filesystemlayout': 'str',
        'machine': 'str'
    }

    attribute_map = {
        'filesystemlayout': 'filesystemlayout',
        'machine': 'machine'
    }

    def __init__(self, filesystemlayout=None, machine=None):  # noqa: E501
        """V1FilesystemLayoutMatchRequest - a model defined in Swagger"""  # noqa: E501

        self._filesystemlayout = None
        self._machine = None
        self.discriminator = None

        self.filesystemlayout = filesystemlayout
        self.machine = machine

    @property
    def filesystemlayout(self):
        """Gets the filesystemlayout of this V1FilesystemLayoutMatchRequest.  # noqa: E501

        filesystemlayout id to check  # noqa: E501

        :return: The filesystemlayout of this V1FilesystemLayoutMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._filesystemlayout

    @filesystemlayout.setter
    def filesystemlayout(self, filesystemlayout):
        """Sets the filesystemlayout of this V1FilesystemLayoutMatchRequest.

        filesystemlayout id to check  # noqa: E501

        :param filesystemlayout: The filesystemlayout of this V1FilesystemLayoutMatchRequest.  # noqa: E501
        :type: str
        """
        if filesystemlayout is None:
            raise ValueError("Invalid value for `filesystemlayout`, must not be `None`")  # noqa: E501

        self._filesystemlayout = filesystemlayout

    @property
    def machine(self):
        """Gets the machine of this V1FilesystemLayoutMatchRequest.  # noqa: E501

        machine id to check  # noqa: E501

        :return: The machine of this V1FilesystemLayoutMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._machine

    @machine.setter
    def machine(self, machine):
        """Sets the machine of this V1FilesystemLayoutMatchRequest.

        machine id to check  # noqa: E501

        :param machine: The machine of this V1FilesystemLayoutMatchRequest.  # noqa: E501
        :type: str
        """
        if machine is None:
            raise ValueError("Invalid value for `machine`, must not be `None`")  # noqa: E501

        self._machine = machine

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
        if issubclass(V1FilesystemLayoutMatchRequest, dict):
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
        if not isinstance(other, V1FilesystemLayoutMatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
