# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.22.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineIpmiReportResponse(object):
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
        'created': 'list[str]',
        'updated': 'list[str]'
    }

    attribute_map = {
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, created=None, updated=None):  # noqa: E501
        """V1MachineIpmiReportResponse - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._updated = None
        self.discriminator = None

        self.created = created
        self.updated = updated

    @property
    def created(self):
        """Gets the created of this V1MachineIpmiReportResponse.  # noqa: E501

        the machine uuids that triggered a creation of a machine entity  # noqa: E501

        :return: The created of this V1MachineIpmiReportResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this V1MachineIpmiReportResponse.

        the machine uuids that triggered a creation of a machine entity  # noqa: E501

        :param created: The created of this V1MachineIpmiReportResponse.  # noqa: E501
        :type: list[str]
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this V1MachineIpmiReportResponse.  # noqa: E501

        the machine uuids that triggered an update of ipmi data  # noqa: E501

        :return: The updated of this V1MachineIpmiReportResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this V1MachineIpmiReportResponse.

        the machine uuids that triggered an update of ipmi data  # noqa: E501

        :param updated: The updated of this V1MachineIpmiReportResponse.  # noqa: E501
        :type: list[str]
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

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
        if issubclass(V1MachineIpmiReportResponse, dict):
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
        if not isinstance(other, V1MachineIpmiReportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
