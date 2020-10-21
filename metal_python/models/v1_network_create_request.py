# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.9.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1NetworkCreateRequest(object):
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
        'description': 'str',
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
        'vrf': 'int',
        'vrfshared': 'bool'
    }

    attribute_map = {
        'description': 'description',
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
        'vrf': 'vrf',
        'vrfshared': 'vrfshared'
    }

    def __init__(self, description=None, destinationprefixes=None, id=None, labels=None, name=None, nat=None, parentnetworkid=None, partitionid=None, prefixes=None, privatesuper=None, projectid=None, underlay=None, vrf=None, vrfshared=None):  # noqa: E501
        """V1NetworkCreateRequest - a model defined in Swagger"""  # noqa: E501

        self._description = None
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
        self._vrfshared = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.destinationprefixes = destinationprefixes
        self.id = id
        if labels is not None:
            self.labels = labels
        if name is not None:
            self.name = name
        self.nat = nat
        self.parentnetworkid = parentnetworkid
        if partitionid is not None:
            self.partitionid = partitionid
        self.prefixes = prefixes
        self.privatesuper = privatesuper
        if projectid is not None:
            self.projectid = projectid
        self.underlay = underlay
        if vrf is not None:
            self.vrf = vrf
        if vrfshared is not None:
            self.vrfshared = vrfshared

    @property
    def description(self):
        """Gets the description of this V1NetworkCreateRequest.  # noqa: E501

        a description for this entity  # noqa: E501

        :return: The description of this V1NetworkCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1NetworkCreateRequest.

        a description for this entity  # noqa: E501

        :param description: The description of this V1NetworkCreateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def destinationprefixes(self):
        """Gets the destinationprefixes of this V1NetworkCreateRequest.  # noqa: E501

        the destination prefixes of this network  # noqa: E501

        :return: The destinationprefixes of this V1NetworkCreateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._destinationprefixes

    @destinationprefixes.setter
    def destinationprefixes(self, destinationprefixes):
        """Sets the destinationprefixes of this V1NetworkCreateRequest.

        the destination prefixes of this network  # noqa: E501

        :param destinationprefixes: The destinationprefixes of this V1NetworkCreateRequest.  # noqa: E501
        :type: list[str]
        """
        if destinationprefixes is None:
            raise ValueError("Invalid value for `destinationprefixes`, must not be `None`")  # noqa: E501

        self._destinationprefixes = destinationprefixes

    @property
    def id(self):
        """Gets the id of this V1NetworkCreateRequest.  # noqa: E501

        the unique ID of this entity, auto-generated if left empty  # noqa: E501

        :return: The id of this V1NetworkCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1NetworkCreateRequest.

        the unique ID of this entity, auto-generated if left empty  # noqa: E501

        :param id: The id of this V1NetworkCreateRequest.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this V1NetworkCreateRequest.  # noqa: E501

        free labels that you associate with this network.  # noqa: E501

        :return: The labels of this V1NetworkCreateRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this V1NetworkCreateRequest.

        free labels that you associate with this network.  # noqa: E501

        :param labels: The labels of this V1NetworkCreateRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this V1NetworkCreateRequest.  # noqa: E501

        a readable name for this entity  # noqa: E501

        :return: The name of this V1NetworkCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1NetworkCreateRequest.

        a readable name for this entity  # noqa: E501

        :param name: The name of this V1NetworkCreateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def nat(self):
        """Gets the nat of this V1NetworkCreateRequest.  # noqa: E501

        if set to true, packets leaving this network get masqueraded behind interface ip  # noqa: E501

        :return: The nat of this V1NetworkCreateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._nat

    @nat.setter
    def nat(self, nat):
        """Sets the nat of this V1NetworkCreateRequest.

        if set to true, packets leaving this network get masqueraded behind interface ip  # noqa: E501

        :param nat: The nat of this V1NetworkCreateRequest.  # noqa: E501
        :type: bool
        """
        if nat is None:
            raise ValueError("Invalid value for `nat`, must not be `None`")  # noqa: E501

        self._nat = nat

    @property
    def parentnetworkid(self):
        """Gets the parentnetworkid of this V1NetworkCreateRequest.  # noqa: E501

        the id of the parent network  # noqa: E501

        :return: The parentnetworkid of this V1NetworkCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._parentnetworkid

    @parentnetworkid.setter
    def parentnetworkid(self, parentnetworkid):
        """Sets the parentnetworkid of this V1NetworkCreateRequest.

        the id of the parent network  # noqa: E501

        :param parentnetworkid: The parentnetworkid of this V1NetworkCreateRequest.  # noqa: E501
        :type: str
        """
        if parentnetworkid is None:
            raise ValueError("Invalid value for `parentnetworkid`, must not be `None`")  # noqa: E501

        self._parentnetworkid = parentnetworkid

    @property
    def partitionid(self):
        """Gets the partitionid of this V1NetworkCreateRequest.  # noqa: E501

        the partition this network belongs to  # noqa: E501

        :return: The partitionid of this V1NetworkCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._partitionid

    @partitionid.setter
    def partitionid(self, partitionid):
        """Sets the partitionid of this V1NetworkCreateRequest.

        the partition this network belongs to  # noqa: E501

        :param partitionid: The partitionid of this V1NetworkCreateRequest.  # noqa: E501
        :type: str
        """

        self._partitionid = partitionid

    @property
    def prefixes(self):
        """Gets the prefixes of this V1NetworkCreateRequest.  # noqa: E501

        the prefixes of this network  # noqa: E501

        :return: The prefixes of this V1NetworkCreateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._prefixes

    @prefixes.setter
    def prefixes(self, prefixes):
        """Sets the prefixes of this V1NetworkCreateRequest.

        the prefixes of this network  # noqa: E501

        :param prefixes: The prefixes of this V1NetworkCreateRequest.  # noqa: E501
        :type: list[str]
        """
        if prefixes is None:
            raise ValueError("Invalid value for `prefixes`, must not be `None`")  # noqa: E501

        self._prefixes = prefixes

    @property
    def privatesuper(self):
        """Gets the privatesuper of this V1NetworkCreateRequest.  # noqa: E501

        if set to true, this network will serve as a partition's super network for the internal machine networks,there can only be one privatesuper network per partition  # noqa: E501

        :return: The privatesuper of this V1NetworkCreateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._privatesuper

    @privatesuper.setter
    def privatesuper(self, privatesuper):
        """Sets the privatesuper of this V1NetworkCreateRequest.

        if set to true, this network will serve as a partition's super network for the internal machine networks,there can only be one privatesuper network per partition  # noqa: E501

        :param privatesuper: The privatesuper of this V1NetworkCreateRequest.  # noqa: E501
        :type: bool
        """
        if privatesuper is None:
            raise ValueError("Invalid value for `privatesuper`, must not be `None`")  # noqa: E501

        self._privatesuper = privatesuper

    @property
    def projectid(self):
        """Gets the projectid of this V1NetworkCreateRequest.  # noqa: E501

        the project id this network belongs to, can be empty if globally available  # noqa: E501

        :return: The projectid of this V1NetworkCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._projectid

    @projectid.setter
    def projectid(self, projectid):
        """Sets the projectid of this V1NetworkCreateRequest.

        the project id this network belongs to, can be empty if globally available  # noqa: E501

        :param projectid: The projectid of this V1NetworkCreateRequest.  # noqa: E501
        :type: str
        """

        self._projectid = projectid

    @property
    def underlay(self):
        """Gets the underlay of this V1NetworkCreateRequest.  # noqa: E501

        if set to true, this network can be used for underlay communication  # noqa: E501

        :return: The underlay of this V1NetworkCreateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._underlay

    @underlay.setter
    def underlay(self, underlay):
        """Sets the underlay of this V1NetworkCreateRequest.

        if set to true, this network can be used for underlay communication  # noqa: E501

        :param underlay: The underlay of this V1NetworkCreateRequest.  # noqa: E501
        :type: bool
        """
        if underlay is None:
            raise ValueError("Invalid value for `underlay`, must not be `None`")  # noqa: E501

        self._underlay = underlay

    @property
    def vrf(self):
        """Gets the vrf of this V1NetworkCreateRequest.  # noqa: E501

        the vrf this network is associated with  # noqa: E501

        :return: The vrf of this V1NetworkCreateRequest.  # noqa: E501
        :rtype: int
        """
        return self._vrf

    @vrf.setter
    def vrf(self, vrf):
        """Sets the vrf of this V1NetworkCreateRequest.

        the vrf this network is associated with  # noqa: E501

        :param vrf: The vrf of this V1NetworkCreateRequest.  # noqa: E501
        :type: int
        """

        self._vrf = vrf

    @property
    def vrfshared(self):
        """Gets the vrfshared of this V1NetworkCreateRequest.  # noqa: E501

        if set to true, given vrf can be used by multiple networks, which is sometimes useful for network partioning (default: false)  # noqa: E501

        :return: The vrfshared of this V1NetworkCreateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._vrfshared

    @vrfshared.setter
    def vrfshared(self, vrfshared):
        """Sets the vrfshared of this V1NetworkCreateRequest.

        if set to true, given vrf can be used by multiple networks, which is sometimes useful for network partioning (default: false)  # noqa: E501

        :param vrfshared: The vrfshared of this V1NetworkCreateRequest.  # noqa: E501
        :type: bool
        """

        self._vrfshared = vrfshared

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
        if issubclass(V1NetworkCreateRequest, dict):
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
        if not isinstance(other, V1NetworkCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
