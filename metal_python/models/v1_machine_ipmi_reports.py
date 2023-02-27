# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.22.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1MachineIpmiReports(object):
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
        'partitionid': 'str',
        'reports': 'dict(str, V1MachineIpmiReport)'
    }

    attribute_map = {
        'partitionid': 'partitionid',
        'reports': 'reports'
    }

    def __init__(self, partitionid=None, reports=None):  # noqa: E501
        """V1MachineIpmiReports - a model defined in Swagger"""  # noqa: E501

        self._partitionid = None
        self._reports = None
        self.discriminator = None

        if partitionid is not None:
            self.partitionid = partitionid
        if reports is not None:
            self.reports = reports

    @property
    def partitionid(self):
        """Gets the partitionid of this V1MachineIpmiReports.  # noqa: E501

        the partition id for the ipmi report  # noqa: E501

        :return: The partitionid of this V1MachineIpmiReports.  # noqa: E501
        :rtype: str
        """
        return self._partitionid

    @partitionid.setter
    def partitionid(self, partitionid):
        """Sets the partitionid of this V1MachineIpmiReports.

        the partition id for the ipmi report  # noqa: E501

        :param partitionid: The partitionid of this V1MachineIpmiReports.  # noqa: E501
        :type: str
        """

        self._partitionid = partitionid

    @property
    def reports(self):
        """Gets the reports of this V1MachineIpmiReports.  # noqa: E501

        uuid to machinereport  # noqa: E501

        :return: The reports of this V1MachineIpmiReports.  # noqa: E501
        :rtype: dict(str, V1MachineIpmiReport)
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """Sets the reports of this V1MachineIpmiReports.

        uuid to machinereport  # noqa: E501

        :param reports: The reports of this V1MachineIpmiReports.  # noqa: E501
        :type: dict(str, V1MachineIpmiReport)
        """

        self._reports = reports

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
        if issubclass(V1MachineIpmiReports, dict):
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
        if not isinstance(other, V1MachineIpmiReports):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
