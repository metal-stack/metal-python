# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.29.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1Disk(object):
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
        'device': 'str',
        'partitions': 'list[V1DiskPartition]',
        'wipeonreinstall': 'bool'
    }

    attribute_map = {
        'device': 'device',
        'partitions': 'partitions',
        'wipeonreinstall': 'wipeonreinstall'
    }

    def __init__(self, device=None, partitions=None, wipeonreinstall=None):  # noqa: E501
        """V1Disk - a model defined in Swagger"""  # noqa: E501

        self._device = None
        self._partitions = None
        self._wipeonreinstall = None
        self.discriminator = None

        self.device = device
        if partitions is not None:
            self.partitions = partitions
        self.wipeonreinstall = wipeonreinstall

    @property
    def device(self):
        """Gets the device of this V1Disk.  # noqa: E501

        the device to create the partitions  # noqa: E501

        :return: The device of this V1Disk.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this V1Disk.

        the device to create the partitions  # noqa: E501

        :param device: The device of this V1Disk.  # noqa: E501
        :type: str
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def partitions(self):
        """Gets the partitions of this V1Disk.  # noqa: E501

        list of partitions to create on this disk  # noqa: E501

        :return: The partitions of this V1Disk.  # noqa: E501
        :rtype: list[V1DiskPartition]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """Sets the partitions of this V1Disk.

        list of partitions to create on this disk  # noqa: E501

        :param partitions: The partitions of this V1Disk.  # noqa: E501
        :type: list[V1DiskPartition]
        """

        self._partitions = partitions

    @property
    def wipeonreinstall(self):
        """Gets the wipeonreinstall of this V1Disk.  # noqa: E501

        if set to true, this disk will be wiped before reinstallation  # noqa: E501

        :return: The wipeonreinstall of this V1Disk.  # noqa: E501
        :rtype: bool
        """
        return self._wipeonreinstall

    @wipeonreinstall.setter
    def wipeonreinstall(self, wipeonreinstall):
        """Sets the wipeonreinstall of this V1Disk.

        if set to true, this disk will be wiped before reinstallation  # noqa: E501

        :param wipeonreinstall: The wipeonreinstall of this V1Disk.  # noqa: E501
        :type: bool
        """
        if wipeonreinstall is None:
            raise ValueError("Invalid value for `wipeonreinstall`, must not be `None`")  # noqa: E501

        self._wipeonreinstall = wipeonreinstall

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
        if issubclass(V1Disk, dict):
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
        if not isinstance(other, V1Disk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
