# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.39.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1ServerCapacity(object):
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
        'allocatable': 'int',
        'allocated': 'int',
        'faulty': 'int',
        'faultymachines': 'list[str]',
        'free': 'int',
        'other': 'int',
        'othermachines': 'list[str]',
        'phoned_home': 'int',
        'remainingreservations': 'int',
        'reservations': 'int',
        'size': 'str',
        'total': 'int',
        'unavailable': 'int',
        'usedreservations': 'int',
        'waiting': 'int'
    }

    attribute_map = {
        'allocatable': 'allocatable',
        'allocated': 'allocated',
        'faulty': 'faulty',
        'faultymachines': 'faultymachines',
        'free': 'free',
        'other': 'other',
        'othermachines': 'othermachines',
        'phoned_home': 'phoned_home',
        'remainingreservations': 'remainingreservations',
        'reservations': 'reservations',
        'size': 'size',
        'total': 'total',
        'unavailable': 'unavailable',
        'usedreservations': 'usedreservations',
        'waiting': 'waiting'
    }

    def __init__(self, allocatable=None, allocated=None, faulty=None, faultymachines=None, free=None, other=None, othermachines=None, phoned_home=None, remainingreservations=None, reservations=None, size=None, total=None, unavailable=None, usedreservations=None, waiting=None):  # noqa: E501
        """V1ServerCapacity - a model defined in Swagger"""  # noqa: E501

        self._allocatable = None
        self._allocated = None
        self._faulty = None
        self._faultymachines = None
        self._free = None
        self._other = None
        self._othermachines = None
        self._phoned_home = None
        self._remainingreservations = None
        self._reservations = None
        self._size = None
        self._total = None
        self._unavailable = None
        self._usedreservations = None
        self._waiting = None
        self.discriminator = None

        if allocatable is not None:
            self.allocatable = allocatable
        if allocated is not None:
            self.allocated = allocated
        if faulty is not None:
            self.faulty = faulty
        if faultymachines is not None:
            self.faultymachines = faultymachines
        if free is not None:
            self.free = free
        if other is not None:
            self.other = other
        if othermachines is not None:
            self.othermachines = othermachines
        if phoned_home is not None:
            self.phoned_home = phoned_home
        if remainingreservations is not None:
            self.remainingreservations = remainingreservations
        if reservations is not None:
            self.reservations = reservations
        self.size = size
        if total is not None:
            self.total = total
        if unavailable is not None:
            self.unavailable = unavailable
        if usedreservations is not None:
            self.usedreservations = usedreservations
        if waiting is not None:
            self.waiting = waiting

    @property
    def allocatable(self):
        """Gets the allocatable of this V1ServerCapacity.  # noqa: E501

        free machines with this size, size reservations are not considered  # noqa: E501

        :return: The allocatable of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._allocatable

    @allocatable.setter
    def allocatable(self, allocatable):
        """Sets the allocatable of this V1ServerCapacity.

        free machines with this size, size reservations are not considered  # noqa: E501

        :param allocatable: The allocatable of this V1ServerCapacity.  # noqa: E501
        :type: int
        """

        self._allocatable = allocatable

    @property
    def allocated(self):
        """Gets the allocated of this V1ServerCapacity.  # noqa: E501

        allocated machines  # noqa: E501

        :return: The allocated of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._allocated

    @allocated.setter
    def allocated(self, allocated):
        """Sets the allocated of this V1ServerCapacity.

        allocated machines  # noqa: E501

        :param allocated: The allocated of this V1ServerCapacity.  # noqa: E501
        :type: int
        """

        self._allocated = allocated

    @property
    def faulty(self):
        """Gets the faulty of this V1ServerCapacity.  # noqa: E501

        machines with issues with this size  # noqa: E501

        :return: The faulty of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._faulty

    @faulty.setter
    def faulty(self, faulty):
        """Sets the faulty of this V1ServerCapacity.

        machines with issues with this size  # noqa: E501

        :param faulty: The faulty of this V1ServerCapacity.  # noqa: E501
        :type: int
        """

        self._faulty = faulty

    @property
    def faultymachines(self):
        """Gets the faultymachines of this V1ServerCapacity.  # noqa: E501

        machine ids with issues with this size  # noqa: E501

        :return: The faultymachines of this V1ServerCapacity.  # noqa: E501
        :rtype: list[str]
        """
        return self._faultymachines

    @faultymachines.setter
    def faultymachines(self, faultymachines):
        """Sets the faultymachines of this V1ServerCapacity.

        machine ids with issues with this size  # noqa: E501

        :param faultymachines: The faultymachines of this V1ServerCapacity.  # noqa: E501
        :type: list[str]
        """

        self._faultymachines = faultymachines

    @property
    def free(self):
        """Gets the free of this V1ServerCapacity.  # noqa: E501

        free machines with this size (freely allocatable)  # noqa: E501

        :return: The free of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._free

    @free.setter
    def free(self, free):
        """Sets the free of this V1ServerCapacity.

        free machines with this size (freely allocatable)  # noqa: E501

        :param free: The free of this V1ServerCapacity.  # noqa: E501
        :type: int
        """

        self._free = free

    @property
    def other(self):
        """Gets the other of this V1ServerCapacity.  # noqa: E501

        machines neither phoned home nor waiting but in another provisioning state  # noqa: E501

        :return: The other of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._other

    @other.setter
    def other(self, other):
        """Sets the other of this V1ServerCapacity.

        machines neither phoned home nor waiting but in another provisioning state  # noqa: E501

        :param other: The other of this V1ServerCapacity.  # noqa: E501
        :type: int
        """

        self._other = other

    @property
    def othermachines(self):
        """Gets the othermachines of this V1ServerCapacity.  # noqa: E501

        machine ids neither allocated nor waiting with this size  # noqa: E501

        :return: The othermachines of this V1ServerCapacity.  # noqa: E501
        :rtype: list[str]
        """
        return self._othermachines

    @othermachines.setter
    def othermachines(self, othermachines):
        """Sets the othermachines of this V1ServerCapacity.

        machine ids neither allocated nor waiting with this size  # noqa: E501

        :param othermachines: The othermachines of this V1ServerCapacity.  # noqa: E501
        :type: list[str]
        """

        self._othermachines = othermachines

    @property
    def phoned_home(self):
        """Gets the phoned_home of this V1ServerCapacity.  # noqa: E501

        machines in phoned home provisioning state  # noqa: E501

        :return: The phoned_home of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._phoned_home

    @phoned_home.setter
    def phoned_home(self, phoned_home):
        """Sets the phoned_home of this V1ServerCapacity.

        machines in phoned home provisioning state  # noqa: E501

        :param phoned_home: The phoned_home of this V1ServerCapacity.  # noqa: E501
        :type: int
        """

        self._phoned_home = phoned_home

    @property
    def remainingreservations(self):
        """Gets the remainingreservations of this V1ServerCapacity.  # noqa: E501

        the amount of unused / remaining / open reservations for this size  # noqa: E501

        :return: The remainingreservations of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._remainingreservations

    @remainingreservations.setter
    def remainingreservations(self, remainingreservations):
        """Sets the remainingreservations of this V1ServerCapacity.

        the amount of unused / remaining / open reservations for this size  # noqa: E501

        :param remainingreservations: The remainingreservations of this V1ServerCapacity.  # noqa: E501
        :type: int
        """

        self._remainingreservations = remainingreservations

    @property
    def reservations(self):
        """Gets the reservations of this V1ServerCapacity.  # noqa: E501

        the amount of reservations for this size  # noqa: E501

        :return: The reservations of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._reservations

    @reservations.setter
    def reservations(self, reservations):
        """Sets the reservations of this V1ServerCapacity.

        the amount of reservations for this size  # noqa: E501

        :param reservations: The reservations of this V1ServerCapacity.  # noqa: E501
        :type: int
        """

        self._reservations = reservations

    @property
    def size(self):
        """Gets the size of this V1ServerCapacity.  # noqa: E501

        the size of the machine  # noqa: E501

        :return: The size of this V1ServerCapacity.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this V1ServerCapacity.

        the size of the machine  # noqa: E501

        :param size: The size of this V1ServerCapacity.  # noqa: E501
        :type: str
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def total(self):
        """Gets the total of this V1ServerCapacity.  # noqa: E501

        total amount of machines with size  # noqa: E501

        :return: The total of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this V1ServerCapacity.

        total amount of machines with size  # noqa: E501

        :param total: The total of this V1ServerCapacity.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def unavailable(self):
        """Gets the unavailable of this V1ServerCapacity.  # noqa: E501

        unavailable machines with this size  # noqa: E501

        :return: The unavailable of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._unavailable

    @unavailable.setter
    def unavailable(self, unavailable):
        """Sets the unavailable of this V1ServerCapacity.

        unavailable machines with this size  # noqa: E501

        :param unavailable: The unavailable of this V1ServerCapacity.  # noqa: E501
        :type: int
        """

        self._unavailable = unavailable

    @property
    def usedreservations(self):
        """Gets the usedreservations of this V1ServerCapacity.  # noqa: E501

        the amount of used reservations for this size  # noqa: E501

        :return: The usedreservations of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._usedreservations

    @usedreservations.setter
    def usedreservations(self, usedreservations):
        """Sets the usedreservations of this V1ServerCapacity.

        the amount of used reservations for this size  # noqa: E501

        :param usedreservations: The usedreservations of this V1ServerCapacity.  # noqa: E501
        :type: int
        """

        self._usedreservations = usedreservations

    @property
    def waiting(self):
        """Gets the waiting of this V1ServerCapacity.  # noqa: E501

        machines in waiting provisioning state  # noqa: E501

        :return: The waiting of this V1ServerCapacity.  # noqa: E501
        :rtype: int
        """
        return self._waiting

    @waiting.setter
    def waiting(self, waiting):
        """Sets the waiting of this V1ServerCapacity.

        machines in waiting provisioning state  # noqa: E501

        :param waiting: The waiting of this V1ServerCapacity.  # noqa: E501
        :type: int
        """

        self._waiting = waiting

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
        if issubclass(V1ServerCapacity, dict):
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
        if not isinstance(other, V1ServerCapacity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
