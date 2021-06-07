# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.14.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineAbortReinstallRequest(object):
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
        'primary_disk_wiped': 'bool'
    }

    attribute_map = {
        'primary_disk_wiped': 'primary_disk_wiped'
    }

    def __init__(self, primary_disk_wiped=None):  # noqa: E501
        """V1MachineAbortReinstallRequest - a model defined in Swagger"""  # noqa: E501

        self._primary_disk_wiped = None
        self.discriminator = None

        self.primary_disk_wiped = primary_disk_wiped

    @property
    def primary_disk_wiped(self):
        """Gets the primary_disk_wiped of this V1MachineAbortReinstallRequest.  # noqa: E501

        indicates whether the primary disk is already wiped  # noqa: E501

        :return: The primary_disk_wiped of this V1MachineAbortReinstallRequest.  # noqa: E501
        :rtype: bool
        """
        return self._primary_disk_wiped

    @primary_disk_wiped.setter
    def primary_disk_wiped(self, primary_disk_wiped):
        """Sets the primary_disk_wiped of this V1MachineAbortReinstallRequest.

        indicates whether the primary disk is already wiped  # noqa: E501

        :param primary_disk_wiped: The primary_disk_wiped of this V1MachineAbortReinstallRequest.  # noqa: E501
        :type: bool
        """
        if primary_disk_wiped is None:
            raise ValueError("Invalid value for `primary_disk_wiped`, must not be `None`")  # noqa: E501

        self._primary_disk_wiped = primary_disk_wiped

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
        if issubclass(V1MachineAbortReinstallRequest, dict):
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
        if not isinstance(other, V1MachineAbortReinstallRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
