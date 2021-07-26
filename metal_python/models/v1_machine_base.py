# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.15.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineBase(object):
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
        'allocation': 'V1MachineAllocation',
        'bios': 'V1MachineBIOS',
        'events': 'V1MachineRecentProvisioningEvents',
        'hardware': 'V1MachineHardware',
        'ledstate': 'V1ChassisIdentifyLEDState',
        'liveliness': 'str',
        'partition': 'V1PartitionResponse',
        'rackid': 'str',
        'size': 'V1SizeResponse',
        'state': 'V1MachineState',
        'tags': 'list[str]'
    }

    attribute_map = {
        'allocation': 'allocation',
        'bios': 'bios',
        'events': 'events',
        'hardware': 'hardware',
        'ledstate': 'ledstate',
        'liveliness': 'liveliness',
        'partition': 'partition',
        'rackid': 'rackid',
        'size': 'size',
        'state': 'state',
        'tags': 'tags'
    }

    def __init__(self, allocation=None, bios=None, events=None, hardware=None, ledstate=None, liveliness=None, partition=None, rackid=None, size=None, state=None, tags=None):  # noqa: E501
        """V1MachineBase - a model defined in Swagger"""  # noqa: E501

        self._allocation = None
        self._bios = None
        self._events = None
        self._hardware = None
        self._ledstate = None
        self._liveliness = None
        self._partition = None
        self._rackid = None
        self._size = None
        self._state = None
        self._tags = None
        self.discriminator = None

        if allocation is not None:
            self.allocation = allocation
        self.bios = bios
        self.events = events
        self.hardware = hardware
        self.ledstate = ledstate
        self.liveliness = liveliness
        if partition is not None:
            self.partition = partition
        if rackid is not None:
            self.rackid = rackid
        if size is not None:
            self.size = size
        self.state = state
        self.tags = tags

    @property
    def allocation(self):
        """Gets the allocation of this V1MachineBase.  # noqa: E501

        the allocation data of an allocated machine  # noqa: E501

        :return: The allocation of this V1MachineBase.  # noqa: E501
        :rtype: V1MachineAllocation
        """
        return self._allocation

    @allocation.setter
    def allocation(self, allocation):
        """Sets the allocation of this V1MachineBase.

        the allocation data of an allocated machine  # noqa: E501

        :param allocation: The allocation of this V1MachineBase.  # noqa: E501
        :type: V1MachineAllocation
        """

        self._allocation = allocation

    @property
    def bios(self):
        """Gets the bios of this V1MachineBase.  # noqa: E501

        bios information of this machine  # noqa: E501

        :return: The bios of this V1MachineBase.  # noqa: E501
        :rtype: V1MachineBIOS
        """
        return self._bios

    @bios.setter
    def bios(self, bios):
        """Sets the bios of this V1MachineBase.

        bios information of this machine  # noqa: E501

        :param bios: The bios of this V1MachineBase.  # noqa: E501
        :type: V1MachineBIOS
        """
        if bios is None:
            raise ValueError("Invalid value for `bios`, must not be `None`")  # noqa: E501

        self._bios = bios

    @property
    def events(self):
        """Gets the events of this V1MachineBase.  # noqa: E501

        recent events of this machine during provisioning  # noqa: E501

        :return: The events of this V1MachineBase.  # noqa: E501
        :rtype: V1MachineRecentProvisioningEvents
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this V1MachineBase.

        recent events of this machine during provisioning  # noqa: E501

        :param events: The events of this V1MachineBase.  # noqa: E501
        :type: V1MachineRecentProvisioningEvents
        """
        if events is None:
            raise ValueError("Invalid value for `events`, must not be `None`")  # noqa: E501

        self._events = events

    @property
    def hardware(self):
        """Gets the hardware of this V1MachineBase.  # noqa: E501

        the hardware of this machine  # noqa: E501

        :return: The hardware of this V1MachineBase.  # noqa: E501
        :rtype: V1MachineHardware
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this V1MachineBase.

        the hardware of this machine  # noqa: E501

        :param hardware: The hardware of this V1MachineBase.  # noqa: E501
        :type: V1MachineHardware
        """
        if hardware is None:
            raise ValueError("Invalid value for `hardware`, must not be `None`")  # noqa: E501

        self._hardware = hardware

    @property
    def ledstate(self):
        """Gets the ledstate of this V1MachineBase.  # noqa: E501

        the state of this chassis identify LED  # noqa: E501

        :return: The ledstate of this V1MachineBase.  # noqa: E501
        :rtype: V1ChassisIdentifyLEDState
        """
        return self._ledstate

    @ledstate.setter
    def ledstate(self, ledstate):
        """Sets the ledstate of this V1MachineBase.

        the state of this chassis identify LED  # noqa: E501

        :param ledstate: The ledstate of this V1MachineBase.  # noqa: E501
        :type: V1ChassisIdentifyLEDState
        """
        if ledstate is None:
            raise ValueError("Invalid value for `ledstate`, must not be `None`")  # noqa: E501

        self._ledstate = ledstate

    @property
    def liveliness(self):
        """Gets the liveliness of this V1MachineBase.  # noqa: E501

        the liveliness of this machine  # noqa: E501

        :return: The liveliness of this V1MachineBase.  # noqa: E501
        :rtype: str
        """
        return self._liveliness

    @liveliness.setter
    def liveliness(self, liveliness):
        """Sets the liveliness of this V1MachineBase.

        the liveliness of this machine  # noqa: E501

        :param liveliness: The liveliness of this V1MachineBase.  # noqa: E501
        :type: str
        """
        if liveliness is None:
            raise ValueError("Invalid value for `liveliness`, must not be `None`")  # noqa: E501

        self._liveliness = liveliness

    @property
    def partition(self):
        """Gets the partition of this V1MachineBase.  # noqa: E501

        the partition assigned to this machine  # noqa: E501

        :return: The partition of this V1MachineBase.  # noqa: E501
        :rtype: V1PartitionResponse
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this V1MachineBase.

        the partition assigned to this machine  # noqa: E501

        :param partition: The partition of this V1MachineBase.  # noqa: E501
        :type: V1PartitionResponse
        """

        self._partition = partition

    @property
    def rackid(self):
        """Gets the rackid of this V1MachineBase.  # noqa: E501

        the rack assigned to this machine  # noqa: E501

        :return: The rackid of this V1MachineBase.  # noqa: E501
        :rtype: str
        """
        return self._rackid

    @rackid.setter
    def rackid(self, rackid):
        """Sets the rackid of this V1MachineBase.

        the rack assigned to this machine  # noqa: E501

        :param rackid: The rackid of this V1MachineBase.  # noqa: E501
        :type: str
        """

        self._rackid = rackid

    @property
    def size(self):
        """Gets the size of this V1MachineBase.  # noqa: E501

        the size of this machine  # noqa: E501

        :return: The size of this V1MachineBase.  # noqa: E501
        :rtype: V1SizeResponse
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this V1MachineBase.

        the size of this machine  # noqa: E501

        :param size: The size of this V1MachineBase.  # noqa: E501
        :type: V1SizeResponse
        """

        self._size = size

    @property
    def state(self):
        """Gets the state of this V1MachineBase.  # noqa: E501

        the state of this machine  # noqa: E501

        :return: The state of this V1MachineBase.  # noqa: E501
        :rtype: V1MachineState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this V1MachineBase.

        the state of this machine  # noqa: E501

        :param state: The state of this V1MachineBase.  # noqa: E501
        :type: V1MachineState
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def tags(self):
        """Gets the tags of this V1MachineBase.  # noqa: E501

        tags for this machine  # noqa: E501

        :return: The tags of this V1MachineBase.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this V1MachineBase.

        tags for this machine  # noqa: E501

        :param tags: The tags of this V1MachineBase.  # noqa: E501
        :type: list[str]
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

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
        if issubclass(V1MachineBase, dict):
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
        if not isinstance(other, V1MachineBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other