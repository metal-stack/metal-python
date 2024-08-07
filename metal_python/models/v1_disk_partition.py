# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.32.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1DiskPartition(object):
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
        'gpttype': 'str',
        'label': 'str',
        'number': 'int',
        'size': 'int'
    }

    attribute_map = {
        'gpttype': 'gpttype',
        'label': 'label',
        'number': 'number',
        'size': 'size'
    }

    def __init__(self, gpttype=None, label=None, number=None, size=None):  # noqa: E501
        """V1DiskPartition - a model defined in Swagger"""  # noqa: E501

        self._gpttype = None
        self._label = None
        self._number = None
        self._size = None
        self.discriminator = None

        self.gpttype = gpttype
        if label is not None:
            self.label = label
        self.number = number
        self.size = size

    @property
    def gpttype(self):
        """Gets the gpttype of this V1DiskPartition.  # noqa: E501

        the gpt partition table type of this partition  # noqa: E501

        :return: The gpttype of this V1DiskPartition.  # noqa: E501
        :rtype: str
        """
        return self._gpttype

    @gpttype.setter
    def gpttype(self, gpttype):
        """Sets the gpttype of this V1DiskPartition.

        the gpt partition table type of this partition  # noqa: E501

        :param gpttype: The gpttype of this V1DiskPartition.  # noqa: E501
        :type: str
        """
        if gpttype is None:
            raise ValueError("Invalid value for `gpttype`, must not be `None`")  # noqa: E501

        self._gpttype = gpttype

    @property
    def label(self):
        """Gets the label of this V1DiskPartition.  # noqa: E501

        optional label for this this partition  # noqa: E501

        :return: The label of this V1DiskPartition.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this V1DiskPartition.

        optional label for this this partition  # noqa: E501

        :param label: The label of this V1DiskPartition.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def number(self):
        """Gets the number of this V1DiskPartition.  # noqa: E501

        partition number, will be appended to partitionprefix to create the final devicename  # noqa: E501

        :return: The number of this V1DiskPartition.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this V1DiskPartition.

        partition number, will be appended to partitionprefix to create the final devicename  # noqa: E501

        :param number: The number of this V1DiskPartition.  # noqa: E501
        :type: int
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def size(self):
        """Gets the size of this V1DiskPartition.  # noqa: E501

        size in mebibytes (MiB) of this partition  # noqa: E501

        :return: The size of this V1DiskPartition.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this V1DiskPartition.

        size in mebibytes (MiB) of this partition  # noqa: E501

        :param size: The size of this V1DiskPartition.  # noqa: E501
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
        if issubclass(V1DiskPartition, dict):
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
        if not isinstance(other, V1DiskPartition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
