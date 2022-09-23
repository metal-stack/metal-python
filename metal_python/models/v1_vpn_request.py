# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.21.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1VPNRequest(object):
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
        'ephemeral': 'bool',
        'expiration': 'int',
        'pid': 'str'
    }

    attribute_map = {
        'ephemeral': 'ephemeral',
        'expiration': 'expiration',
        'pid': 'pid'
    }

    def __init__(self, ephemeral=None, expiration=None, pid=None):  # noqa: E501
        """V1VPNRequest - a model defined in Swagger"""  # noqa: E501

        self._ephemeral = None
        self._expiration = None
        self._pid = None
        self.discriminator = None

        self.ephemeral = ephemeral
        if expiration is not None:
            self.expiration = expiration
        self.pid = pid

    @property
    def ephemeral(self):
        """Gets the ephemeral of this V1VPNRequest.  # noqa: E501

        specifies if auth key should be ephemeral  # noqa: E501

        :return: The ephemeral of this V1VPNRequest.  # noqa: E501
        :rtype: bool
        """
        return self._ephemeral

    @ephemeral.setter
    def ephemeral(self, ephemeral):
        """Sets the ephemeral of this V1VPNRequest.

        specifies if auth key should be ephemeral  # noqa: E501

        :param ephemeral: The ephemeral of this V1VPNRequest.  # noqa: E501
        :type: bool
        """
        if ephemeral is None:
            raise ValueError("Invalid value for `ephemeral`, must not be `None`")  # noqa: E501

        self._ephemeral = ephemeral

    @property
    def expiration(self):
        """Gets the expiration of this V1VPNRequest.  # noqa: E501

        expiration time  # noqa: E501

        :return: The expiration of this V1VPNRequest.  # noqa: E501
        :rtype: int
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this V1VPNRequest.

        expiration time  # noqa: E501

        :param expiration: The expiration of this V1VPNRequest.  # noqa: E501
        :type: int
        """

        self._expiration = expiration

    @property
    def pid(self):
        """Gets the pid of this V1VPNRequest.  # noqa: E501

        project ID  # noqa: E501

        :return: The pid of this V1VPNRequest.  # noqa: E501
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this V1VPNRequest.

        project ID  # noqa: E501

        :param pid: The pid of this V1VPNRequest.  # noqa: E501
        :type: str
        """
        if pid is None:
            raise ValueError("Invalid value for `pid`, must not be `None`")  # noqa: E501

        self._pid = pid

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
        if issubclass(V1VPNRequest, dict):
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
        if not isinstance(other, V1VPNRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
