# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.21.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1ProjectUpdateRequest(object):
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
        'meta': 'V1Meta',
        'name': 'str',
        'quotas': 'V1QuotaSet',
        'tenant_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'meta': 'meta',
        'name': 'name',
        'quotas': 'quotas',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, description=None, meta=None, name=None, quotas=None, tenant_id=None):  # noqa: E501
        """V1ProjectUpdateRequest - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._meta = None
        self._name = None
        self._quotas = None
        self._tenant_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if meta is not None:
            self.meta = meta
        if name is not None:
            self.name = name
        if quotas is not None:
            self.quotas = quotas
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def description(self):
        """Gets the description of this V1ProjectUpdateRequest.  # noqa: E501


        :return: The description of this V1ProjectUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1ProjectUpdateRequest.


        :param description: The description of this V1ProjectUpdateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def meta(self):
        """Gets the meta of this V1ProjectUpdateRequest.  # noqa: E501


        :return: The meta of this V1ProjectUpdateRequest.  # noqa: E501
        :rtype: V1Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this V1ProjectUpdateRequest.


        :param meta: The meta of this V1ProjectUpdateRequest.  # noqa: E501
        :type: V1Meta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this V1ProjectUpdateRequest.  # noqa: E501


        :return: The name of this V1ProjectUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1ProjectUpdateRequest.


        :param name: The name of this V1ProjectUpdateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def quotas(self):
        """Gets the quotas of this V1ProjectUpdateRequest.  # noqa: E501


        :return: The quotas of this V1ProjectUpdateRequest.  # noqa: E501
        :rtype: V1QuotaSet
        """
        return self._quotas

    @quotas.setter
    def quotas(self, quotas):
        """Sets the quotas of this V1ProjectUpdateRequest.


        :param quotas: The quotas of this V1ProjectUpdateRequest.  # noqa: E501
        :type: V1QuotaSet
        """

        self._quotas = quotas

    @property
    def tenant_id(self):
        """Gets the tenant_id of this V1ProjectUpdateRequest.  # noqa: E501


        :return: The tenant_id of this V1ProjectUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this V1ProjectUpdateRequest.


        :param tenant_id: The tenant_id of this V1ProjectUpdateRequest.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

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
        if issubclass(V1ProjectUpdateRequest, dict):
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
        if not isinstance(other, V1ProjectUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
