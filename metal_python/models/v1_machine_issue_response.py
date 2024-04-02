# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.28.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineIssueResponse(object):
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
        'issues': 'list[str]',
        'machineid': 'str'
    }

    attribute_map = {
        'issues': 'issues',
        'machineid': 'machineid'
    }

    def __init__(self, issues=None, machineid=None):  # noqa: E501
        """V1MachineIssueResponse - a model defined in Swagger"""  # noqa: E501

        self._issues = None
        self._machineid = None
        self.discriminator = None

        self.issues = issues
        self.machineid = machineid

    @property
    def issues(self):
        """Gets the issues of this V1MachineIssueResponse.  # noqa: E501

        the list of issues (only issue ids) of this machine  # noqa: E501

        :return: The issues of this V1MachineIssueResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._issues

    @issues.setter
    def issues(self, issues):
        """Sets the issues of this V1MachineIssueResponse.

        the list of issues (only issue ids) of this machine  # noqa: E501

        :param issues: The issues of this V1MachineIssueResponse.  # noqa: E501
        :type: list[str]
        """
        if issues is None:
            raise ValueError("Invalid value for `issues`, must not be `None`")  # noqa: E501

        self._issues = issues

    @property
    def machineid(self):
        """Gets the machineid of this V1MachineIssueResponse.  # noqa: E501

        the machine id that has the given issues  # noqa: E501

        :return: The machineid of this V1MachineIssueResponse.  # noqa: E501
        :rtype: str
        """
        return self._machineid

    @machineid.setter
    def machineid(self, machineid):
        """Sets the machineid of this V1MachineIssueResponse.

        the machine id that has the given issues  # noqa: E501

        :param machineid: The machineid of this V1MachineIssueResponse.  # noqa: E501
        :type: str
        """
        if machineid is None:
            raise ValueError("Invalid value for `machineid`, must not be `None`")  # noqa: E501

        self._machineid = machineid

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
        if issubclass(V1MachineIssueResponse, dict):
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
        if not isinstance(other, V1MachineIssueResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
