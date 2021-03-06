# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.14.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineBlockDevice(object):
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
        'name': 'str',
        'partitions': 'list[V1MachineDiskPartition]',
        'primary': 'bool',
        'size': 'int'
    }

    attribute_map = {
        'name': 'name',
        'partitions': 'partitions',
        'primary': 'primary',
        'size': 'size'
    }

    def __init__(self, name=None, partitions=None, primary=None, size=None):  # noqa: E501
        """V1MachineBlockDevice - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._partitions = None
        self._primary = None
        self._size = None
        self.discriminator = None

        self.name = name
        if partitions is not None:
            self.partitions = partitions
        self.primary = primary
        self.size = size

    @property
    def name(self):
        """Gets the name of this V1MachineBlockDevice.  # noqa: E501

        the name of this block device  # noqa: E501

        :return: The name of this V1MachineBlockDevice.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1MachineBlockDevice.

        the name of this block device  # noqa: E501

        :param name: The name of this V1MachineBlockDevice.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def partitions(self):
        """Gets the partitions of this V1MachineBlockDevice.  # noqa: E501

        the partitions of this disk  # noqa: E501

        :return: The partitions of this V1MachineBlockDevice.  # noqa: E501
        :rtype: list[V1MachineDiskPartition]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """Sets the partitions of this V1MachineBlockDevice.

        the partitions of this disk  # noqa: E501

        :param partitions: The partitions of this V1MachineBlockDevice.  # noqa: E501
        :type: list[V1MachineDiskPartition]
        """

        self._partitions = partitions

    @property
    def primary(self):
        """Gets the primary of this V1MachineBlockDevice.  # noqa: E501

        whether this disk has the OS installed  # noqa: E501

        :return: The primary of this V1MachineBlockDevice.  # noqa: E501
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this V1MachineBlockDevice.

        whether this disk has the OS installed  # noqa: E501

        :param primary: The primary of this V1MachineBlockDevice.  # noqa: E501
        :type: bool
        """
        if primary is None:
            raise ValueError("Invalid value for `primary`, must not be `None`")  # noqa: E501

        self._primary = primary

    @property
    def size(self):
        """Gets the size of this V1MachineBlockDevice.  # noqa: E501

        the size of this block device  # noqa: E501

        :return: The size of this V1MachineBlockDevice.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this V1MachineBlockDevice.

        the size of this block device  # noqa: E501

        :param size: The size of this V1MachineBlockDevice.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

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
        if issubclass(V1MachineBlockDevice, dict):
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
        if not isinstance(other, V1MachineBlockDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
