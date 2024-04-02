# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.28.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SwitchFindRequest(object):
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
        'id': 'str',
        'name': 'str',
        'osvendor': 'str',
        'osversion': 'str',
        'partitionid': 'str',
        'rackid': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'osvendor': 'osvendor',
        'osversion': 'osversion',
        'partitionid': 'partitionid',
        'rackid': 'rackid'
    }

    def __init__(self, id=None, name=None, osvendor=None, osversion=None, partitionid=None, rackid=None):  # noqa: E501
        """V1SwitchFindRequest - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._osvendor = None
        self._osversion = None
        self._partitionid = None
        self._rackid = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if osvendor is not None:
            self.osvendor = osvendor
        if osversion is not None:
            self.osversion = osversion
        if partitionid is not None:
            self.partitionid = partitionid
        if rackid is not None:
            self.rackid = rackid

    @property
    def id(self):
        """Gets the id of this V1SwitchFindRequest.  # noqa: E501


        :return: The id of this V1SwitchFindRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1SwitchFindRequest.


        :param id: The id of this V1SwitchFindRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this V1SwitchFindRequest.  # noqa: E501


        :return: The name of this V1SwitchFindRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1SwitchFindRequest.


        :param name: The name of this V1SwitchFindRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def osvendor(self):
        """Gets the osvendor of this V1SwitchFindRequest.  # noqa: E501


        :return: The osvendor of this V1SwitchFindRequest.  # noqa: E501
        :rtype: str
        """
        return self._osvendor

    @osvendor.setter
    def osvendor(self, osvendor):
        """Sets the osvendor of this V1SwitchFindRequest.


        :param osvendor: The osvendor of this V1SwitchFindRequest.  # noqa: E501
        :type: str
        """

        self._osvendor = osvendor

    @property
    def osversion(self):
        """Gets the osversion of this V1SwitchFindRequest.  # noqa: E501


        :return: The osversion of this V1SwitchFindRequest.  # noqa: E501
        :rtype: str
        """
        return self._osversion

    @osversion.setter
    def osversion(self, osversion):
        """Sets the osversion of this V1SwitchFindRequest.


        :param osversion: The osversion of this V1SwitchFindRequest.  # noqa: E501
        :type: str
        """

        self._osversion = osversion

    @property
    def partitionid(self):
        """Gets the partitionid of this V1SwitchFindRequest.  # noqa: E501


        :return: The partitionid of this V1SwitchFindRequest.  # noqa: E501
        :rtype: str
        """
        return self._partitionid

    @partitionid.setter
    def partitionid(self, partitionid):
        """Sets the partitionid of this V1SwitchFindRequest.


        :param partitionid: The partitionid of this V1SwitchFindRequest.  # noqa: E501
        :type: str
        """

        self._partitionid = partitionid

    @property
    def rackid(self):
        """Gets the rackid of this V1SwitchFindRequest.  # noqa: E501


        :return: The rackid of this V1SwitchFindRequest.  # noqa: E501
        :rtype: str
        """
        return self._rackid

    @rackid.setter
    def rackid(self, rackid):
        """Sets the rackid of this V1SwitchFindRequest.


        :param rackid: The rackid of this V1SwitchFindRequest.  # noqa: E501
        :type: str
        """

        self._rackid = rackid

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
        if issubclass(V1SwitchFindRequest, dict):
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
        if not isinstance(other, V1SwitchFindRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
