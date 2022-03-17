# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.16.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineBIOS(object):
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
        '_date': 'str',
        'vendor': 'str',
        'version': 'str'
    }

    attribute_map = {
        '_date': 'date',
        'vendor': 'vendor',
        'version': 'version'
    }

    def __init__(self, _date=None, vendor=None, version=None):  # noqa: E501
        """V1MachineBIOS - a model defined in Swagger"""  # noqa: E501

        self.__date = None
        self._vendor = None
        self._version = None
        self.discriminator = None

        self._date = _date
        self.vendor = vendor
        self.version = version

    @property
    def _date(self):
        """Gets the _date of this V1MachineBIOS.  # noqa: E501

        the bios date  # noqa: E501

        :return: The _date of this V1MachineBIOS.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this V1MachineBIOS.

        the bios date  # noqa: E501

        :param _date: The _date of this V1MachineBIOS.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def vendor(self):
        """Gets the vendor of this V1MachineBIOS.  # noqa: E501

        the bios vendor  # noqa: E501

        :return: The vendor of this V1MachineBIOS.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this V1MachineBIOS.

        the bios vendor  # noqa: E501

        :param vendor: The vendor of this V1MachineBIOS.  # noqa: E501
        :type: str
        """
        if vendor is None:
            raise ValueError("Invalid value for `vendor`, must not be `None`")  # noqa: E501

        self._vendor = vendor

    @property
    def version(self):
        """Gets the version of this V1MachineBIOS.  # noqa: E501

        the bios version  # noqa: E501

        :return: The version of this V1MachineBIOS.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1MachineBIOS.

        the bios version  # noqa: E501

        :param version: The version of this V1MachineBIOS.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

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
        if issubclass(V1MachineBIOS, dict):
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
        if not isinstance(other, V1MachineBIOS):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
