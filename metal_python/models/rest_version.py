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


class RestVersion(object):
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
        'builddate': 'str',
        'gitsha1': 'str',
        'name': 'str',
        'revision': 'str',
        'version': 'str'
    }

    attribute_map = {
        'builddate': 'builddate',
        'gitsha1': 'gitsha1',
        'name': 'name',
        'revision': 'revision',
        'version': 'version'
    }

    def __init__(self, builddate=None, gitsha1=None, name=None, revision=None, version=None):  # noqa: E501
        """RestVersion - a model defined in Swagger"""  # noqa: E501

        self._builddate = None
        self._gitsha1 = None
        self._name = None
        self._revision = None
        self._version = None
        self.discriminator = None

        self.builddate = builddate
        self.gitsha1 = gitsha1
        self.name = name
        self.revision = revision
        self.version = version

    @property
    def builddate(self):
        """Gets the builddate of this RestVersion.  # noqa: E501


        :return: The builddate of this RestVersion.  # noqa: E501
        :rtype: str
        """
        return self._builddate

    @builddate.setter
    def builddate(self, builddate):
        """Sets the builddate of this RestVersion.


        :param builddate: The builddate of this RestVersion.  # noqa: E501
        :type: str
        """
        if builddate is None:
            raise ValueError("Invalid value for `builddate`, must not be `None`")  # noqa: E501

        self._builddate = builddate

    @property
    def gitsha1(self):
        """Gets the gitsha1 of this RestVersion.  # noqa: E501


        :return: The gitsha1 of this RestVersion.  # noqa: E501
        :rtype: str
        """
        return self._gitsha1

    @gitsha1.setter
    def gitsha1(self, gitsha1):
        """Sets the gitsha1 of this RestVersion.


        :param gitsha1: The gitsha1 of this RestVersion.  # noqa: E501
        :type: str
        """
        if gitsha1 is None:
            raise ValueError("Invalid value for `gitsha1`, must not be `None`")  # noqa: E501

        self._gitsha1 = gitsha1

    @property
    def name(self):
        """Gets the name of this RestVersion.  # noqa: E501


        :return: The name of this RestVersion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RestVersion.


        :param name: The name of this RestVersion.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def revision(self):
        """Gets the revision of this RestVersion.  # noqa: E501


        :return: The revision of this RestVersion.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this RestVersion.


        :param revision: The revision of this RestVersion.  # noqa: E501
        :type: str
        """
        if revision is None:
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501

        self._revision = revision

    @property
    def version(self):
        """Gets the version of this RestVersion.  # noqa: E501


        :return: The version of this RestVersion.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RestVersion.


        :param version: The version of this RestVersion.  # noqa: E501
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
        if issubclass(RestVersion, dict):
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
        if not isinstance(other, RestVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
