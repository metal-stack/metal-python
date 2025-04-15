# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.41.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineVPN(object):
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
        'address': 'str',
        'auth_key': 'str',
        'connected': 'bool'
    }

    attribute_map = {
        'address': 'address',
        'auth_key': 'auth_key',
        'connected': 'connected'
    }

    def __init__(self, address=None, auth_key=None, connected=None):  # noqa: E501
        """V1MachineVPN - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._auth_key = None
        self._connected = None
        self.discriminator = None

        self.address = address
        self.auth_key = auth_key
        self.connected = connected

    @property
    def address(self):
        """Gets the address of this V1MachineVPN.  # noqa: E501

        address of VPN control plane  # noqa: E501

        :return: The address of this V1MachineVPN.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this V1MachineVPN.

        address of VPN control plane  # noqa: E501

        :param address: The address of this V1MachineVPN.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def auth_key(self):
        """Gets the auth_key of this V1MachineVPN.  # noqa: E501

        auth key used to connect to VPN  # noqa: E501

        :return: The auth_key of this V1MachineVPN.  # noqa: E501
        :rtype: str
        """
        return self._auth_key

    @auth_key.setter
    def auth_key(self, auth_key):
        """Sets the auth_key of this V1MachineVPN.

        auth key used to connect to VPN  # noqa: E501

        :param auth_key: The auth_key of this V1MachineVPN.  # noqa: E501
        :type: str
        """
        if auth_key is None:
            raise ValueError("Invalid value for `auth_key`, must not be `None`")  # noqa: E501

        self._auth_key = auth_key

    @property
    def connected(self):
        """Gets the connected of this V1MachineVPN.  # noqa: E501

        connected to the VPN  # noqa: E501

        :return: The connected of this V1MachineVPN.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this V1MachineVPN.

        connected to the VPN  # noqa: E501

        :param connected: The connected of this V1MachineVPN.  # noqa: E501
        :type: bool
        """
        if connected is None:
            raise ValueError("Invalid value for `connected`, must not be `None`")  # noqa: E501

        self._connected = connected

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
        if issubclass(V1MachineVPN, dict):
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
        if not isinstance(other, V1MachineVPN):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
