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


class RestHealthResponse(object):
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
        'message': 'str',
        'services': 'dict(str, RestHealthResponse)',
        'status': 'str'
    }

    attribute_map = {
        'message': 'message',
        'services': 'services',
        'status': 'status'
    }

    def __init__(self, message=None, services=None, status=None):  # noqa: E501
        """RestHealthResponse - a model defined in Swagger"""  # noqa: E501

        self._message = None
        self._services = None
        self._status = None
        self.discriminator = None

        self.message = message
        if services is not None:
            self.services = services
        self.status = status

    @property
    def message(self):
        """Gets the message of this RestHealthResponse.  # noqa: E501


        :return: The message of this RestHealthResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RestHealthResponse.


        :param message: The message of this RestHealthResponse.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def services(self):
        """Gets the services of this RestHealthResponse.  # noqa: E501


        :return: The services of this RestHealthResponse.  # noqa: E501
        :rtype: dict(str, RestHealthResponse)
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this RestHealthResponse.


        :param services: The services of this RestHealthResponse.  # noqa: E501
        :type: dict(str, RestHealthResponse)
        """

        self._services = services

    @property
    def status(self):
        """Gets the status of this RestHealthResponse.  # noqa: E501


        :return: The status of this RestHealthResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RestHealthResponse.


        :param status: The status of this RestHealthResponse.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(RestHealthResponse, dict):
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
        if not isinstance(other, RestHealthResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
