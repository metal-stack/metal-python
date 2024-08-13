# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.33.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1ChassisIdentifyLEDState(object):
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
        'description': 'str',
        'value': 'str'
    }

    attribute_map = {
        'description': 'description',
        'value': 'value'
    }

    def __init__(self, description=None, value=None):  # noqa: E501
        """V1ChassisIdentifyLEDState - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._value = None
        self.discriminator = None

        self.description = description
        self.value = value

    @property
    def description(self):
        """Gets the description of this V1ChassisIdentifyLEDState.  # noqa: E501

        a description why this chassis identify LED is in the given state  # noqa: E501

        :return: The description of this V1ChassisIdentifyLEDState.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1ChassisIdentifyLEDState.

        a description why this chassis identify LED is in the given state  # noqa: E501

        :param description: The description of this V1ChassisIdentifyLEDState.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def value(self):
        """Gets the value of this V1ChassisIdentifyLEDState.  # noqa: E501

        the state of this chassis identify LED. empty means LED-OFF  # noqa: E501

        :return: The value of this V1ChassisIdentifyLEDState.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this V1ChassisIdentifyLEDState.

        the state of this chassis identify LED. empty means LED-OFF  # noqa: E501

        :param value: The value of this V1ChassisIdentifyLEDState.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(V1ChassisIdentifyLEDState, dict):
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
        if not isinstance(other, V1ChassisIdentifyLEDState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
