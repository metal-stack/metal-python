# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.39.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1PowerSupplyStatus(object):
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
        'health': 'str',
        'state': 'str'
    }

    attribute_map = {
        'health': 'health',
        'state': 'state'
    }

    def __init__(self, health=None, state=None):  # noqa: E501
        """V1PowerSupplyStatus - a model defined in Swagger"""  # noqa: E501

        self._health = None
        self._state = None
        self.discriminator = None

        self.health = health
        self.state = state

    @property
    def health(self):
        """Gets the health of this V1PowerSupplyStatus.  # noqa: E501


        :return: The health of this V1PowerSupplyStatus.  # noqa: E501
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this V1PowerSupplyStatus.


        :param health: The health of this V1PowerSupplyStatus.  # noqa: E501
        :type: str
        """
        if health is None:
            raise ValueError("Invalid value for `health`, must not be `None`")  # noqa: E501

        self._health = health

    @property
    def state(self):
        """Gets the state of this V1PowerSupplyStatus.  # noqa: E501


        :return: The state of this V1PowerSupplyStatus.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this V1PowerSupplyStatus.


        :param state: The state of this V1PowerSupplyStatus.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

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
        if issubclass(V1PowerSupplyStatus, dict):
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
        if not isinstance(other, V1PowerSupplyStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
