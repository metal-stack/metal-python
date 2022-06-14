# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.18.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class HttperrorsHTTPErrorResponse(object):
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
        'statuscode': 'int'
    }

    attribute_map = {
        'message': 'message',
        'statuscode': 'statuscode'
    }

    def __init__(self, message=None, statuscode=None):  # noqa: E501
        """HttperrorsHTTPErrorResponse - a model defined in Swagger"""  # noqa: E501

        self._message = None
        self._statuscode = None
        self.discriminator = None

        self.message = message
        self.statuscode = statuscode

    @property
    def message(self):
        """Gets the message of this HttperrorsHTTPErrorResponse.  # noqa: E501

        error message  # noqa: E501

        :return: The message of this HttperrorsHTTPErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this HttperrorsHTTPErrorResponse.

        error message  # noqa: E501

        :param message: The message of this HttperrorsHTTPErrorResponse.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def statuscode(self):
        """Gets the statuscode of this HttperrorsHTTPErrorResponse.  # noqa: E501

        http status code  # noqa: E501

        :return: The statuscode of this HttperrorsHTTPErrorResponse.  # noqa: E501
        :rtype: int
        """
        return self._statuscode

    @statuscode.setter
    def statuscode(self, statuscode):
        """Sets the statuscode of this HttperrorsHTTPErrorResponse.

        http status code  # noqa: E501

        :param statuscode: The statuscode of this HttperrorsHTTPErrorResponse.  # noqa: E501
        :type: int
        """
        if statuscode is None:
            raise ValueError("Invalid value for `statuscode`, must not be `None`")  # noqa: E501

        self._statuscode = statuscode

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
        if issubclass(HttperrorsHTTPErrorResponse, dict):
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
        if not isinstance(other, HttperrorsHTTPErrorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
