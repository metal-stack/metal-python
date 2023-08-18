# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.22.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1QuotaSet(object):
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
        'cluster': 'V1Quota',
        'ip': 'V1Quota',
        'machine': 'V1Quota',
        'project': 'V1Quota'
    }

    attribute_map = {
        'cluster': 'cluster',
        'ip': 'ip',
        'machine': 'machine',
        'project': 'project'
    }

    def __init__(self, cluster=None, ip=None, machine=None, project=None):  # noqa: E501
        """V1QuotaSet - a model defined in Swagger"""  # noqa: E501

        self._cluster = None
        self._ip = None
        self._machine = None
        self._project = None
        self.discriminator = None

        if cluster is not None:
            self.cluster = cluster
        if ip is not None:
            self.ip = ip
        if machine is not None:
            self.machine = machine
        if project is not None:
            self.project = project

    @property
    def cluster(self):
        """Gets the cluster of this V1QuotaSet.  # noqa: E501


        :return: The cluster of this V1QuotaSet.  # noqa: E501
        :rtype: V1Quota
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this V1QuotaSet.


        :param cluster: The cluster of this V1QuotaSet.  # noqa: E501
        :type: V1Quota
        """

        self._cluster = cluster

    @property
    def ip(self):
        """Gets the ip of this V1QuotaSet.  # noqa: E501


        :return: The ip of this V1QuotaSet.  # noqa: E501
        :rtype: V1Quota
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this V1QuotaSet.


        :param ip: The ip of this V1QuotaSet.  # noqa: E501
        :type: V1Quota
        """

        self._ip = ip

    @property
    def machine(self):
        """Gets the machine of this V1QuotaSet.  # noqa: E501


        :return: The machine of this V1QuotaSet.  # noqa: E501
        :rtype: V1Quota
        """
        return self._machine

    @machine.setter
    def machine(self, machine):
        """Sets the machine of this V1QuotaSet.


        :param machine: The machine of this V1QuotaSet.  # noqa: E501
        :type: V1Quota
        """

        self._machine = machine

    @property
    def project(self):
        """Gets the project of this V1QuotaSet.  # noqa: E501


        :return: The project of this V1QuotaSet.  # noqa: E501
        :rtype: V1Quota
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this V1QuotaSet.


        :param project: The project of this V1QuotaSet.  # noqa: E501
        :type: V1Quota
        """

        self._project = project

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
        if issubclass(V1QuotaSet, dict):
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
        if not isinstance(other, V1QuotaSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
