# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.14.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineDiskPartition(object):
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
        'device': 'str',
        'filesystem': 'str',
        'gptguid': 'str',
        'gpttyoe': 'str',
        'label': 'str',
        'mountoptions': 'list[str]',
        'mountpoint': 'str',
        'number': 'int',
        'properties': 'dict(str, str)',
        'size': 'int'
    }

    attribute_map = {
        'device': 'device',
        'filesystem': 'filesystem',
        'gptguid': 'gptguid',
        'gpttyoe': 'gpttyoe',
        'label': 'label',
        'mountoptions': 'mountoptions',
        'mountpoint': 'mountpoint',
        'number': 'number',
        'properties': 'properties',
        'size': 'size'
    }

    def __init__(self, device=None, filesystem=None, gptguid=None, gpttyoe=None, label=None, mountoptions=None, mountpoint=None, number=None, properties=None, size=None):  # noqa: E501
        """V1MachineDiskPartition - a model defined in Swagger"""  # noqa: E501

        self._device = None
        self._filesystem = None
        self._gptguid = None
        self._gpttyoe = None
        self._label = None
        self._mountoptions = None
        self._mountpoint = None
        self._number = None
        self._properties = None
        self._size = None
        self.discriminator = None

        self.device = device
        self.filesystem = filesystem
        self.gptguid = gptguid
        self.gpttyoe = gpttyoe
        self.label = label
        self.mountoptions = mountoptions
        self.mountpoint = mountpoint
        self.number = number
        self.properties = properties
        self.size = size

    @property
    def device(self):
        """Gets the device of this V1MachineDiskPartition.  # noqa: E501

        the partition device name, e.g. sda1  # noqa: E501

        :return: The device of this V1MachineDiskPartition.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this V1MachineDiskPartition.

        the partition device name, e.g. sda1  # noqa: E501

        :param device: The device of this V1MachineDiskPartition.  # noqa: E501
        :type: str
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def filesystem(self):
        """Gets the filesystem of this V1MachineDiskPartition.  # noqa: E501

        the partition filesystem  # noqa: E501

        :return: The filesystem of this V1MachineDiskPartition.  # noqa: E501
        :rtype: str
        """
        return self._filesystem

    @filesystem.setter
    def filesystem(self, filesystem):
        """Sets the filesystem of this V1MachineDiskPartition.

        the partition filesystem  # noqa: E501

        :param filesystem: The filesystem of this V1MachineDiskPartition.  # noqa: E501
        :type: str
        """
        if filesystem is None:
            raise ValueError("Invalid value for `filesystem`, must not be `None`")  # noqa: E501

        self._filesystem = filesystem

    @property
    def gptguid(self):
        """Gets the gptguid of this V1MachineDiskPartition.  # noqa: E501

        the partition GPT guid  # noqa: E501

        :return: The gptguid of this V1MachineDiskPartition.  # noqa: E501
        :rtype: str
        """
        return self._gptguid

    @gptguid.setter
    def gptguid(self, gptguid):
        """Sets the gptguid of this V1MachineDiskPartition.

        the partition GPT guid  # noqa: E501

        :param gptguid: The gptguid of this V1MachineDiskPartition.  # noqa: E501
        :type: str
        """
        if gptguid is None:
            raise ValueError("Invalid value for `gptguid`, must not be `None`")  # noqa: E501

        self._gptguid = gptguid

    @property
    def gpttyoe(self):
        """Gets the gpttyoe of this V1MachineDiskPartition.  # noqa: E501

        the partition GPT type  # noqa: E501

        :return: The gpttyoe of this V1MachineDiskPartition.  # noqa: E501
        :rtype: str
        """
        return self._gpttyoe

    @gpttyoe.setter
    def gpttyoe(self, gpttyoe):
        """Sets the gpttyoe of this V1MachineDiskPartition.

        the partition GPT type  # noqa: E501

        :param gpttyoe: The gpttyoe of this V1MachineDiskPartition.  # noqa: E501
        :type: str
        """
        if gpttyoe is None:
            raise ValueError("Invalid value for `gpttyoe`, must not be `None`")  # noqa: E501

        self._gpttyoe = gpttyoe

    @property
    def label(self):
        """Gets the label of this V1MachineDiskPartition.  # noqa: E501

        the partition label  # noqa: E501

        :return: The label of this V1MachineDiskPartition.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this V1MachineDiskPartition.

        the partition label  # noqa: E501

        :param label: The label of this V1MachineDiskPartition.  # noqa: E501
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def mountoptions(self):
        """Gets the mountoptions of this V1MachineDiskPartition.  # noqa: E501

        the partition mount options  # noqa: E501

        :return: The mountoptions of this V1MachineDiskPartition.  # noqa: E501
        :rtype: list[str]
        """
        return self._mountoptions

    @mountoptions.setter
    def mountoptions(self, mountoptions):
        """Sets the mountoptions of this V1MachineDiskPartition.

        the partition mount options  # noqa: E501

        :param mountoptions: The mountoptions of this V1MachineDiskPartition.  # noqa: E501
        :type: list[str]
        """
        if mountoptions is None:
            raise ValueError("Invalid value for `mountoptions`, must not be `None`")  # noqa: E501

        self._mountoptions = mountoptions

    @property
    def mountpoint(self):
        """Gets the mountpoint of this V1MachineDiskPartition.  # noqa: E501

        the partition mount point  # noqa: E501

        :return: The mountpoint of this V1MachineDiskPartition.  # noqa: E501
        :rtype: str
        """
        return self._mountpoint

    @mountpoint.setter
    def mountpoint(self, mountpoint):
        """Sets the mountpoint of this V1MachineDiskPartition.

        the partition mount point  # noqa: E501

        :param mountpoint: The mountpoint of this V1MachineDiskPartition.  # noqa: E501
        :type: str
        """
        if mountpoint is None:
            raise ValueError("Invalid value for `mountpoint`, must not be `None`")  # noqa: E501

        self._mountpoint = mountpoint

    @property
    def number(self):
        """Gets the number of this V1MachineDiskPartition.  # noqa: E501

        the partition number  # noqa: E501

        :return: The number of this V1MachineDiskPartition.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this V1MachineDiskPartition.

        the partition number  # noqa: E501

        :param number: The number of this V1MachineDiskPartition.  # noqa: E501
        :type: int
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def properties(self):
        """Gets the properties of this V1MachineDiskPartition.  # noqa: E501

        the partition properties  # noqa: E501

        :return: The properties of this V1MachineDiskPartition.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this V1MachineDiskPartition.

        the partition properties  # noqa: E501

        :param properties: The properties of this V1MachineDiskPartition.  # noqa: E501
        :type: dict(str, str)
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def size(self):
        """Gets the size of this V1MachineDiskPartition.  # noqa: E501

        the partition size  # noqa: E501

        :return: The size of this V1MachineDiskPartition.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this V1MachineDiskPartition.

        the partition size  # noqa: E501

        :param size: The size of this V1MachineDiskPartition.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

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
        if issubclass(V1MachineDiskPartition, dict):
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
        if not isinstance(other, V1MachineDiskPartition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
