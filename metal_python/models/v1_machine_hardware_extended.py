# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.15.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineHardwareExtended(object):
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
        'cpu_cores': 'int',
        'disks': 'list[V1MachineBlockDevice]',
        'memory': 'int',
        'nics': 'list[V1MachineNicExtended]'
    }

    attribute_map = {
        'cpu_cores': 'cpu_cores',
        'disks': 'disks',
        'memory': 'memory',
        'nics': 'nics'
    }

    def __init__(self, cpu_cores=None, disks=None, memory=None, nics=None):  # noqa: E501
        """V1MachineHardwareExtended - a model defined in Swagger"""  # noqa: E501

        self._cpu_cores = None
        self._disks = None
        self._memory = None
        self._nics = None
        self.discriminator = None

        self.cpu_cores = cpu_cores
        self.disks = disks
        self.memory = memory
        self.nics = nics

    @property
    def cpu_cores(self):
        """Gets the cpu_cores of this V1MachineHardwareExtended.  # noqa: E501

        the number of cpu cores  # noqa: E501

        :return: The cpu_cores of this V1MachineHardwareExtended.  # noqa: E501
        :rtype: int
        """
        return self._cpu_cores

    @cpu_cores.setter
    def cpu_cores(self, cpu_cores):
        """Sets the cpu_cores of this V1MachineHardwareExtended.

        the number of cpu cores  # noqa: E501

        :param cpu_cores: The cpu_cores of this V1MachineHardwareExtended.  # noqa: E501
        :type: int
        """
        if cpu_cores is None:
            raise ValueError("Invalid value for `cpu_cores`, must not be `None`")  # noqa: E501

        self._cpu_cores = cpu_cores

    @property
    def disks(self):
        """Gets the disks of this V1MachineHardwareExtended.  # noqa: E501

        the list of block devices of this machine  # noqa: E501

        :return: The disks of this V1MachineHardwareExtended.  # noqa: E501
        :rtype: list[V1MachineBlockDevice]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this V1MachineHardwareExtended.

        the list of block devices of this machine  # noqa: E501

        :param disks: The disks of this V1MachineHardwareExtended.  # noqa: E501
        :type: list[V1MachineBlockDevice]
        """
        if disks is None:
            raise ValueError("Invalid value for `disks`, must not be `None`")  # noqa: E501

        self._disks = disks

    @property
    def memory(self):
        """Gets the memory of this V1MachineHardwareExtended.  # noqa: E501

        the total memory of the machine  # noqa: E501

        :return: The memory of this V1MachineHardwareExtended.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this V1MachineHardwareExtended.

        the total memory of the machine  # noqa: E501

        :param memory: The memory of this V1MachineHardwareExtended.  # noqa: E501
        :type: int
        """
        if memory is None:
            raise ValueError("Invalid value for `memory`, must not be `None`")  # noqa: E501

        self._memory = memory

    @property
    def nics(self):
        """Gets the nics of this V1MachineHardwareExtended.  # noqa: E501

        the list of network interfaces of this machine with extended information  # noqa: E501

        :return: The nics of this V1MachineHardwareExtended.  # noqa: E501
        :rtype: list[V1MachineNicExtended]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this V1MachineHardwareExtended.

        the list of network interfaces of this machine with extended information  # noqa: E501

        :param nics: The nics of this V1MachineHardwareExtended.  # noqa: E501
        :type: list[V1MachineNicExtended]
        """
        if nics is None:
            raise ValueError("Invalid value for `nics`, must not be `None`")  # noqa: E501

        self._nics = nics

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
        if issubclass(V1MachineHardwareExtended, dict):
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
        if not isinstance(other, V1MachineHardwareExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
