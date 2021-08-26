# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.15.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1FilesystemLayoutResponse(object):
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
        'constraints': 'V1FilesystemLayoutConstraints',
        'description': 'str',
        'disks': 'list[V1Disk]',
        'filesystems': 'list[V1Filesystem]',
        'id': 'str',
        'logicalvolumes': 'list[V1LogicalVolume]',
        'name': 'str',
        'raid': 'list[V1Raid]',
        'volumegroups': 'list[V1VolumeGroup]'
    }

    attribute_map = {
        'constraints': 'constraints',
        'description': 'description',
        'disks': 'disks',
        'filesystems': 'filesystems',
        'id': 'id',
        'logicalvolumes': 'logicalvolumes',
        'name': 'name',
        'raid': 'raid',
        'volumegroups': 'volumegroups'
    }

    def __init__(self, constraints=None, description=None, disks=None, filesystems=None, id=None, logicalvolumes=None, name=None, raid=None, volumegroups=None):  # noqa: E501
        """V1FilesystemLayoutResponse - a model defined in Swagger"""  # noqa: E501

        self._constraints = None
        self._description = None
        self._disks = None
        self._filesystems = None
        self._id = None
        self._logicalvolumes = None
        self._name = None
        self._raid = None
        self._volumegroups = None
        self.discriminator = None

        self.constraints = constraints
        if description is not None:
            self.description = description
        if disks is not None:
            self.disks = disks
        if filesystems is not None:
            self.filesystems = filesystems
        self.id = id
        if logicalvolumes is not None:
            self.logicalvolumes = logicalvolumes
        if name is not None:
            self.name = name
        if raid is not None:
            self.raid = raid
        if volumegroups is not None:
            self.volumegroups = volumegroups

    @property
    def constraints(self):
        """Gets the constraints of this V1FilesystemLayoutResponse.  # noqa: E501

        constraints which must match that this layout is taken, if sizes and images are empty these are develop layouts  # noqa: E501

        :return: The constraints of this V1FilesystemLayoutResponse.  # noqa: E501
        :rtype: V1FilesystemLayoutConstraints
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this V1FilesystemLayoutResponse.

        constraints which must match that this layout is taken, if sizes and images are empty these are develop layouts  # noqa: E501

        :param constraints: The constraints of this V1FilesystemLayoutResponse.  # noqa: E501
        :type: V1FilesystemLayoutConstraints
        """
        if constraints is None:
            raise ValueError("Invalid value for `constraints`, must not be `None`")  # noqa: E501

        self._constraints = constraints

    @property
    def description(self):
        """Gets the description of this V1FilesystemLayoutResponse.  # noqa: E501

        a description for this entity  # noqa: E501

        :return: The description of this V1FilesystemLayoutResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1FilesystemLayoutResponse.

        a description for this entity  # noqa: E501

        :param description: The description of this V1FilesystemLayoutResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def disks(self):
        """Gets the disks of this V1FilesystemLayoutResponse.  # noqa: E501

        list of disks that belong to this layout  # noqa: E501

        :return: The disks of this V1FilesystemLayoutResponse.  # noqa: E501
        :rtype: list[V1Disk]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this V1FilesystemLayoutResponse.

        list of disks that belong to this layout  # noqa: E501

        :param disks: The disks of this V1FilesystemLayoutResponse.  # noqa: E501
        :type: list[V1Disk]
        """

        self._disks = disks

    @property
    def filesystems(self):
        """Gets the filesystems of this V1FilesystemLayoutResponse.  # noqa: E501

        list of filesystems to create  # noqa: E501

        :return: The filesystems of this V1FilesystemLayoutResponse.  # noqa: E501
        :rtype: list[V1Filesystem]
        """
        return self._filesystems

    @filesystems.setter
    def filesystems(self, filesystems):
        """Sets the filesystems of this V1FilesystemLayoutResponse.

        list of filesystems to create  # noqa: E501

        :param filesystems: The filesystems of this V1FilesystemLayoutResponse.  # noqa: E501
        :type: list[V1Filesystem]
        """

        self._filesystems = filesystems

    @property
    def id(self):
        """Gets the id of this V1FilesystemLayoutResponse.  # noqa: E501

        the unique ID of this entity  # noqa: E501

        :return: The id of this V1FilesystemLayoutResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1FilesystemLayoutResponse.

        the unique ID of this entity  # noqa: E501

        :param id: The id of this V1FilesystemLayoutResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def logicalvolumes(self):
        """Gets the logicalvolumes of this V1FilesystemLayoutResponse.  # noqa: E501

        list of logicalvolumes to create  # noqa: E501

        :return: The logicalvolumes of this V1FilesystemLayoutResponse.  # noqa: E501
        :rtype: list[V1LogicalVolume]
        """
        return self._logicalvolumes

    @logicalvolumes.setter
    def logicalvolumes(self, logicalvolumes):
        """Sets the logicalvolumes of this V1FilesystemLayoutResponse.

        list of logicalvolumes to create  # noqa: E501

        :param logicalvolumes: The logicalvolumes of this V1FilesystemLayoutResponse.  # noqa: E501
        :type: list[V1LogicalVolume]
        """

        self._logicalvolumes = logicalvolumes

    @property
    def name(self):
        """Gets the name of this V1FilesystemLayoutResponse.  # noqa: E501

        a readable name for this entity  # noqa: E501

        :return: The name of this V1FilesystemLayoutResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1FilesystemLayoutResponse.

        a readable name for this entity  # noqa: E501

        :param name: The name of this V1FilesystemLayoutResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def raid(self):
        """Gets the raid of this V1FilesystemLayoutResponse.  # noqa: E501

        list of raid arrays to create  # noqa: E501

        :return: The raid of this V1FilesystemLayoutResponse.  # noqa: E501
        :rtype: list[V1Raid]
        """
        return self._raid

    @raid.setter
    def raid(self, raid):
        """Sets the raid of this V1FilesystemLayoutResponse.

        list of raid arrays to create  # noqa: E501

        :param raid: The raid of this V1FilesystemLayoutResponse.  # noqa: E501
        :type: list[V1Raid]
        """

        self._raid = raid

    @property
    def volumegroups(self):
        """Gets the volumegroups of this V1FilesystemLayoutResponse.  # noqa: E501

        list of volumegroups to create  # noqa: E501

        :return: The volumegroups of this V1FilesystemLayoutResponse.  # noqa: E501
        :rtype: list[V1VolumeGroup]
        """
        return self._volumegroups

    @volumegroups.setter
    def volumegroups(self, volumegroups):
        """Sets the volumegroups of this V1FilesystemLayoutResponse.

        list of volumegroups to create  # noqa: E501

        :param volumegroups: The volumegroups of this V1FilesystemLayoutResponse.  # noqa: E501
        :type: list[V1VolumeGroup]
        """

        self._volumegroups = volumegroups

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
        if issubclass(V1FilesystemLayoutResponse, dict):
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
        if not isinstance(other, V1FilesystemLayoutResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
