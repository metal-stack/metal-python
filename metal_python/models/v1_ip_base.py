# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.31.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1IPBase(object):
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
        'networkid': 'str',
        'projectid': 'str',
        'tags': 'list[str]',
        'type': 'str'
    }

    attribute_map = {
        'networkid': 'networkid',
        'projectid': 'projectid',
        'tags': 'tags',
        'type': 'type'
    }

    def __init__(self, networkid=None, projectid=None, tags=None, type=None):  # noqa: E501
        """V1IPBase - a model defined in Swagger"""  # noqa: E501

        self._networkid = None
        self._projectid = None
        self._tags = None
        self._type = None
        self.discriminator = None

        self.networkid = networkid
        self.projectid = projectid
        if tags is not None:
            self.tags = tags
        self.type = type

    @property
    def networkid(self):
        """Gets the networkid of this V1IPBase.  # noqa: E501

        the network this ip allocate request address belongs to  # noqa: E501

        :return: The networkid of this V1IPBase.  # noqa: E501
        :rtype: str
        """
        return self._networkid

    @networkid.setter
    def networkid(self, networkid):
        """Sets the networkid of this V1IPBase.

        the network this ip allocate request address belongs to  # noqa: E501

        :param networkid: The networkid of this V1IPBase.  # noqa: E501
        :type: str
        """
        if networkid is None:
            raise ValueError("Invalid value for `networkid`, must not be `None`")  # noqa: E501

        self._networkid = networkid

    @property
    def projectid(self):
        """Gets the projectid of this V1IPBase.  # noqa: E501

        the project this ip address belongs to  # noqa: E501

        :return: The projectid of this V1IPBase.  # noqa: E501
        :rtype: str
        """
        return self._projectid

    @projectid.setter
    def projectid(self, projectid):
        """Sets the projectid of this V1IPBase.

        the project this ip address belongs to  # noqa: E501

        :param projectid: The projectid of this V1IPBase.  # noqa: E501
        :type: str
        """
        if projectid is None:
            raise ValueError("Invalid value for `projectid`, must not be `None`")  # noqa: E501

        self._projectid = projectid

    @property
    def tags(self):
        """Gets the tags of this V1IPBase.  # noqa: E501

        free tags that you associate with this ip.  # noqa: E501

        :return: The tags of this V1IPBase.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this V1IPBase.

        free tags that you associate with this ip.  # noqa: E501

        :param tags: The tags of this V1IPBase.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this V1IPBase.  # noqa: E501

        the ip type, ephemeral leads to automatic cleanup of the ip address, static will enable re-use of the ip at a later point in time  # noqa: E501

        :return: The type of this V1IPBase.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1IPBase.

        the ip type, ephemeral leads to automatic cleanup of the ip address, static will enable re-use of the ip at a later point in time  # noqa: E501

        :param type: The type of this V1IPBase.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["ephemeral", "static"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

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
        if issubclass(V1IPBase, dict):
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
        if not isinstance(other, V1IPBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
