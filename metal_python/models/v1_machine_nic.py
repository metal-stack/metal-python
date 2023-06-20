# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.22.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineNic(object):
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
        'identifier': 'str',
        'mac': 'str',
        'name': 'str',
        'neighbors': 'list[V1MachineNic]'
    }

    attribute_map = {
        'identifier': 'identifier',
        'mac': 'mac',
        'name': 'name',
        'neighbors': 'neighbors'
    }

    def __init__(self, identifier=None, mac=None, name=None, neighbors=None):  # noqa: E501
        """V1MachineNic - a model defined in Swagger"""  # noqa: E501

        self._identifier = None
        self._mac = None
        self._name = None
        self._neighbors = None
        self.discriminator = None

        self.identifier = identifier
        self.mac = mac
        self.name = name
        self.neighbors = neighbors

    @property
    def identifier(self):
        """Gets the identifier of this V1MachineNic.  # noqa: E501

        the unique identifier of this network interface  # noqa: E501

        :return: The identifier of this V1MachineNic.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this V1MachineNic.

        the unique identifier of this network interface  # noqa: E501

        :param identifier: The identifier of this V1MachineNic.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def mac(self):
        """Gets the mac of this V1MachineNic.  # noqa: E501

        the mac address of this network interface  # noqa: E501

        :return: The mac of this V1MachineNic.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this V1MachineNic.

        the mac address of this network interface  # noqa: E501

        :param mac: The mac of this V1MachineNic.  # noqa: E501
        :type: str
        """
        if mac is None:
            raise ValueError("Invalid value for `mac`, must not be `None`")  # noqa: E501

        self._mac = mac

    @property
    def name(self):
        """Gets the name of this V1MachineNic.  # noqa: E501

        the name of this network interface  # noqa: E501

        :return: The name of this V1MachineNic.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1MachineNic.

        the name of this network interface  # noqa: E501

        :param name: The name of this V1MachineNic.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def neighbors(self):
        """Gets the neighbors of this V1MachineNic.  # noqa: E501

        the neighbors visible to this network interface  # noqa: E501

        :return: The neighbors of this V1MachineNic.  # noqa: E501
        :rtype: list[V1MachineNic]
        """
        return self._neighbors

    @neighbors.setter
    def neighbors(self, neighbors):
        """Sets the neighbors of this V1MachineNic.

        the neighbors visible to this network interface  # noqa: E501

        :param neighbors: The neighbors of this V1MachineNic.  # noqa: E501
        :type: list[V1MachineNic]
        """
        if neighbors is None:
            raise ValueError("Invalid value for `neighbors`, must not be `None`")  # noqa: E501

        self._neighbors = neighbors

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
        if issubclass(V1MachineNic, dict):
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
        if not isinstance(other, V1MachineNic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
