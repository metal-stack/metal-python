# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.26.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SwitchSync(object):
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
        'duration': 'int',
        'error': 'str',
        'time': 'datetime'
    }

    attribute_map = {
        'duration': 'duration',
        'error': 'error',
        'time': 'time'
    }

    def __init__(self, duration=None, error=None, time=None):  # noqa: E501
        """V1SwitchSync - a model defined in Swagger"""  # noqa: E501

        self._duration = None
        self._error = None
        self._time = None
        self.discriminator = None

        self.duration = duration
        if error is not None:
            self.error = error
        self.time = time

    @property
    def duration(self):
        """Gets the duration of this V1SwitchSync.  # noqa: E501

        the duration that lat switch sync took  # noqa: E501

        :return: The duration of this V1SwitchSync.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this V1SwitchSync.

        the duration that lat switch sync took  # noqa: E501

        :param duration: The duration of this V1SwitchSync.  # noqa: E501
        :type: int
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def error(self):
        """Gets the error of this V1SwitchSync.  # noqa: E501

        shows the error occurred during the sync  # noqa: E501

        :return: The error of this V1SwitchSync.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this V1SwitchSync.

        shows the error occurred during the sync  # noqa: E501

        :param error: The error of this V1SwitchSync.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def time(self):
        """Gets the time of this V1SwitchSync.  # noqa: E501

        point in time when the last switch sync happened  # noqa: E501

        :return: The time of this V1SwitchSync.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this V1SwitchSync.

        point in time when the last switch sync happened  # noqa: E501

        :param time: The time of this V1SwitchSync.  # noqa: E501
        :type: datetime
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

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
        if issubclass(V1SwitchSync, dict):
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
        if not isinstance(other, V1SwitchSync):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
