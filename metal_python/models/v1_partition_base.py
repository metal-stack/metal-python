# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.39.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1PartitionBase(object):
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
        'dns_servers': 'list[V1DNSServer]',
        'labels': 'dict(str, str)',
        'mgmtserviceaddress': 'str',
        'ntp_servers': 'list[V1NTPServer]',
        'privatenetworkprefixlength': 'int'
    }

    attribute_map = {
        'dns_servers': 'dns_servers',
        'labels': 'labels',
        'mgmtserviceaddress': 'mgmtserviceaddress',
        'ntp_servers': 'ntp_servers',
        'privatenetworkprefixlength': 'privatenetworkprefixlength'
    }

    def __init__(self, dns_servers=None, labels=None, mgmtserviceaddress=None, ntp_servers=None, privatenetworkprefixlength=None):  # noqa: E501
        """V1PartitionBase - a model defined in Swagger"""  # noqa: E501

        self._dns_servers = None
        self._labels = None
        self._mgmtserviceaddress = None
        self._ntp_servers = None
        self._privatenetworkprefixlength = None
        self.discriminator = None

        if dns_servers is not None:
            self.dns_servers = dns_servers
        if labels is not None:
            self.labels = labels
        if mgmtserviceaddress is not None:
            self.mgmtserviceaddress = mgmtserviceaddress
        if ntp_servers is not None:
            self.ntp_servers = ntp_servers
        if privatenetworkprefixlength is not None:
            self.privatenetworkprefixlength = privatenetworkprefixlength

    @property
    def dns_servers(self):
        """Gets the dns_servers of this V1PartitionBase.  # noqa: E501

        the dns servers for this partition  # noqa: E501

        :return: The dns_servers of this V1PartitionBase.  # noqa: E501
        :rtype: list[V1DNSServer]
        """
        return self._dns_servers

    @dns_servers.setter
    def dns_servers(self, dns_servers):
        """Sets the dns_servers of this V1PartitionBase.

        the dns servers for this partition  # noqa: E501

        :param dns_servers: The dns_servers of this V1PartitionBase.  # noqa: E501
        :type: list[V1DNSServer]
        """

        self._dns_servers = dns_servers

    @property
    def labels(self):
        """Gets the labels of this V1PartitionBase.  # noqa: E501

        free labels that you associate with this partition  # noqa: E501

        :return: The labels of this V1PartitionBase.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this V1PartitionBase.

        free labels that you associate with this partition  # noqa: E501

        :param labels: The labels of this V1PartitionBase.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def mgmtserviceaddress(self):
        """Gets the mgmtserviceaddress of this V1PartitionBase.  # noqa: E501

        the address to the management service of this partition  # noqa: E501

        :return: The mgmtserviceaddress of this V1PartitionBase.  # noqa: E501
        :rtype: str
        """
        return self._mgmtserviceaddress

    @mgmtserviceaddress.setter
    def mgmtserviceaddress(self, mgmtserviceaddress):
        """Sets the mgmtserviceaddress of this V1PartitionBase.

        the address to the management service of this partition  # noqa: E501

        :param mgmtserviceaddress: The mgmtserviceaddress of this V1PartitionBase.  # noqa: E501
        :type: str
        """

        self._mgmtserviceaddress = mgmtserviceaddress

    @property
    def ntp_servers(self):
        """Gets the ntp_servers of this V1PartitionBase.  # noqa: E501

        the ntp servers for this partition  # noqa: E501

        :return: The ntp_servers of this V1PartitionBase.  # noqa: E501
        :rtype: list[V1NTPServer]
        """
        return self._ntp_servers

    @ntp_servers.setter
    def ntp_servers(self, ntp_servers):
        """Sets the ntp_servers of this V1PartitionBase.

        the ntp servers for this partition  # noqa: E501

        :param ntp_servers: The ntp_servers of this V1PartitionBase.  # noqa: E501
        :type: list[V1NTPServer]
        """

        self._ntp_servers = ntp_servers

    @property
    def privatenetworkprefixlength(self):
        """Gets the privatenetworkprefixlength of this V1PartitionBase.  # noqa: E501

        the length of private networks for the machine's child networks in this partition, default 22  # noqa: E501

        :return: The privatenetworkprefixlength of this V1PartitionBase.  # noqa: E501
        :rtype: int
        """
        return self._privatenetworkprefixlength

    @privatenetworkprefixlength.setter
    def privatenetworkprefixlength(self, privatenetworkprefixlength):
        """Sets the privatenetworkprefixlength of this V1PartitionBase.

        the length of private networks for the machine's child networks in this partition, default 22  # noqa: E501

        :param privatenetworkprefixlength: The privatenetworkprefixlength of this V1PartitionBase.  # noqa: E501
        :type: int
        """
        if privatenetworkprefixlength is not None and privatenetworkprefixlength > 30:  # noqa: E501
            raise ValueError("Invalid value for `privatenetworkprefixlength`, must be a value less than or equal to `30`")  # noqa: E501
        if privatenetworkprefixlength is not None and privatenetworkprefixlength < 16:  # noqa: E501
            raise ValueError("Invalid value for `privatenetworkprefixlength`, must be a value greater than or equal to `16`")  # noqa: E501

        self._privatenetworkprefixlength = privatenetworkprefixlength

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
        if issubclass(V1PartitionBase, dict):
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
        if not isinstance(other, V1PartitionBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
