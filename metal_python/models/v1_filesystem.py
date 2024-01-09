# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.26.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1Filesystem(object):
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
        'createoptions': 'list[str]',
        'device': 'str',
        'format': 'str',
        'label': 'str',
        'mountoptions': 'list[str]',
        'path': 'str'
    }

    attribute_map = {
        'createoptions': 'createoptions',
        'device': 'device',
        'format': 'format',
        'label': 'label',
        'mountoptions': 'mountoptions',
        'path': 'path'
    }

    def __init__(self, createoptions=None, device=None, format=None, label=None, mountoptions=None, path=None):  # noqa: E501
        """V1Filesystem - a model defined in Swagger"""  # noqa: E501

        self._createoptions = None
        self._device = None
        self._format = None
        self._label = None
        self._mountoptions = None
        self._path = None
        self.discriminator = None

        if createoptions is not None:
            self.createoptions = createoptions
        self.device = device
        self.format = format
        if label is not None:
            self.label = label
        if mountoptions is not None:
            self.mountoptions = mountoptions
        if path is not None:
            self.path = path

    @property
    def createoptions(self):
        """Gets the createoptions of this V1Filesystem.  # noqa: E501

        the options to use to create (mkfs) this filesystem  # noqa: E501

        :return: The createoptions of this V1Filesystem.  # noqa: E501
        :rtype: list[str]
        """
        return self._createoptions

    @createoptions.setter
    def createoptions(self, createoptions):
        """Sets the createoptions of this V1Filesystem.

        the options to use to create (mkfs) this filesystem  # noqa: E501

        :param createoptions: The createoptions of this V1Filesystem.  # noqa: E501
        :type: list[str]
        """

        self._createoptions = createoptions

    @property
    def device(self):
        """Gets the device of this V1Filesystem.  # noqa: E501

        the underlaying device where this filesystem should be created  # noqa: E501

        :return: The device of this V1Filesystem.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this V1Filesystem.

        the underlaying device where this filesystem should be created  # noqa: E501

        :param device: The device of this V1Filesystem.  # noqa: E501
        :type: str
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def format(self):
        """Gets the format of this V1Filesystem.  # noqa: E501

        the filesystem format  # noqa: E501

        :return: The format of this V1Filesystem.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this V1Filesystem.

        the filesystem format  # noqa: E501

        :param format: The format of this V1Filesystem.  # noqa: E501
        :type: str
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")  # noqa: E501

        self._format = format

    @property
    def label(self):
        """Gets the label of this V1Filesystem.  # noqa: E501

        optional label for this this filesystem  # noqa: E501

        :return: The label of this V1Filesystem.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this V1Filesystem.

        optional label for this this filesystem  # noqa: E501

        :param label: The label of this V1Filesystem.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def mountoptions(self):
        """Gets the mountoptions of this V1Filesystem.  # noqa: E501

        the options to use to mount this filesystem  # noqa: E501

        :return: The mountoptions of this V1Filesystem.  # noqa: E501
        :rtype: list[str]
        """
        return self._mountoptions

    @mountoptions.setter
    def mountoptions(self, mountoptions):
        """Sets the mountoptions of this V1Filesystem.

        the options to use to mount this filesystem  # noqa: E501

        :param mountoptions: The mountoptions of this V1Filesystem.  # noqa: E501
        :type: list[str]
        """

        self._mountoptions = mountoptions

    @property
    def path(self):
        """Gets the path of this V1Filesystem.  # noqa: E501

        the mountpoint where this filesystem should be mounted on  # noqa: E501

        :return: The path of this V1Filesystem.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1Filesystem.

        the mountpoint where this filesystem should be mounted on  # noqa: E501

        :param path: The path of this V1Filesystem.  # noqa: E501
        :type: str
        """

        self._path = path

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
        if issubclass(V1Filesystem, dict):
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
        if not isinstance(other, V1Filesystem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
