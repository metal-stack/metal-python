# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.19.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineRecentProvisioningEventsResponse(object):
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
        'events': 'int',
        'failed': 'list[str]'
    }

    attribute_map = {
        'events': 'events',
        'failed': 'failed'
    }

    def __init__(self, events=None, failed=None):  # noqa: E501
        """V1MachineRecentProvisioningEventsResponse - a model defined in Swagger"""  # noqa: E501

        self._events = None
        self._failed = None
        self.discriminator = None

        self.events = events
        self.failed = failed

    @property
    def events(self):
        """Gets the events of this V1MachineRecentProvisioningEventsResponse.  # noqa: E501

        number of events stored  # noqa: E501

        :return: The events of this V1MachineRecentProvisioningEventsResponse.  # noqa: E501
        :rtype: int
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this V1MachineRecentProvisioningEventsResponse.

        number of events stored  # noqa: E501

        :param events: The events of this V1MachineRecentProvisioningEventsResponse.  # noqa: E501
        :type: int
        """
        if events is None:
            raise ValueError("Invalid value for `events`, must not be `None`")  # noqa: E501

        self._events = events

    @property
    def failed(self):
        """Gets the failed of this V1MachineRecentProvisioningEventsResponse.  # noqa: E501

        slice of machineIDs for which event was not published  # noqa: E501

        :return: The failed of this V1MachineRecentProvisioningEventsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this V1MachineRecentProvisioningEventsResponse.

        slice of machineIDs for which event was not published  # noqa: E501

        :param failed: The failed of this V1MachineRecentProvisioningEventsResponse.  # noqa: E501
        :type: list[str]
        """
        if failed is None:
            raise ValueError("Invalid value for `failed`, must not be `None`")  # noqa: E501

        self._failed = failed

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
        if issubclass(V1MachineRecentProvisioningEventsResponse, dict):
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
        if not isinstance(other, V1MachineRecentProvisioningEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
