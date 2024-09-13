# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.35.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SizeImageConstraintBase(object):
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
        'images': 'dict(str, str)'
    }

    attribute_map = {
        'images': 'images'
    }

    def __init__(self, images=None):  # noqa: E501
        """V1SizeImageConstraintBase - a model defined in Swagger"""  # noqa: E501

        self._images = None
        self.discriminator = None

        self.images = images

    @property
    def images(self):
        """Gets the images of this V1SizeImageConstraintBase.  # noqa: E501

        a list of images for this constraints apply  # noqa: E501

        :return: The images of this V1SizeImageConstraintBase.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this V1SizeImageConstraintBase.

        a list of images for this constraints apply  # noqa: E501

        :param images: The images of this V1SizeImageConstraintBase.  # noqa: E501
        :type: dict(str, str)
        """
        if images is None:
            raise ValueError("Invalid value for `images`, must not be `None`")  # noqa: E501

        self._images = images

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
        if issubclass(V1SizeImageConstraintBase, dict):
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
        if not isinstance(other, V1SizeImageConstraintBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
