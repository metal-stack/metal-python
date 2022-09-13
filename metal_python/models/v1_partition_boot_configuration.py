# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.21.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1PartitionBootConfiguration(object):
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
        'commandline': 'str',
        'imageurl': 'str',
        'kernelurl': 'str'
    }

    attribute_map = {
        'commandline': 'commandline',
        'imageurl': 'imageurl',
        'kernelurl': 'kernelurl'
    }

    def __init__(self, commandline=None, imageurl=None, kernelurl=None):  # noqa: E501
        """V1PartitionBootConfiguration - a model defined in Swagger"""  # noqa: E501

        self._commandline = None
        self._imageurl = None
        self._kernelurl = None
        self.discriminator = None

        if commandline is not None:
            self.commandline = commandline
        if imageurl is not None:
            self.imageurl = imageurl
        if kernelurl is not None:
            self.kernelurl = kernelurl

    @property
    def commandline(self):
        """Gets the commandline of this V1PartitionBootConfiguration.  # noqa: E501

        the cmdline to the kernel for the boot image  # noqa: E501

        :return: The commandline of this V1PartitionBootConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._commandline

    @commandline.setter
    def commandline(self, commandline):
        """Sets the commandline of this V1PartitionBootConfiguration.

        the cmdline to the kernel for the boot image  # noqa: E501

        :param commandline: The commandline of this V1PartitionBootConfiguration.  # noqa: E501
        :type: str
        """

        self._commandline = commandline

    @property
    def imageurl(self):
        """Gets the imageurl of this V1PartitionBootConfiguration.  # noqa: E501

        the url to download the initrd for the boot image  # noqa: E501

        :return: The imageurl of this V1PartitionBootConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._imageurl

    @imageurl.setter
    def imageurl(self, imageurl):
        """Sets the imageurl of this V1PartitionBootConfiguration.

        the url to download the initrd for the boot image  # noqa: E501

        :param imageurl: The imageurl of this V1PartitionBootConfiguration.  # noqa: E501
        :type: str
        """

        self._imageurl = imageurl

    @property
    def kernelurl(self):
        """Gets the kernelurl of this V1PartitionBootConfiguration.  # noqa: E501

        the url to download the kernel for the boot image  # noqa: E501

        :return: The kernelurl of this V1PartitionBootConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._kernelurl

    @kernelurl.setter
    def kernelurl(self, kernelurl):
        """Sets the kernelurl of this V1PartitionBootConfiguration.

        the url to download the kernel for the boot image  # noqa: E501

        :param kernelurl: The kernelurl of this V1PartitionBootConfiguration.  # noqa: E501
        :type: str
        """

        self._kernelurl = kernelurl

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
        if issubclass(V1PartitionBootConfiguration, dict):
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
        if not isinstance(other, V1PartitionBootConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
