# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.37.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1FirewallEgressRule(object):
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
        'comment': 'str',
        'ports': 'list[int]',
        'protocol': 'str',
        'to': 'list[str]'
    }

    attribute_map = {
        'comment': 'comment',
        'ports': 'ports',
        'protocol': 'protocol',
        'to': 'to'
    }

    def __init__(self, comment=None, ports=None, protocol=None, to=None):  # noqa: E501
        """V1FirewallEgressRule - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self._ports = None
        self._protocol = None
        self._to = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        self.ports = ports
        if protocol is not None:
            self.protocol = protocol
        self.to = to

    @property
    def comment(self):
        """Gets the comment of this V1FirewallEgressRule.  # noqa: E501

        an optional comment describing what this rule is used for  # noqa: E501

        :return: The comment of this V1FirewallEgressRule.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this V1FirewallEgressRule.

        an optional comment describing what this rule is used for  # noqa: E501

        :param comment: The comment of this V1FirewallEgressRule.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def ports(self):
        """Gets the ports of this V1FirewallEgressRule.  # noqa: E501

        the ports affected by this rule  # noqa: E501

        :return: The ports of this V1FirewallEgressRule.  # noqa: E501
        :rtype: list[int]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this V1FirewallEgressRule.

        the ports affected by this rule  # noqa: E501

        :param ports: The ports of this V1FirewallEgressRule.  # noqa: E501
        :type: list[int]
        """
        if ports is None:
            raise ValueError("Invalid value for `ports`, must not be `None`")  # noqa: E501

        self._ports = ports

    @property
    def protocol(self):
        """Gets the protocol of this V1FirewallEgressRule.  # noqa: E501

        the protocol for the rule, defaults to tcp  # noqa: E501

        :return: The protocol of this V1FirewallEgressRule.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this V1FirewallEgressRule.

        the protocol for the rule, defaults to tcp  # noqa: E501

        :param protocol: The protocol of this V1FirewallEgressRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["tcp", "udp"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def to(self):
        """Gets the to of this V1FirewallEgressRule.  # noqa: E501

        the cidrs affected by this rule  # noqa: E501

        :return: The to of this V1FirewallEgressRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this V1FirewallEgressRule.

        the cidrs affected by this rule  # noqa: E501

        :param to: The to of this V1FirewallEgressRule.  # noqa: E501
        :type: list[str]
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

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
        if issubclass(V1FirewallEgressRule, dict):
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
        if not isinstance(other, V1FirewallEgressRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
