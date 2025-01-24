# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.39.6
    
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
        'actual': 'str',
        'bgp_port_state': 'MetalSwitchBGPPortState',
        'filter': 'V1BGPFilter',
        'identifier': 'str',
        'mac': 'str',
        'name': 'str',
        'vrf': 'str'
    }

    attribute_map = {
        'actual': 'actual',
        'bgp_port_state': 'bgp_port_state',
        'filter': 'filter',
        'identifier': 'identifier',
        'mac': 'mac',
        'name': 'name',
        'vrf': 'vrf'
    }

    def __init__(self, actual=None, bgp_port_state=None, filter=None, identifier=None, mac=None, name=None, vrf=None):  # noqa: E501
        """V1SwitchNic - a model defined in Swagger"""  # noqa: E501

        self._actual = None
        self._bgp_port_state = None
        self._filter = None
        self._identifier = None
        self._mac = None
        self._name = None
        self._vrf = None
        self.discriminator = None

        self.actual = actual
        if bgp_port_state is not None:
            self.bgp_port_state = bgp_port_state
        if filter is not None:
            self.filter = filter
        self.identifier = identifier
        self.mac = mac
        self.name = name
        if vrf is not None:
            self.vrf = vrf

    @property
    def actual(self):
        """Gets the actual of this V1SwitchNic.  # noqa: E501

        the current state of the nic  # noqa: E501

        :return: The actual of this V1SwitchNic.  # noqa: E501
        :rtype: str
        """
        return self._actual

    @actual.setter
    def actual(self, actual):
        """Sets the actual of this V1SwitchNic.

        the current state of the nic  # noqa: E501

        :param actual: The actual of this V1SwitchNic.  # noqa: E501
        :type: str
        """
        if actual is None:
            raise ValueError("Invalid value for `actual`, must not be `None`")  # noqa: E501
        allowed_values = ["DOWN", "UNKNOWN", "UP"]  # noqa: E501
        if actual not in allowed_values:
            raise ValueError(
                "Invalid value for `actual` ({0}), must be one of {1}"  # noqa: E501
                .format(actual, allowed_values)
            )

        self._actual = actual

    @property
    def bgp_port_state(self):
        """Gets the bgp_port_state of this V1SwitchNic.  # noqa: E501

        the current bgp port state  # noqa: E501

        :return: The bgp_port_state of this V1SwitchNic.  # noqa: E501
        :rtype: MetalSwitchBGPPortState
        """
        return self._bgp_port_state

    @bgp_port_state.setter
    def bgp_port_state(self, bgp_port_state):
        """Sets the bgp_port_state of this V1SwitchNic.

        the current bgp port state  # noqa: E501

        :param bgp_port_state: The bgp_port_state of this V1SwitchNic.  # noqa: E501
        :type: MetalSwitchBGPPortState
        """

        self._bgp_port_state = bgp_port_state

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
    def identifier(self):
        """Gets the identifier of this V1SwitchNic.  # noqa: E501

        the identifier of this network interface  # noqa: E501

        :return: The identifier of this V1SwitchNic.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this V1SwitchNic.

        the identifier of this network interface  # noqa: E501

        :param identifier: The identifier of this V1SwitchNic.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

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
