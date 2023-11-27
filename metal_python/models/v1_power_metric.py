# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.25.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1PowerMetric(object):
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
        'averageconsumedwatts': 'float',
        'intervalinmin': 'float',
        'maxconsumedwatts': 'float',
        'minconsumedwatts': 'float'
    }

    attribute_map = {
        'averageconsumedwatts': 'averageconsumedwatts',
        'intervalinmin': 'intervalinmin',
        'maxconsumedwatts': 'maxconsumedwatts',
        'minconsumedwatts': 'minconsumedwatts'
    }

    def __init__(self, averageconsumedwatts=None, intervalinmin=None, maxconsumedwatts=None, minconsumedwatts=None):  # noqa: E501
        """V1PowerMetric - a model defined in Swagger"""  # noqa: E501

        self._averageconsumedwatts = None
        self._intervalinmin = None
        self._maxconsumedwatts = None
        self._minconsumedwatts = None
        self.discriminator = None

        self.averageconsumedwatts = averageconsumedwatts
        self.intervalinmin = intervalinmin
        self.maxconsumedwatts = maxconsumedwatts
        self.minconsumedwatts = minconsumedwatts

    @property
    def averageconsumedwatts(self):
        """Gets the averageconsumedwatts of this V1PowerMetric.  # noqa: E501


        :return: The averageconsumedwatts of this V1PowerMetric.  # noqa: E501
        :rtype: float
        """
        return self._averageconsumedwatts

    @averageconsumedwatts.setter
    def averageconsumedwatts(self, averageconsumedwatts):
        """Sets the averageconsumedwatts of this V1PowerMetric.


        :param averageconsumedwatts: The averageconsumedwatts of this V1PowerMetric.  # noqa: E501
        :type: float
        """
        if averageconsumedwatts is None:
            raise ValueError("Invalid value for `averageconsumedwatts`, must not be `None`")  # noqa: E501

        self._averageconsumedwatts = averageconsumedwatts

    @property
    def intervalinmin(self):
        """Gets the intervalinmin of this V1PowerMetric.  # noqa: E501


        :return: The intervalinmin of this V1PowerMetric.  # noqa: E501
        :rtype: float
        """
        return self._intervalinmin

    @intervalinmin.setter
    def intervalinmin(self, intervalinmin):
        """Sets the intervalinmin of this V1PowerMetric.


        :param intervalinmin: The intervalinmin of this V1PowerMetric.  # noqa: E501
        :type: float
        """
        if intervalinmin is None:
            raise ValueError("Invalid value for `intervalinmin`, must not be `None`")  # noqa: E501

        self._intervalinmin = intervalinmin

    @property
    def maxconsumedwatts(self):
        """Gets the maxconsumedwatts of this V1PowerMetric.  # noqa: E501


        :return: The maxconsumedwatts of this V1PowerMetric.  # noqa: E501
        :rtype: float
        """
        return self._maxconsumedwatts

    @maxconsumedwatts.setter
    def maxconsumedwatts(self, maxconsumedwatts):
        """Sets the maxconsumedwatts of this V1PowerMetric.


        :param maxconsumedwatts: The maxconsumedwatts of this V1PowerMetric.  # noqa: E501
        :type: float
        """
        if maxconsumedwatts is None:
            raise ValueError("Invalid value for `maxconsumedwatts`, must not be `None`")  # noqa: E501

        self._maxconsumedwatts = maxconsumedwatts

    @property
    def minconsumedwatts(self):
        """Gets the minconsumedwatts of this V1PowerMetric.  # noqa: E501


        :return: The minconsumedwatts of this V1PowerMetric.  # noqa: E501
        :rtype: float
        """
        return self._minconsumedwatts

    @minconsumedwatts.setter
    def minconsumedwatts(self, minconsumedwatts):
        """Sets the minconsumedwatts of this V1PowerMetric.


        :param minconsumedwatts: The minconsumedwatts of this V1PowerMetric.  # noqa: E501
        :type: float
        """
        if minconsumedwatts is None:
            raise ValueError("Invalid value for `minconsumedwatts`, must not be `None`")  # noqa: E501

        self._minconsumedwatts = minconsumedwatts

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
        if issubclass(V1PowerMetric, dict):
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
        if not isinstance(other, V1PowerMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
