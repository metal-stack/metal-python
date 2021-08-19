# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.15.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SwitchNotifyRequest(object):
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
        'error': 'str',
        'sync_duration': 'int'
    }

    attribute_map = {
        'error': 'error',
        'sync_duration': 'sync_duration'
    }

    def __init__(self, error=None, sync_duration=None):  # noqa: E501
        """V1SwitchNotifyRequest - a model defined in Swagger"""  # noqa: E501

        self._error = None
        self._sync_duration = None
        self.discriminator = None

        self.error = error
        self.sync_duration = sync_duration

    @property
    def error(self):
        """Gets the error of this V1SwitchNotifyRequest.  # noqa: E501


        :return: The error of this V1SwitchNotifyRequest.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this V1SwitchNotifyRequest.


        :param error: The error of this V1SwitchNotifyRequest.  # noqa: E501
        :type: str
        """
        if error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

    @property
    def sync_duration(self):
        """Gets the sync_duration of this V1SwitchNotifyRequest.  # noqa: E501

        the duration of the switch synchronization  # noqa: E501

        :return: The sync_duration of this V1SwitchNotifyRequest.  # noqa: E501
        :rtype: int
        """
        return self._sync_duration

    @sync_duration.setter
    def sync_duration(self, sync_duration):
        """Sets the sync_duration of this V1SwitchNotifyRequest.

        the duration of the switch synchronization  # noqa: E501

        :param sync_duration: The sync_duration of this V1SwitchNotifyRequest.  # noqa: E501
        :type: int
        """
        if sync_duration is None:
            raise ValueError("Invalid value for `sync_duration`, must not be `None`")  # noqa: E501

        self._sync_duration = sync_duration

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
        if issubclass(V1SwitchNotifyRequest, dict):
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
        if not isinstance(other, V1SwitchNotifyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
