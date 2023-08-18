# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.22.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DatastoreImageSearchQuery(object):
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
        'classification': 'str',
        'features': 'list[str]',
        'id': 'str',
        'name': 'str',
        'os': 'str',
        'version': 'str'
    }

    attribute_map = {
        'classification': 'classification',
        'features': 'features',
        'id': 'id',
        'name': 'name',
        'os': 'os',
        'version': 'version'
    }

    def __init__(self, classification=None, features=None, id=None, name=None, os=None, version=None):  # noqa: E501
        """DatastoreImageSearchQuery - a model defined in Swagger"""  # noqa: E501

        self._classification = None
        self._features = None
        self._id = None
        self._name = None
        self._os = None
        self._version = None
        self.discriminator = None

        if classification is not None:
            self.classification = classification
        if features is not None:
            self.features = features
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if os is not None:
            self.os = os
        if version is not None:
            self.version = version

    @property
    def classification(self):
        """Gets the classification of this DatastoreImageSearchQuery.  # noqa: E501


        :return: The classification of this DatastoreImageSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this DatastoreImageSearchQuery.


        :param classification: The classification of this DatastoreImageSearchQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["deprecated", "preview", "supported"]  # noqa: E501
        if classification not in allowed_values:
            raise ValueError(
                "Invalid value for `classification` ({0}), must be one of {1}"  # noqa: E501
                .format(classification, allowed_values)
            )

        self._classification = classification

    @property
    def features(self):
        """Gets the features of this DatastoreImageSearchQuery.  # noqa: E501


        :return: The features of this DatastoreImageSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this DatastoreImageSearchQuery.


        :param features: The features of this DatastoreImageSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._features = features

    @property
    def id(self):
        """Gets the id of this DatastoreImageSearchQuery.  # noqa: E501


        :return: The id of this DatastoreImageSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatastoreImageSearchQuery.


        :param id: The id of this DatastoreImageSearchQuery.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DatastoreImageSearchQuery.  # noqa: E501


        :return: The name of this DatastoreImageSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatastoreImageSearchQuery.


        :param name: The name of this DatastoreImageSearchQuery.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def os(self):
        """Gets the os of this DatastoreImageSearchQuery.  # noqa: E501


        :return: The os of this DatastoreImageSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this DatastoreImageSearchQuery.


        :param os: The os of this DatastoreImageSearchQuery.  # noqa: E501
        :type: str
        """

        self._os = os

    @property
    def version(self):
        """Gets the version of this DatastoreImageSearchQuery.  # noqa: E501


        :return: The version of this DatastoreImageSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DatastoreImageSearchQuery.


        :param version: The version of this DatastoreImageSearchQuery.  # noqa: E501
        :type: str
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
        if issubclass(DatastoreImageSearchQuery, dict):
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
        if not isinstance(other, DatastoreImageSearchQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
