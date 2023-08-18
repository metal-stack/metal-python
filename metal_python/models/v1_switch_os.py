# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.23.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SwitchOS(object):
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
        'metal_core_version': 'str',
        'vendor': 'str',
        'version': 'str'
    }

    attribute_map = {
        'metal_core_version': 'metal_core_version',
        'vendor': 'vendor',
        'version': 'version'
    }

    def __init__(self, metal_core_version=None, vendor=None, version=None):  # noqa: E501
        """V1SwitchOS - a model defined in Swagger"""  # noqa: E501

        self._metal_core_version = None
        self._vendor = None
        self._version = None
        self.discriminator = None

        if metal_core_version is not None:
            self.metal_core_version = metal_core_version
        if vendor is not None:
            self.vendor = vendor
        if version is not None:
            self.version = version

    @property
    def metal_core_version(self):
        """Gets the metal_core_version of this V1SwitchOS.  # noqa: E501

        the version of metal-core running  # noqa: E501

        :return: The metal_core_version of this V1SwitchOS.  # noqa: E501
        :rtype: str
        """
        return self._metal_core_version

    @metal_core_version.setter
    def metal_core_version(self, metal_core_version):
        """Sets the metal_core_version of this V1SwitchOS.

        the version of metal-core running  # noqa: E501

        :param metal_core_version: The metal_core_version of this V1SwitchOS.  # noqa: E501
        :type: str
        """

        self._metal_core_version = metal_core_version

    @property
    def vendor(self):
        """Gets the vendor of this V1SwitchOS.  # noqa: E501

        the operating system vendor the switch currently has  # noqa: E501

        :return: The vendor of this V1SwitchOS.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this V1SwitchOS.

        the operating system vendor the switch currently has  # noqa: E501

        :param vendor: The vendor of this V1SwitchOS.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def version(self):
        """Gets the version of this V1SwitchOS.  # noqa: E501

        the operating system version the switch currently has  # noqa: E501

        :return: The version of this V1SwitchOS.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1SwitchOS.

        the operating system version the switch currently has  # noqa: E501

        :param version: The version of this V1SwitchOS.  # noqa: E501
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
        if issubclass(V1SwitchOS, dict):
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
        if not isinstance(other, V1SwitchOS):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
