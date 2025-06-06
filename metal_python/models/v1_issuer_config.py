# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.41.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1IssuerConfig(object):
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
        'client_id': 'str',
        'url': 'str'
    }

    attribute_map = {
        'client_id': 'client_id',
        'url': 'url'
    }

    def __init__(self, client_id=None, url=None):  # noqa: E501
        """V1IssuerConfig - a model defined in Swagger"""  # noqa: E501

        self._client_id = None
        self._url = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if url is not None:
            self.url = url

    @property
    def client_id(self):
        """Gets the client_id of this V1IssuerConfig.  # noqa: E501


        :return: The client_id of this V1IssuerConfig.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this V1IssuerConfig.


        :param client_id: The client_id of this V1IssuerConfig.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def url(self):
        """Gets the url of this V1IssuerConfig.  # noqa: E501


        :return: The url of this V1IssuerConfig.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this V1IssuerConfig.


        :param url: The url of this V1IssuerConfig.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(V1IssuerConfig, dict):
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
        if not isinstance(other, V1IssuerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
