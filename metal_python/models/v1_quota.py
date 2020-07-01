# coding: utf-8

"""
    metal-api

    Resource for managing pure metal  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1Quota(object):
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
        'quota': 'WrappersInt32Value'
    }

    attribute_map = {
        'quota': 'quota'
    }

    def __init__(self, quota=None):  # noqa: E501
        """V1Quota - a model defined in Swagger"""  # noqa: E501

        self._quota = None
        self.discriminator = None

        if quota is not None:
            self.quota = quota

    @property
    def quota(self):
        """Gets the quota of this V1Quota.  # noqa: E501


        :return: The quota of this V1Quota.  # noqa: E501
        :rtype: WrappersInt32Value
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this V1Quota.


        :param quota: The quota of this V1Quota.  # noqa: E501
        :type: WrappersInt32Value
        """

        self._quota = quota

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
        if issubclass(V1Quota, dict):
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
        if not isinstance(other, V1Quota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
