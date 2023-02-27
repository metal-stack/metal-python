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


class V1SwitchBase(object):
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
        'console_command': 'str',
        'management_ip': 'str',
        'management_user': 'str',
        'mode': 'str',
        'os': 'V1SwitchOS',
        'rack_id': 'str'
    }

    attribute_map = {
        'console_command': 'console_command',
        'management_ip': 'management_ip',
        'management_user': 'management_user',
        'mode': 'mode',
        'os': 'os',
        'rack_id': 'rack_id'
    }

    def __init__(self, console_command=None, management_ip=None, management_user=None, mode=None, os=None, rack_id=None):  # noqa: E501
        """V1SwitchBase - a model defined in Swagger"""  # noqa: E501

        self._console_command = None
        self._management_ip = None
        self._management_user = None
        self._mode = None
        self._os = None
        self._rack_id = None
        self.discriminator = None

        if console_command is not None:
            self.console_command = console_command
        if management_ip is not None:
            self.management_ip = management_ip
        if management_user is not None:
            self.management_user = management_user
        if mode is not None:
            self.mode = mode
        if os is not None:
            self.os = os
        self.rack_id = rack_id

    @property
    def console_command(self):
        """Gets the console_command of this V1SwitchBase.  # noqa: E501

        command to access the console of the switch  # noqa: E501

        :return: The console_command of this V1SwitchBase.  # noqa: E501
        :rtype: str
        """
        return self._console_command

    @console_command.setter
    def console_command(self, console_command):
        """Sets the console_command of this V1SwitchBase.

        command to access the console of the switch  # noqa: E501

        :param console_command: The console_command of this V1SwitchBase.  # noqa: E501
        :type: str
        """

        self._console_command = console_command

    @property
    def management_ip(self):
        """Gets the management_ip of this V1SwitchBase.  # noqa: E501

        the ip address of the management interface of the switch  # noqa: E501

        :return: The management_ip of this V1SwitchBase.  # noqa: E501
        :rtype: str
        """
        return self._management_ip

    @management_ip.setter
    def management_ip(self, management_ip):
        """Sets the management_ip of this V1SwitchBase.

        the ip address of the management interface of the switch  # noqa: E501

        :param management_ip: The management_ip of this V1SwitchBase.  # noqa: E501
        :type: str
        """

        self._management_ip = management_ip

    @property
    def management_user(self):
        """Gets the management_user of this V1SwitchBase.  # noqa: E501

        the user to connect to the switch  # noqa: E501

        :return: The management_user of this V1SwitchBase.  # noqa: E501
        :rtype: str
        """
        return self._management_user

    @management_user.setter
    def management_user(self, management_user):
        """Sets the management_user of this V1SwitchBase.

        the user to connect to the switch  # noqa: E501

        :param management_user: The management_user of this V1SwitchBase.  # noqa: E501
        :type: str
        """

        self._management_user = management_user

    @property
    def mode(self):
        """Gets the mode of this V1SwitchBase.  # noqa: E501

        the mode the switch currently has  # noqa: E501

        :return: The mode of this V1SwitchBase.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this V1SwitchBase.

        the mode the switch currently has  # noqa: E501

        :param mode: The mode of this V1SwitchBase.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def os(self):
        """Gets the os of this V1SwitchBase.  # noqa: E501

        the operating system the switch currently has  # noqa: E501

        :return: The os of this V1SwitchBase.  # noqa: E501
        :rtype: V1SwitchOS
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this V1SwitchBase.

        the operating system the switch currently has  # noqa: E501

        :param os: The os of this V1SwitchBase.  # noqa: E501
        :type: V1SwitchOS
        """

        self._os = os

    @property
    def rack_id(self):
        """Gets the rack_id of this V1SwitchBase.  # noqa: E501

        the id of the rack in which this switch is located  # noqa: E501

        :return: The rack_id of this V1SwitchBase.  # noqa: E501
        :rtype: str
        """
        return self._rack_id

    @rack_id.setter
    def rack_id(self, rack_id):
        """Sets the rack_id of this V1SwitchBase.

        the id of the rack in which this switch is located  # noqa: E501

        :param rack_id: The rack_id of this V1SwitchBase.  # noqa: E501
        :type: str
        """
        if rack_id is None:
            raise ValueError("Invalid value for `rack_id`, must not be `None`")  # noqa: E501

        self._rack_id = rack_id

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
        if issubclass(V1SwitchBase, dict):
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
        if not isinstance(other, V1SwitchBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
