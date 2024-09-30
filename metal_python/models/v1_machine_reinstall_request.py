# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.37.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineReinstallRequest(object):
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
        'id': 'str',
        'imageid': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'imageid': 'imageid',
        'name': 'name'
    }

    def __init__(self, description=None, id=None, imageid=None, name=None):  # noqa: E501
        """V1MachineReinstallRequest - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._id = None
        self._imageid = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.id = id
        self.imageid = imageid
        if name is not None:
            self.name = name

    @property
    def description(self):
        """Gets the description of this V1MachineReinstallRequest.  # noqa: E501

        a description for this entity  # noqa: E501

        :return: The description of this V1MachineReinstallRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1MachineReinstallRequest.

        a description for this entity  # noqa: E501

        :param description: The description of this V1MachineReinstallRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this V1MachineReinstallRequest.  # noqa: E501

        the unique ID of this entity  # noqa: E501

        :return: The id of this V1MachineReinstallRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1MachineReinstallRequest.

        the unique ID of this entity  # noqa: E501

        :param id: The id of this V1MachineReinstallRequest.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def imageid(self):
        """Gets the imageid of this V1MachineReinstallRequest.  # noqa: E501

        the image id to be installed  # noqa: E501

        :return: The imageid of this V1MachineReinstallRequest.  # noqa: E501
        :rtype: str
        """
        return self._imageid

    @imageid.setter
    def imageid(self, imageid):
        """Sets the imageid of this V1MachineReinstallRequest.

        the image id to be installed  # noqa: E501

        :param imageid: The imageid of this V1MachineReinstallRequest.  # noqa: E501
        :type: str
        """
        if imageid is None:
            raise ValueError("Invalid value for `imageid`, must not be `None`")  # noqa: E501

        self._imageid = imageid

    @property
    def name(self):
        """Gets the name of this V1MachineReinstallRequest.  # noqa: E501

        a readable name for this entity  # noqa: E501

        :return: The name of this V1MachineReinstallRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1MachineReinstallRequest.

        a readable name for this entity  # noqa: E501

        :param name: The name of this V1MachineReinstallRequest.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(V1MachineReinstallRequest, dict):
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
        if not isinstance(other, V1MachineReinstallRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
