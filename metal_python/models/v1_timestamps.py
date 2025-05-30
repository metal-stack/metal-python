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


class V1Timestamps(object):
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
        'changed': 'datetime',
        'created': 'datetime'
    }

    attribute_map = {
        'changed': 'changed',
        'created': 'created'
    }

    def __init__(self, changed=None, created=None):  # noqa: E501
        """V1Timestamps - a model defined in Swagger"""  # noqa: E501

        self._changed = None
        self._created = None
        self.discriminator = None

        if changed is not None:
            self.changed = changed
        if created is not None:
            self.created = created

    @property
    def changed(self):
        """Gets the changed of this V1Timestamps.  # noqa: E501

        the last changed timestamp of this entity  # noqa: E501

        :return: The changed of this V1Timestamps.  # noqa: E501
        :rtype: datetime
        """
        return self._changed

    @changed.setter
    def changed(self, changed):
        """Sets the changed of this V1Timestamps.

        the last changed timestamp of this entity  # noqa: E501

        :param changed: The changed of this V1Timestamps.  # noqa: E501
        :type: datetime
        """

        self._changed = changed

    @property
    def created(self):
        """Gets the created of this V1Timestamps.  # noqa: E501

        the creation time of this entity  # noqa: E501

        :return: The created of this V1Timestamps.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this V1Timestamps.

        the creation time of this entity  # noqa: E501

        :param created: The created of this V1Timestamps.  # noqa: E501
        :type: datetime
        """

        self._created = created

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
        if issubclass(V1Timestamps, dict):
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
        if not isinstance(other, V1Timestamps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
