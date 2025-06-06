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


class V1MetalGPU(object):
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
        'model': 'str',
        'vendor': 'str'
    }

    attribute_map = {
        'model': 'model',
        'vendor': 'vendor'
    }

    def __init__(self, model=None, vendor=None):  # noqa: E501
        """V1MetalGPU - a model defined in Swagger"""  # noqa: E501

        self._model = None
        self._vendor = None
        self.discriminator = None

        self.model = model
        self.vendor = vendor

    @property
    def model(self):
        """Gets the model of this V1MetalGPU.  # noqa: E501

        the gpu model  # noqa: E501

        :return: The model of this V1MetalGPU.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this V1MetalGPU.

        the gpu model  # noqa: E501

        :param model: The model of this V1MetalGPU.  # noqa: E501
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def vendor(self):
        """Gets the vendor of this V1MetalGPU.  # noqa: E501

        the gpu vendor  # noqa: E501

        :return: The vendor of this V1MetalGPU.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this V1MetalGPU.

        the gpu vendor  # noqa: E501

        :param vendor: The vendor of this V1MetalGPU.  # noqa: E501
        :type: str
        """
        if vendor is None:
            raise ValueError("Invalid value for `vendor`, must not be `None`")  # noqa: E501

        self._vendor = vendor

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
        if issubclass(V1MetalGPU, dict):
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
        if not isinstance(other, V1MetalGPU):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
