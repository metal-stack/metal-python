# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.27.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1VendorRevisions(object):
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
        'vendor_revisions': 'dict(str, V1BoardRevisions)'
    }

    attribute_map = {
        'vendor_revisions': 'VendorRevisions'
    }

    def __init__(self, vendor_revisions=None):  # noqa: E501
        """V1VendorRevisions - a model defined in Swagger"""  # noqa: E501

        self._vendor_revisions = None
        self.discriminator = None

        self.vendor_revisions = vendor_revisions

    @property
    def vendor_revisions(self):
        """Gets the vendor_revisions of this V1VendorRevisions.  # noqa: E501


        :return: The vendor_revisions of this V1VendorRevisions.  # noqa: E501
        :rtype: dict(str, V1BoardRevisions)
        """
        return self._vendor_revisions

    @vendor_revisions.setter
    def vendor_revisions(self, vendor_revisions):
        """Sets the vendor_revisions of this V1VendorRevisions.


        :param vendor_revisions: The vendor_revisions of this V1VendorRevisions.  # noqa: E501
        :type: dict(str, V1BoardRevisions)
        """
        if vendor_revisions is None:
            raise ValueError("Invalid value for `vendor_revisions`, must not be `None`")  # noqa: E501

        self._vendor_revisions = vendor_revisions

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
        if issubclass(V1VendorRevisions, dict):
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
        if not isinstance(other, V1VendorRevisions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
