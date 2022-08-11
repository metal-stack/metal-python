# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.19.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SwitchNic(object):
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
        'filter': 'V1BGPFilter',
        'mac': 'str',
        'name': 'str',
        'vrf': 'str'
    }

    attribute_map = {
        'filter': 'filter',
        'mac': 'mac',
        'name': 'name',
        'vrf': 'vrf'
    }

    def __init__(self, filter=None, mac=None, name=None, vrf=None):  # noqa: E501
        """V1SwitchNic - a model defined in Swagger"""  # noqa: E501

        self._filter = None
        self._mac = None
        self._name = None
        self._vrf = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        self.mac = mac
        self.name = name
        if vrf is not None:
            self.vrf = vrf

    @property
    def filter(self):
        """Gets the filter of this V1SwitchNic.  # noqa: E501

        configures the bgp filter applied at the switch port  # noqa: E501

        :return: The filter of this V1SwitchNic.  # noqa: E501
        :rtype: V1BGPFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this V1SwitchNic.

        configures the bgp filter applied at the switch port  # noqa: E501

        :param filter: The filter of this V1SwitchNic.  # noqa: E501
        :type: V1BGPFilter
        """

        self._filter = filter

    @property
    def mac(self):
        """Gets the mac of this V1SwitchNic.  # noqa: E501

        the mac address of this network interface  # noqa: E501

        :return: The mac of this V1SwitchNic.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this V1SwitchNic.

        the mac address of this network interface  # noqa: E501

        :param mac: The mac of this V1SwitchNic.  # noqa: E501
        :type: str
        """
        if mac is None:
            raise ValueError("Invalid value for `mac`, must not be `None`")  # noqa: E501

        self._mac = mac

    @property
    def name(self):
        """Gets the name of this V1SwitchNic.  # noqa: E501

        the name of this network interface  # noqa: E501

        :return: The name of this V1SwitchNic.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1SwitchNic.

        the name of this network interface  # noqa: E501

        :param name: The name of this V1SwitchNic.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def vrf(self):
        """Gets the vrf of this V1SwitchNic.  # noqa: E501

        the vrf this network interface is part of  # noqa: E501

        :return: The vrf of this V1SwitchNic.  # noqa: E501
        :rtype: str
        """
        return self._vrf

    @vrf.setter
    def vrf(self, vrf):
        """Sets the vrf of this V1SwitchNic.

        the vrf this network interface is part of  # noqa: E501

        :param vrf: The vrf of this V1SwitchNic.  # noqa: E501
        :type: str
        """

        self._vrf = vrf

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
        if issubclass(V1SwitchNic, dict):
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
        if not isinstance(other, V1SwitchNic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
