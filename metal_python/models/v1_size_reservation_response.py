# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.32.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1SizeReservationResponse(object):
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
        'labels': 'dict(str, str)',
        'partitionid': 'str',
        'projectallocations': 'int',
        'projectid': 'str',
        'projectname': 'str',
        'reservations': 'int',
        'sizeid': 'str',
        'tenant': 'str',
        'usedreservations': 'int'
    }

    attribute_map = {
        'labels': 'labels',
        'partitionid': 'partitionid',
        'projectallocations': 'projectallocations',
        'projectid': 'projectid',
        'projectname': 'projectname',
        'reservations': 'reservations',
        'sizeid': 'sizeid',
        'tenant': 'tenant',
        'usedreservations': 'usedreservations'
    }

    def __init__(self, labels=None, partitionid=None, projectallocations=None, projectid=None, projectname=None, reservations=None, sizeid=None, tenant=None, usedreservations=None):  # noqa: E501
        """V1SizeReservationResponse - a model defined in Swagger"""  # noqa: E501

        self._labels = None
        self._partitionid = None
        self._projectallocations = None
        self._projectid = None
        self._projectname = None
        self._reservations = None
        self._sizeid = None
        self._tenant = None
        self._usedreservations = None
        self.discriminator = None

        if labels is not None:
            self.labels = labels
        self.partitionid = partitionid
        self.projectallocations = projectallocations
        self.projectid = projectid
        self.projectname = projectname
        self.reservations = reservations
        self.sizeid = sizeid
        self.tenant = tenant
        self.usedreservations = usedreservations

    @property
    def labels(self):
        """Gets the labels of this V1SizeReservationResponse.  # noqa: E501

        free labels associated with this size reservation.  # noqa: E501

        :return: The labels of this V1SizeReservationResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this V1SizeReservationResponse.

        free labels associated with this size reservation.  # noqa: E501

        :param labels: The labels of this V1SizeReservationResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def partitionid(self):
        """Gets the partitionid of this V1SizeReservationResponse.  # noqa: E501

        the partition id of this size reservation  # noqa: E501

        :return: The partitionid of this V1SizeReservationResponse.  # noqa: E501
        :rtype: str
        """
        return self._partitionid

    @partitionid.setter
    def partitionid(self, partitionid):
        """Sets the partitionid of this V1SizeReservationResponse.

        the partition id of this size reservation  # noqa: E501

        :param partitionid: The partitionid of this V1SizeReservationResponse.  # noqa: E501
        :type: str
        """
        if partitionid is None:
            raise ValueError("Invalid value for `partitionid`, must not be `None`")  # noqa: E501

        self._partitionid = partitionid

    @property
    def projectallocations(self):
        """Gets the projectallocations of this V1SizeReservationResponse.  # noqa: E501

        the amount of allocations of this project referenced by this size reservation  # noqa: E501

        :return: The projectallocations of this V1SizeReservationResponse.  # noqa: E501
        :rtype: int
        """
        return self._projectallocations

    @projectallocations.setter
    def projectallocations(self, projectallocations):
        """Sets the projectallocations of this V1SizeReservationResponse.

        the amount of allocations of this project referenced by this size reservation  # noqa: E501

        :param projectallocations: The projectallocations of this V1SizeReservationResponse.  # noqa: E501
        :type: int
        """
        if projectallocations is None:
            raise ValueError("Invalid value for `projectallocations`, must not be `None`")  # noqa: E501

        self._projectallocations = projectallocations

    @property
    def projectid(self):
        """Gets the projectid of this V1SizeReservationResponse.  # noqa: E501

        the project id of this size reservation  # noqa: E501

        :return: The projectid of this V1SizeReservationResponse.  # noqa: E501
        :rtype: str
        """
        return self._projectid

    @projectid.setter
    def projectid(self, projectid):
        """Sets the projectid of this V1SizeReservationResponse.

        the project id of this size reservation  # noqa: E501

        :param projectid: The projectid of this V1SizeReservationResponse.  # noqa: E501
        :type: str
        """
        if projectid is None:
            raise ValueError("Invalid value for `projectid`, must not be `None`")  # noqa: E501

        self._projectid = projectid

    @property
    def projectname(self):
        """Gets the projectname of this V1SizeReservationResponse.  # noqa: E501

        the project name of this size reservation  # noqa: E501

        :return: The projectname of this V1SizeReservationResponse.  # noqa: E501
        :rtype: str
        """
        return self._projectname

    @projectname.setter
    def projectname(self, projectname):
        """Sets the projectname of this V1SizeReservationResponse.

        the project name of this size reservation  # noqa: E501

        :param projectname: The projectname of this V1SizeReservationResponse.  # noqa: E501
        :type: str
        """
        if projectname is None:
            raise ValueError("Invalid value for `projectname`, must not be `None`")  # noqa: E501

        self._projectname = projectname

    @property
    def reservations(self):
        """Gets the reservations of this V1SizeReservationResponse.  # noqa: E501

        the amount of reservations of this size reservation  # noqa: E501

        :return: The reservations of this V1SizeReservationResponse.  # noqa: E501
        :rtype: int
        """
        return self._reservations

    @reservations.setter
    def reservations(self, reservations):
        """Sets the reservations of this V1SizeReservationResponse.

        the amount of reservations of this size reservation  # noqa: E501

        :param reservations: The reservations of this V1SizeReservationResponse.  # noqa: E501
        :type: int
        """
        if reservations is None:
            raise ValueError("Invalid value for `reservations`, must not be `None`")  # noqa: E501

        self._reservations = reservations

    @property
    def sizeid(self):
        """Gets the sizeid of this V1SizeReservationResponse.  # noqa: E501

        the size id of this size reservation  # noqa: E501

        :return: The sizeid of this V1SizeReservationResponse.  # noqa: E501
        :rtype: str
        """
        return self._sizeid

    @sizeid.setter
    def sizeid(self, sizeid):
        """Sets the sizeid of this V1SizeReservationResponse.

        the size id of this size reservation  # noqa: E501

        :param sizeid: The sizeid of this V1SizeReservationResponse.  # noqa: E501
        :type: str
        """
        if sizeid is None:
            raise ValueError("Invalid value for `sizeid`, must not be `None`")  # noqa: E501

        self._sizeid = sizeid

    @property
    def tenant(self):
        """Gets the tenant of this V1SizeReservationResponse.  # noqa: E501

        the tenant of this size reservation  # noqa: E501

        :return: The tenant of this V1SizeReservationResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this V1SizeReservationResponse.

        the tenant of this size reservation  # noqa: E501

        :param tenant: The tenant of this V1SizeReservationResponse.  # noqa: E501
        :type: str
        """
        if tenant is None:
            raise ValueError("Invalid value for `tenant`, must not be `None`")  # noqa: E501

        self._tenant = tenant

    @property
    def usedreservations(self):
        """Gets the usedreservations of this V1SizeReservationResponse.  # noqa: E501

        the used amount of reservations of this size reservation  # noqa: E501

        :return: The usedreservations of this V1SizeReservationResponse.  # noqa: E501
        :rtype: int
        """
        return self._usedreservations

    @usedreservations.setter
    def usedreservations(self, usedreservations):
        """Sets the usedreservations of this V1SizeReservationResponse.

        the used amount of reservations of this size reservation  # noqa: E501

        :param usedreservations: The usedreservations of this V1SizeReservationResponse.  # noqa: E501
        :type: int
        """
        if usedreservations is None:
            raise ValueError("Invalid value for `usedreservations`, must not be `None`")  # noqa: E501

        self._usedreservations = usedreservations

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
        if issubclass(V1SizeReservationResponse, dict):
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
        if not isinstance(other, V1SizeReservationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
