# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.32.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineNetwork(object):
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
        'asn': 'int',
        'destinationprefixes': 'list[str]',
        'ips': 'list[str]',
        'nat': 'bool',
        'networkid': 'str',
        'networktype': 'str',
        'prefixes': 'list[str]',
        'private': 'bool',
        'underlay': 'bool',
        'vrf': 'int'
    }

    attribute_map = {
        'asn': 'asn',
        'destinationprefixes': 'destinationprefixes',
        'ips': 'ips',
        'nat': 'nat',
        'networkid': 'networkid',
        'networktype': 'networktype',
        'prefixes': 'prefixes',
        'private': 'private',
        'underlay': 'underlay',
        'vrf': 'vrf'
    }

    def __init__(self, asn=None, destinationprefixes=None, ips=None, nat=None, networkid=None, networktype=None, prefixes=None, private=None, underlay=None, vrf=None):  # noqa: E501
        """V1MachineNetwork - a model defined in Swagger"""  # noqa: E501

        self._asn = None
        self._destinationprefixes = None
        self._ips = None
        self._nat = None
        self._networkid = None
        self._networktype = None
        self._prefixes = None
        self._private = None
        self._underlay = None
        self._vrf = None
        self.discriminator = None

        self.asn = asn
        self.destinationprefixes = destinationprefixes
        self.ips = ips
        self.nat = nat
        self.networkid = networkid
        self.networktype = networktype
        self.prefixes = prefixes
        self.private = private
        self.underlay = underlay
        self.vrf = vrf

    @property
    def asn(self):
        """Gets the asn of this V1MachineNetwork.  # noqa: E501

        ASN number for this network in the bgp configuration  # noqa: E501

        :return: The asn of this V1MachineNetwork.  # noqa: E501
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """Sets the asn of this V1MachineNetwork.

        ASN number for this network in the bgp configuration  # noqa: E501

        :param asn: The asn of this V1MachineNetwork.  # noqa: E501
        :type: int
        """
        if asn is None:
            raise ValueError("Invalid value for `asn`, must not be `None`")  # noqa: E501

        self._asn = asn

    @property
    def destinationprefixes(self):
        """Gets the destinationprefixes of this V1MachineNetwork.  # noqa: E501

        the destination prefixes of this network  # noqa: E501

        :return: The destinationprefixes of this V1MachineNetwork.  # noqa: E501
        :rtype: list[str]
        """
        return self._destinationprefixes

    @destinationprefixes.setter
    def destinationprefixes(self, destinationprefixes):
        """Sets the destinationprefixes of this V1MachineNetwork.

        the destination prefixes of this network  # noqa: E501

        :param destinationprefixes: The destinationprefixes of this V1MachineNetwork.  # noqa: E501
        :type: list[str]
        """
        if destinationprefixes is None:
            raise ValueError("Invalid value for `destinationprefixes`, must not be `None`")  # noqa: E501

        self._destinationprefixes = destinationprefixes

    @property
    def ips(self):
        """Gets the ips of this V1MachineNetwork.  # noqa: E501

        the ip addresses of the allocated machine in this vrf  # noqa: E501

        :return: The ips of this V1MachineNetwork.  # noqa: E501
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this V1MachineNetwork.

        the ip addresses of the allocated machine in this vrf  # noqa: E501

        :param ips: The ips of this V1MachineNetwork.  # noqa: E501
        :type: list[str]
        """
        if ips is None:
            raise ValueError("Invalid value for `ips`, must not be `None`")  # noqa: E501

        self._ips = ips

    @property
    def nat(self):
        """Gets the nat of this V1MachineNetwork.  # noqa: E501

        if set to true, packets leaving this network get masqueraded behind interface ip  # noqa: E501

        :return: The nat of this V1MachineNetwork.  # noqa: E501
        :rtype: bool
        """
        return self._nat

    @nat.setter
    def nat(self, nat):
        """Sets the nat of this V1MachineNetwork.

        if set to true, packets leaving this network get masqueraded behind interface ip  # noqa: E501

        :param nat: The nat of this V1MachineNetwork.  # noqa: E501
        :type: bool
        """
        if nat is None:
            raise ValueError("Invalid value for `nat`, must not be `None`")  # noqa: E501

        self._nat = nat

    @property
    def networkid(self):
        """Gets the networkid of this V1MachineNetwork.  # noqa: E501

        the networkID of the allocated machine in this vrf  # noqa: E501

        :return: The networkid of this V1MachineNetwork.  # noqa: E501
        :rtype: str
        """
        return self._networkid

    @networkid.setter
    def networkid(self, networkid):
        """Sets the networkid of this V1MachineNetwork.

        the networkID of the allocated machine in this vrf  # noqa: E501

        :param networkid: The networkid of this V1MachineNetwork.  # noqa: E501
        :type: str
        """
        if networkid is None:
            raise ValueError("Invalid value for `networkid`, must not be `None`")  # noqa: E501

        self._networkid = networkid

    @property
    def networktype(self):
        """Gets the networktype of this V1MachineNetwork.  # noqa: E501

        the network type, types can be looked up in the network package of metal-lib  # noqa: E501

        :return: The networktype of this V1MachineNetwork.  # noqa: E501
        :rtype: str
        """
        return self._networktype

    @networktype.setter
    def networktype(self, networktype):
        """Sets the networktype of this V1MachineNetwork.

        the network type, types can be looked up in the network package of metal-lib  # noqa: E501

        :param networktype: The networktype of this V1MachineNetwork.  # noqa: E501
        :type: str
        """
        if networktype is None:
            raise ValueError("Invalid value for `networktype`, must not be `None`")  # noqa: E501

        self._networktype = networktype

    @property
    def prefixes(self):
        """Gets the prefixes of this V1MachineNetwork.  # noqa: E501

        the prefixes of this network  # noqa: E501

        :return: The prefixes of this V1MachineNetwork.  # noqa: E501
        :rtype: list[str]
        """
        return self._prefixes

    @prefixes.setter
    def prefixes(self, prefixes):
        """Sets the prefixes of this V1MachineNetwork.

        the prefixes of this network  # noqa: E501

        :param prefixes: The prefixes of this V1MachineNetwork.  # noqa: E501
        :type: list[str]
        """
        if prefixes is None:
            raise ValueError("Invalid value for `prefixes`, must not be `None`")  # noqa: E501

        self._prefixes = prefixes

    @property
    def private(self):
        """Gets the private of this V1MachineNetwork.  # noqa: E501

        indicates whether this network is the private network of this machine  # noqa: E501

        :return: The private of this V1MachineNetwork.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this V1MachineNetwork.

        indicates whether this network is the private network of this machine  # noqa: E501

        :param private: The private of this V1MachineNetwork.  # noqa: E501
        :type: bool
        """
        if private is None:
            raise ValueError("Invalid value for `private`, must not be `None`")  # noqa: E501

        self._private = private

    @property
    def underlay(self):
        """Gets the underlay of this V1MachineNetwork.  # noqa: E501

        if set to true, this network can be used for underlay communication  # noqa: E501

        :return: The underlay of this V1MachineNetwork.  # noqa: E501
        :rtype: bool
        """
        return self._underlay

    @underlay.setter
    def underlay(self, underlay):
        """Sets the underlay of this V1MachineNetwork.

        if set to true, this network can be used for underlay communication  # noqa: E501

        :param underlay: The underlay of this V1MachineNetwork.  # noqa: E501
        :type: bool
        """
        if underlay is None:
            raise ValueError("Invalid value for `underlay`, must not be `None`")  # noqa: E501

        self._underlay = underlay

    @property
    def vrf(self):
        """Gets the vrf of this V1MachineNetwork.  # noqa: E501

        the vrf of the allocated machine  # noqa: E501

        :return: The vrf of this V1MachineNetwork.  # noqa: E501
        :rtype: int
        """
        return self._vrf

    @vrf.setter
    def vrf(self, vrf):
        """Sets the vrf of this V1MachineNetwork.

        the vrf of the allocated machine  # noqa: E501

        :param vrf: The vrf of this V1MachineNetwork.  # noqa: E501
        :type: int
        """
        if vrf is None:
            raise ValueError("Invalid value for `vrf`, must not be `None`")  # noqa: E501

        self._vrf = vrf

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
        if issubclass(V1MachineNetwork, dict):
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
        if not isinstance(other, V1MachineNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
