# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.16.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1NetworkFindRequest(object):
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
        'destinationprefixes': 'list[str]',
        'id': 'str',
        'labels': 'dict(str, str)',
        'name': 'str',
        'nat': 'bool',
        'parentnetworkid': 'str',
        'partitionid': 'str',
        'prefixes': 'list[str]',
        'privatesuper': 'bool',
        'projectid': 'str',
        'underlay': 'bool',
        'vrf': 'int'
    }

    attribute_map = {
        'destinationprefixes': 'destinationprefixes',
        'id': 'id',
        'labels': 'labels',
        'name': 'name',
        'nat': 'nat',
        'parentnetworkid': 'parentnetworkid',
        'partitionid': 'partitionid',
        'prefixes': 'prefixes',
        'privatesuper': 'privatesuper',
        'projectid': 'projectid',
        'underlay': 'underlay',
        'vrf': 'vrf'
    }

    def __init__(self, destinationprefixes=None, id=None, labels=None, name=None, nat=None, parentnetworkid=None, partitionid=None, prefixes=None, privatesuper=None, projectid=None, underlay=None, vrf=None):  # noqa: E501
        """V1NetworkFindRequest - a model defined in Swagger"""  # noqa: E501

        self._destinationprefixes = None
        self._id = None
        self._labels = None
        self._name = None
        self._nat = None
        self._parentnetworkid = None
        self._partitionid = None
        self._prefixes = None
        self._privatesuper = None
        self._projectid = None
        self._underlay = None
        self._vrf = None
        self.discriminator = None

        if destinationprefixes is not None:
            self.destinationprefixes = destinationprefixes
        if id is not None:
            self.id = id
        if labels is not None:
            self.labels = labels
        if name is not None:
            self.name = name
        if nat is not None:
            self.nat = nat
        if parentnetworkid is not None:
            self.parentnetworkid = parentnetworkid
        if partitionid is not None:
            self.partitionid = partitionid
        if prefixes is not None:
            self.prefixes = prefixes
        if privatesuper is not None:
            self.privatesuper = privatesuper
        if projectid is not None:
            self.projectid = projectid
        if underlay is not None:
            self.underlay = underlay
        if vrf is not None:
            self.vrf = vrf

    @property
    def destinationprefixes(self):
        """Gets the destinationprefixes of this V1NetworkFindRequest.  # noqa: E501


        :return: The destinationprefixes of this V1NetworkFindRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._destinationprefixes

    @destinationprefixes.setter
    def destinationprefixes(self, destinationprefixes):
        """Sets the destinationprefixes of this V1NetworkFindRequest.


        :param destinationprefixes: The destinationprefixes of this V1NetworkFindRequest.  # noqa: E501
        :type: list[str]
        """

        self._destinationprefixes = destinationprefixes

    @property
    def id(self):
        """Gets the id of this V1NetworkFindRequest.  # noqa: E501


        :return: The id of this V1NetworkFindRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1NetworkFindRequest.


        :param id: The id of this V1NetworkFindRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this V1NetworkFindRequest.  # noqa: E501


        :return: The labels of this V1NetworkFindRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this V1NetworkFindRequest.


        :param labels: The labels of this V1NetworkFindRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this V1NetworkFindRequest.  # noqa: E501


        :return: The name of this V1NetworkFindRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1NetworkFindRequest.


        :param name: The name of this V1NetworkFindRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def nat(self):
        """Gets the nat of this V1NetworkFindRequest.  # noqa: E501


        :return: The nat of this V1NetworkFindRequest.  # noqa: E501
        :rtype: bool
        """
        return self._nat

    @nat.setter
    def nat(self, nat):
        """Sets the nat of this V1NetworkFindRequest.


        :param nat: The nat of this V1NetworkFindRequest.  # noqa: E501
        :type: bool
        """

        self._nat = nat

    @property
    def parentnetworkid(self):
        """Gets the parentnetworkid of this V1NetworkFindRequest.  # noqa: E501


        :return: The parentnetworkid of this V1NetworkFindRequest.  # noqa: E501
        :rtype: str
        """
        return self._parentnetworkid

    @parentnetworkid.setter
    def parentnetworkid(self, parentnetworkid):
        """Sets the parentnetworkid of this V1NetworkFindRequest.


        :param parentnetworkid: The parentnetworkid of this V1NetworkFindRequest.  # noqa: E501
        :type: str
        """

        self._parentnetworkid = parentnetworkid

    @property
    def partitionid(self):
        """Gets the partitionid of this V1NetworkFindRequest.  # noqa: E501


        :return: The partitionid of this V1NetworkFindRequest.  # noqa: E501
        :rtype: str
        """
        return self._partitionid

    @partitionid.setter
    def partitionid(self, partitionid):
        """Sets the partitionid of this V1NetworkFindRequest.


        :param partitionid: The partitionid of this V1NetworkFindRequest.  # noqa: E501
        :type: str
        """

        self._partitionid = partitionid

    @property
    def prefixes(self):
        """Gets the prefixes of this V1NetworkFindRequest.  # noqa: E501


        :return: The prefixes of this V1NetworkFindRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._prefixes

    @prefixes.setter
    def prefixes(self, prefixes):
        """Sets the prefixes of this V1NetworkFindRequest.


        :param prefixes: The prefixes of this V1NetworkFindRequest.  # noqa: E501
        :type: list[str]
        """

        self._prefixes = prefixes

    @property
    def privatesuper(self):
        """Gets the privatesuper of this V1NetworkFindRequest.  # noqa: E501


        :return: The privatesuper of this V1NetworkFindRequest.  # noqa: E501
        :rtype: bool
        """
        return self._privatesuper

    @privatesuper.setter
    def privatesuper(self, privatesuper):
        """Sets the privatesuper of this V1NetworkFindRequest.


        :param privatesuper: The privatesuper of this V1NetworkFindRequest.  # noqa: E501
        :type: bool
        """

        self._privatesuper = privatesuper

    @property
    def projectid(self):
        """Gets the projectid of this V1NetworkFindRequest.  # noqa: E501


        :return: The projectid of this V1NetworkFindRequest.  # noqa: E501
        :rtype: str
        """
        return self._projectid

    @projectid.setter
    def projectid(self, projectid):
        """Sets the projectid of this V1NetworkFindRequest.


        :param projectid: The projectid of this V1NetworkFindRequest.  # noqa: E501
        :type: str
        """

        self._projectid = projectid

    @property
    def underlay(self):
        """Gets the underlay of this V1NetworkFindRequest.  # noqa: E501


        :return: The underlay of this V1NetworkFindRequest.  # noqa: E501
        :rtype: bool
        """
        return self._underlay

    @underlay.setter
    def underlay(self, underlay):
        """Sets the underlay of this V1NetworkFindRequest.


        :param underlay: The underlay of this V1NetworkFindRequest.  # noqa: E501
        :type: bool
        """

        self._underlay = underlay

    @property
    def vrf(self):
        """Gets the vrf of this V1NetworkFindRequest.  # noqa: E501


        :return: The vrf of this V1NetworkFindRequest.  # noqa: E501
        :rtype: int
        """
        return self._vrf

    @vrf.setter
    def vrf(self, vrf):
        """Sets the vrf of this V1NetworkFindRequest.


        :param vrf: The vrf of this V1NetworkFindRequest.  # noqa: E501
        :type: int
        """

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
        if issubclass(V1NetworkFindRequest, dict):
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
        if not isinstance(other, V1NetworkFindRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
