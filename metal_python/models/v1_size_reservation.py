# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.31.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SizeReservation(object):
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
        'amount': 'int',
        'description': 'str',
        'partitionids': 'list[str]',
        'projectid': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'description': 'description',
        'partitionids': 'partitionids',
        'projectid': 'projectid'
    }

    def __init__(self, amount=None, description=None, partitionids=None, projectid=None):  # noqa: E501
        """V1SizeReservation - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._description = None
        self._partitionids = None
        self._projectid = None
        self.discriminator = None

        self.amount = amount
        if description is not None:
            self.description = description
        self.partitionids = partitionids
        self.projectid = projectid

    @property
    def amount(self):
        """Gets the amount of this V1SizeReservation.  # noqa: E501

        the amount of reserved machine allocations for this size  # noqa: E501

        :return: The amount of this V1SizeReservation.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this V1SizeReservation.

        the amount of reserved machine allocations for this size  # noqa: E501

        :param amount: The amount of this V1SizeReservation.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def description(self):
        """Gets the description of this V1SizeReservation.  # noqa: E501

        a description for this reservation  # noqa: E501

        :return: The description of this V1SizeReservation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1SizeReservation.

        a description for this reservation  # noqa: E501

        :param description: The description of this V1SizeReservation.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def partitionids(self):
        """Gets the partitionids of this V1SizeReservation.  # noqa: E501

        the partitions in which this size reservation is considered, the amount is valid for every partition  # noqa: E501

        :return: The partitionids of this V1SizeReservation.  # noqa: E501
        :rtype: list[str]
        """
        return self._partitionids

    @partitionids.setter
    def partitionids(self, partitionids):
        """Sets the partitionids of this V1SizeReservation.

        the partitions in which this size reservation is considered, the amount is valid for every partition  # noqa: E501

        :param partitionids: The partitionids of this V1SizeReservation.  # noqa: E501
        :type: list[str]
        """
        if partitionids is None:
            raise ValueError("Invalid value for `partitionids`, must not be `None`")  # noqa: E501

        self._partitionids = partitionids

    @property
    def projectid(self):
        """Gets the projectid of this V1SizeReservation.  # noqa: E501

        the project for which this size reservation is considered  # noqa: E501

        :return: The projectid of this V1SizeReservation.  # noqa: E501
        :rtype: str
        """
        return self._projectid

    @projectid.setter
    def projectid(self, projectid):
        """Sets the projectid of this V1SizeReservation.

        the project for which this size reservation is considered  # noqa: E501

        :param projectid: The projectid of this V1SizeReservation.  # noqa: E501
        :type: str
        """
        if projectid is None:
            raise ValueError("Invalid value for `projectid`, must not be `None`")  # noqa: E501

        self._projectid = projectid

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
        if issubclass(V1SizeReservation, dict):
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
        if not isinstance(other, V1SizeReservation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
