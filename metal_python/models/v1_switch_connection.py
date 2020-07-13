# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SwitchConnection(object):
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
        'machine_id': 'str',
        'nic': 'V1SwitchNic'
    }

    attribute_map = {
        'machine_id': 'machine_id',
        'nic': 'nic'
    }

    def __init__(self, machine_id=None, nic=None):  # noqa: E501
        """V1SwitchConnection - a model defined in Swagger"""  # noqa: E501

        self._machine_id = None
        self._nic = None
        self.discriminator = None

        if machine_id is not None:
            self.machine_id = machine_id
        self.nic = nic

    @property
    def machine_id(self):
        """Gets the machine_id of this V1SwitchConnection.  # noqa: E501

        the machine id of the machine connected to the nic  # noqa: E501

        :return: The machine_id of this V1SwitchConnection.  # noqa: E501
        :rtype: str
        """
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        """Sets the machine_id of this V1SwitchConnection.

        the machine id of the machine connected to the nic  # noqa: E501

        :param machine_id: The machine_id of this V1SwitchConnection.  # noqa: E501
        :type: str
        """

        self._machine_id = machine_id

    @property
    def nic(self):
        """Gets the nic of this V1SwitchConnection.  # noqa: E501

        a network interface on the switch  # noqa: E501

        :return: The nic of this V1SwitchConnection.  # noqa: E501
        :rtype: V1SwitchNic
        """
        return self._nic

    @nic.setter
    def nic(self, nic):
        """Sets the nic of this V1SwitchConnection.

        a network interface on the switch  # noqa: E501

        :param nic: The nic of this V1SwitchConnection.  # noqa: E501
        :type: V1SwitchNic
        """
        if nic is None:
            raise ValueError("Invalid value for `nic`, must not be `None`")  # noqa: E501

        self._nic = nic

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
        if issubclass(V1SwitchConnection, dict):
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
        if not isinstance(other, V1SwitchConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
