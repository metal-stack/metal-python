# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.39.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineIssue(object):
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
        'details': 'str',
        'id': 'str',
        'ref_url': 'str',
        'severity': 'str'
    }

    attribute_map = {
        'description': 'description',
        'details': 'details',
        'id': 'id',
        'ref_url': 'ref_url',
        'severity': 'severity'
    }

    def __init__(self, description=None, details=None, id=None, ref_url=None, severity=None):  # noqa: E501
        """V1MachineIssue - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._details = None
        self._id = None
        self._ref_url = None
        self._severity = None
        self.discriminator = None

        self.description = description
        self.details = details
        self.id = id
        self.ref_url = ref_url
        self.severity = severity

    @property
    def description(self):
        """Gets the description of this V1MachineIssue.  # noqa: E501

        a description of the issue  # noqa: E501

        :return: The description of this V1MachineIssue.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1MachineIssue.

        a description of the issue  # noqa: E501

        :param description: The description of this V1MachineIssue.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def details(self):
        """Gets the details of this V1MachineIssue.  # noqa: E501

        details of the issue  # noqa: E501

        :return: The details of this V1MachineIssue.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this V1MachineIssue.

        details of the issue  # noqa: E501

        :param details: The details of this V1MachineIssue.  # noqa: E501
        :type: str
        """
        if details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")  # noqa: E501

        self._details = details

    @property
    def id(self):
        """Gets the id of this V1MachineIssue.  # noqa: E501

        the id of the issue  # noqa: E501

        :return: The id of this V1MachineIssue.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1MachineIssue.

        the id of the issue  # noqa: E501

        :param id: The id of this V1MachineIssue.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def ref_url(self):
        """Gets the ref_url of this V1MachineIssue.  # noqa: E501

        an issue reference to the issue in metal-stack docs  # noqa: E501

        :return: The ref_url of this V1MachineIssue.  # noqa: E501
        :rtype: str
        """
        return self._ref_url

    @ref_url.setter
    def ref_url(self, ref_url):
        """Sets the ref_url of this V1MachineIssue.

        an issue reference to the issue in metal-stack docs  # noqa: E501

        :param ref_url: The ref_url of this V1MachineIssue.  # noqa: E501
        :type: str
        """
        if ref_url is None:
            raise ValueError("Invalid value for `ref_url`, must not be `None`")  # noqa: E501

        self._ref_url = ref_url

    @property
    def severity(self):
        """Gets the severity of this V1MachineIssue.  # noqa: E501

        the severity of the issue  # noqa: E501

        :return: The severity of this V1MachineIssue.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this V1MachineIssue.

        the severity of the issue  # noqa: E501

        :param severity: The severity of this V1MachineIssue.  # noqa: E501
        :type: str
        """
        if severity is None:
            raise ValueError("Invalid value for `severity`, must not be `None`")  # noqa: E501

        self._severity = severity

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
        if issubclass(V1MachineIssue, dict):
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
        if not isinstance(other, V1MachineIssue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
