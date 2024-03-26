# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.28.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SwitchNotifyResponse(object):
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
        'id': 'str',
        'last_sync': 'V1SwitchSync',
        'last_sync_error': 'V1SwitchSync',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'last_sync': 'last_sync',
        'last_sync_error': 'last_sync_error',
        'name': 'name'
    }

    def __init__(self, description=None, id=None, last_sync=None, last_sync_error=None, name=None):  # noqa: E501
        """V1SwitchNotifyResponse - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._id = None
        self._last_sync = None
        self._last_sync_error = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.id = id
        if last_sync is not None:
            self.last_sync = last_sync
        if last_sync_error is not None:
            self.last_sync_error = last_sync_error
        if name is not None:
            self.name = name

    @property
    def description(self):
        """Gets the description of this V1SwitchNotifyResponse.  # noqa: E501

        a description for this entity  # noqa: E501

        :return: The description of this V1SwitchNotifyResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1SwitchNotifyResponse.

        a description for this entity  # noqa: E501

        :param description: The description of this V1SwitchNotifyResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this V1SwitchNotifyResponse.  # noqa: E501

        the unique ID of this entity  # noqa: E501

        :return: The id of this V1SwitchNotifyResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1SwitchNotifyResponse.

        the unique ID of this entity  # noqa: E501

        :param id: The id of this V1SwitchNotifyResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def last_sync(self):
        """Gets the last_sync of this V1SwitchNotifyResponse.  # noqa: E501

        last successful synchronization to the switch  # noqa: E501

        :return: The last_sync of this V1SwitchNotifyResponse.  # noqa: E501
        :rtype: V1SwitchSync
        """
        return self._last_sync

    @last_sync.setter
    def last_sync(self, last_sync):
        """Sets the last_sync of this V1SwitchNotifyResponse.

        last successful synchronization to the switch  # noqa: E501

        :param last_sync: The last_sync of this V1SwitchNotifyResponse.  # noqa: E501
        :type: V1SwitchSync
        """

        self._last_sync = last_sync

    @property
    def last_sync_error(self):
        """Gets the last_sync_error of this V1SwitchNotifyResponse.  # noqa: E501

        last synchronization to the switch that was erroneous  # noqa: E501

        :return: The last_sync_error of this V1SwitchNotifyResponse.  # noqa: E501
        :rtype: V1SwitchSync
        """
        return self._last_sync_error

    @last_sync_error.setter
    def last_sync_error(self, last_sync_error):
        """Sets the last_sync_error of this V1SwitchNotifyResponse.

        last synchronization to the switch that was erroneous  # noqa: E501

        :param last_sync_error: The last_sync_error of this V1SwitchNotifyResponse.  # noqa: E501
        :type: V1SwitchSync
        """

        self._last_sync_error = last_sync_error

    @property
    def name(self):
        """Gets the name of this V1SwitchNotifyResponse.  # noqa: E501

        a readable name for this entity  # noqa: E501

        :return: The name of this V1SwitchNotifyResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1SwitchNotifyResponse.

        a readable name for this entity  # noqa: E501

        :param name: The name of this V1SwitchNotifyResponse.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(V1SwitchNotifyResponse, dict):
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
        if not isinstance(other, V1SwitchNotifyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
