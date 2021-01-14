# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.11.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineRecentProvisioningEvents(object):
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
        'incomplete_provisioning_cycles': 'str',
        'last_event_time': 'datetime',
        'log': 'list[V1MachineProvisioningEvent]'
    }

    attribute_map = {
        'incomplete_provisioning_cycles': 'incomplete_provisioning_cycles',
        'last_event_time': 'last_event_time',
        'log': 'log'
    }

    def __init__(self, incomplete_provisioning_cycles=None, last_event_time=None, log=None):  # noqa: E501
        """V1MachineRecentProvisioningEvents - a model defined in Swagger"""  # noqa: E501

        self._incomplete_provisioning_cycles = None
        self._last_event_time = None
        self._log = None
        self.discriminator = None

        self.incomplete_provisioning_cycles = incomplete_provisioning_cycles
        self.last_event_time = last_event_time
        self.log = log

    @property
    def incomplete_provisioning_cycles(self):
        """Gets the incomplete_provisioning_cycles of this V1MachineRecentProvisioningEvents.  # noqa: E501

        the amount of incomplete provisioning cycles in the event container  # noqa: E501

        :return: The incomplete_provisioning_cycles of this V1MachineRecentProvisioningEvents.  # noqa: E501
        :rtype: str
        """
        return self._incomplete_provisioning_cycles

    @incomplete_provisioning_cycles.setter
    def incomplete_provisioning_cycles(self, incomplete_provisioning_cycles):
        """Sets the incomplete_provisioning_cycles of this V1MachineRecentProvisioningEvents.

        the amount of incomplete provisioning cycles in the event container  # noqa: E501

        :param incomplete_provisioning_cycles: The incomplete_provisioning_cycles of this V1MachineRecentProvisioningEvents.  # noqa: E501
        :type: str
        """
        if incomplete_provisioning_cycles is None:
            raise ValueError("Invalid value for `incomplete_provisioning_cycles`, must not be `None`")  # noqa: E501

        self._incomplete_provisioning_cycles = incomplete_provisioning_cycles

    @property
    def last_event_time(self):
        """Gets the last_event_time of this V1MachineRecentProvisioningEvents.  # noqa: E501

        the time where the last event was received  # noqa: E501

        :return: The last_event_time of this V1MachineRecentProvisioningEvents.  # noqa: E501
        :rtype: datetime
        """
        return self._last_event_time

    @last_event_time.setter
    def last_event_time(self, last_event_time):
        """Sets the last_event_time of this V1MachineRecentProvisioningEvents.

        the time where the last event was received  # noqa: E501

        :param last_event_time: The last_event_time of this V1MachineRecentProvisioningEvents.  # noqa: E501
        :type: datetime
        """
        if last_event_time is None:
            raise ValueError("Invalid value for `last_event_time`, must not be `None`")  # noqa: E501

        self._last_event_time = last_event_time

    @property
    def log(self):
        """Gets the log of this V1MachineRecentProvisioningEvents.  # noqa: E501

        the log of recent machine provisioning events  # noqa: E501

        :return: The log of this V1MachineRecentProvisioningEvents.  # noqa: E501
        :rtype: list[V1MachineProvisioningEvent]
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this V1MachineRecentProvisioningEvents.

        the log of recent machine provisioning events  # noqa: E501

        :param log: The log of this V1MachineRecentProvisioningEvents.  # noqa: E501
        :type: list[V1MachineProvisioningEvent]
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")  # noqa: E501

        self._log = log

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
        if issubclass(V1MachineRecentProvisioningEvents, dict):
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
        if not isinstance(other, V1MachineRecentProvisioningEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
