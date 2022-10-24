# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.21.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1IDMConfig(object):
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
        'idm_type': 'str'
    }

    attribute_map = {
        'idm_type': 'idm_type'
    }

    def __init__(self, idm_type=None):  # noqa: E501
        """V1IDMConfig - a model defined in Swagger"""  # noqa: E501

        self._idm_type = None
        self.discriminator = None

        if idm_type is not None:
            self.idm_type = idm_type

    @property
    def idm_type(self):
        """Gets the idm_type of this V1IDMConfig.  # noqa: E501


        :return: The idm_type of this V1IDMConfig.  # noqa: E501
        :rtype: str
        """
        return self._idm_type

    @idm_type.setter
    def idm_type(self, idm_type):
        """Sets the idm_type of this V1IDMConfig.


        :param idm_type: The idm_type of this V1IDMConfig.  # noqa: E501
        :type: str
        """

        self._idm_type = idm_type

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
        if issubclass(V1IDMConfig, dict):
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
        if not isinstance(other, V1IDMConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
