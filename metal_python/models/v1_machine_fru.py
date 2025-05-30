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


class V1MachineFru(object):
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
        'board_mfg': 'str',
        'board_mfg_serial': 'str',
        'board_part_number': 'str',
        'chassis_part_number': 'str',
        'chassis_part_serial': 'str',
        'product_manufacturer': 'str',
        'product_part_number': 'str',
        'product_serial': 'str'
    }

    attribute_map = {
        'board_mfg': 'board_mfg',
        'board_mfg_serial': 'board_mfg_serial',
        'board_part_number': 'board_part_number',
        'chassis_part_number': 'chassis_part_number',
        'chassis_part_serial': 'chassis_part_serial',
        'product_manufacturer': 'product_manufacturer',
        'product_part_number': 'product_part_number',
        'product_serial': 'product_serial'
    }

    def __init__(self, board_mfg=None, board_mfg_serial=None, board_part_number=None, chassis_part_number=None, chassis_part_serial=None, product_manufacturer=None, product_part_number=None, product_serial=None):  # noqa: E501
        """V1MachineFru - a model defined in Swagger"""  # noqa: E501

        self._board_mfg = None
        self._board_mfg_serial = None
        self._board_part_number = None
        self._chassis_part_number = None
        self._chassis_part_serial = None
        self._product_manufacturer = None
        self._product_part_number = None
        self._product_serial = None
        self.discriminator = None

        if board_mfg is not None:
            self.board_mfg = board_mfg
        if board_mfg_serial is not None:
            self.board_mfg_serial = board_mfg_serial
        if board_part_number is not None:
            self.board_part_number = board_part_number
        if chassis_part_number is not None:
            self.chassis_part_number = chassis_part_number
        if chassis_part_serial is not None:
            self.chassis_part_serial = chassis_part_serial
        if product_manufacturer is not None:
            self.product_manufacturer = product_manufacturer
        if product_part_number is not None:
            self.product_part_number = product_part_number
        if product_serial is not None:
            self.product_serial = product_serial

    @property
    def board_mfg(self):
        """Gets the board_mfg of this V1MachineFru.  # noqa: E501

        the board mfg  # noqa: E501

        :return: The board_mfg of this V1MachineFru.  # noqa: E501
        :rtype: str
        """
        return self._board_mfg

    @board_mfg.setter
    def board_mfg(self, board_mfg):
        """Sets the board_mfg of this V1MachineFru.

        the board mfg  # noqa: E501

        :param board_mfg: The board_mfg of this V1MachineFru.  # noqa: E501
        :type: str
        """

        self._board_mfg = board_mfg

    @property
    def board_mfg_serial(self):
        """Gets the board_mfg_serial of this V1MachineFru.  # noqa: E501

        the board mfg serial  # noqa: E501

        :return: The board_mfg_serial of this V1MachineFru.  # noqa: E501
        :rtype: str
        """
        return self._board_mfg_serial

    @board_mfg_serial.setter
    def board_mfg_serial(self, board_mfg_serial):
        """Sets the board_mfg_serial of this V1MachineFru.

        the board mfg serial  # noqa: E501

        :param board_mfg_serial: The board_mfg_serial of this V1MachineFru.  # noqa: E501
        :type: str
        """

        self._board_mfg_serial = board_mfg_serial

    @property
    def board_part_number(self):
        """Gets the board_part_number of this V1MachineFru.  # noqa: E501

        the board part number  # noqa: E501

        :return: The board_part_number of this V1MachineFru.  # noqa: E501
        :rtype: str
        """
        return self._board_part_number

    @board_part_number.setter
    def board_part_number(self, board_part_number):
        """Sets the board_part_number of this V1MachineFru.

        the board part number  # noqa: E501

        :param board_part_number: The board_part_number of this V1MachineFru.  # noqa: E501
        :type: str
        """

        self._board_part_number = board_part_number

    @property
    def chassis_part_number(self):
        """Gets the chassis_part_number of this V1MachineFru.  # noqa: E501

        the chassis part number  # noqa: E501

        :return: The chassis_part_number of this V1MachineFru.  # noqa: E501
        :rtype: str
        """
        return self._chassis_part_number

    @chassis_part_number.setter
    def chassis_part_number(self, chassis_part_number):
        """Sets the chassis_part_number of this V1MachineFru.

        the chassis part number  # noqa: E501

        :param chassis_part_number: The chassis_part_number of this V1MachineFru.  # noqa: E501
        :type: str
        """

        self._chassis_part_number = chassis_part_number

    @property
    def chassis_part_serial(self):
        """Gets the chassis_part_serial of this V1MachineFru.  # noqa: E501

        the chassis part serial  # noqa: E501

        :return: The chassis_part_serial of this V1MachineFru.  # noqa: E501
        :rtype: str
        """
        return self._chassis_part_serial

    @chassis_part_serial.setter
    def chassis_part_serial(self, chassis_part_serial):
        """Sets the chassis_part_serial of this V1MachineFru.

        the chassis part serial  # noqa: E501

        :param chassis_part_serial: The chassis_part_serial of this V1MachineFru.  # noqa: E501
        :type: str
        """

        self._chassis_part_serial = chassis_part_serial

    @property
    def product_manufacturer(self):
        """Gets the product_manufacturer of this V1MachineFru.  # noqa: E501

        the product manufacturer  # noqa: E501

        :return: The product_manufacturer of this V1MachineFru.  # noqa: E501
        :rtype: str
        """
        return self._product_manufacturer

    @product_manufacturer.setter
    def product_manufacturer(self, product_manufacturer):
        """Sets the product_manufacturer of this V1MachineFru.

        the product manufacturer  # noqa: E501

        :param product_manufacturer: The product_manufacturer of this V1MachineFru.  # noqa: E501
        :type: str
        """

        self._product_manufacturer = product_manufacturer

    @property
    def product_part_number(self):
        """Gets the product_part_number of this V1MachineFru.  # noqa: E501

        the product part number  # noqa: E501

        :return: The product_part_number of this V1MachineFru.  # noqa: E501
        :rtype: str
        """
        return self._product_part_number

    @product_part_number.setter
    def product_part_number(self, product_part_number):
        """Sets the product_part_number of this V1MachineFru.

        the product part number  # noqa: E501

        :param product_part_number: The product_part_number of this V1MachineFru.  # noqa: E501
        :type: str
        """

        self._product_part_number = product_part_number

    @property
    def product_serial(self):
        """Gets the product_serial of this V1MachineFru.  # noqa: E501

        the product serial  # noqa: E501

        :return: The product_serial of this V1MachineFru.  # noqa: E501
        :rtype: str
        """
        return self._product_serial

    @product_serial.setter
    def product_serial(self, product_serial):
        """Sets the product_serial of this V1MachineFru.

        the product serial  # noqa: E501

        :param product_serial: The product_serial of this V1MachineFru.  # noqa: E501
        :type: str
        """

        self._product_serial = product_serial

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
        if issubclass(V1MachineFru, dict):
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
        if not isinstance(other, V1MachineFru):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
