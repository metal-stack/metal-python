# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.22.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1BGPFilter(object):
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
        'cidrs': 'list[str]',
        'vnis': 'list[str]'
    }

    attribute_map = {
        'cidrs': 'cidrs',
        'vnis': 'vnis'
    }

    def __init__(self, cidrs=None, vnis=None):  # noqa: E501
        """V1BGPFilter - a model defined in Swagger"""  # noqa: E501

        self._cidrs = None
        self._vnis = None
        self.discriminator = None

        self.cidrs = cidrs
        if vnis is not None:
            self.vnis = vnis

    @property
    def cidrs(self):
        """Gets the cidrs of this V1BGPFilter.  # noqa: E501

        the cidr addresses that are allowed to be announced at this switch port  # noqa: E501

        :return: The cidrs of this V1BGPFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._cidrs

    @cidrs.setter
    def cidrs(self, cidrs):
        """Sets the cidrs of this V1BGPFilter.

        the cidr addresses that are allowed to be announced at this switch port  # noqa: E501

        :param cidrs: The cidrs of this V1BGPFilter.  # noqa: E501
        :type: list[str]
        """
        if cidrs is None:
            raise ValueError("Invalid value for `cidrs`, must not be `None`")  # noqa: E501

        self._cidrs = cidrs

    @property
    def vnis(self):
        """Gets the vnis of this V1BGPFilter.  # noqa: E501

        the virtual networks that are exposed at this switch port  # noqa: E501

        :return: The vnis of this V1BGPFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._vnis

    @vnis.setter
    def vnis(self, vnis):
        """Sets the vnis of this V1BGPFilter.

        the virtual networks that are exposed at this switch port  # noqa: E501

        :param vnis: The vnis of this V1BGPFilter.  # noqa: E501
        :type: list[str]
        """

        self._vnis = vnis

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
        if issubclass(V1BGPFilter, dict):
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
        if not isinstance(other, V1BGPFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
