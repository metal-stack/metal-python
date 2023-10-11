# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.24.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1NetworkUpdateRequest(object):
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
        'prefixes': 'list[str]',
        'shared': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'destinationprefixes': 'destinationprefixes',
        'id': 'id',
        'labels': 'labels',
        'name': 'name',
        'prefixes': 'prefixes',
        'shared': 'shared'
    }

    def __init__(self, description=None, destinationprefixes=None, id=None, labels=None, name=None, prefixes=None, shared=None):  # noqa: E501
        """V1NetworkUpdateRequest - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._destinationprefixes = None
        self._id = None
        self._labels = None
        self._name = None
        self._prefixes = None
        self._shared = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if destinationprefixes is not None:
            self.destinationprefixes = destinationprefixes
        self.id = id
        if labels is not None:
            self.labels = labels
        if name is not None:
            self.name = name
        if prefixes is not None:
            self.prefixes = prefixes
        if shared is not None:
            self.shared = shared

    @property
    def description(self):
        """Gets the description of this V1NetworkUpdateRequest.  # noqa: E501

        a description for this entity  # noqa: E501

        :return: The description of this V1NetworkUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1NetworkUpdateRequest.

        a description for this entity  # noqa: E501

        :param description: The description of this V1NetworkUpdateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def destinationprefixes(self):
        """Gets the destinationprefixes of this V1NetworkUpdateRequest.  # noqa: E501

        the destination prefixes of this network  # noqa: E501

        :return: The destinationprefixes of this V1NetworkUpdateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._destinationprefixes

    @destinationprefixes.setter
    def destinationprefixes(self, destinationprefixes):
        """Sets the destinationprefixes of this V1NetworkUpdateRequest.

        the destination prefixes of this network  # noqa: E501

        :param destinationprefixes: The destinationprefixes of this V1NetworkUpdateRequest.  # noqa: E501
        :type: list[str]
        """

        self._destinationprefixes = destinationprefixes

    @property
    def id(self):
        """Gets the id of this V1NetworkUpdateRequest.  # noqa: E501

        the unique ID of this entity  # noqa: E501

        :return: The id of this V1NetworkUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1NetworkUpdateRequest.

        the unique ID of this entity  # noqa: E501

        :param id: The id of this V1NetworkUpdateRequest.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this V1NetworkUpdateRequest.  # noqa: E501

        free labels that you associate with this network.  # noqa: E501

        :return: The labels of this V1NetworkUpdateRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this V1NetworkUpdateRequest.

        free labels that you associate with this network.  # noqa: E501

        :param labels: The labels of this V1NetworkUpdateRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this V1NetworkUpdateRequest.  # noqa: E501

        a readable name for this entity  # noqa: E501

        :return: The name of this V1NetworkUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1NetworkUpdateRequest.

        a readable name for this entity  # noqa: E501

        :param name: The name of this V1NetworkUpdateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def prefixes(self):
        """Gets the prefixes of this V1NetworkUpdateRequest.  # noqa: E501

        the prefixes of this network  # noqa: E501

        :return: The prefixes of this V1NetworkUpdateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._prefixes

    @prefixes.setter
    def prefixes(self, prefixes):
        """Sets the prefixes of this V1NetworkUpdateRequest.

        the prefixes of this network  # noqa: E501

        :param prefixes: The prefixes of this V1NetworkUpdateRequest.  # noqa: E501
        :type: list[str]
        """

        self._prefixes = prefixes

    @property
    def shared(self):
        """Gets the shared of this V1NetworkUpdateRequest.  # noqa: E501

        marks a network as shareable.  # noqa: E501

        :return: The shared of this V1NetworkUpdateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this V1NetworkUpdateRequest.

        marks a network as shareable.  # noqa: E501

        :param shared: The shared of this V1NetworkUpdateRequest.  # noqa: E501
        :type: bool
        """

        self._shared = shared

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
        if issubclass(V1NetworkUpdateRequest, dict):
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
        if not isinstance(other, V1NetworkUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
