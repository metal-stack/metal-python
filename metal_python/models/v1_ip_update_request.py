# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.28.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1IPUpdateRequest(object):
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
        'ipaddress': 'str',
        'name': 'str',
        'tags': 'list[str]',
        'type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'ipaddress': 'ipaddress',
        'name': 'name',
        'tags': 'tags',
        'type': 'type'
    }

    def __init__(self, description=None, ipaddress=None, name=None, tags=None, type=None):  # noqa: E501
        """V1IPUpdateRequest - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._ipaddress = None
        self._name = None
        self._tags = None
        self._type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.ipaddress = ipaddress
        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags
        self.type = type

    @property
    def description(self):
        """Gets the description of this V1IPUpdateRequest.  # noqa: E501

        a description for this entity  # noqa: E501

        :return: The description of this V1IPUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1IPUpdateRequest.

        a description for this entity  # noqa: E501

        :param description: The description of this V1IPUpdateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ipaddress(self):
        """Gets the ipaddress of this V1IPUpdateRequest.  # noqa: E501

        the address (ipv4 or ipv6) of this ip  # noqa: E501

        :return: The ipaddress of this V1IPUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._ipaddress

    @ipaddress.setter
    def ipaddress(self, ipaddress):
        """Sets the ipaddress of this V1IPUpdateRequest.

        the address (ipv4 or ipv6) of this ip  # noqa: E501

        :param ipaddress: The ipaddress of this V1IPUpdateRequest.  # noqa: E501
        :type: str
        """
        if ipaddress is None:
            raise ValueError("Invalid value for `ipaddress`, must not be `None`")  # noqa: E501

        self._ipaddress = ipaddress

    @property
    def name(self):
        """Gets the name of this V1IPUpdateRequest.  # noqa: E501

        a readable name for this entity  # noqa: E501

        :return: The name of this V1IPUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1IPUpdateRequest.

        a readable name for this entity  # noqa: E501

        :param name: The name of this V1IPUpdateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this V1IPUpdateRequest.  # noqa: E501

        free tags that you associate with this ip.  # noqa: E501

        :return: The tags of this V1IPUpdateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this V1IPUpdateRequest.

        free tags that you associate with this ip.  # noqa: E501

        :param tags: The tags of this V1IPUpdateRequest.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this V1IPUpdateRequest.  # noqa: E501

        the ip type, ephemeral leads to automatic cleanup of the ip address, static will enable re-use of the ip at a later point in time  # noqa: E501

        :return: The type of this V1IPUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1IPUpdateRequest.

        the ip type, ephemeral leads to automatic cleanup of the ip address, static will enable re-use of the ip at a later point in time  # noqa: E501

        :param type: The type of this V1IPUpdateRequest.  # noqa: E501
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
        if issubclass(V1IPUpdateRequest, dict):
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
        if not isinstance(other, V1IPUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
