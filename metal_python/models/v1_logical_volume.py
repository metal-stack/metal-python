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


class V1LogicalVolume(object):
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
        'lvmtype': 'str',
        'name': 'str',
        'size': 'int',
        'volumegroup': 'str'
    }

    attribute_map = {
        'lvmtype': 'lvmtype',
        'name': 'name',
        'size': 'size',
        'volumegroup': 'volumegroup'
    }

    def __init__(self, lvmtype=None, name=None, size=None, volumegroup=None):  # noqa: E501
        """V1LogicalVolume - a model defined in Swagger"""  # noqa: E501

        self._lvmtype = None
        self._name = None
        self._size = None
        self._volumegroup = None
        self.discriminator = None

        self.lvmtype = lvmtype
        self.name = name
        self.size = size
        self.volumegroup = volumegroup

    @property
    def lvmtype(self):
        """Gets the lvmtype of this V1LogicalVolume.  # noqa: E501

        the type of this logical volume can be either linear|striped|raid1  # noqa: E501

        :return: The lvmtype of this V1LogicalVolume.  # noqa: E501
        :rtype: str
        """
        return self._lvmtype

    @lvmtype.setter
    def lvmtype(self, lvmtype):
        """Sets the lvmtype of this V1LogicalVolume.

        the type of this logical volume can be either linear|striped|raid1  # noqa: E501

        :param lvmtype: The lvmtype of this V1LogicalVolume.  # noqa: E501
        :type: str
        """
        if lvmtype is None:
            raise ValueError("Invalid value for `lvmtype`, must not be `None`")  # noqa: E501

        self._lvmtype = lvmtype

    @property
    def name(self):
        """Gets the name of this V1LogicalVolume.  # noqa: E501

        the name of the logical volume  # noqa: E501

        :return: The name of this V1LogicalVolume.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1LogicalVolume.

        the name of the logical volume  # noqa: E501

        :param name: The name of this V1LogicalVolume.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def size(self):
        """Gets the size of this V1LogicalVolume.  # noqa: E501

        size in mebibytes (MiB) of this volume  # noqa: E501

        :return: The size of this V1LogicalVolume.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this V1LogicalVolume.

        size in mebibytes (MiB) of this volume  # noqa: E501

        :param size: The size of this V1LogicalVolume.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def volumegroup(self):
        """Gets the volumegroup of this V1LogicalVolume.  # noqa: E501

        the name of the volume group where to create the logical volume onto  # noqa: E501

        :return: The volumegroup of this V1LogicalVolume.  # noqa: E501
        :rtype: str
        """
        return self._volumegroup

    @volumegroup.setter
    def volumegroup(self, volumegroup):
        """Sets the volumegroup of this V1LogicalVolume.

        the name of the volume group where to create the logical volume onto  # noqa: E501

        :param volumegroup: The volumegroup of this V1LogicalVolume.  # noqa: E501
        :type: str
        """
        if volumegroup is None:
            raise ValueError("Invalid value for `volumegroup`, must not be `None`")  # noqa: E501

        self._volumegroup = volumegroup

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
        if issubclass(V1LogicalVolume, dict):
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
        if not isinstance(other, V1LogicalVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
