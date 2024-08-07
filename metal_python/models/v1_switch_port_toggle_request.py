# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.32.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SwitchPortToggleRequest(object):
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
        'nic': 'str',
        'status': 'str'
    }

    attribute_map = {
        'nic': 'nic',
        'status': 'status'
    }

    def __init__(self, nic=None, status=None):  # noqa: E501
        """V1SwitchPortToggleRequest - a model defined in Swagger"""  # noqa: E501

        self._nic = None
        self._status = None
        self.discriminator = None

        self.nic = nic
        self.status = status

    @property
    def nic(self):
        """Gets the nic of this V1SwitchPortToggleRequest.  # noqa: E501

        the nic of the switch you want to change  # noqa: E501

        :return: The nic of this V1SwitchPortToggleRequest.  # noqa: E501
        :rtype: str
        """
        return self._nic

    @nic.setter
    def nic(self, nic):
        """Sets the nic of this V1SwitchPortToggleRequest.

        the nic of the switch you want to change  # noqa: E501

        :param nic: The nic of this V1SwitchPortToggleRequest.  # noqa: E501
        :type: str
        """
        if nic is None:
            raise ValueError("Invalid value for `nic`, must not be `None`")  # noqa: E501

        self._nic = nic

    @property
    def status(self):
        """Gets the status of this V1SwitchPortToggleRequest.  # noqa: E501

        sets the port status  # noqa: E501

        :return: The status of this V1SwitchPortToggleRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1SwitchPortToggleRequest.

        sets the port status  # noqa: E501

        :param status: The status of this V1SwitchPortToggleRequest.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["DOWN", "UP"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(V1SwitchPortToggleRequest, dict):
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
        if not isinstance(other, V1SwitchPortToggleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
