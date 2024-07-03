# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.32.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1Raid(object):
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
        'arrayname': 'str',
        'createoptions': 'list[str]',
        'devices': 'list[str]',
        'level': 'str',
        'spares': 'int'
    }

    attribute_map = {
        'arrayname': 'arrayname',
        'createoptions': 'createoptions',
        'devices': 'devices',
        'level': 'level',
        'spares': 'spares'
    }

    def __init__(self, arrayname=None, createoptions=None, devices=None, level=None, spares=None):  # noqa: E501
        """V1Raid - a model defined in Swagger"""  # noqa: E501

        self._arrayname = None
        self._createoptions = None
        self._devices = None
        self._level = None
        self._spares = None
        self.discriminator = None

        self.arrayname = arrayname
        if createoptions is not None:
            self.createoptions = createoptions
        if devices is not None:
            self.devices = devices
        self.level = level
        self.spares = spares

    @property
    def arrayname(self):
        """Gets the arrayname of this V1Raid.  # noqa: E501

        the name of the resulting array device  # noqa: E501

        :return: The arrayname of this V1Raid.  # noqa: E501
        :rtype: str
        """
        return self._arrayname

    @arrayname.setter
    def arrayname(self, arrayname):
        """Sets the arrayname of this V1Raid.

        the name of the resulting array device  # noqa: E501

        :param arrayname: The arrayname of this V1Raid.  # noqa: E501
        :type: str
        """
        if arrayname is None:
            raise ValueError("Invalid value for `arrayname`, must not be `None`")  # noqa: E501

        self._arrayname = arrayname

    @property
    def createoptions(self):
        """Gets the createoptions of this V1Raid.  # noqa: E501

        the options to use to create the raid array  # noqa: E501

        :return: The createoptions of this V1Raid.  # noqa: E501
        :rtype: list[str]
        """
        return self._createoptions

    @createoptions.setter
    def createoptions(self, createoptions):
        """Sets the createoptions of this V1Raid.

        the options to use to create the raid array  # noqa: E501

        :param createoptions: The createoptions of this V1Raid.  # noqa: E501
        :type: list[str]
        """

        self._createoptions = createoptions

    @property
    def devices(self):
        """Gets the devices of this V1Raid.  # noqa: E501

        list of devices to form the raid array from  # noqa: E501

        :return: The devices of this V1Raid.  # noqa: E501
        :rtype: list[str]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this V1Raid.

        list of devices to form the raid array from  # noqa: E501

        :param devices: The devices of this V1Raid.  # noqa: E501
        :type: list[str]
        """

        self._devices = devices

    @property
    def level(self):
        """Gets the level of this V1Raid.  # noqa: E501

        raid level to create, should be 0 or 1  # noqa: E501

        :return: The level of this V1Raid.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this V1Raid.

        raid level to create, should be 0 or 1  # noqa: E501

        :param level: The level of this V1Raid.  # noqa: E501
        :type: str
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

    @property
    def spares(self):
        """Gets the spares of this V1Raid.  # noqa: E501

        number of spares for the raid array  # noqa: E501

        :return: The spares of this V1Raid.  # noqa: E501
        :rtype: int
        """
        return self._spares

    @spares.setter
    def spares(self, spares):
        """Sets the spares of this V1Raid.

        number of spares for the raid array  # noqa: E501

        :param spares: The spares of this V1Raid.  # noqa: E501
        :type: int
        """
        if spares is None:
            raise ValueError("Invalid value for `spares`, must not be `None`")  # noqa: E501

        self._spares = spares

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
        if issubclass(V1Raid, dict):
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
        if not isinstance(other, V1Raid):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
