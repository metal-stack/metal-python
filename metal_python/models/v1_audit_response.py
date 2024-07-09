# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.32.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1AuditResponse(object):
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
        'body': 'str',
        'component': 'str',
        'detail': 'str',
        'error': 'str',
        'forwarded_for': 'str',
        'path': 'str',
        'phase': 'str',
        'remote_addr': 'str',
        'rqid': 'str',
        'status_code': 'int',
        'tenant': 'str',
        'timestamp': 'datetime',
        'type': 'str',
        'user': 'str'
    }

    attribute_map = {
        'body': 'body',
        'component': 'component',
        'detail': 'detail',
        'error': 'error',
        'forwarded_for': 'forwarded_for',
        'path': 'path',
        'phase': 'phase',
        'remote_addr': 'remote_addr',
        'rqid': 'rqid',
        'status_code': 'status_code',
        'tenant': 'tenant',
        'timestamp': 'timestamp',
        'type': 'type',
        'user': 'user'
    }

    def __init__(self, body=None, component=None, detail=None, error=None, forwarded_for=None, path=None, phase=None, remote_addr=None, rqid=None, status_code=None, tenant=None, timestamp=None, type=None, user=None):  # noqa: E501
        """V1AuditResponse - a model defined in Swagger"""  # noqa: E501

        self._body = None
        self._component = None
        self._detail = None
        self._error = None
        self._forwarded_for = None
        self._path = None
        self._phase = None
        self._remote_addr = None
        self._rqid = None
        self._status_code = None
        self._tenant = None
        self._timestamp = None
        self._type = None
        self._user = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if component is not None:
            self.component = component
        if detail is not None:
            self.detail = detail
        if error is not None:
            self.error = error
        if forwarded_for is not None:
            self.forwarded_for = forwarded_for
        if path is not None:
            self.path = path
        if phase is not None:
            self.phase = phase
        if remote_addr is not None:
            self.remote_addr = remote_addr
        if rqid is not None:
            self.rqid = rqid
        if status_code is not None:
            self.status_code = status_code
        if tenant is not None:
            self.tenant = tenant
        if timestamp is not None:
            self.timestamp = timestamp
        if type is not None:
            self.type = type
        if user is not None:
            self.user = user

    @property
    def body(self):
        """Gets the body of this V1AuditResponse.  # noqa: E501


        :return: The body of this V1AuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this V1AuditResponse.


        :param body: The body of this V1AuditResponse.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def component(self):
        """Gets the component of this V1AuditResponse.  # noqa: E501


        :return: The component of this V1AuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this V1AuditResponse.


        :param component: The component of this V1AuditResponse.  # noqa: E501
        :type: str
        """

        self._component = component

    @property
    def detail(self):
        """Gets the detail of this V1AuditResponse.  # noqa: E501


        :return: The detail of this V1AuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this V1AuditResponse.


        :param detail: The detail of this V1AuditResponse.  # noqa: E501
        :type: str
        """

        self._detail = detail

    @property
    def error(self):
        """Gets the error of this V1AuditResponse.  # noqa: E501


        :return: The error of this V1AuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this V1AuditResponse.


        :param error: The error of this V1AuditResponse.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def forwarded_for(self):
        """Gets the forwarded_for of this V1AuditResponse.  # noqa: E501


        :return: The forwarded_for of this V1AuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._forwarded_for

    @forwarded_for.setter
    def forwarded_for(self, forwarded_for):
        """Sets the forwarded_for of this V1AuditResponse.


        :param forwarded_for: The forwarded_for of this V1AuditResponse.  # noqa: E501
        :type: str
        """

        self._forwarded_for = forwarded_for

    @property
    def path(self):
        """Gets the path of this V1AuditResponse.  # noqa: E501


        :return: The path of this V1AuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1AuditResponse.


        :param path: The path of this V1AuditResponse.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def phase(self):
        """Gets the phase of this V1AuditResponse.  # noqa: E501


        :return: The phase of this V1AuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this V1AuditResponse.


        :param phase: The phase of this V1AuditResponse.  # noqa: E501
        :type: str
        """

        self._phase = phase

    @property
    def remote_addr(self):
        """Gets the remote_addr of this V1AuditResponse.  # noqa: E501


        :return: The remote_addr of this V1AuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._remote_addr

    @remote_addr.setter
    def remote_addr(self, remote_addr):
        """Sets the remote_addr of this V1AuditResponse.


        :param remote_addr: The remote_addr of this V1AuditResponse.  # noqa: E501
        :type: str
        """

        self._remote_addr = remote_addr

    @property
    def rqid(self):
        """Gets the rqid of this V1AuditResponse.  # noqa: E501


        :return: The rqid of this V1AuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._rqid

    @rqid.setter
    def rqid(self, rqid):
        """Sets the rqid of this V1AuditResponse.


        :param rqid: The rqid of this V1AuditResponse.  # noqa: E501
        :type: str
        """

        self._rqid = rqid

    @property
    def status_code(self):
        """Gets the status_code of this V1AuditResponse.  # noqa: E501


        :return: The status_code of this V1AuditResponse.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this V1AuditResponse.


        :param status_code: The status_code of this V1AuditResponse.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def tenant(self):
        """Gets the tenant of this V1AuditResponse.  # noqa: E501


        :return: The tenant of this V1AuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this V1AuditResponse.


        :param tenant: The tenant of this V1AuditResponse.  # noqa: E501
        :type: str
        """

        self._tenant = tenant

    @property
    def timestamp(self):
        """Gets the timestamp of this V1AuditResponse.  # noqa: E501


        :return: The timestamp of this V1AuditResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this V1AuditResponse.


        :param timestamp: The timestamp of this V1AuditResponse.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def type(self):
        """Gets the type of this V1AuditResponse.  # noqa: E501


        :return: The type of this V1AuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1AuditResponse.


        :param type: The type of this V1AuditResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def user(self):
        """Gets the user of this V1AuditResponse.  # noqa: E501


        :return: The user of this V1AuditResponse.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this V1AuditResponse.


        :param user: The user of this V1AuditResponse.  # noqa: E501
        :type: str
        """

        self._user = user

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
        if issubclass(V1AuditResponse, dict):
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
        if not isinstance(other, V1AuditResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
