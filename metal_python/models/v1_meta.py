# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.24.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1Meta(object):
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
        'annotations': 'dict(str, str)',
        'apiversion': 'str',
        'created_time': 'datetime',
        'id': 'str',
        'kind': 'str',
        'labels': 'list[str]',
        'updated_time': 'datetime',
        'version': 'int'
    }

    attribute_map = {
        'annotations': 'annotations',
        'apiversion': 'apiversion',
        'created_time': 'created_time',
        'id': 'id',
        'kind': 'kind',
        'labels': 'labels',
        'updated_time': 'updated_time',
        'version': 'version'
    }

    def __init__(self, annotations=None, apiversion=None, created_time=None, id=None, kind=None, labels=None, updated_time=None, version=None):  # noqa: E501
        """V1Meta - a model defined in Swagger"""  # noqa: E501

        self._annotations = None
        self._apiversion = None
        self._created_time = None
        self._id = None
        self._kind = None
        self._labels = None
        self._updated_time = None
        self._version = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if apiversion is not None:
            self.apiversion = apiversion
        if created_time is not None:
            self.created_time = created_time
        if id is not None:
            self.id = id
        if kind is not None:
            self.kind = kind
        if labels is not None:
            self.labels = labels
        if updated_time is not None:
            self.updated_time = updated_time
        if version is not None:
            self.version = version

    @property
    def annotations(self):
        """Gets the annotations of this V1Meta.  # noqa: E501


        :return: The annotations of this V1Meta.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this V1Meta.


        :param annotations: The annotations of this V1Meta.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def apiversion(self):
        """Gets the apiversion of this V1Meta.  # noqa: E501


        :return: The apiversion of this V1Meta.  # noqa: E501
        :rtype: str
        """
        return self._apiversion

    @apiversion.setter
    def apiversion(self, apiversion):
        """Sets the apiversion of this V1Meta.


        :param apiversion: The apiversion of this V1Meta.  # noqa: E501
        :type: str
        """

        self._apiversion = apiversion

    @property
    def created_time(self):
        """Gets the created_time of this V1Meta.  # noqa: E501


        :return: The created_time of this V1Meta.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this V1Meta.


        :param created_time: The created_time of this V1Meta.  # noqa: E501
        :type: datetime
        """

        self._created_time = created_time

    @property
    def id(self):
        """Gets the id of this V1Meta.  # noqa: E501


        :return: The id of this V1Meta.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1Meta.


        :param id: The id of this V1Meta.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def kind(self):
        """Gets the kind of this V1Meta.  # noqa: E501


        :return: The kind of this V1Meta.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1Meta.


        :param kind: The kind of this V1Meta.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def labels(self):
        """Gets the labels of this V1Meta.  # noqa: E501


        :return: The labels of this V1Meta.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this V1Meta.


        :param labels: The labels of this V1Meta.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def updated_time(self):
        """Gets the updated_time of this V1Meta.  # noqa: E501


        :return: The updated_time of this V1Meta.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this V1Meta.


        :param updated_time: The updated_time of this V1Meta.  # noqa: E501
        :type: datetime
        """

        self._updated_time = updated_time

    @property
    def version(self):
        """Gets the version of this V1Meta.  # noqa: E501


        :return: The version of this V1Meta.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1Meta.


        :param version: The version of this V1Meta.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(V1Meta, dict):
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
        if not isinstance(other, V1Meta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
