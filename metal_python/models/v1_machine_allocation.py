# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.41.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineAllocation(object):
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
        'allocationuuid': 'str',
        'boot_info': 'V1BootInfo',
        'created': 'datetime',
        'creator': 'str',
        'description': 'str',
        'dns_servers': 'list[V1DNSServer]',
        'filesystemlayout': 'V1FilesystemLayoutResponse',
        'firewall_rules': 'V1FirewallRules',
        'hostname': 'str',
        'image': 'V1ImageResponse',
        'name': 'str',
        'networks': 'list[V1MachineNetwork]',
        'ntp_servers': 'list[V1NTPServer]',
        'project': 'str',
        'reinstall': 'bool',
        'role': 'str',
        'ssh_pub_keys': 'list[str]',
        'succeeded': 'bool',
        'user_data': 'str',
        'vpn': 'V1MachineVPN'
    }

    attribute_map = {
        'allocationuuid': 'allocationuuid',
        'boot_info': 'boot_info',
        'created': 'created',
        'creator': 'creator',
        'description': 'description',
        'dns_servers': 'dns_servers',
        'filesystemlayout': 'filesystemlayout',
        'firewall_rules': 'firewall_rules',
        'hostname': 'hostname',
        'image': 'image',
        'name': 'name',
        'networks': 'networks',
        'ntp_servers': 'ntp_servers',
        'project': 'project',
        'reinstall': 'reinstall',
        'role': 'role',
        'ssh_pub_keys': 'ssh_pub_keys',
        'succeeded': 'succeeded',
        'user_data': 'user_data',
        'vpn': 'vpn'
    }

    def __init__(self, allocationuuid=None, boot_info=None, created=None, creator=None, description=None, dns_servers=None, filesystemlayout=None, firewall_rules=None, hostname=None, image=None, name=None, networks=None, ntp_servers=None, project=None, reinstall=None, role=None, ssh_pub_keys=None, succeeded=None, user_data=None, vpn=None):  # noqa: E501
        """V1MachineAllocation - a model defined in Swagger"""  # noqa: E501

        self._allocationuuid = None
        self._boot_info = None
        self._created = None
        self._creator = None
        self._description = None
        self._dns_servers = None
        self._filesystemlayout = None
        self._firewall_rules = None
        self._hostname = None
        self._image = None
        self._name = None
        self._networks = None
        self._ntp_servers = None
        self._project = None
        self._reinstall = None
        self._role = None
        self._ssh_pub_keys = None
        self._succeeded = None
        self._user_data = None
        self._vpn = None
        self.discriminator = None

        self.allocationuuid = allocationuuid
        if boot_info is not None:
            self.boot_info = boot_info
        self.created = created
        self.creator = creator
        if description is not None:
            self.description = description
        if dns_servers is not None:
            self.dns_servers = dns_servers
        if filesystemlayout is not None:
            self.filesystemlayout = filesystemlayout
        if firewall_rules is not None:
            self.firewall_rules = firewall_rules
        self.hostname = hostname
        if image is not None:
            self.image = image
        self.name = name
        self.networks = networks
        if ntp_servers is not None:
            self.ntp_servers = ntp_servers
        self.project = project
        self.reinstall = reinstall
        self.role = role
        self.ssh_pub_keys = ssh_pub_keys
        self.succeeded = succeeded
        if user_data is not None:
            self.user_data = user_data
        if vpn is not None:
            self.vpn = vpn

    @property
    def allocationuuid(self):
        """Gets the allocationuuid of this V1MachineAllocation.  # noqa: E501

        a unique identifier for this machine allocation, can be used to distinguish between machine allocations over time.  # noqa: E501

        :return: The allocationuuid of this V1MachineAllocation.  # noqa: E501
        :rtype: str
        """
        return self._allocationuuid

    @allocationuuid.setter
    def allocationuuid(self, allocationuuid):
        """Sets the allocationuuid of this V1MachineAllocation.

        a unique identifier for this machine allocation, can be used to distinguish between machine allocations over time.  # noqa: E501

        :param allocationuuid: The allocationuuid of this V1MachineAllocation.  # noqa: E501
        :type: str
        """
        if allocationuuid is None:
            raise ValueError("Invalid value for `allocationuuid`, must not be `None`")  # noqa: E501

        self._allocationuuid = allocationuuid

    @property
    def boot_info(self):
        """Gets the boot_info of this V1MachineAllocation.  # noqa: E501

        information required for booting the machine from HD  # noqa: E501

        :return: The boot_info of this V1MachineAllocation.  # noqa: E501
        :rtype: V1BootInfo
        """
        return self._boot_info

    @boot_info.setter
    def boot_info(self, boot_info):
        """Sets the boot_info of this V1MachineAllocation.

        information required for booting the machine from HD  # noqa: E501

        :param boot_info: The boot_info of this V1MachineAllocation.  # noqa: E501
        :type: V1BootInfo
        """

        self._boot_info = boot_info

    @property
    def created(self):
        """Gets the created of this V1MachineAllocation.  # noqa: E501

        the time when the machine was created  # noqa: E501

        :return: The created of this V1MachineAllocation.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this V1MachineAllocation.

        the time when the machine was created  # noqa: E501

        :param created: The created of this V1MachineAllocation.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def creator(self):
        """Gets the creator of this V1MachineAllocation.  # noqa: E501

        email of machine creator  # noqa: E501

        :return: The creator of this V1MachineAllocation.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this V1MachineAllocation.

        email of machine creator  # noqa: E501

        :param creator: The creator of this V1MachineAllocation.  # noqa: E501
        :type: str
        """
        if creator is None:
            raise ValueError("Invalid value for `creator`, must not be `None`")  # noqa: E501

        self._creator = creator

    @property
    def description(self):
        """Gets the description of this V1MachineAllocation.  # noqa: E501

        a description for this machine  # noqa: E501

        :return: The description of this V1MachineAllocation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1MachineAllocation.

        a description for this machine  # noqa: E501

        :param description: The description of this V1MachineAllocation.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dns_servers(self):
        """Gets the dns_servers of this V1MachineAllocation.  # noqa: E501

        the dns servers used for the machine  # noqa: E501

        :return: The dns_servers of this V1MachineAllocation.  # noqa: E501
        :rtype: list[V1DNSServer]
        """
        return self._dns_servers

    @dns_servers.setter
    def dns_servers(self, dns_servers):
        """Sets the dns_servers of this V1MachineAllocation.

        the dns servers used for the machine  # noqa: E501

        :param dns_servers: The dns_servers of this V1MachineAllocation.  # noqa: E501
        :type: list[V1DNSServer]
        """

        self._dns_servers = dns_servers

    @property
    def filesystemlayout(self):
        """Gets the filesystemlayout of this V1MachineAllocation.  # noqa: E501

        filesystemlayout to create on this machine  # noqa: E501

        :return: The filesystemlayout of this V1MachineAllocation.  # noqa: E501
        :rtype: V1FilesystemLayoutResponse
        """
        return self._filesystemlayout

    @filesystemlayout.setter
    def filesystemlayout(self, filesystemlayout):
        """Sets the filesystemlayout of this V1MachineAllocation.

        filesystemlayout to create on this machine  # noqa: E501

        :param filesystemlayout: The filesystemlayout of this V1MachineAllocation.  # noqa: E501
        :type: V1FilesystemLayoutResponse
        """

        self._filesystemlayout = filesystemlayout

    @property
    def firewall_rules(self):
        """Gets the firewall_rules of this V1MachineAllocation.  # noqa: E501

        a set of firewall rules to apply  # noqa: E501

        :return: The firewall_rules of this V1MachineAllocation.  # noqa: E501
        :rtype: V1FirewallRules
        """
        return self._firewall_rules

    @firewall_rules.setter
    def firewall_rules(self, firewall_rules):
        """Sets the firewall_rules of this V1MachineAllocation.

        a set of firewall rules to apply  # noqa: E501

        :param firewall_rules: The firewall_rules of this V1MachineAllocation.  # noqa: E501
        :type: V1FirewallRules
        """

        self._firewall_rules = firewall_rules

    @property
    def hostname(self):
        """Gets the hostname of this V1MachineAllocation.  # noqa: E501

        the hostname which will be used when creating the machine  # noqa: E501

        :return: The hostname of this V1MachineAllocation.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this V1MachineAllocation.

        the hostname which will be used when creating the machine  # noqa: E501

        :param hostname: The hostname of this V1MachineAllocation.  # noqa: E501
        :type: str
        """
        if hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def image(self):
        """Gets the image of this V1MachineAllocation.  # noqa: E501

        the image assigned to this machine  # noqa: E501

        :return: The image of this V1MachineAllocation.  # noqa: E501
        :rtype: V1ImageResponse
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this V1MachineAllocation.

        the image assigned to this machine  # noqa: E501

        :param image: The image of this V1MachineAllocation.  # noqa: E501
        :type: V1ImageResponse
        """

        self._image = image

    @property
    def name(self):
        """Gets the name of this V1MachineAllocation.  # noqa: E501

        the name of the machine  # noqa: E501

        :return: The name of this V1MachineAllocation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1MachineAllocation.

        the name of the machine  # noqa: E501

        :param name: The name of this V1MachineAllocation.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def networks(self):
        """Gets the networks of this V1MachineAllocation.  # noqa: E501

        the networks of this machine  # noqa: E501

        :return: The networks of this V1MachineAllocation.  # noqa: E501
        :rtype: list[V1MachineNetwork]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this V1MachineAllocation.

        the networks of this machine  # noqa: E501

        :param networks: The networks of this V1MachineAllocation.  # noqa: E501
        :type: list[V1MachineNetwork]
        """
        if networks is None:
            raise ValueError("Invalid value for `networks`, must not be `None`")  # noqa: E501

        self._networks = networks

    @property
    def ntp_servers(self):
        """Gets the ntp_servers of this V1MachineAllocation.  # noqa: E501

        the ntp servers used for the machine  # noqa: E501

        :return: The ntp_servers of this V1MachineAllocation.  # noqa: E501
        :rtype: list[V1NTPServer]
        """
        return self._ntp_servers

    @ntp_servers.setter
    def ntp_servers(self, ntp_servers):
        """Sets the ntp_servers of this V1MachineAllocation.

        the ntp servers used for the machine  # noqa: E501

        :param ntp_servers: The ntp_servers of this V1MachineAllocation.  # noqa: E501
        :type: list[V1NTPServer]
        """

        self._ntp_servers = ntp_servers

    @property
    def project(self):
        """Gets the project of this V1MachineAllocation.  # noqa: E501

        the project id that this machine is assigned to  # noqa: E501

        :return: The project of this V1MachineAllocation.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this V1MachineAllocation.

        the project id that this machine is assigned to  # noqa: E501

        :param project: The project of this V1MachineAllocation.  # noqa: E501
        :type: str
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def reinstall(self):
        """Gets the reinstall of this V1MachineAllocation.  # noqa: E501

        indicates whether to reinstall the machine  # noqa: E501

        :return: The reinstall of this V1MachineAllocation.  # noqa: E501
        :rtype: bool
        """
        return self._reinstall

    @reinstall.setter
    def reinstall(self, reinstall):
        """Sets the reinstall of this V1MachineAllocation.

        indicates whether to reinstall the machine  # noqa: E501

        :param reinstall: The reinstall of this V1MachineAllocation.  # noqa: E501
        :type: bool
        """
        if reinstall is None:
            raise ValueError("Invalid value for `reinstall`, must not be `None`")  # noqa: E501

        self._reinstall = reinstall

    @property
    def role(self):
        """Gets the role of this V1MachineAllocation.  # noqa: E501

        the role of the machine  # noqa: E501

        :return: The role of this V1MachineAllocation.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this V1MachineAllocation.

        the role of the machine  # noqa: E501

        :param role: The role of this V1MachineAllocation.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["firewall", "machine"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def ssh_pub_keys(self):
        """Gets the ssh_pub_keys of this V1MachineAllocation.  # noqa: E501

        the public ssh keys to access the machine with  # noqa: E501

        :return: The ssh_pub_keys of this V1MachineAllocation.  # noqa: E501
        :rtype: list[str]
        """
        return self._ssh_pub_keys

    @ssh_pub_keys.setter
    def ssh_pub_keys(self, ssh_pub_keys):
        """Sets the ssh_pub_keys of this V1MachineAllocation.

        the public ssh keys to access the machine with  # noqa: E501

        :param ssh_pub_keys: The ssh_pub_keys of this V1MachineAllocation.  # noqa: E501
        :type: list[str]
        """
        if ssh_pub_keys is None:
            raise ValueError("Invalid value for `ssh_pub_keys`, must not be `None`")  # noqa: E501

        self._ssh_pub_keys = ssh_pub_keys

    @property
    def succeeded(self):
        """Gets the succeeded of this V1MachineAllocation.  # noqa: E501

        if the allocation of the machine was successful, this is set to true  # noqa: E501

        :return: The succeeded of this V1MachineAllocation.  # noqa: E501
        :rtype: bool
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """Sets the succeeded of this V1MachineAllocation.

        if the allocation of the machine was successful, this is set to true  # noqa: E501

        :param succeeded: The succeeded of this V1MachineAllocation.  # noqa: E501
        :type: bool
        """
        if succeeded is None:
            raise ValueError("Invalid value for `succeeded`, must not be `None`")  # noqa: E501

        self._succeeded = succeeded

    @property
    def user_data(self):
        """Gets the user_data of this V1MachineAllocation.  # noqa: E501

        userdata to execute post installation tasks  # noqa: E501

        :return: The user_data of this V1MachineAllocation.  # noqa: E501
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this V1MachineAllocation.

        userdata to execute post installation tasks  # noqa: E501

        :param user_data: The user_data of this V1MachineAllocation.  # noqa: E501
        :type: str
        """

        self._user_data = user_data

    @property
    def vpn(self):
        """Gets the vpn of this V1MachineAllocation.  # noqa: E501

        vpn connection info for machine  # noqa: E501

        :return: The vpn of this V1MachineAllocation.  # noqa: E501
        :rtype: V1MachineVPN
        """
        return self._vpn

    @vpn.setter
    def vpn(self, vpn):
        """Sets the vpn of this V1MachineAllocation.

        vpn connection info for machine  # noqa: E501

        :param vpn: The vpn of this V1MachineAllocation.  # noqa: E501
        :type: V1MachineVPN
        """

        self._vpn = vpn

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
        if issubclass(V1MachineAllocation, dict):
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
        if not isinstance(other, V1MachineAllocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
