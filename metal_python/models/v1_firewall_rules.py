# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.40.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1FirewallRules(object):
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
        'egress': 'list[V1FirewallEgressRule]',
        'ingress': 'list[V1FirewallIngressRule]'
    }

    attribute_map = {
        'egress': 'egress',
        'ingress': 'ingress'
    }

    def __init__(self, egress=None, ingress=None):  # noqa: E501
        """V1FirewallRules - a model defined in Swagger"""  # noqa: E501

        self._egress = None
        self._ingress = None
        self.discriminator = None

        if egress is not None:
            self.egress = egress
        if ingress is not None:
            self.ingress = ingress

    @property
    def egress(self):
        """Gets the egress of this V1FirewallRules.  # noqa: E501

        list of egress rules to be deployed during firewall allocation  # noqa: E501

        :return: The egress of this V1FirewallRules.  # noqa: E501
        :rtype: list[V1FirewallEgressRule]
        """
        return self._egress

    @egress.setter
    def egress(self, egress):
        """Sets the egress of this V1FirewallRules.

        list of egress rules to be deployed during firewall allocation  # noqa: E501

        :param egress: The egress of this V1FirewallRules.  # noqa: E501
        :type: list[V1FirewallEgressRule]
        """

        self._egress = egress

    @property
    def ingress(self):
        """Gets the ingress of this V1FirewallRules.  # noqa: E501

        list of ingress rules to be deployed during firewall allocation  # noqa: E501

        :return: The ingress of this V1FirewallRules.  # noqa: E501
        :rtype: list[V1FirewallIngressRule]
        """
        return self._ingress

    @ingress.setter
    def ingress(self, ingress):
        """Sets the ingress of this V1FirewallRules.

        list of ingress rules to be deployed during firewall allocation  # noqa: E501

        :param ingress: The ingress of this V1FirewallRules.  # noqa: E501
        :type: list[V1FirewallIngressRule]
        """

        self._ingress = ingress

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
        if issubclass(V1FirewallRules, dict):
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
        if not isinstance(other, V1FirewallRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
