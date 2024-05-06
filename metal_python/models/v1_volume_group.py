# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.28.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1VolumeGroup(object):
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
        'devices': 'list[str]',
        'name': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'devices': 'devices',
        'name': 'name',
        'tags': 'tags'
    }

    def __init__(self, devices=None, name=None, tags=None):  # noqa: E501
        """V1VolumeGroup - a model defined in Swagger"""  # noqa: E501

        self._devices = None
        self._name = None
        self._tags = None
        self.discriminator = None

        if devices is not None:
            self.devices = devices
        self.name = name
        if tags is not None:
            self.tags = tags

    @property
    def devices(self):
        """Gets the devices of this V1VolumeGroup.  # noqa: E501

        list of devices to form the volume group from  # noqa: E501

        :return: The devices of this V1VolumeGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this V1VolumeGroup.

        list of devices to form the volume group from  # noqa: E501

        :param devices: The devices of this V1VolumeGroup.  # noqa: E501
        :type: list[str]
        """

        self._devices = devices

    @property
    def name(self):
        """Gets the name of this V1VolumeGroup.  # noqa: E501

        the name of the resulting volume group  # noqa: E501

        :return: The name of this V1VolumeGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1VolumeGroup.

        the name of the resulting volume group  # noqa: E501

        :param name: The name of this V1VolumeGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this V1VolumeGroup.  # noqa: E501

        list of tags to add to the volume group  # noqa: E501

        :return: The tags of this V1VolumeGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this V1VolumeGroup.

        list of tags to add to the volume group  # noqa: E501

        :param tags: The tags of this V1VolumeGroup.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if issubclass(V1VolumeGroup, dict):
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
        if not isinstance(other, V1VolumeGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
