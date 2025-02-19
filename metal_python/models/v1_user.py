# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.40.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1User(object):
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
        'e_mail': 'str',
        'groups': 'list[str]',
        'issuer': 'str',
        'name': 'str',
        'subject': 'str',
        'tenant': 'str'
    }

    attribute_map = {
        'e_mail': 'EMail',
        'groups': 'Groups',
        'issuer': 'Issuer',
        'name': 'Name',
        'subject': 'Subject',
        'tenant': 'Tenant'
    }

    def __init__(self, e_mail=None, groups=None, issuer=None, name=None, subject=None, tenant=None):  # noqa: E501
        """V1User - a model defined in Swagger"""  # noqa: E501

        self._e_mail = None
        self._groups = None
        self._issuer = None
        self._name = None
        self._subject = None
        self._tenant = None
        self.discriminator = None

        self.e_mail = e_mail
        self.groups = groups
        self.issuer = issuer
        self.name = name
        self.subject = subject
        self.tenant = tenant

    @property
    def e_mail(self):
        """Gets the e_mail of this V1User.  # noqa: E501


        :return: The e_mail of this V1User.  # noqa: E501
        :rtype: str
        """
        return self._e_mail

    @e_mail.setter
    def e_mail(self, e_mail):
        """Sets the e_mail of this V1User.


        :param e_mail: The e_mail of this V1User.  # noqa: E501
        :type: str
        """
        if e_mail is None:
            raise ValueError("Invalid value for `e_mail`, must not be `None`")  # noqa: E501

        self._e_mail = e_mail

    @property
    def groups(self):
        """Gets the groups of this V1User.  # noqa: E501


        :return: The groups of this V1User.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this V1User.


        :param groups: The groups of this V1User.  # noqa: E501
        :type: list[str]
        """
        if groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")  # noqa: E501

        self._groups = groups

    @property
    def issuer(self):
        """Gets the issuer of this V1User.  # noqa: E501


        :return: The issuer of this V1User.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this V1User.


        :param issuer: The issuer of this V1User.  # noqa: E501
        :type: str
        """
        if issuer is None:
            raise ValueError("Invalid value for `issuer`, must not be `None`")  # noqa: E501

        self._issuer = issuer

    @property
    def name(self):
        """Gets the name of this V1User.  # noqa: E501


        :return: The name of this V1User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1User.


        :param name: The name of this V1User.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def subject(self):
        """Gets the subject of this V1User.  # noqa: E501


        :return: The subject of this V1User.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this V1User.


        :param subject: The subject of this V1User.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def tenant(self):
        """Gets the tenant of this V1User.  # noqa: E501


        :return: The tenant of this V1User.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this V1User.


        :param tenant: The tenant of this V1User.  # noqa: E501
        :type: str
        """
        if tenant is None:
            raise ValueError("Invalid value for `tenant`, must not be `None`")  # noqa: E501

        self._tenant = tenant

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
        if issubclass(V1User, dict):
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
        if not isinstance(other, V1User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
