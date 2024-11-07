# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.38.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SizeReservationUsageResponse(object):
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
        'id': 'str',
        'labels': 'dict(str, str)',
        'name': 'str',
        'partitionid': 'str',
        'projectallocations': 'int',
        'projectid': 'str',
        'sizeid': 'str',
        'usedamount': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'description': 'description',
        'id': 'id',
        'labels': 'labels',
        'name': 'name',
        'partitionid': 'partitionid',
        'projectallocations': 'projectallocations',
        'projectid': 'projectid',
        'sizeid': 'sizeid',
        'usedamount': 'usedamount'
    }

    def __init__(self, amount=None, description=None, id=None, labels=None, name=None, partitionid=None, projectallocations=None, projectid=None, sizeid=None, usedamount=None):  # noqa: E501
        """V1SizeReservationUsageResponse - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._description = None
        self._id = None
        self._labels = None
        self._name = None
        self._partitionid = None
        self._projectallocations = None
        self._projectid = None
        self._sizeid = None
        self._usedamount = None
        self.discriminator = None

        self.amount = amount
        if description is not None:
            self.description = description
        self.id = id
        if labels is not None:
            self.labels = labels
        if name is not None:
            self.name = name
        self.partitionid = partitionid
        self.projectallocations = projectallocations
        self.projectid = projectid
        self.sizeid = sizeid
        self.usedamount = usedamount

    @property
    def amount(self):
        """Gets the amount of this V1SizeReservationUsageResponse.  # noqa: E501

        the amount of reservations of this size reservation  # noqa: E501

        :return: The amount of this V1SizeReservationUsageResponse.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this V1SizeReservationUsageResponse.

        the amount of reservations of this size reservation  # noqa: E501

        :param amount: The amount of this V1SizeReservationUsageResponse.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def description(self):
        """Gets the description of this V1SizeReservationUsageResponse.  # noqa: E501

        a description for this entity  # noqa: E501

        :return: The description of this V1SizeReservationUsageResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1SizeReservationUsageResponse.

        a description for this entity  # noqa: E501

        :param description: The description of this V1SizeReservationUsageResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this V1SizeReservationUsageResponse.  # noqa: E501

        the unique ID of this entity  # noqa: E501

        :return: The id of this V1SizeReservationUsageResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1SizeReservationUsageResponse.

        the unique ID of this entity  # noqa: E501

        :param id: The id of this V1SizeReservationUsageResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this V1SizeReservationUsageResponse.  # noqa: E501

        free labels associated with this size reservation.  # noqa: E501

        :return: The labels of this V1SizeReservationUsageResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this V1SizeReservationUsageResponse.

        free labels associated with this size reservation.  # noqa: E501

        :param labels: The labels of this V1SizeReservationUsageResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this V1SizeReservationUsageResponse.  # noqa: E501

        a readable name for this entity  # noqa: E501

        :return: The name of this V1SizeReservationUsageResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1SizeReservationUsageResponse.

        a readable name for this entity  # noqa: E501

        :param name: The name of this V1SizeReservationUsageResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def partitionid(self):
        """Gets the partitionid of this V1SizeReservationUsageResponse.  # noqa: E501

        the partition id of this size reservation  # noqa: E501

        :return: The partitionid of this V1SizeReservationUsageResponse.  # noqa: E501
        :rtype: str
        """
        return self._partitionid

    @partitionid.setter
    def partitionid(self, partitionid):
        """Sets the partitionid of this V1SizeReservationUsageResponse.

        the partition id of this size reservation  # noqa: E501

        :param partitionid: The partitionid of this V1SizeReservationUsageResponse.  # noqa: E501
        :type: str
        """
        if partitionid is None:
            raise ValueError("Invalid value for `partitionid`, must not be `None`")  # noqa: E501

        self._partitionid = partitionid

    @property
    def projectallocations(self):
        """Gets the projectallocations of this V1SizeReservationUsageResponse.  # noqa: E501

        the amount of allocations of this project referenced by this size reservation  # noqa: E501

        :return: The projectallocations of this V1SizeReservationUsageResponse.  # noqa: E501
        :rtype: int
        """
        return self._projectallocations

    @projectallocations.setter
    def projectallocations(self, projectallocations):
        """Sets the projectallocations of this V1SizeReservationUsageResponse.

        the amount of allocations of this project referenced by this size reservation  # noqa: E501

        :param projectallocations: The projectallocations of this V1SizeReservationUsageResponse.  # noqa: E501
        :type: int
        """
        if projectallocations is None:
            raise ValueError("Invalid value for `projectallocations`, must not be `None`")  # noqa: E501

        self._projectallocations = projectallocations

    @property
    def projectid(self):
        """Gets the projectid of this V1SizeReservationUsageResponse.  # noqa: E501

        the project id of this size reservation  # noqa: E501

        :return: The projectid of this V1SizeReservationUsageResponse.  # noqa: E501
        :rtype: str
        """
        return self._projectid

    @projectid.setter
    def projectid(self, projectid):
        """Sets the projectid of this V1SizeReservationUsageResponse.

        the project id of this size reservation  # noqa: E501

        :param projectid: The projectid of this V1SizeReservationUsageResponse.  # noqa: E501
        :type: str
        """
        if projectid is None:
            raise ValueError("Invalid value for `projectid`, must not be `None`")  # noqa: E501

        self._projectid = projectid

    @property
    def sizeid(self):
        """Gets the sizeid of this V1SizeReservationUsageResponse.  # noqa: E501

        the size id of this size reservation  # noqa: E501

        :return: The sizeid of this V1SizeReservationUsageResponse.  # noqa: E501
        :rtype: str
        """
        return self._sizeid

    @sizeid.setter
    def sizeid(self, sizeid):
        """Sets the sizeid of this V1SizeReservationUsageResponse.

        the size id of this size reservation  # noqa: E501

        :param sizeid: The sizeid of this V1SizeReservationUsageResponse.  # noqa: E501
        :type: str
        """
        if sizeid is None:
            raise ValueError("Invalid value for `sizeid`, must not be `None`")  # noqa: E501

        self._sizeid = sizeid

    @property
    def usedamount(self):
        """Gets the usedamount of this V1SizeReservationUsageResponse.  # noqa: E501

        the used amount of reservations of this size reservation  # noqa: E501

        :return: The usedamount of this V1SizeReservationUsageResponse.  # noqa: E501
        :rtype: int
        """
        return self._usedamount

    @usedamount.setter
    def usedamount(self, usedamount):
        """Sets the usedamount of this V1SizeReservationUsageResponse.

        the used amount of reservations of this size reservation  # noqa: E501

        :param usedamount: The usedamount of this V1SizeReservationUsageResponse.  # noqa: E501
        :type: int
        """
        if usedamount is None:
            raise ValueError("Invalid value for `usedamount`, must not be `None`")  # noqa: E501

        self._usedamount = usedamount

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
        if issubclass(V1SizeReservationUsageResponse, dict):
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
        if not isinstance(other, V1SizeReservationUsageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
