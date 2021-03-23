# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1ServerCapacity(object):
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
        'allocated': 'int',
        'faulty': 'int',
        'faultymachines': 'list[str]',
        'free': 'int',
        'other': 'int',
        'othermachines': 'list[str]',
        'size': 'str',
        'total': 'int'
    }

    attribute_map = {
        'allocated': 'allocated',
        'faulty': 'faulty',
        'faultymachines': 'faultymachines',
        'free': 'free',
        'other': 'other',
        'othermachines': 'othermachines',
        'size': 'size',
        'total': 'total'
    }

    def __init__(self, allocated=None, faulty=None, faultymachines=None, free=None, other=None, othermachines=None, size=None, total=None):  # noqa: E501
        """V1ServerCapacity - a model defined in Swagger"""  # noqa: E501

        self._allocated = None
        self._faulty = None
        self._faultymachines = None
        self._free = None
        self._other = None
        self._othermachines = None
        self._size = None
        self._total = None
        self.discriminator = None

        self.allocated = allocated
        self.faulty = faulty
        self.faultymachines = faultymachines
        self.free = free
        self.other = other
        self.othermachines = othermachines
        self.size = size
        self.total = total

    @property
    def allocated(self):
        """Gets the allocated of this V1ServerCapacity.  # noqa: E501

        allocated servers with this size  # noqa: E501

        :return: The allocated of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._allocated

    @allocated.setter
    def allocated(self, allocated):
        """Sets the allocated of this V1ServerCapacity.

        allocated servers with this size  # noqa: E501

        :param allocated: The allocated of this V1ServerCapacity.  # noqa: E501
        :type: int
        """
        if allocated is None:
            raise ValueError("Invalid value for `allocated`, must not be `None`")  # noqa: E501

        self._allocated = allocated

    @property
    def faulty(self):
        """Gets the faulty of this V1ServerCapacity.  # noqa: E501

        servers with issues with this size  # noqa: E501

        :return: The faulty of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._faulty

    @faulty.setter
    def faulty(self, faulty):
        """Sets the faulty of this V1ServerCapacity.

        servers with issues with this size  # noqa: E501

        :param faulty: The faulty of this V1ServerCapacity.  # noqa: E501
        :type: int
        """
        if faulty is None:
            raise ValueError("Invalid value for `faulty`, must not be `None`")  # noqa: E501

        self._faulty = faulty

    @property
    def faultymachines(self):
        """Gets the faultymachines of this V1ServerCapacity.  # noqa: E501

        servers with issues with this size  # noqa: E501

        :return: The faultymachines of this V1ServerCapacity.  # noqa: E501
        :rtype: list[str]
        """
        return self._faultymachines

    @faultymachines.setter
    def faultymachines(self, faultymachines):
        """Sets the faultymachines of this V1ServerCapacity.

        servers with issues with this size  # noqa: E501

        :param faultymachines: The faultymachines of this V1ServerCapacity.  # noqa: E501
        :type: list[str]
        """
        if faultymachines is None:
            raise ValueError("Invalid value for `faultymachines`, must not be `None`")  # noqa: E501

        self._faultymachines = faultymachines

    @property
    def free(self):
        """Gets the free of this V1ServerCapacity.  # noqa: E501

        free servers with this size  # noqa: E501

        :return: The free of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._free

    @free.setter
    def free(self, free):
        """Sets the free of this V1ServerCapacity.

        free servers with this size  # noqa: E501

        :param free: The free of this V1ServerCapacity.  # noqa: E501
        :type: int
        """
        if free is None:
            raise ValueError("Invalid value for `free`, must not be `None`")  # noqa: E501

        self._free = free

    @property
    def other(self):
        """Gets the other of this V1ServerCapacity.  # noqa: E501

        servers neither free, allocated or faulty with this size  # noqa: E501

        :return: The other of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._other

    @other.setter
    def other(self, other):
        """Sets the other of this V1ServerCapacity.

        servers neither free, allocated or faulty with this size  # noqa: E501

        :param other: The other of this V1ServerCapacity.  # noqa: E501
        :type: int
        """
        if other is None:
            raise ValueError("Invalid value for `other`, must not be `None`")  # noqa: E501

        self._other = other

    @property
    def othermachines(self):
        """Gets the othermachines of this V1ServerCapacity.  # noqa: E501

        servers neither free, allocated or faulty with this size  # noqa: E501

        :return: The othermachines of this V1ServerCapacity.  # noqa: E501
        :rtype: list[str]
        """
        return self._othermachines

    @othermachines.setter
    def othermachines(self, othermachines):
        """Sets the othermachines of this V1ServerCapacity.

        servers neither free, allocated or faulty with this size  # noqa: E501

        :param othermachines: The othermachines of this V1ServerCapacity.  # noqa: E501
        :type: list[str]
        """
        if othermachines is None:
            raise ValueError("Invalid value for `othermachines`, must not be `None`")  # noqa: E501

        self._othermachines = othermachines

    @property
    def size(self):
        """Gets the size of this V1ServerCapacity.  # noqa: E501

        the size of the server  # noqa: E501

        :return: The size of this V1ServerCapacity.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this V1ServerCapacity.

        the size of the server  # noqa: E501

        :param size: The size of this V1ServerCapacity.  # noqa: E501
        :type: str
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def total(self):
        """Gets the total of this V1ServerCapacity.  # noqa: E501

        total amount of servers with this size  # noqa: E501

        :return: The total of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this V1ServerCapacity.

        total amount of servers with this size  # noqa: E501

        :param total: The total of this V1ServerCapacity.  # noqa: E501
        :type: int
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

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
        if issubclass(V1ServerCapacity, dict):
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
        if not isinstance(other, V1ServerCapacity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
