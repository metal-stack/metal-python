# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.11.4-1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineAllocationNetwork(object):
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
        'autoacquire': 'bool',
        'networkid': 'str'
    }

    attribute_map = {
        'autoacquire': 'autoacquire',
        'networkid': 'networkid'
    }

    def __init__(self, autoacquire=None, networkid=None):  # noqa: E501
        """V1MachineAllocationNetwork - a model defined in Swagger"""  # noqa: E501

        self._autoacquire = None
        self._networkid = None
        self.discriminator = None

        self.autoacquire = autoacquire
        self.networkid = networkid

    @property
    def autoacquire(self):
        """Gets the autoacquire of this V1MachineAllocationNetwork.  # noqa: E501

        will automatically acquire an ip in this network if set to true, default is true  # noqa: E501

        :return: The autoacquire of this V1MachineAllocationNetwork.  # noqa: E501
        :rtype: bool
        """
        return self._autoacquire

    @autoacquire.setter
    def autoacquire(self, autoacquire):
        """Sets the autoacquire of this V1MachineAllocationNetwork.

        will automatically acquire an ip in this network if set to true, default is true  # noqa: E501

        :param autoacquire: The autoacquire of this V1MachineAllocationNetwork.  # noqa: E501
        :type: bool
        """
        if autoacquire is None:
            raise ValueError("Invalid value for `autoacquire`, must not be `None`")  # noqa: E501

        self._autoacquire = autoacquire

    @property
    def networkid(self):
        """Gets the networkid of this V1MachineAllocationNetwork.  # noqa: E501

        the id of the network that this machine will be placed in  # noqa: E501

        :return: The networkid of this V1MachineAllocationNetwork.  # noqa: E501
        :rtype: str
        """
        return self._networkid

    @networkid.setter
    def networkid(self, networkid):
        """Sets the networkid of this V1MachineAllocationNetwork.

        the id of the network that this machine will be placed in  # noqa: E501

        :param networkid: The networkid of this V1MachineAllocationNetwork.  # noqa: E501
        :type: str
        """
        if networkid is None:
            raise ValueError("Invalid value for `networkid`, must not be `None`")  # noqa: E501

        self._networkid = networkid

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
        if issubclass(V1MachineAllocationNetwork, dict):
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
        if not isinstance(other, V1MachineAllocationNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
