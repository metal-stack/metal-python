# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.31.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1BootInfo(object):
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
        'bootloaderid': 'str',
        'cmdline': 'str',
        'image_id': 'str',
        'initrd': 'str',
        'kernel': 'str',
        'os_partition': 'str',
        'primary_disk': 'str'
    }

    attribute_map = {
        'bootloaderid': 'bootloaderid',
        'cmdline': 'cmdline',
        'image_id': 'image_id',
        'initrd': 'initrd',
        'kernel': 'kernel',
        'os_partition': 'os_partition',
        'primary_disk': 'primary_disk'
    }

    def __init__(self, bootloaderid=None, cmdline=None, image_id=None, initrd=None, kernel=None, os_partition=None, primary_disk=None):  # noqa: E501
        """V1BootInfo - a model defined in Swagger"""  # noqa: E501

        self._bootloaderid = None
        self._cmdline = None
        self._image_id = None
        self._initrd = None
        self._kernel = None
        self._os_partition = None
        self._primary_disk = None
        self.discriminator = None

        self.bootloaderid = bootloaderid
        self.cmdline = cmdline
        self.image_id = image_id
        self.initrd = initrd
        self.kernel = kernel
        self.os_partition = os_partition
        self.primary_disk = primary_disk

    @property
    def bootloaderid(self):
        """Gets the bootloaderid of this V1BootInfo.  # noqa: E501

        the bootloader ID  # noqa: E501

        :return: The bootloaderid of this V1BootInfo.  # noqa: E501
        :rtype: str
        """
        return self._bootloaderid

    @bootloaderid.setter
    def bootloaderid(self, bootloaderid):
        """Sets the bootloaderid of this V1BootInfo.

        the bootloader ID  # noqa: E501

        :param bootloaderid: The bootloaderid of this V1BootInfo.  # noqa: E501
        :type: str
        """
        if bootloaderid is None:
            raise ValueError("Invalid value for `bootloaderid`, must not be `None`")  # noqa: E501

        self._bootloaderid = bootloaderid

    @property
    def cmdline(self):
        """Gets the cmdline of this V1BootInfo.  # noqa: E501

        the cmdline  # noqa: E501

        :return: The cmdline of this V1BootInfo.  # noqa: E501
        :rtype: str
        """
        return self._cmdline

    @cmdline.setter
    def cmdline(self, cmdline):
        """Sets the cmdline of this V1BootInfo.

        the cmdline  # noqa: E501

        :param cmdline: The cmdline of this V1BootInfo.  # noqa: E501
        :type: str
        """
        if cmdline is None:
            raise ValueError("Invalid value for `cmdline`, must not be `None`")  # noqa: E501

        self._cmdline = cmdline

    @property
    def image_id(self):
        """Gets the image_id of this V1BootInfo.  # noqa: E501

        the ID of the current image  # noqa: E501

        :return: The image_id of this V1BootInfo.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this V1BootInfo.

        the ID of the current image  # noqa: E501

        :param image_id: The image_id of this V1BootInfo.  # noqa: E501
        :type: str
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def initrd(self):
        """Gets the initrd of this V1BootInfo.  # noqa: E501

        the initrd image  # noqa: E501

        :return: The initrd of this V1BootInfo.  # noqa: E501
        :rtype: str
        """
        return self._initrd

    @initrd.setter
    def initrd(self, initrd):
        """Sets the initrd of this V1BootInfo.

        the initrd image  # noqa: E501

        :param initrd: The initrd of this V1BootInfo.  # noqa: E501
        :type: str
        """
        if initrd is None:
            raise ValueError("Invalid value for `initrd`, must not be `None`")  # noqa: E501

        self._initrd = initrd

    @property
    def kernel(self):
        """Gets the kernel of this V1BootInfo.  # noqa: E501

        the kernel  # noqa: E501

        :return: The kernel of this V1BootInfo.  # noqa: E501
        :rtype: str
        """
        return self._kernel

    @kernel.setter
    def kernel(self, kernel):
        """Sets the kernel of this V1BootInfo.

        the kernel  # noqa: E501

        :param kernel: The kernel of this V1BootInfo.  # noqa: E501
        :type: str
        """
        if kernel is None:
            raise ValueError("Invalid value for `kernel`, must not be `None`")  # noqa: E501

        self._kernel = kernel

    @property
    def os_partition(self):
        """Gets the os_partition of this V1BootInfo.  # noqa: E501

        the partition containing the OS  # noqa: E501

        :return: The os_partition of this V1BootInfo.  # noqa: E501
        :rtype: str
        """
        return self._os_partition

    @os_partition.setter
    def os_partition(self, os_partition):
        """Sets the os_partition of this V1BootInfo.

        the partition containing the OS  # noqa: E501

        :param os_partition: The os_partition of this V1BootInfo.  # noqa: E501
        :type: str
        """
        if os_partition is None:
            raise ValueError("Invalid value for `os_partition`, must not be `None`")  # noqa: E501

        self._os_partition = os_partition

    @property
    def primary_disk(self):
        """Gets the primary_disk of this V1BootInfo.  # noqa: E501

        the primary disk  # noqa: E501

        :return: The primary_disk of this V1BootInfo.  # noqa: E501
        :rtype: str
        """
        return self._primary_disk

    @primary_disk.setter
    def primary_disk(self, primary_disk):
        """Sets the primary_disk of this V1BootInfo.

        the primary disk  # noqa: E501

        :param primary_disk: The primary_disk of this V1BootInfo.  # noqa: E501
        :type: str
        """
        if primary_disk is None:
            raise ValueError("Invalid value for `primary_disk`, must not be `None`")  # noqa: E501

        self._primary_disk = primary_disk

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
        if issubclass(V1BootInfo, dict):
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
        if not isinstance(other, V1BootInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
