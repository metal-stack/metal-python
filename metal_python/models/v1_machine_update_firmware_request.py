# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.18.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineUpdateFirmwareRequest(object):
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
        'kind': 'str',
        'revision': 'str'
    }

    attribute_map = {
        'description': 'description',
        'kind': 'kind',
        'revision': 'revision'
    }

    def __init__(self, description=None, kind=None, revision=None):  # noqa: E501
        """V1MachineUpdateFirmwareRequest - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._kind = None
        self._revision = None
        self.discriminator = None

        self.description = description
        self.kind = kind
        self.revision = revision

    @property
    def description(self):
        """Gets the description of this V1MachineUpdateFirmwareRequest.  # noqa: E501

        a description why the machine has been updated  # noqa: E501

        :return: The description of this V1MachineUpdateFirmwareRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1MachineUpdateFirmwareRequest.

        a description why the machine has been updated  # noqa: E501

        :param description: The description of this V1MachineUpdateFirmwareRequest.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def kind(self):
        """Gets the kind of this V1MachineUpdateFirmwareRequest.  # noqa: E501

        the firmware kind, i.e. [bios|bmc]  # noqa: E501

        :return: The kind of this V1MachineUpdateFirmwareRequest.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1MachineUpdateFirmwareRequest.

        the firmware kind, i.e. [bios|bmc]  # noqa: E501

        :param kind: The kind of this V1MachineUpdateFirmwareRequest.  # noqa: E501
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def revision(self):
        """Gets the revision of this V1MachineUpdateFirmwareRequest.  # noqa: E501

        the update revision  # noqa: E501

        :return: The revision of this V1MachineUpdateFirmwareRequest.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this V1MachineUpdateFirmwareRequest.

        the update revision  # noqa: E501

        :param revision: The revision of this V1MachineUpdateFirmwareRequest.  # noqa: E501
        :type: str
        """
        if revision is None:
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501

        self._revision = revision

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
        if issubclass(V1MachineUpdateFirmwareRequest, dict):
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
        if not isinstance(other, V1MachineUpdateFirmwareRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
