# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.23.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineAllocateRequest(object):
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
        'filesystemlayoutid': 'str',
        'hostname': 'str',
        'imageid': 'str',
        'ips': 'list[str]',
        'name': 'str',
        'networks': 'list[V1MachineAllocationNetwork]',
        'partitionid': 'str',
        'placement_tags': 'list[str]',
        'projectid': 'str',
        'sizeid': 'str',
        'ssh_pub_keys': 'list[str]',
        'tags': 'list[str]',
        'user_data': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'description': 'description',
        'filesystemlayoutid': 'filesystemlayoutid',
        'hostname': 'hostname',
        'imageid': 'imageid',
        'ips': 'ips',
        'name': 'name',
        'networks': 'networks',
        'partitionid': 'partitionid',
        'placement_tags': 'placement_tags',
        'projectid': 'projectid',
        'sizeid': 'sizeid',
        'ssh_pub_keys': 'ssh_pub_keys',
        'tags': 'tags',
        'user_data': 'user_data',
        'uuid': 'uuid'
    }

    def __init__(self, description=None, filesystemlayoutid=None, hostname=None, imageid=None, ips=None, name=None, networks=None, partitionid=None, placement_tags=None, projectid=None, sizeid=None, ssh_pub_keys=None, tags=None, user_data=None, uuid=None):  # noqa: E501
        """V1MachineAllocateRequest - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._filesystemlayoutid = None
        self._hostname = None
        self._imageid = None
        self._ips = None
        self._name = None
        self._networks = None
        self._partitionid = None
        self._placement_tags = None
        self._projectid = None
        self._sizeid = None
        self._ssh_pub_keys = None
        self._tags = None
        self._user_data = None
        self._uuid = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if filesystemlayoutid is not None:
            self.filesystemlayoutid = filesystemlayoutid
        if hostname is not None:
            self.hostname = hostname
        self.imageid = imageid
        if ips is not None:
            self.ips = ips
        if name is not None:
            self.name = name
        if networks is not None:
            self.networks = networks
        self.partitionid = partitionid
        if placement_tags is not None:
            self.placement_tags = placement_tags
        self.projectid = projectid
        self.sizeid = sizeid
        self.ssh_pub_keys = ssh_pub_keys
        if tags is not None:
            self.tags = tags
        if user_data is not None:
            self.user_data = user_data
        if uuid is not None:
            self.uuid = uuid

    @property
    def description(self):
        """Gets the description of this V1MachineAllocateRequest.  # noqa: E501

        a description for this entity  # noqa: E501

        :return: The description of this V1MachineAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1MachineAllocateRequest.

        a description for this entity  # noqa: E501

        :param description: The description of this V1MachineAllocateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def filesystemlayoutid(self):
        """Gets the filesystemlayoutid of this V1MachineAllocateRequest.  # noqa: E501

        the filesystemlayout id to assing to this machine  # noqa: E501

        :return: The filesystemlayoutid of this V1MachineAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._filesystemlayoutid

    @filesystemlayoutid.setter
    def filesystemlayoutid(self, filesystemlayoutid):
        """Sets the filesystemlayoutid of this V1MachineAllocateRequest.

        the filesystemlayout id to assing to this machine  # noqa: E501

        :param filesystemlayoutid: The filesystemlayoutid of this V1MachineAllocateRequest.  # noqa: E501
        :type: str
        """

        self._filesystemlayoutid = filesystemlayoutid

    @property
    def hostname(self):
        """Gets the hostname of this V1MachineAllocateRequest.  # noqa: E501

        the hostname for the allocated machine (defaults to metal)  # noqa: E501

        :return: The hostname of this V1MachineAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this V1MachineAllocateRequest.

        the hostname for the allocated machine (defaults to metal)  # noqa: E501

        :param hostname: The hostname of this V1MachineAllocateRequest.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def imageid(self):
        """Gets the imageid of this V1MachineAllocateRequest.  # noqa: E501

        the image id to assign this machine to  # noqa: E501

        :return: The imageid of this V1MachineAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._imageid

    @imageid.setter
    def imageid(self, imageid):
        """Sets the imageid of this V1MachineAllocateRequest.

        the image id to assign this machine to  # noqa: E501

        :param imageid: The imageid of this V1MachineAllocateRequest.  # noqa: E501
        :type: str
        """
        if imageid is None:
            raise ValueError("Invalid value for `imageid`, must not be `None`")  # noqa: E501

        self._imageid = imageid

    @property
    def ips(self):
        """Gets the ips of this V1MachineAllocateRequest.  # noqa: E501

        the ips to attach to this machine additionally  # noqa: E501

        :return: The ips of this V1MachineAllocateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this V1MachineAllocateRequest.

        the ips to attach to this machine additionally  # noqa: E501

        :param ips: The ips of this V1MachineAllocateRequest.  # noqa: E501
        :type: list[str]
        """

        self._ips = ips

    @property
    def name(self):
        """Gets the name of this V1MachineAllocateRequest.  # noqa: E501

        a readable name for this entity  # noqa: E501

        :return: The name of this V1MachineAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1MachineAllocateRequest.

        a readable name for this entity  # noqa: E501

        :param name: The name of this V1MachineAllocateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def networks(self):
        """Gets the networks of this V1MachineAllocateRequest.  # noqa: E501

        the networks that this machine will be placed in.  # noqa: E501

        :return: The networks of this V1MachineAllocateRequest.  # noqa: E501
        :rtype: list[V1MachineAllocationNetwork]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this V1MachineAllocateRequest.

        the networks that this machine will be placed in.  # noqa: E501

        :param networks: The networks of this V1MachineAllocateRequest.  # noqa: E501
        :type: list[V1MachineAllocationNetwork]
        """

        self._networks = networks

    @property
    def partitionid(self):
        """Gets the partitionid of this V1MachineAllocateRequest.  # noqa: E501

        the partition id to assign this machine to  # noqa: E501

        :return: The partitionid of this V1MachineAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._partitionid

    @partitionid.setter
    def partitionid(self, partitionid):
        """Sets the partitionid of this V1MachineAllocateRequest.

        the partition id to assign this machine to  # noqa: E501

        :param partitionid: The partitionid of this V1MachineAllocateRequest.  # noqa: E501
        :type: str
        """
        if partitionid is None:
            raise ValueError("Invalid value for `partitionid`, must not be `None`")  # noqa: E501

        self._partitionid = partitionid

    @property
    def placement_tags(self):
        """Gets the placement_tags of this V1MachineAllocateRequest.  # noqa: E501

        by default machines are spread across the racks inside a partition for every project. if placement tags are provided, the machine candidate has an additional anti-affinity to other machines having the same tags  # noqa: E501

        :return: The placement_tags of this V1MachineAllocateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._placement_tags

    @placement_tags.setter
    def placement_tags(self, placement_tags):
        """Sets the placement_tags of this V1MachineAllocateRequest.

        by default machines are spread across the racks inside a partition for every project. if placement tags are provided, the machine candidate has an additional anti-affinity to other machines having the same tags  # noqa: E501

        :param placement_tags: The placement_tags of this V1MachineAllocateRequest.  # noqa: E501
        :type: list[str]
        """

        self._placement_tags = placement_tags

    @property
    def projectid(self):
        """Gets the projectid of this V1MachineAllocateRequest.  # noqa: E501

        the project id to assign this machine to  # noqa: E501

        :return: The projectid of this V1MachineAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._projectid

    @projectid.setter
    def projectid(self, projectid):
        """Sets the projectid of this V1MachineAllocateRequest.

        the project id to assign this machine to  # noqa: E501

        :param projectid: The projectid of this V1MachineAllocateRequest.  # noqa: E501
        :type: str
        """
        if projectid is None:
            raise ValueError("Invalid value for `projectid`, must not be `None`")  # noqa: E501

        self._projectid = projectid

    @property
    def sizeid(self):
        """Gets the sizeid of this V1MachineAllocateRequest.  # noqa: E501

        the size id to assign this machine to  # noqa: E501

        :return: The sizeid of this V1MachineAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._sizeid

    @sizeid.setter
    def sizeid(self, sizeid):
        """Sets the sizeid of this V1MachineAllocateRequest.

        the size id to assign this machine to  # noqa: E501

        :param sizeid: The sizeid of this V1MachineAllocateRequest.  # noqa: E501
        :type: str
        """
        if sizeid is None:
            raise ValueError("Invalid value for `sizeid`, must not be `None`")  # noqa: E501

        self._sizeid = sizeid

    @property
    def ssh_pub_keys(self):
        """Gets the ssh_pub_keys of this V1MachineAllocateRequest.  # noqa: E501

        the public ssh keys to access the machine with  # noqa: E501

        :return: The ssh_pub_keys of this V1MachineAllocateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._ssh_pub_keys

    @ssh_pub_keys.setter
    def ssh_pub_keys(self, ssh_pub_keys):
        """Sets the ssh_pub_keys of this V1MachineAllocateRequest.

        the public ssh keys to access the machine with  # noqa: E501

        :param ssh_pub_keys: The ssh_pub_keys of this V1MachineAllocateRequest.  # noqa: E501
        :type: list[str]
        """
        if ssh_pub_keys is None:
            raise ValueError("Invalid value for `ssh_pub_keys`, must not be `None`")  # noqa: E501

        self._ssh_pub_keys = ssh_pub_keys

    @property
    def tags(self):
        """Gets the tags of this V1MachineAllocateRequest.  # noqa: E501

        tags for this machine  # noqa: E501

        :return: The tags of this V1MachineAllocateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this V1MachineAllocateRequest.

        tags for this machine  # noqa: E501

        :param tags: The tags of this V1MachineAllocateRequest.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def user_data(self):
        """Gets the user_data of this V1MachineAllocateRequest.  # noqa: E501

        cloud-init.io compatible userdata must be base64 encoded  # noqa: E501

        :return: The user_data of this V1MachineAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this V1MachineAllocateRequest.

        cloud-init.io compatible userdata must be base64 encoded  # noqa: E501

        :param user_data: The user_data of this V1MachineAllocateRequest.  # noqa: E501
        :type: str
        """

        self._user_data = user_data

    @property
    def uuid(self):
        """Gets the uuid of this V1MachineAllocateRequest.  # noqa: E501

        if this field is set, this specific machine will be allocated if it is not in available state and not currently allocated. this field overrules size and partition  # noqa: E501

        :return: The uuid of this V1MachineAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this V1MachineAllocateRequest.

        if this field is set, this specific machine will be allocated if it is not in available state and not currently allocated. this field overrules size and partition  # noqa: E501

        :param uuid: The uuid of this V1MachineAllocateRequest.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(V1MachineAllocateRequest, dict):
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
        if not isinstance(other, V1MachineAllocateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
