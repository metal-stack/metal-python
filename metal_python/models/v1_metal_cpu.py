# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.34.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MetalCPU(object):
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
        'cores': 'int',
        'model': 'str',
        'threads': 'int',
        'vendor': 'str'
    }

    attribute_map = {
        'cores': 'cores',
        'model': 'model',
        'threads': 'threads',
        'vendor': 'vendor'
    }

    def __init__(self, cores=None, model=None, threads=None, vendor=None):  # noqa: E501
        """V1MetalCPU - a model defined in Swagger"""  # noqa: E501

        self._cores = None
        self._model = None
        self._threads = None
        self._vendor = None
        self.discriminator = None

        self.cores = cores
        self.model = model
        self.threads = threads
        self.vendor = vendor

    @property
    def cores(self):
        """Gets the cores of this V1MetalCPU.  # noqa: E501

        the cpu cores  # noqa: E501

        :return: The cores of this V1MetalCPU.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this V1MetalCPU.

        the cpu cores  # noqa: E501

        :param cores: The cores of this V1MetalCPU.  # noqa: E501
        :type: int
        """
        if cores is None:
            raise ValueError("Invalid value for `cores`, must not be `None`")  # noqa: E501

        self._cores = cores

    @property
    def model(self):
        """Gets the model of this V1MetalCPU.  # noqa: E501

        the cpu model  # noqa: E501

        :return: The model of this V1MetalCPU.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this V1MetalCPU.

        the cpu model  # noqa: E501

        :param model: The model of this V1MetalCPU.  # noqa: E501
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def threads(self):
        """Gets the threads of this V1MetalCPU.  # noqa: E501

        the cpu threads  # noqa: E501

        :return: The threads of this V1MetalCPU.  # noqa: E501
        :rtype: int
        """
        return self._threads

    @threads.setter
    def threads(self, threads):
        """Sets the threads of this V1MetalCPU.

        the cpu threads  # noqa: E501

        :param threads: The threads of this V1MetalCPU.  # noqa: E501
        :type: int
        """
        if threads is None:
            raise ValueError("Invalid value for `threads`, must not be `None`")  # noqa: E501

        self._threads = threads

    @property
    def vendor(self):
        """Gets the vendor of this V1MetalCPU.  # noqa: E501

        the cpu vendor  # noqa: E501

        :return: The vendor of this V1MetalCPU.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this V1MetalCPU.

        the cpu vendor  # noqa: E501

        :param vendor: The vendor of this V1MetalCPU.  # noqa: E501
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
        if issubclass(V1MetalCPU, dict):
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
        if not isinstance(other, V1MetalCPU):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
