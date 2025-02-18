# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.39.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SwitchMigrateRequest(object):
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
        'new_switch_id': 'str',
        'old_switch_id': 'str'
    }

    attribute_map = {
        'new_switch_id': 'new_switch_id',
        'old_switch_id': 'old_switch_id'
    }

    def __init__(self, new_switch_id=None, old_switch_id=None):  # noqa: E501
        """V1SwitchMigrateRequest - a model defined in Swagger"""  # noqa: E501

        self._new_switch_id = None
        self._old_switch_id = None
        self.discriminator = None

        self.new_switch_id = new_switch_id
        self.old_switch_id = old_switch_id

    @property
    def new_switch_id(self):
        """Gets the new_switch_id of this V1SwitchMigrateRequest.  # noqa: E501

        the id of the new switch to migrate to  # noqa: E501

        :return: The new_switch_id of this V1SwitchMigrateRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_switch_id

    @new_switch_id.setter
    def new_switch_id(self, new_switch_id):
        """Sets the new_switch_id of this V1SwitchMigrateRequest.

        the id of the new switch to migrate to  # noqa: E501

        :param new_switch_id: The new_switch_id of this V1SwitchMigrateRequest.  # noqa: E501
        :type: str
        """
        if new_switch_id is None:
            raise ValueError("Invalid value for `new_switch_id`, must not be `None`")  # noqa: E501

        self._new_switch_id = new_switch_id

    @property
    def old_switch_id(self):
        """Gets the old_switch_id of this V1SwitchMigrateRequest.  # noqa: E501

        the id of the switch that should be migrated away from  # noqa: E501

        :return: The old_switch_id of this V1SwitchMigrateRequest.  # noqa: E501
        :rtype: str
        """
        return self._old_switch_id

    @old_switch_id.setter
    def old_switch_id(self, old_switch_id):
        """Sets the old_switch_id of this V1SwitchMigrateRequest.

        the id of the switch that should be migrated away from  # noqa: E501

        :param old_switch_id: The old_switch_id of this V1SwitchMigrateRequest.  # noqa: E501
        :type: str
        """
        if old_switch_id is None:
            raise ValueError("Invalid value for `old_switch_id`, must not be `None`")  # noqa: E501

        self._old_switch_id = old_switch_id

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
        if issubclass(V1SwitchMigrateRequest, dict):
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
        if not isinstance(other, V1SwitchMigrateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
