# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.41.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1NetworkUsage(object):
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
        'available_ips': 'int',
        'available_prefixes': 'int',
        'used_ips': 'int',
        'used_prefixes': 'int'
    }

    attribute_map = {
        'available_ips': 'available_ips',
        'available_prefixes': 'available_prefixes',
        'used_ips': 'used_ips',
        'used_prefixes': 'used_prefixes'
    }

    def __init__(self, available_ips=None, available_prefixes=None, used_ips=None, used_prefixes=None):  # noqa: E501
        """V1NetworkUsage - a model defined in Swagger"""  # noqa: E501

        self._available_ips = None
        self._available_prefixes = None
        self._used_ips = None
        self._used_prefixes = None
        self.discriminator = None

        self.available_ips = available_ips
        self.available_prefixes = available_prefixes
        self.used_ips = used_ips
        self.used_prefixes = used_prefixes

    @property
    def available_ips(self):
        """Gets the available_ips of this V1NetworkUsage.  # noqa: E501

        the total available IPs  # noqa: E501

        :return: The available_ips of this V1NetworkUsage.  # noqa: E501
        :rtype: int
        """
        return self._available_ips

    @available_ips.setter
    def available_ips(self, available_ips):
        """Sets the available_ips of this V1NetworkUsage.

        the total available IPs  # noqa: E501

        :param available_ips: The available_ips of this V1NetworkUsage.  # noqa: E501
        :type: int
        """
        if available_ips is None:
            raise ValueError("Invalid value for `available_ips`, must not be `None`")  # noqa: E501

        self._available_ips = available_ips

    @property
    def available_prefixes(self):
        """Gets the available_prefixes of this V1NetworkUsage.  # noqa: E501

        the total available 2 bit Prefixes  # noqa: E501

        :return: The available_prefixes of this V1NetworkUsage.  # noqa: E501
        :rtype: int
        """
        return self._available_prefixes

    @available_prefixes.setter
    def available_prefixes(self, available_prefixes):
        """Sets the available_prefixes of this V1NetworkUsage.

        the total available 2 bit Prefixes  # noqa: E501

        :param available_prefixes: The available_prefixes of this V1NetworkUsage.  # noqa: E501
        :type: int
        """
        if available_prefixes is None:
            raise ValueError("Invalid value for `available_prefixes`, must not be `None`")  # noqa: E501

        self._available_prefixes = available_prefixes

    @property
    def used_ips(self):
        """Gets the used_ips of this V1NetworkUsage.  # noqa: E501

        the total used IPs  # noqa: E501

        :return: The used_ips of this V1NetworkUsage.  # noqa: E501
        :rtype: int
        """
        return self._used_ips

    @used_ips.setter
    def used_ips(self, used_ips):
        """Sets the used_ips of this V1NetworkUsage.

        the total used IPs  # noqa: E501

        :param used_ips: The used_ips of this V1NetworkUsage.  # noqa: E501
        :type: int
        """
        if used_ips is None:
            raise ValueError("Invalid value for `used_ips`, must not be `None`")  # noqa: E501

        self._used_ips = used_ips

    @property
    def used_prefixes(self):
        """Gets the used_prefixes of this V1NetworkUsage.  # noqa: E501

        the total used Prefixes  # noqa: E501

        :return: The used_prefixes of this V1NetworkUsage.  # noqa: E501
        :rtype: int
        """
        return self._used_prefixes

    @used_prefixes.setter
    def used_prefixes(self, used_prefixes):
        """Sets the used_prefixes of this V1NetworkUsage.

        the total used Prefixes  # noqa: E501

        :param used_prefixes: The used_prefixes of this V1NetworkUsage.  # noqa: E501
        :type: int
        """
        if used_prefixes is None:
            raise ValueError("Invalid value for `used_prefixes`, must not be `None`")  # noqa: E501

        self._used_prefixes = used_prefixes

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
        if issubclass(V1NetworkUsage, dict):
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
        if not isinstance(other, V1NetworkUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
