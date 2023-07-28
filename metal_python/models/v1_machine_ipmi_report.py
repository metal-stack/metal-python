# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.22.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineIpmiReport(object):
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
        'bios_version': 'str',
        'bmc_ip': 'str',
        'bmc_version': 'str',
        'fru': 'V1MachineFru',
        'indicator_led_state': 'str',
        'power_metric': 'V1PowerMetric',
        'power_state': 'str'
    }

    attribute_map = {
        'bios_version': 'BIOSVersion',
        'bmc_ip': 'BMCIp',
        'bmc_version': 'BMCVersion',
        'fru': 'FRU',
        'indicator_led_state': 'IndicatorLEDState',
        'power_metric': 'PowerMetric',
        'power_state': 'PowerState'
    }

    def __init__(self, bios_version=None, bmc_ip=None, bmc_version=None, fru=None, indicator_led_state=None, power_metric=None, power_state=None):  # noqa: E501
        """V1MachineIpmiReport - a model defined in Swagger"""  # noqa: E501

        self._bios_version = None
        self._bmc_ip = None
        self._bmc_version = None
        self._fru = None
        self._indicator_led_state = None
        self._power_metric = None
        self._power_state = None
        self.discriminator = None

        self.bios_version = bios_version
        self.bmc_ip = bmc_ip
        self.bmc_version = bmc_version
        self.fru = fru
        self.indicator_led_state = indicator_led_state
        self.power_metric = power_metric
        self.power_state = power_state

    @property
    def bios_version(self):
        """Gets the bios_version of this V1MachineIpmiReport.  # noqa: E501


        :return: The bios_version of this V1MachineIpmiReport.  # noqa: E501
        :rtype: str
        """
        return self._bios_version

    @bios_version.setter
    def bios_version(self, bios_version):
        """Sets the bios_version of this V1MachineIpmiReport.


        :param bios_version: The bios_version of this V1MachineIpmiReport.  # noqa: E501
        :type: str
        """
        if bios_version is None:
            raise ValueError("Invalid value for `bios_version`, must not be `None`")  # noqa: E501

        self._bios_version = bios_version

    @property
    def bmc_ip(self):
        """Gets the bmc_ip of this V1MachineIpmiReport.  # noqa: E501


        :return: The bmc_ip of this V1MachineIpmiReport.  # noqa: E501
        :rtype: str
        """
        return self._bmc_ip

    @bmc_ip.setter
    def bmc_ip(self, bmc_ip):
        """Sets the bmc_ip of this V1MachineIpmiReport.


        :param bmc_ip: The bmc_ip of this V1MachineIpmiReport.  # noqa: E501
        :type: str
        """
        if bmc_ip is None:
            raise ValueError("Invalid value for `bmc_ip`, must not be `None`")  # noqa: E501

        self._bmc_ip = bmc_ip

    @property
    def bmc_version(self):
        """Gets the bmc_version of this V1MachineIpmiReport.  # noqa: E501


        :return: The bmc_version of this V1MachineIpmiReport.  # noqa: E501
        :rtype: str
        """
        return self._bmc_version

    @bmc_version.setter
    def bmc_version(self, bmc_version):
        """Sets the bmc_version of this V1MachineIpmiReport.


        :param bmc_version: The bmc_version of this V1MachineIpmiReport.  # noqa: E501
        :type: str
        """
        if bmc_version is None:
            raise ValueError("Invalid value for `bmc_version`, must not be `None`")  # noqa: E501

        self._bmc_version = bmc_version

    @property
    def fru(self):
        """Gets the fru of this V1MachineIpmiReport.  # noqa: E501


        :return: The fru of this V1MachineIpmiReport.  # noqa: E501
        :rtype: V1MachineFru
        """
        return self._fru

    @fru.setter
    def fru(self, fru):
        """Sets the fru of this V1MachineIpmiReport.


        :param fru: The fru of this V1MachineIpmiReport.  # noqa: E501
        :type: V1MachineFru
        """
        if fru is None:
            raise ValueError("Invalid value for `fru`, must not be `None`")  # noqa: E501

        self._fru = fru

    @property
    def indicator_led_state(self):
        """Gets the indicator_led_state of this V1MachineIpmiReport.  # noqa: E501


        :return: The indicator_led_state of this V1MachineIpmiReport.  # noqa: E501
        :rtype: str
        """
        return self._indicator_led_state

    @indicator_led_state.setter
    def indicator_led_state(self, indicator_led_state):
        """Sets the indicator_led_state of this V1MachineIpmiReport.


        :param indicator_led_state: The indicator_led_state of this V1MachineIpmiReport.  # noqa: E501
        :type: str
        """
        if indicator_led_state is None:
            raise ValueError("Invalid value for `indicator_led_state`, must not be `None`")  # noqa: E501

        self._indicator_led_state = indicator_led_state

    @property
    def power_metric(self):
        """Gets the power_metric of this V1MachineIpmiReport.  # noqa: E501


        :return: The power_metric of this V1MachineIpmiReport.  # noqa: E501
        :rtype: V1PowerMetric
        """
        return self._power_metric

    @power_metric.setter
    def power_metric(self, power_metric):
        """Sets the power_metric of this V1MachineIpmiReport.


        :param power_metric: The power_metric of this V1MachineIpmiReport.  # noqa: E501
        :type: V1PowerMetric
        """
        if power_metric is None:
            raise ValueError("Invalid value for `power_metric`, must not be `None`")  # noqa: E501

        self._power_metric = power_metric

    @property
    def power_state(self):
        """Gets the power_state of this V1MachineIpmiReport.  # noqa: E501


        :return: The power_state of this V1MachineIpmiReport.  # noqa: E501
        :rtype: str
        """
        return self._power_state

    @power_state.setter
    def power_state(self, power_state):
        """Sets the power_state of this V1MachineIpmiReport.


        :param power_state: The power_state of this V1MachineIpmiReport.  # noqa: E501
        :type: str
        """
        if power_state is None:
            raise ValueError("Invalid value for `power_state`, must not be `None`")  # noqa: E501

        self._power_state = power_state

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
        if issubclass(V1MachineIpmiReport, dict):
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
        if not isinstance(other, V1MachineIpmiReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
