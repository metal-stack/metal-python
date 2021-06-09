# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.14.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineConsolePasswordRequest(object):
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
        'reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'reason': 'reason'
    }

    def __init__(self, id=None, reason=None):  # noqa: E501
        """V1MachineConsolePasswordRequest - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._reason = None
        self.discriminator = None

        self.id = id
        self.reason = reason

    @property
    def id(self):
        """Gets the id of this V1MachineConsolePasswordRequest.  # noqa: E501

        id of the machine to get the consolepassword for  # noqa: E501

        :return: The id of this V1MachineConsolePasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1MachineConsolePasswordRequest.

        id of the machine to get the consolepassword for  # noqa: E501

        :param id: The id of this V1MachineConsolePasswordRequest.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def reason(self):
        """Gets the reason of this V1MachineConsolePasswordRequest.  # noqa: E501

        reason why the consolepassword is requested, typically a incident number with short description  # noqa: E501

        :return: The reason of this V1MachineConsolePasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1MachineConsolePasswordRequest.

        reason why the consolepassword is requested, typically a incident number with short description  # noqa: E501

        :param reason: The reason of this V1MachineConsolePasswordRequest.  # noqa: E501
        :type: str
        """
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501

        self._reason = reason

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
        if issubclass(V1MachineConsolePasswordRequest, dict):
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
        if not isinstance(other, V1MachineConsolePasswordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other