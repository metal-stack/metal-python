# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.15.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineFinalizeAllocationRequest(object):
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
        'console_password': 'str',
        'initrd': 'str',
        'kernel': 'str',
        'ospartition': 'str',
        'primarydisk': 'str'
    }

    attribute_map = {
        'bootloaderid': 'bootloaderid',
        'cmdline': 'cmdline',
        'console_password': 'console_password',
        'initrd': 'initrd',
        'kernel': 'kernel',
        'ospartition': 'ospartition',
        'primarydisk': 'primarydisk'
    }

    def __init__(self, bootloaderid=None, cmdline=None, console_password=None, initrd=None, kernel=None, ospartition=None, primarydisk=None):  # noqa: E501
        """V1MachineFinalizeAllocationRequest - a model defined in Swagger"""  # noqa: E501

        self._bootloaderid = None
        self._cmdline = None
        self._console_password = None
        self._initrd = None
        self._kernel = None
        self._ospartition = None
        self._primarydisk = None
        self.discriminator = None

        self.bootloaderid = bootloaderid
        self.cmdline = cmdline
        self.console_password = console_password
        self.initrd = initrd
        self.kernel = kernel
        self.ospartition = ospartition
        self.primarydisk = primarydisk

    @property
    def bootloaderid(self):
        """Gets the bootloaderid of this V1MachineFinalizeAllocationRequest.  # noqa: E501

        the bootloader ID  # noqa: E501

        :return: The bootloaderid of this V1MachineFinalizeAllocationRequest.  # noqa: E501
        :rtype: str
        """
        return self._bootloaderid

    @bootloaderid.setter
    def bootloaderid(self, bootloaderid):
        """Sets the bootloaderid of this V1MachineFinalizeAllocationRequest.

        the bootloader ID  # noqa: E501

        :param bootloaderid: The bootloaderid of this V1MachineFinalizeAllocationRequest.  # noqa: E501
        :type: str
        """
        if bootloaderid is None:
            raise ValueError("Invalid value for `bootloaderid`, must not be `None`")  # noqa: E501

        self._bootloaderid = bootloaderid

    @property
    def cmdline(self):
        """Gets the cmdline of this V1MachineFinalizeAllocationRequest.  # noqa: E501

        the cmdline  # noqa: E501

        :return: The cmdline of this V1MachineFinalizeAllocationRequest.  # noqa: E501
        :rtype: str
        """
        return self._cmdline

    @cmdline.setter
    def cmdline(self, cmdline):
        """Sets the cmdline of this V1MachineFinalizeAllocationRequest.

        the cmdline  # noqa: E501

        :param cmdline: The cmdline of this V1MachineFinalizeAllocationRequest.  # noqa: E501
        :type: str
        """
        if cmdline is None:
            raise ValueError("Invalid value for `cmdline`, must not be `None`")  # noqa: E501

        self._cmdline = cmdline

    @property
    def console_password(self):
        """Gets the console_password of this V1MachineFinalizeAllocationRequest.  # noqa: E501

        the console password which was generated while provisioning  # noqa: E501

        :return: The console_password of this V1MachineFinalizeAllocationRequest.  # noqa: E501
        :rtype: str
        """
        return self._console_password

    @console_password.setter
    def console_password(self, console_password):
        """Sets the console_password of this V1MachineFinalizeAllocationRequest.

        the console password which was generated while provisioning  # noqa: E501

        :param console_password: The console_password of this V1MachineFinalizeAllocationRequest.  # noqa: E501
        :type: str
        """
        if console_password is None:
            raise ValueError("Invalid value for `console_password`, must not be `None`")  # noqa: E501

        self._console_password = console_password

    @property
    def initrd(self):
        """Gets the initrd of this V1MachineFinalizeAllocationRequest.  # noqa: E501

        the initrd image  # noqa: E501

        :return: The initrd of this V1MachineFinalizeAllocationRequest.  # noqa: E501
        :rtype: str
        """
        return self._initrd

    @initrd.setter
    def initrd(self, initrd):
        """Sets the initrd of this V1MachineFinalizeAllocationRequest.

        the initrd image  # noqa: E501

        :param initrd: The initrd of this V1MachineFinalizeAllocationRequest.  # noqa: E501
        :type: str
        """
        if initrd is None:
            raise ValueError("Invalid value for `initrd`, must not be `None`")  # noqa: E501

        self._initrd = initrd

    @property
    def kernel(self):
        """Gets the kernel of this V1MachineFinalizeAllocationRequest.  # noqa: E501

        the kernel  # noqa: E501

        :return: The kernel of this V1MachineFinalizeAllocationRequest.  # noqa: E501
        :rtype: str
        """
        return self._kernel

    @kernel.setter
    def kernel(self, kernel):
        """Sets the kernel of this V1MachineFinalizeAllocationRequest.

        the kernel  # noqa: E501

        :param kernel: The kernel of this V1MachineFinalizeAllocationRequest.  # noqa: E501
        :type: str
        """
        if kernel is None:
            raise ValueError("Invalid value for `kernel`, must not be `None`")  # noqa: E501

        self._kernel = kernel

    @property
    def ospartition(self):
        """Gets the ospartition of this V1MachineFinalizeAllocationRequest.  # noqa: E501

        the partition that has the OS installed  # noqa: E501

        :return: The ospartition of this V1MachineFinalizeAllocationRequest.  # noqa: E501
        :rtype: str
        """
        return self._ospartition

    @ospartition.setter
    def ospartition(self, ospartition):
        """Sets the ospartition of this V1MachineFinalizeAllocationRequest.

        the partition that has the OS installed  # noqa: E501

        :param ospartition: The ospartition of this V1MachineFinalizeAllocationRequest.  # noqa: E501
        :type: str
        """
        if ospartition is None:
            raise ValueError("Invalid value for `ospartition`, must not be `None`")  # noqa: E501

        self._ospartition = ospartition

    @property
    def primarydisk(self):
        """Gets the primarydisk of this V1MachineFinalizeAllocationRequest.  # noqa: E501

        the device name of the primary disk  # noqa: E501

        :return: The primarydisk of this V1MachineFinalizeAllocationRequest.  # noqa: E501
        :rtype: str
        """
        return self._primarydisk

    @primarydisk.setter
    def primarydisk(self, primarydisk):
        """Sets the primarydisk of this V1MachineFinalizeAllocationRequest.

        the device name of the primary disk  # noqa: E501

        :param primarydisk: The primarydisk of this V1MachineFinalizeAllocationRequest.  # noqa: E501
        :type: str
        """
        if primarydisk is None:
            raise ValueError("Invalid value for `primarydisk`, must not be `None`")  # noqa: E501

        self._primarydisk = primarydisk

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
        if issubclass(V1MachineFinalizeAllocationRequest, dict):
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
        if not isinstance(other, V1MachineFinalizeAllocationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
