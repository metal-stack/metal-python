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


class V1MachineProvisioningEvent(object):
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
        'event': 'str',
        'message': 'str',
        'time': 'datetime'
    }

    attribute_map = {
        'event': 'event',
        'message': 'message',
        'time': 'time'
    }

    def __init__(self, event=None, message=None, time=None):  # noqa: E501
        """V1MachineProvisioningEvent - a model defined in Swagger"""  # noqa: E501

        self._event = None
        self._message = None
        self._time = None
        self.discriminator = None

        self.event = event
        if message is not None:
            self.message = message
        if time is not None:
            self.time = time

    @property
    def event(self):
        """Gets the event of this V1MachineProvisioningEvent.  # noqa: E501

        the event emitted by the machine  # noqa: E501

        :return: The event of this V1MachineProvisioningEvent.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this V1MachineProvisioningEvent.

        the event emitted by the machine  # noqa: E501

        :param event: The event of this V1MachineProvisioningEvent.  # noqa: E501
        :type: str
        """
        if event is None:
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501

        self._event = event

    @property
    def message(self):
        """Gets the message of this V1MachineProvisioningEvent.  # noqa: E501

        an additional message to add to the event  # noqa: E501

        :return: The message of this V1MachineProvisioningEvent.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1MachineProvisioningEvent.

        an additional message to add to the event  # noqa: E501

        :param message: The message of this V1MachineProvisioningEvent.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def time(self):
        """Gets the time of this V1MachineProvisioningEvent.  # noqa: E501

        the time that this event was received  # noqa: E501

        :return: The time of this V1MachineProvisioningEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this V1MachineProvisioningEvent.

        the time that this event was received  # noqa: E501

        :param time: The time of this V1MachineProvisioningEvent.  # noqa: E501
        :type: datetime
        """

        self._time = time

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
        if issubclass(V1MachineProvisioningEvent, dict):
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
        if not isinstance(other, V1MachineProvisioningEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
