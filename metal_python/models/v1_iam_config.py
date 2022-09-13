# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.21.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1IAMConfig(object):
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
        'idm_config': 'V1IDMConfig',
        'issuer_config': 'V1IssuerConfig'
    }

    attribute_map = {
        'idm_config': 'idm_config',
        'issuer_config': 'issuer_config'
    }

    def __init__(self, idm_config=None, issuer_config=None):  # noqa: E501
        """V1IAMConfig - a model defined in Swagger"""  # noqa: E501

        self._idm_config = None
        self._issuer_config = None
        self.discriminator = None

        if idm_config is not None:
            self.idm_config = idm_config
        if issuer_config is not None:
            self.issuer_config = issuer_config

    @property
    def idm_config(self):
        """Gets the idm_config of this V1IAMConfig.  # noqa: E501


        :return: The idm_config of this V1IAMConfig.  # noqa: E501
        :rtype: V1IDMConfig
        """
        return self._idm_config

    @idm_config.setter
    def idm_config(self, idm_config):
        """Sets the idm_config of this V1IAMConfig.


        :param idm_config: The idm_config of this V1IAMConfig.  # noqa: E501
        :type: V1IDMConfig
        """

        self._idm_config = idm_config

    @property
    def issuer_config(self):
        """Gets the issuer_config of this V1IAMConfig.  # noqa: E501


        :return: The issuer_config of this V1IAMConfig.  # noqa: E501
        :rtype: V1IssuerConfig
        """
        return self._issuer_config

    @issuer_config.setter
    def issuer_config(self, issuer_config):
        """Sets the issuer_config of this V1IAMConfig.


        :param issuer_config: The issuer_config of this V1IAMConfig.  # noqa: E501
        :type: V1IssuerConfig
        """

        self._issuer_config = issuer_config

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
        if issubclass(V1IAMConfig, dict):
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
        if not isinstance(other, V1IAMConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
