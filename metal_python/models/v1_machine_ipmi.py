# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.22.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineIPMI(object):
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
        'bmcversion': 'str',
        'fru': 'V1MachineFru',
        'interface': 'str',
        'mac': 'str',
        'password': 'str',
        'powermetric': 'V1PowerMetric',
        'powerstate': 'str',
        'user': 'str'
    }

    attribute_map = {
        'address': 'address',
        'bmcversion': 'bmcversion',
        'fru': 'fru',
        'interface': 'interface',
        'mac': 'mac',
        'password': 'password',
        'powermetric': 'powermetric',
        'powerstate': 'powerstate',
        'user': 'user'
    }

    def __init__(self, address=None, bmcversion=None, fru=None, interface=None, mac=None, password=None, powermetric=None, powerstate=None, user=None):  # noqa: E501
        """V1MachineIPMI - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._bmcversion = None
        self._fru = None
        self._interface = None
        self._mac = None
        self._password = None
        self._powermetric = None
        self._powerstate = None
        self._user = None
        self.discriminator = None

        self.address = address
        self.bmcversion = bmcversion
        self.fru = fru
        self.interface = interface
        self.mac = mac
        self.password = password
        self.powermetric = powermetric
        self.powerstate = powerstate
        self.user = user

    @property
    def address(self):
        """Gets the address of this V1MachineIPMI.  # noqa: E501


        :return: The address of this V1MachineIPMI.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this V1MachineIPMI.


        :param address: The address of this V1MachineIPMI.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def bmcversion(self):
        """Gets the bmcversion of this V1MachineIPMI.  # noqa: E501


        :return: The bmcversion of this V1MachineIPMI.  # noqa: E501
        :rtype: str
        """
        return self._bmcversion

    @bmcversion.setter
    def bmcversion(self, bmcversion):
        """Sets the bmcversion of this V1MachineIPMI.


        :param bmcversion: The bmcversion of this V1MachineIPMI.  # noqa: E501
        :type: str
        """
        if bmcversion is None:
            raise ValueError("Invalid value for `bmcversion`, must not be `None`")  # noqa: E501

        self._bmcversion = bmcversion

    @property
    def fru(self):
        """Gets the fru of this V1MachineIPMI.  # noqa: E501


        :return: The fru of this V1MachineIPMI.  # noqa: E501
        :rtype: V1MachineFru
        """
        return self._fru

    @fru.setter
    def fru(self, fru):
        """Sets the fru of this V1MachineIPMI.


        :param fru: The fru of this V1MachineIPMI.  # noqa: E501
        :type: V1MachineFru
        """
        if fru is None:
            raise ValueError("Invalid value for `fru`, must not be `None`")  # noqa: E501

        self._fru = fru

    @property
    def interface(self):
        """Gets the interface of this V1MachineIPMI.  # noqa: E501


        :return: The interface of this V1MachineIPMI.  # noqa: E501
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this V1MachineIPMI.


        :param interface: The interface of this V1MachineIPMI.  # noqa: E501
        :type: str
        """
        if interface is None:
            raise ValueError("Invalid value for `interface`, must not be `None`")  # noqa: E501

        self._interface = interface

    @property
    def mac(self):
        """Gets the mac of this V1MachineIPMI.  # noqa: E501


        :return: The mac of this V1MachineIPMI.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this V1MachineIPMI.


        :param mac: The mac of this V1MachineIPMI.  # noqa: E501
        :type: str
        """
        if mac is None:
            raise ValueError("Invalid value for `mac`, must not be `None`")  # noqa: E501

        self._mac = mac

    @property
    def password(self):
        """Gets the password of this V1MachineIPMI.  # noqa: E501


        :return: The password of this V1MachineIPMI.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this V1MachineIPMI.


        :param password: The password of this V1MachineIPMI.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def powermetric(self):
        """Gets the powermetric of this V1MachineIPMI.  # noqa: E501


        :return: The powermetric of this V1MachineIPMI.  # noqa: E501
        :rtype: V1PowerMetric
        """
        return self._powermetric

    @powermetric.setter
    def powermetric(self, powermetric):
        """Sets the powermetric of this V1MachineIPMI.


        :param powermetric: The powermetric of this V1MachineIPMI.  # noqa: E501
        :type: V1PowerMetric
        """
        if powermetric is None:
            raise ValueError("Invalid value for `powermetric`, must not be `None`")  # noqa: E501

        self._powermetric = powermetric

    @property
    def powerstate(self):
        """Gets the powerstate of this V1MachineIPMI.  # noqa: E501


        :return: The powerstate of this V1MachineIPMI.  # noqa: E501
        :rtype: str
        """
        return self._powerstate

    @powerstate.setter
    def powerstate(self, powerstate):
        """Sets the powerstate of this V1MachineIPMI.


        :param powerstate: The powerstate of this V1MachineIPMI.  # noqa: E501
        :type: str
        """
        if powerstate is None:
            raise ValueError("Invalid value for `powerstate`, must not be `None`")  # noqa: E501

        self._powerstate = powerstate

    @property
    def user(self):
        """Gets the user of this V1MachineIPMI.  # noqa: E501


        :return: The user of this V1MachineIPMI.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this V1MachineIPMI.


        :param user: The user of this V1MachineIPMI.  # noqa: E501
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

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
        if issubclass(V1MachineIPMI, dict):
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
        if not isinstance(other, V1MachineIPMI):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
