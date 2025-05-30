# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.41.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineHardware(object):
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
        'cpus': 'list[V1MetalCPU]',
        'disks': 'list[V1MachineBlockDevice]',
        'gpus': 'list[V1MetalGPU]',
        'memory': 'int',
        'nics': 'list[V1MachineNic]'
    }

    attribute_map = {
        'cpu_cores': 'cpu_cores',
        'cpus': 'cpus',
        'disks': 'disks',
        'gpus': 'gpus',
        'memory': 'memory',
        'nics': 'nics'
    }

    def __init__(self, cpu_cores=None, cpus=None, disks=None, gpus=None, memory=None, nics=None):  # noqa: E501
        """V1MachineHardware - a model defined in Swagger"""  # noqa: E501

        self._cpu_cores = None
        self._cpus = None
        self._disks = None
        self._gpus = None
        self._memory = None
        self._nics = None
        self.discriminator = None

        self.cpu_cores = cpu_cores
        if cpus is not None:
            self.cpus = cpus
        self.disks = disks
        if gpus is not None:
            self.gpus = gpus
        self.memory = memory
        self.nics = nics

    @property
    def cpu_cores(self):
        """Gets the cpu_cores of this V1MachineHardware.  # noqa: E501

        the number of cpu cores  # noqa: E501

        :return: The cpu_cores of this V1MachineHardware.  # noqa: E501
        :rtype: int
        """
        return self._cpu_cores

    @cpu_cores.setter
    def cpu_cores(self, cpu_cores):
        """Sets the cpu_cores of this V1MachineHardware.

        the number of cpu cores  # noqa: E501

        :param cpu_cores: The cpu_cores of this V1MachineHardware.  # noqa: E501
        :type: int
        """
        if cpu_cores is None:
            raise ValueError("Invalid value for `cpu_cores`, must not be `None`")  # noqa: E501

        self._cpu_cores = cpu_cores

    @property
    def cpus(self):
        """Gets the cpus of this V1MachineHardware.  # noqa: E501

        the cpu details  # noqa: E501

        :return: The cpus of this V1MachineHardware.  # noqa: E501
        :rtype: list[V1MetalCPU]
        """
        return self._cpus

    @cpus.setter
    def cpus(self, cpus):
        """Sets the cpus of this V1MachineHardware.

        the cpu details  # noqa: E501

        :param cpus: The cpus of this V1MachineHardware.  # noqa: E501
        :type: list[V1MetalCPU]
        """

        self._cpus = cpus

    @property
    def disks(self):
        """Gets the disks of this V1MachineHardware.  # noqa: E501

        the list of block devices of this machine  # noqa: E501

        :return: The disks of this V1MachineHardware.  # noqa: E501
        :rtype: list[V1MachineBlockDevice]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this V1MachineHardware.

        the list of block devices of this machine  # noqa: E501

        :param disks: The disks of this V1MachineHardware.  # noqa: E501
        :type: list[V1MachineBlockDevice]
        """
        if disks is None:
            raise ValueError("Invalid value for `disks`, must not be `None`")  # noqa: E501

        self._disks = disks

    @property
    def gpus(self):
        """Gets the gpus of this V1MachineHardware.  # noqa: E501

        the gpu details  # noqa: E501

        :return: The gpus of this V1MachineHardware.  # noqa: E501
        :rtype: list[V1MetalGPU]
        """
        return self._gpus

    @gpus.setter
    def gpus(self, gpus):
        """Sets the gpus of this V1MachineHardware.

        the gpu details  # noqa: E501

        :param gpus: The gpus of this V1MachineHardware.  # noqa: E501
        :type: list[V1MetalGPU]
        """

        self._gpus = gpus

    @property
    def memory(self):
        """Gets the memory of this V1MachineHardware.  # noqa: E501

        the total memory of the machine  # noqa: E501

        :return: The memory of this V1MachineHardware.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this V1MachineHardware.

        the total memory of the machine  # noqa: E501

        :param memory: The memory of this V1MachineHardware.  # noqa: E501
        :type: int
        """
        if memory is None:
            raise ValueError("Invalid value for `memory`, must not be `None`")  # noqa: E501

        self._memory = memory

    @property
    def nics(self):
        """Gets the nics of this V1MachineHardware.  # noqa: E501

        the list of network interfaces of this machine  # noqa: E501

        :return: The nics of this V1MachineHardware.  # noqa: E501
        :rtype: list[V1MachineNic]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this V1MachineHardware.

        the list of network interfaces of this machine  # noqa: E501

        :param nics: The nics of this V1MachineHardware.  # noqa: E501
        :type: list[V1MachineNic]
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
        if issubclass(V1MachineHardware, dict):
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
        if not isinstance(other, V1MachineHardware):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
