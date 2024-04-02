# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.28.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1ImageBase(object):
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
        'classification': 'str',
        'expiration_date': 'datetime',
        'features': 'list[str]',
        'url': 'str',
        'usedby': 'list[str]'
    }

    attribute_map = {
        'classification': 'classification',
        'expiration_date': 'expirationDate',
        'features': 'features',
        'url': 'url',
        'usedby': 'usedby'
    }

    def __init__(self, classification=None, expiration_date=None, features=None, url=None, usedby=None):  # noqa: E501
        """V1ImageBase - a model defined in Swagger"""  # noqa: E501

        self._classification = None
        self._expiration_date = None
        self._features = None
        self._url = None
        self._usedby = None
        self.discriminator = None

        if classification is not None:
            self.classification = classification
        self.expiration_date = expiration_date
        if features is not None:
            self.features = features
        if url is not None:
            self.url = url
        if usedby is not None:
            self.usedby = usedby

    @property
    def classification(self):
        """Gets the classification of this V1ImageBase.  # noqa: E501

        classification of this image  # noqa: E501

        :return: The classification of this V1ImageBase.  # noqa: E501
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this V1ImageBase.

        classification of this image  # noqa: E501

        :param classification: The classification of this V1ImageBase.  # noqa: E501
        :type: str
        """

        self._classification = classification

    @property
    def expiration_date(self):
        """Gets the expiration_date of this V1ImageBase.  # noqa: E501

        expirationDate of this image  # noqa: E501

        :return: The expiration_date of this V1ImageBase.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this V1ImageBase.

        expirationDate of this image  # noqa: E501

        :param expiration_date: The expiration_date of this V1ImageBase.  # noqa: E501
        :type: datetime
        """
        if expiration_date is None:
            raise ValueError("Invalid value for `expiration_date`, must not be `None`")  # noqa: E501

        self._expiration_date = expiration_date

    @property
    def features(self):
        """Gets the features of this V1ImageBase.  # noqa: E501

        features of this image  # noqa: E501

        :return: The features of this V1ImageBase.  # noqa: E501
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this V1ImageBase.

        features of this image  # noqa: E501

        :param features: The features of this V1ImageBase.  # noqa: E501
        :type: list[str]
        """

        self._features = features

    @property
    def url(self):
        """Gets the url of this V1ImageBase.  # noqa: E501

        the url of this image  # noqa: E501

        :return: The url of this V1ImageBase.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this V1ImageBase.

        the url of this image  # noqa: E501

        :param url: The url of this V1ImageBase.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def usedby(self):
        """Gets the usedby of this V1ImageBase.  # noqa: E501

        machines where this image is in use  # noqa: E501

        :return: The usedby of this V1ImageBase.  # noqa: E501
        :rtype: list[str]
        """
        return self._usedby

    @usedby.setter
    def usedby(self, usedby):
        """Sets the usedby of this V1ImageBase.

        machines where this image is in use  # noqa: E501

        :param usedby: The usedby of this V1ImageBase.  # noqa: E501
        :type: list[str]
        """

        self._usedby = usedby

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
        if issubclass(V1ImageBase, dict):
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
        if not isinstance(other, V1ImageBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
