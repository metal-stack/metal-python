# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.21.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SizeMatchingLog(object):
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
        'constraints': 'list[V1SizeConstraintMatchingLog]',
        'log': 'str',
        'match': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'constraints': 'constraints',
        'log': 'log',
        'match': 'match',
        'name': 'name'
    }

    def __init__(self, constraints=None, log=None, match=None, name=None):  # noqa: E501
        """V1SizeMatchingLog - a model defined in Swagger"""  # noqa: E501

        self._constraints = None
        self._log = None
        self._match = None
        self._name = None
        self.discriminator = None

        self.constraints = constraints
        self.log = log
        self.match = match
        self.name = name

    @property
    def constraints(self):
        """Gets the constraints of this V1SizeMatchingLog.  # noqa: E501


        :return: The constraints of this V1SizeMatchingLog.  # noqa: E501
        :rtype: list[V1SizeConstraintMatchingLog]
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this V1SizeMatchingLog.


        :param constraints: The constraints of this V1SizeMatchingLog.  # noqa: E501
        :type: list[V1SizeConstraintMatchingLog]
        """
        if constraints is None:
            raise ValueError("Invalid value for `constraints`, must not be `None`")  # noqa: E501

        self._constraints = constraints

    @property
    def log(self):
        """Gets the log of this V1SizeMatchingLog.  # noqa: E501


        :return: The log of this V1SizeMatchingLog.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this V1SizeMatchingLog.


        :param log: The log of this V1SizeMatchingLog.  # noqa: E501
        :type: str
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")  # noqa: E501

        self._log = log

    @property
    def match(self):
        """Gets the match of this V1SizeMatchingLog.  # noqa: E501


        :return: The match of this V1SizeMatchingLog.  # noqa: E501
        :rtype: bool
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this V1SizeMatchingLog.


        :param match: The match of this V1SizeMatchingLog.  # noqa: E501
        :type: bool
        """
        if match is None:
            raise ValueError("Invalid value for `match`, must not be `None`")  # noqa: E501

        self._match = match

    @property
    def name(self):
        """Gets the name of this V1SizeMatchingLog.  # noqa: E501


        :return: The name of this V1SizeMatchingLog.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1SizeMatchingLog.


        :param name: The name of this V1SizeMatchingLog.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(V1SizeMatchingLog, dict):
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
        if not isinstance(other, V1SizeMatchingLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
