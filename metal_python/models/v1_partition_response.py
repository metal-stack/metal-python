# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.37.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1PartitionResponse(object):
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
        'bootconfig': 'V1PartitionBootConfiguration',
        'changed': 'datetime',
        'created': 'datetime',
        'description': 'str',
        'id': 'str',
        'labels': 'dict(str, str)',
        'mgmtserviceaddress': 'str',
        'name': 'str',
        'privatenetworkprefixlength': 'int'
    }

    attribute_map = {
        'bootconfig': 'bootconfig',
        'changed': 'changed',
        'created': 'created',
        'description': 'description',
        'id': 'id',
        'labels': 'labels',
        'mgmtserviceaddress': 'mgmtserviceaddress',
        'name': 'name',
        'privatenetworkprefixlength': 'privatenetworkprefixlength'
    }

    def __init__(self, bootconfig=None, changed=None, created=None, description=None, id=None, labels=None, mgmtserviceaddress=None, name=None, privatenetworkprefixlength=None):  # noqa: E501
        """V1PartitionResponse - a model defined in Swagger"""  # noqa: E501

        self._bootconfig = None
        self._changed = None
        self._created = None
        self._description = None
        self._id = None
        self._labels = None
        self._mgmtserviceaddress = None
        self._name = None
        self._privatenetworkprefixlength = None
        self.discriminator = None

        self.bootconfig = bootconfig
        if changed is not None:
            self.changed = changed
        if created is not None:
            self.created = created
        if description is not None:
            self.description = description
        self.id = id
        if labels is not None:
            self.labels = labels
        if mgmtserviceaddress is not None:
            self.mgmtserviceaddress = mgmtserviceaddress
        if name is not None:
            self.name = name
        if privatenetworkprefixlength is not None:
            self.privatenetworkprefixlength = privatenetworkprefixlength

    @property
    def bootconfig(self):
        """Gets the bootconfig of this V1PartitionResponse.  # noqa: E501

        the boot configuration of this partition  # noqa: E501

        :return: The bootconfig of this V1PartitionResponse.  # noqa: E501
        :rtype: V1PartitionBootConfiguration
        """
        return self._bootconfig

    @bootconfig.setter
    def bootconfig(self, bootconfig):
        """Sets the bootconfig of this V1PartitionResponse.

        the boot configuration of this partition  # noqa: E501

        :param bootconfig: The bootconfig of this V1PartitionResponse.  # noqa: E501
        :type: V1PartitionBootConfiguration
        """
        if bootconfig is None:
            raise ValueError("Invalid value for `bootconfig`, must not be `None`")  # noqa: E501

        self._bootconfig = bootconfig

    @property
    def changed(self):
        """Gets the changed of this V1PartitionResponse.  # noqa: E501

        the last changed timestamp of this entity  # noqa: E501

        :return: The changed of this V1PartitionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._changed

    @changed.setter
    def changed(self, changed):
        """Sets the changed of this V1PartitionResponse.

        the last changed timestamp of this entity  # noqa: E501

        :param changed: The changed of this V1PartitionResponse.  # noqa: E501
        :type: datetime
        """

        self._changed = changed

    @property
    def created(self):
        """Gets the created of this V1PartitionResponse.  # noqa: E501

        the creation time of this entity  # noqa: E501

        :return: The created of this V1PartitionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this V1PartitionResponse.

        the creation time of this entity  # noqa: E501

        :param created: The created of this V1PartitionResponse.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def description(self):
        """Gets the description of this V1PartitionResponse.  # noqa: E501

        a description for this entity  # noqa: E501

        :return: The description of this V1PartitionResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1PartitionResponse.

        a description for this entity  # noqa: E501

        :param description: The description of this V1PartitionResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this V1PartitionResponse.  # noqa: E501

        the unique ID of this entity  # noqa: E501

        :return: The id of this V1PartitionResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1PartitionResponse.

        the unique ID of this entity  # noqa: E501

        :param id: The id of this V1PartitionResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this V1PartitionResponse.  # noqa: E501

        free labels that you associate with this partition  # noqa: E501

        :return: The labels of this V1PartitionResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this V1PartitionResponse.

        free labels that you associate with this partition  # noqa: E501

        :param labels: The labels of this V1PartitionResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def mgmtserviceaddress(self):
        """Gets the mgmtserviceaddress of this V1PartitionResponse.  # noqa: E501

        the address to the management service of this partition  # noqa: E501

        :return: The mgmtserviceaddress of this V1PartitionResponse.  # noqa: E501
        :rtype: str
        """
        return self._mgmtserviceaddress

    @mgmtserviceaddress.setter
    def mgmtserviceaddress(self, mgmtserviceaddress):
        """Sets the mgmtserviceaddress of this V1PartitionResponse.

        the address to the management service of this partition  # noqa: E501

        :param mgmtserviceaddress: The mgmtserviceaddress of this V1PartitionResponse.  # noqa: E501
        :type: str
        """

        self._mgmtserviceaddress = mgmtserviceaddress

    @property
    def name(self):
        """Gets the name of this V1PartitionResponse.  # noqa: E501

        a readable name for this entity  # noqa: E501

        :return: The name of this V1PartitionResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1PartitionResponse.

        a readable name for this entity  # noqa: E501

        :param name: The name of this V1PartitionResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def privatenetworkprefixlength(self):
        """Gets the privatenetworkprefixlength of this V1PartitionResponse.  # noqa: E501

        the length of private networks for the machine's child networks in this partition, default 22  # noqa: E501

        :return: The privatenetworkprefixlength of this V1PartitionResponse.  # noqa: E501
        :rtype: int
        """
        return self._privatenetworkprefixlength

    @privatenetworkprefixlength.setter
    def privatenetworkprefixlength(self, privatenetworkprefixlength):
        """Sets the privatenetworkprefixlength of this V1PartitionResponse.

        the length of private networks for the machine's child networks in this partition, default 22  # noqa: E501

        :param privatenetworkprefixlength: The privatenetworkprefixlength of this V1PartitionResponse.  # noqa: E501
        :type: int
        """
        if privatenetworkprefixlength is not None and privatenetworkprefixlength > 30:  # noqa: E501
            raise ValueError("Invalid value for `privatenetworkprefixlength`, must be a value less than or equal to `30`")  # noqa: E501
        if privatenetworkprefixlength is not None and privatenetworkprefixlength < 16:  # noqa: E501
            raise ValueError("Invalid value for `privatenetworkprefixlength`, must be a value greater than or equal to `16`")  # noqa: E501

        self._privatenetworkprefixlength = privatenetworkprefixlength

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
        if issubclass(V1PartitionResponse, dict):
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
        if not isinstance(other, V1PartitionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
