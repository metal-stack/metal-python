# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.21.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SizeConstraint(object):
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
        'max': 'int',
        'min': 'int',
        'type': 'str'
    }

    attribute_map = {
        'max': 'max',
        'min': 'min',
        'type': 'type'
    }

    def __init__(self, max=None, min=None, type=None):  # noqa: E501
        """V1SizeConstraint - a model defined in Swagger"""  # noqa: E501

        self._max = None
        self._min = None
        self._type = None
        self.discriminator = None

        self.max = max
        self.min = min
        self.type = type

    @property
    def max(self):
        """Gets the max of this V1SizeConstraint.  # noqa: E501

        the maximum value of the constraint  # noqa: E501

        :return: The max of this V1SizeConstraint.  # noqa: E501
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this V1SizeConstraint.

        the maximum value of the constraint  # noqa: E501

        :param max: The max of this V1SizeConstraint.  # noqa: E501
        :type: int
        """
        if max is None:
            raise ValueError("Invalid value for `max`, must not be `None`")  # noqa: E501

        self._max = max

    @property
    def min(self):
        """Gets the min of this V1SizeConstraint.  # noqa: E501

        the minimum value of the constraint  # noqa: E501

        :return: The min of this V1SizeConstraint.  # noqa: E501
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this V1SizeConstraint.

        the minimum value of the constraint  # noqa: E501

        :param min: The min of this V1SizeConstraint.  # noqa: E501
        :type: int
        """
        if min is None:
            raise ValueError("Invalid value for `min`, must not be `None`")  # noqa: E501

        self._min = min

    @property
    def type(self):
        """Gets the type of this V1SizeConstraint.  # noqa: E501

        the type of the constraint  # noqa: E501

        :return: The type of this V1SizeConstraint.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1SizeConstraint.

        the type of the constraint  # noqa: E501

        :param type: The type of this V1SizeConstraint.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["cores", "memory", "storage"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(V1SizeConstraint, dict):
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
        if not isinstance(other, V1SizeConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
