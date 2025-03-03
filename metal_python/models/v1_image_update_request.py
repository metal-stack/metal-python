# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.40.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1ImageUpdateRequest(object):
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
        'description': 'str',
        'expiration_date': 'datetime',
        'features': 'list[str]',
        'id': 'str',
        'name': 'str',
        'url': 'str',
        'usedby': 'list[str]'
    }

    attribute_map = {
        'classification': 'classification',
        'description': 'description',
        'expiration_date': 'expirationDate',
        'features': 'features',
        'id': 'id',
        'name': 'name',
        'url': 'url',
        'usedby': 'usedby'
    }

    def __init__(self, classification=None, description=None, expiration_date=None, features=None, id=None, name=None, url=None, usedby=None):  # noqa: E501
        """V1ImageUpdateRequest - a model defined in Swagger"""  # noqa: E501

        self._classification = None
        self._description = None
        self._expiration_date = None
        self._features = None
        self._id = None
        self._name = None
        self._url = None
        self._usedby = None
        self.discriminator = None

        if classification is not None:
            self.classification = classification
        if description is not None:
            self.description = description
        self.expiration_date = expiration_date
        if features is not None:
            self.features = features
        self.id = id
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if usedby is not None:
            self.usedby = usedby

    @property
    def classification(self):
        """Gets the classification of this V1ImageUpdateRequest.  # noqa: E501

        classification of this image  # noqa: E501

        :return: The classification of this V1ImageUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this V1ImageUpdateRequest.

        classification of this image  # noqa: E501

        :param classification: The classification of this V1ImageUpdateRequest.  # noqa: E501
        :type: str
        """

        self._classification = classification

    @property
    def description(self):
        """Gets the description of this V1ImageUpdateRequest.  # noqa: E501

        a description for this entity  # noqa: E501

        :return: The description of this V1ImageUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1ImageUpdateRequest.

        a description for this entity  # noqa: E501

        :param description: The description of this V1ImageUpdateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def expiration_date(self):
        """Gets the expiration_date of this V1ImageUpdateRequest.  # noqa: E501

        expirationDate of this image  # noqa: E501

        :return: The expiration_date of this V1ImageUpdateRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this V1ImageUpdateRequest.

        expirationDate of this image  # noqa: E501

        :param expiration_date: The expiration_date of this V1ImageUpdateRequest.  # noqa: E501
        :type: datetime
        """
        if expiration_date is None:
            raise ValueError("Invalid value for `expiration_date`, must not be `None`")  # noqa: E501

        self._expiration_date = expiration_date

    @property
    def features(self):
        """Gets the features of this V1ImageUpdateRequest.  # noqa: E501

        features of this image  # noqa: E501

        :return: The features of this V1ImageUpdateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this V1ImageUpdateRequest.

        features of this image  # noqa: E501

        :param features: The features of this V1ImageUpdateRequest.  # noqa: E501
        :type: list[str]
        """

        self._features = features

    @property
    def id(self):
        """Gets the id of this V1ImageUpdateRequest.  # noqa: E501

        the unique ID of this entity  # noqa: E501

        :return: The id of this V1ImageUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1ImageUpdateRequest.

        the unique ID of this entity  # noqa: E501

        :param id: The id of this V1ImageUpdateRequest.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this V1ImageUpdateRequest.  # noqa: E501

        a readable name for this entity  # noqa: E501

        :return: The name of this V1ImageUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1ImageUpdateRequest.

        a readable name for this entity  # noqa: E501

        :param name: The name of this V1ImageUpdateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this V1ImageUpdateRequest.  # noqa: E501

        the url of this image  # noqa: E501

        :return: The url of this V1ImageUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this V1ImageUpdateRequest.

        the url of this image  # noqa: E501

        :param url: The url of this V1ImageUpdateRequest.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def usedby(self):
        """Gets the usedby of this V1ImageUpdateRequest.  # noqa: E501

        machines where this image is in use  # noqa: E501

        :return: The usedby of this V1ImageUpdateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._usedby

    @usedby.setter
    def usedby(self, usedby):
        """Sets the usedby of this V1ImageUpdateRequest.

        machines where this image is in use  # noqa: E501

        :param usedby: The usedby of this V1ImageUpdateRequest.  # noqa: E501
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
        if issubclass(V1ImageUpdateRequest, dict):
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
        if not isinstance(other, V1ImageUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
