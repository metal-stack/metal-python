# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.26.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SizeSuggestRequest(object):
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
        'machine_id': 'str'
    }

    attribute_map = {
        'machine_id': 'machineID'
    }

    def __init__(self, machine_id=None):  # noqa: E501
        """V1SizeSuggestRequest - a model defined in Swagger"""  # noqa: E501

        self._machine_id = None
        self.discriminator = None

        self.machine_id = machine_id

    @property
    def machine_id(self):
        """Gets the machine_id of this V1SizeSuggestRequest.  # noqa: E501

        machineID to retrieve size suggestion for  # noqa: E501

        :return: The machine_id of this V1SizeSuggestRequest.  # noqa: E501
        :rtype: str
        """
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        """Sets the machine_id of this V1SizeSuggestRequest.

        machineID to retrieve size suggestion for  # noqa: E501

        :param machine_id: The machine_id of this V1SizeSuggestRequest.  # noqa: E501
        :type: str
        """
        if machine_id is None:
            raise ValueError("Invalid value for `machine_id`, must not be `None`")  # noqa: E501

        self._machine_id = machine_id

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
        if issubclass(V1SizeSuggestRequest, dict):
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
        if not isinstance(other, V1SizeSuggestRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
