# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.28.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SizeConstraintMatchingLog(object):
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
        'constraint': 'V1SizeConstraint',
        'log': 'str',
        'match': 'bool'
    }

    attribute_map = {
        'constraint': 'constraint',
        'log': 'log',
        'match': 'match'
    }

    def __init__(self, constraint=None, log=None, match=None):  # noqa: E501
        """V1SizeConstraintMatchingLog - a model defined in Swagger"""  # noqa: E501

        self._constraint = None
        self._log = None
        self._match = None
        self.discriminator = None

        self.constraint = constraint
        self.log = log
        self.match = match

    @property
    def constraint(self):
        """Gets the constraint of this V1SizeConstraintMatchingLog.  # noqa: E501

        the size constraint to which this log relates to  # noqa: E501

        :return: The constraint of this V1SizeConstraintMatchingLog.  # noqa: E501
        :rtype: V1SizeConstraint
        """
        return self._constraint

    @constraint.setter
    def constraint(self, constraint):
        """Sets the constraint of this V1SizeConstraintMatchingLog.

        the size constraint to which this log relates to  # noqa: E501

        :param constraint: The constraint of this V1SizeConstraintMatchingLog.  # noqa: E501
        :type: V1SizeConstraint
        """
        if constraint is None:
            raise ValueError("Invalid value for `constraint`, must not be `None`")  # noqa: E501

        self._constraint = constraint

    @property
    def log(self):
        """Gets the log of this V1SizeConstraintMatchingLog.  # noqa: E501

        a string represention of the matching condition  # noqa: E501

        :return: The log of this V1SizeConstraintMatchingLog.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this V1SizeConstraintMatchingLog.

        a string represention of the matching condition  # noqa: E501

        :param log: The log of this V1SizeConstraintMatchingLog.  # noqa: E501
        :type: str
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")  # noqa: E501

        self._log = log

    @property
    def match(self):
        """Gets the match of this V1SizeConstraintMatchingLog.  # noqa: E501

        indicates whether the constraint matched or not  # noqa: E501

        :return: The match of this V1SizeConstraintMatchingLog.  # noqa: E501
        :rtype: bool
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this V1SizeConstraintMatchingLog.

        indicates whether the constraint matched or not  # noqa: E501

        :param match: The match of this V1SizeConstraintMatchingLog.  # noqa: E501
        :type: bool
        """
        if match is None:
            raise ValueError("Invalid value for `match`, must not be `None`")  # noqa: E501

        self._match = match

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
        if issubclass(V1SizeConstraintMatchingLog, dict):
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
        if not isinstance(other, V1SizeConstraintMatchingLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
