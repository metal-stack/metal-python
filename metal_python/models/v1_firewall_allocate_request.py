# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.39.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1FirewallAllocateRequest(object):
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
        'firewall_rules': 'V1FirewallRules'
    }

    attribute_map = {
        'firewall_rules': 'firewall_rules'
    }

    def __init__(self, firewall_rules=None):  # noqa: E501
        """V1FirewallAllocateRequest - a model defined in Swagger"""  # noqa: E501

        self._firewall_rules = None
        self.discriminator = None

        if firewall_rules is not None:
            self.firewall_rules = firewall_rules

    @property
    def firewall_rules(self):
        """Gets the firewall_rules of this V1FirewallAllocateRequest.  # noqa: E501

        optional egress and ingress firewall rules to deploy during firewall allocation  # noqa: E501

        :return: The firewall_rules of this V1FirewallAllocateRequest.  # noqa: E501
        :rtype: V1FirewallRules
        """
        return self._firewall_rules

    @firewall_rules.setter
    def firewall_rules(self, firewall_rules):
        """Sets the firewall_rules of this V1FirewallAllocateRequest.

        optional egress and ingress firewall rules to deploy during firewall allocation  # noqa: E501

        :param firewall_rules: The firewall_rules of this V1FirewallAllocateRequest.  # noqa: E501
        :type: V1FirewallRules
        """

        self._firewall_rules = firewall_rules

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
        if issubclass(V1FirewallAllocateRequest, dict):
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
        if not isinstance(other, V1FirewallAllocateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
