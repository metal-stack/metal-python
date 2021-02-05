# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.12.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1NetworkAllocateRequest(object):
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
        'labels': 'dict(str, str)',
        'name': 'str',
        'partitionid': 'str',
        'projectid': 'str',
        'shared': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'labels': 'labels',
        'name': 'name',
        'partitionid': 'partitionid',
        'projectid': 'projectid',
        'shared': 'shared'
    }

    def __init__(self, description=None, labels=None, name=None, partitionid=None, projectid=None, shared=None):  # noqa: E501
        """V1NetworkAllocateRequest - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._labels = None
        self._name = None
        self._partitionid = None
        self._projectid = None
        self._shared = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        if name is not None:
            self.name = name
        if partitionid is not None:
            self.partitionid = partitionid
        if projectid is not None:
            self.projectid = projectid
        if shared is not None:
            self.shared = shared

    @property
    def description(self):
        """Gets the description of this V1NetworkAllocateRequest.  # noqa: E501

        a description for this entity  # noqa: E501

        :return: The description of this V1NetworkAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1NetworkAllocateRequest.

        a description for this entity  # noqa: E501

        :param description: The description of this V1NetworkAllocateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def labels(self):
        """Gets the labels of this V1NetworkAllocateRequest.  # noqa: E501

        free labels that you associate with this network.  # noqa: E501

        :return: The labels of this V1NetworkAllocateRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this V1NetworkAllocateRequest.

        free labels that you associate with this network.  # noqa: E501

        :param labels: The labels of this V1NetworkAllocateRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this V1NetworkAllocateRequest.  # noqa: E501

        a readable name for this entity  # noqa: E501

        :return: The name of this V1NetworkAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1NetworkAllocateRequest.

        a readable name for this entity  # noqa: E501

        :param name: The name of this V1NetworkAllocateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def partitionid(self):
        """Gets the partitionid of this V1NetworkAllocateRequest.  # noqa: E501

        the partition this network belongs to  # noqa: E501

        :return: The partitionid of this V1NetworkAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._partitionid

    @partitionid.setter
    def partitionid(self, partitionid):
        """Sets the partitionid of this V1NetworkAllocateRequest.

        the partition this network belongs to  # noqa: E501

        :param partitionid: The partitionid of this V1NetworkAllocateRequest.  # noqa: E501
        :type: str
        """

        self._partitionid = partitionid

    @property
    def projectid(self):
        """Gets the projectid of this V1NetworkAllocateRequest.  # noqa: E501

        the project id this network belongs to, can be empty if globally available  # noqa: E501

        :return: The projectid of this V1NetworkAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._projectid

    @projectid.setter
    def projectid(self, projectid):
        """Sets the projectid of this V1NetworkAllocateRequest.

        the project id this network belongs to, can be empty if globally available  # noqa: E501

        :param projectid: The projectid of this V1NetworkAllocateRequest.  # noqa: E501
        :type: str
        """

        self._projectid = projectid

    @property
    def shared(self):
        """Gets the shared of this V1NetworkAllocateRequest.  # noqa: E501

        marks a network as shareable.  # noqa: E501

        :return: The shared of this V1NetworkAllocateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this V1NetworkAllocateRequest.

        marks a network as shareable.  # noqa: E501

        :param shared: The shared of this V1NetworkAllocateRequest.  # noqa: E501
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
        if issubclass(V1NetworkAllocateRequest, dict):
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
        if not isinstance(other, V1NetworkAllocateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
