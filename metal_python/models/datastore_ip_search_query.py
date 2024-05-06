# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.28.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DatastoreIPSearchQuery(object):
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
        'ipaddress': 'str',
        'machineid': 'str',
        'name': 'str',
        'networkid': 'str',
        'networkprefix': 'str',
        'projectid': 'str',
        'tags': 'list[str]',
        'type': 'str'
    }

    attribute_map = {
        'allocationuuid': 'allocationuuid',
        'ipaddress': 'ipaddress',
        'machineid': 'machineid',
        'name': 'name',
        'networkid': 'networkid',
        'networkprefix': 'networkprefix',
        'projectid': 'projectid',
        'tags': 'tags',
        'type': 'type'
    }

    def __init__(self, allocationuuid=None, ipaddress=None, machineid=None, name=None, networkid=None, networkprefix=None, projectid=None, tags=None, type=None):  # noqa: E501
        """DatastoreIPSearchQuery - a model defined in Swagger"""  # noqa: E501

        self._allocationuuid = None
        self._ipaddress = None
        self._machineid = None
        self._name = None
        self._networkid = None
        self._networkprefix = None
        self._projectid = None
        self._tags = None
        self._type = None
        self.discriminator = None

        if allocationuuid is not None:
            self.allocationuuid = allocationuuid
        if ipaddress is not None:
            self.ipaddress = ipaddress
        if machineid is not None:
            self.machineid = machineid
        if name is not None:
            self.name = name
        if networkid is not None:
            self.networkid = networkid
        if networkprefix is not None:
            self.networkprefix = networkprefix
        if projectid is not None:
            self.projectid = projectid
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type

    @property
    def allocationuuid(self):
        """Gets the allocationuuid of this DatastoreIPSearchQuery.  # noqa: E501

        a unique identifier for this ip address allocation, can be used to distinguish between ip address allocation over time.  # noqa: E501

        :return: The allocationuuid of this DatastoreIPSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._allocationuuid

    @allocationuuid.setter
    def allocationuuid(self, allocationuuid):
        """Sets the allocationuuid of this DatastoreIPSearchQuery.

        a unique identifier for this ip address allocation, can be used to distinguish between ip address allocation over time.  # noqa: E501

        :param allocationuuid: The allocationuuid of this DatastoreIPSearchQuery.  # noqa: E501
        :type: str
        """

        self._allocationuuid = allocationuuid

    @property
    def ipaddress(self):
        """Gets the ipaddress of this DatastoreIPSearchQuery.  # noqa: E501

        the address (ipv4 or ipv6) of this ip  # noqa: E501

        :return: The ipaddress of this DatastoreIPSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._ipaddress

    @ipaddress.setter
    def ipaddress(self, ipaddress):
        """Sets the ipaddress of this DatastoreIPSearchQuery.

        the address (ipv4 or ipv6) of this ip  # noqa: E501

        :param ipaddress: The ipaddress of this DatastoreIPSearchQuery.  # noqa: E501
        :type: str
        """

        self._ipaddress = ipaddress

    @property
    def machineid(self):
        """Gets the machineid of this DatastoreIPSearchQuery.  # noqa: E501

        the machine an ip address is associated to  # noqa: E501

        :return: The machineid of this DatastoreIPSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._machineid

    @machineid.setter
    def machineid(self, machineid):
        """Sets the machineid of this DatastoreIPSearchQuery.

        the machine an ip address is associated to  # noqa: E501

        :param machineid: The machineid of this DatastoreIPSearchQuery.  # noqa: E501
        :type: str
        """

        self._machineid = machineid

    @property
    def name(self):
        """Gets the name of this DatastoreIPSearchQuery.  # noqa: E501

        the name of the ip address  # noqa: E501

        :return: The name of this DatastoreIPSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatastoreIPSearchQuery.

        the name of the ip address  # noqa: E501

        :param name: The name of this DatastoreIPSearchQuery.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def networkid(self):
        """Gets the networkid of this DatastoreIPSearchQuery.  # noqa: E501

        the network this ip allocate request address belongs to  # noqa: E501

        :return: The networkid of this DatastoreIPSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._networkid

    @networkid.setter
    def networkid(self, networkid):
        """Sets the networkid of this DatastoreIPSearchQuery.

        the network this ip allocate request address belongs to  # noqa: E501

        :param networkid: The networkid of this DatastoreIPSearchQuery.  # noqa: E501
        :type: str
        """

        self._networkid = networkid

    @property
    def networkprefix(self):
        """Gets the networkprefix of this DatastoreIPSearchQuery.  # noqa: E501

        the prefix of the network this ip address belongs to  # noqa: E501

        :return: The networkprefix of this DatastoreIPSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._networkprefix

    @networkprefix.setter
    def networkprefix(self, networkprefix):
        """Sets the networkprefix of this DatastoreIPSearchQuery.

        the prefix of the network this ip address belongs to  # noqa: E501

        :param networkprefix: The networkprefix of this DatastoreIPSearchQuery.  # noqa: E501
        :type: str
        """

        self._networkprefix = networkprefix

    @property
    def projectid(self):
        """Gets the projectid of this DatastoreIPSearchQuery.  # noqa: E501

        the project this ip address belongs to, empty if not strong coupled  # noqa: E501

        :return: The projectid of this DatastoreIPSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._projectid

    @projectid.setter
    def projectid(self, projectid):
        """Sets the projectid of this DatastoreIPSearchQuery.

        the project this ip address belongs to, empty if not strong coupled  # noqa: E501

        :param projectid: The projectid of this DatastoreIPSearchQuery.  # noqa: E501
        :type: str
        """

        self._projectid = projectid

    @property
    def tags(self):
        """Gets the tags of this DatastoreIPSearchQuery.  # noqa: E501

        the tags that are assigned to this ip address  # noqa: E501

        :return: The tags of this DatastoreIPSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DatastoreIPSearchQuery.

        the tags that are assigned to this ip address  # noqa: E501

        :param tags: The tags of this DatastoreIPSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this DatastoreIPSearchQuery.  # noqa: E501

        the type of the ip address, ephemeral or static  # noqa: E501

        :return: The type of this DatastoreIPSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DatastoreIPSearchQuery.

        the type of the ip address, ephemeral or static  # noqa: E501

        :param type: The type of this DatastoreIPSearchQuery.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(DatastoreIPSearchQuery, dict):
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
        if not isinstance(other, DatastoreIPSearchQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
