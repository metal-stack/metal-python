# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.27.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DatastoreMachineSearchQuery(object):
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
        'allocation_hostname': 'str',
        'allocation_image_id': 'str',
        'allocation_name': 'str',
        'allocation_project': 'str',
        'allocation_role': 'str',
        'allocation_succeeded': 'bool',
        'disk_names': 'list[str]',
        'disk_sizes': 'list[int]',
        'fru_board_mfg': 'str',
        'fru_board_mfg_serial': 'str',
        'fru_board_part_number': 'str',
        'fru_chassis_part_number': 'str',
        'fru_chassis_part_serial': 'str',
        'fru_product_manufacturer': 'str',
        'fru_product_part_number': 'str',
        'fru_product_serial': 'str',
        'hardware_cpu_cores': 'int',
        'hardware_memory': 'int',
        'id': 'str',
        'ipmi_address': 'str',
        'ipmi_interface': 'str',
        'ipmi_mac_address': 'str',
        'ipmi_user': 'str',
        'name': 'str',
        'network_asns': 'list[int]',
        'network_destination_prefixes': 'list[str]',
        'network_ids': 'list[str]',
        'network_ips': 'list[str]',
        'network_prefixes': 'list[str]',
        'network_vrfs': 'list[int]',
        'nics_mac_addresses': 'list[str]',
        'nics_names': 'list[str]',
        'nics_neighbor_mac_addresses': 'list[str]',
        'nics_neighbor_names': 'list[str]',
        'nics_neighbor_vrfs': 'list[str]',
        'nics_vrfs': 'list[str]',
        'partition_id': 'str',
        'rackid': 'str',
        'sizeid': 'str',
        'state_value': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'allocation_hostname': 'allocation_hostname',
        'allocation_image_id': 'allocation_image_id',
        'allocation_name': 'allocation_name',
        'allocation_project': 'allocation_project',
        'allocation_role': 'allocation_role',
        'allocation_succeeded': 'allocation_succeeded',
        'disk_names': 'disk_names',
        'disk_sizes': 'disk_sizes',
        'fru_board_mfg': 'fru_board_mfg',
        'fru_board_mfg_serial': 'fru_board_mfg_serial',
        'fru_board_part_number': 'fru_board_part_number',
        'fru_chassis_part_number': 'fru_chassis_part_number',
        'fru_chassis_part_serial': 'fru_chassis_part_serial',
        'fru_product_manufacturer': 'fru_product_manufacturer',
        'fru_product_part_number': 'fru_product_part_number',
        'fru_product_serial': 'fru_product_serial',
        'hardware_cpu_cores': 'hardware_cpu_cores',
        'hardware_memory': 'hardware_memory',
        'id': 'id',
        'ipmi_address': 'ipmi_address',
        'ipmi_interface': 'ipmi_interface',
        'ipmi_mac_address': 'ipmi_mac_address',
        'ipmi_user': 'ipmi_user',
        'name': 'name',
        'network_asns': 'network_asns',
        'network_destination_prefixes': 'network_destination_prefixes',
        'network_ids': 'network_ids',
        'network_ips': 'network_ips',
        'network_prefixes': 'network_prefixes',
        'network_vrfs': 'network_vrfs',
        'nics_mac_addresses': 'nics_mac_addresses',
        'nics_names': 'nics_names',
        'nics_neighbor_mac_addresses': 'nics_neighbor_mac_addresses',
        'nics_neighbor_names': 'nics_neighbor_names',
        'nics_neighbor_vrfs': 'nics_neighbor_vrfs',
        'nics_vrfs': 'nics_vrfs',
        'partition_id': 'partition_id',
        'rackid': 'rackid',
        'sizeid': 'sizeid',
        'state_value': 'state_value',
        'tags': 'tags'
    }

    def __init__(self, allocation_hostname=None, allocation_image_id=None, allocation_name=None, allocation_project=None, allocation_role=None, allocation_succeeded=None, disk_names=None, disk_sizes=None, fru_board_mfg=None, fru_board_mfg_serial=None, fru_board_part_number=None, fru_chassis_part_number=None, fru_chassis_part_serial=None, fru_product_manufacturer=None, fru_product_part_number=None, fru_product_serial=None, hardware_cpu_cores=None, hardware_memory=None, id=None, ipmi_address=None, ipmi_interface=None, ipmi_mac_address=None, ipmi_user=None, name=None, network_asns=None, network_destination_prefixes=None, network_ids=None, network_ips=None, network_prefixes=None, network_vrfs=None, nics_mac_addresses=None, nics_names=None, nics_neighbor_mac_addresses=None, nics_neighbor_names=None, nics_neighbor_vrfs=None, nics_vrfs=None, partition_id=None, rackid=None, sizeid=None, state_value=None, tags=None):  # noqa: E501
        """DatastoreMachineSearchQuery - a model defined in Swagger"""  # noqa: E501

        self._allocation_hostname = None
        self._allocation_image_id = None
        self._allocation_name = None
        self._allocation_project = None
        self._allocation_role = None
        self._allocation_succeeded = None
        self._disk_names = None
        self._disk_sizes = None
        self._fru_board_mfg = None
        self._fru_board_mfg_serial = None
        self._fru_board_part_number = None
        self._fru_chassis_part_number = None
        self._fru_chassis_part_serial = None
        self._fru_product_manufacturer = None
        self._fru_product_part_number = None
        self._fru_product_serial = None
        self._hardware_cpu_cores = None
        self._hardware_memory = None
        self._id = None
        self._ipmi_address = None
        self._ipmi_interface = None
        self._ipmi_mac_address = None
        self._ipmi_user = None
        self._name = None
        self._network_asns = None
        self._network_destination_prefixes = None
        self._network_ids = None
        self._network_ips = None
        self._network_prefixes = None
        self._network_vrfs = None
        self._nics_mac_addresses = None
        self._nics_names = None
        self._nics_neighbor_mac_addresses = None
        self._nics_neighbor_names = None
        self._nics_neighbor_vrfs = None
        self._nics_vrfs = None
        self._partition_id = None
        self._rackid = None
        self._sizeid = None
        self._state_value = None
        self._tags = None
        self.discriminator = None

        if allocation_hostname is not None:
            self.allocation_hostname = allocation_hostname
        if allocation_image_id is not None:
            self.allocation_image_id = allocation_image_id
        if allocation_name is not None:
            self.allocation_name = allocation_name
        if allocation_project is not None:
            self.allocation_project = allocation_project
        if allocation_role is not None:
            self.allocation_role = allocation_role
        if allocation_succeeded is not None:
            self.allocation_succeeded = allocation_succeeded
        if disk_names is not None:
            self.disk_names = disk_names
        if disk_sizes is not None:
            self.disk_sizes = disk_sizes
        if fru_board_mfg is not None:
            self.fru_board_mfg = fru_board_mfg
        if fru_board_mfg_serial is not None:
            self.fru_board_mfg_serial = fru_board_mfg_serial
        if fru_board_part_number is not None:
            self.fru_board_part_number = fru_board_part_number
        if fru_chassis_part_number is not None:
            self.fru_chassis_part_number = fru_chassis_part_number
        if fru_chassis_part_serial is not None:
            self.fru_chassis_part_serial = fru_chassis_part_serial
        if fru_product_manufacturer is not None:
            self.fru_product_manufacturer = fru_product_manufacturer
        if fru_product_part_number is not None:
            self.fru_product_part_number = fru_product_part_number
        if fru_product_serial is not None:
            self.fru_product_serial = fru_product_serial
        if hardware_cpu_cores is not None:
            self.hardware_cpu_cores = hardware_cpu_cores
        if hardware_memory is not None:
            self.hardware_memory = hardware_memory
        if id is not None:
            self.id = id
        if ipmi_address is not None:
            self.ipmi_address = ipmi_address
        if ipmi_interface is not None:
            self.ipmi_interface = ipmi_interface
        if ipmi_mac_address is not None:
            self.ipmi_mac_address = ipmi_mac_address
        if ipmi_user is not None:
            self.ipmi_user = ipmi_user
        if name is not None:
            self.name = name
        if network_asns is not None:
            self.network_asns = network_asns
        if network_destination_prefixes is not None:
            self.network_destination_prefixes = network_destination_prefixes
        if network_ids is not None:
            self.network_ids = network_ids
        if network_ips is not None:
            self.network_ips = network_ips
        if network_prefixes is not None:
            self.network_prefixes = network_prefixes
        if network_vrfs is not None:
            self.network_vrfs = network_vrfs
        if nics_mac_addresses is not None:
            self.nics_mac_addresses = nics_mac_addresses
        if nics_names is not None:
            self.nics_names = nics_names
        if nics_neighbor_mac_addresses is not None:
            self.nics_neighbor_mac_addresses = nics_neighbor_mac_addresses
        if nics_neighbor_names is not None:
            self.nics_neighbor_names = nics_neighbor_names
        if nics_neighbor_vrfs is not None:
            self.nics_neighbor_vrfs = nics_neighbor_vrfs
        if nics_vrfs is not None:
            self.nics_vrfs = nics_vrfs
        if partition_id is not None:
            self.partition_id = partition_id
        if rackid is not None:
            self.rackid = rackid
        if sizeid is not None:
            self.sizeid = sizeid
        if state_value is not None:
            self.state_value = state_value
        if tags is not None:
            self.tags = tags

    @property
    def allocation_hostname(self):
        """Gets the allocation_hostname of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The allocation_hostname of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._allocation_hostname

    @allocation_hostname.setter
    def allocation_hostname(self, allocation_hostname):
        """Sets the allocation_hostname of this DatastoreMachineSearchQuery.


        :param allocation_hostname: The allocation_hostname of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._allocation_hostname = allocation_hostname

    @property
    def allocation_image_id(self):
        """Gets the allocation_image_id of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The allocation_image_id of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._allocation_image_id

    @allocation_image_id.setter
    def allocation_image_id(self, allocation_image_id):
        """Sets the allocation_image_id of this DatastoreMachineSearchQuery.


        :param allocation_image_id: The allocation_image_id of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._allocation_image_id = allocation_image_id

    @property
    def allocation_name(self):
        """Gets the allocation_name of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The allocation_name of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._allocation_name

    @allocation_name.setter
    def allocation_name(self, allocation_name):
        """Sets the allocation_name of this DatastoreMachineSearchQuery.


        :param allocation_name: The allocation_name of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._allocation_name = allocation_name

    @property
    def allocation_project(self):
        """Gets the allocation_project of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The allocation_project of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._allocation_project

    @allocation_project.setter
    def allocation_project(self, allocation_project):
        """Sets the allocation_project of this DatastoreMachineSearchQuery.


        :param allocation_project: The allocation_project of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._allocation_project = allocation_project

    @property
    def allocation_role(self):
        """Gets the allocation_role of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The allocation_role of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._allocation_role

    @allocation_role.setter
    def allocation_role(self, allocation_role):
        """Sets the allocation_role of this DatastoreMachineSearchQuery.


        :param allocation_role: The allocation_role of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._allocation_role = allocation_role

    @property
    def allocation_succeeded(self):
        """Gets the allocation_succeeded of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The allocation_succeeded of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: bool
        """
        return self._allocation_succeeded

    @allocation_succeeded.setter
    def allocation_succeeded(self, allocation_succeeded):
        """Sets the allocation_succeeded of this DatastoreMachineSearchQuery.


        :param allocation_succeeded: The allocation_succeeded of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: bool
        """

        self._allocation_succeeded = allocation_succeeded

    @property
    def disk_names(self):
        """Gets the disk_names of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The disk_names of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._disk_names

    @disk_names.setter
    def disk_names(self, disk_names):
        """Sets the disk_names of this DatastoreMachineSearchQuery.


        :param disk_names: The disk_names of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._disk_names = disk_names

    @property
    def disk_sizes(self):
        """Gets the disk_sizes of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The disk_sizes of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: list[int]
        """
        return self._disk_sizes

    @disk_sizes.setter
    def disk_sizes(self, disk_sizes):
        """Sets the disk_sizes of this DatastoreMachineSearchQuery.


        :param disk_sizes: The disk_sizes of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: list[int]
        """

        self._disk_sizes = disk_sizes

    @property
    def fru_board_mfg(self):
        """Gets the fru_board_mfg of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The fru_board_mfg of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._fru_board_mfg

    @fru_board_mfg.setter
    def fru_board_mfg(self, fru_board_mfg):
        """Sets the fru_board_mfg of this DatastoreMachineSearchQuery.


        :param fru_board_mfg: The fru_board_mfg of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._fru_board_mfg = fru_board_mfg

    @property
    def fru_board_mfg_serial(self):
        """Gets the fru_board_mfg_serial of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The fru_board_mfg_serial of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._fru_board_mfg_serial

    @fru_board_mfg_serial.setter
    def fru_board_mfg_serial(self, fru_board_mfg_serial):
        """Sets the fru_board_mfg_serial of this DatastoreMachineSearchQuery.


        :param fru_board_mfg_serial: The fru_board_mfg_serial of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._fru_board_mfg_serial = fru_board_mfg_serial

    @property
    def fru_board_part_number(self):
        """Gets the fru_board_part_number of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The fru_board_part_number of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._fru_board_part_number

    @fru_board_part_number.setter
    def fru_board_part_number(self, fru_board_part_number):
        """Sets the fru_board_part_number of this DatastoreMachineSearchQuery.


        :param fru_board_part_number: The fru_board_part_number of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._fru_board_part_number = fru_board_part_number

    @property
    def fru_chassis_part_number(self):
        """Gets the fru_chassis_part_number of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The fru_chassis_part_number of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._fru_chassis_part_number

    @fru_chassis_part_number.setter
    def fru_chassis_part_number(self, fru_chassis_part_number):
        """Sets the fru_chassis_part_number of this DatastoreMachineSearchQuery.


        :param fru_chassis_part_number: The fru_chassis_part_number of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._fru_chassis_part_number = fru_chassis_part_number

    @property
    def fru_chassis_part_serial(self):
        """Gets the fru_chassis_part_serial of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The fru_chassis_part_serial of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._fru_chassis_part_serial

    @fru_chassis_part_serial.setter
    def fru_chassis_part_serial(self, fru_chassis_part_serial):
        """Sets the fru_chassis_part_serial of this DatastoreMachineSearchQuery.


        :param fru_chassis_part_serial: The fru_chassis_part_serial of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._fru_chassis_part_serial = fru_chassis_part_serial

    @property
    def fru_product_manufacturer(self):
        """Gets the fru_product_manufacturer of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The fru_product_manufacturer of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._fru_product_manufacturer

    @fru_product_manufacturer.setter
    def fru_product_manufacturer(self, fru_product_manufacturer):
        """Sets the fru_product_manufacturer of this DatastoreMachineSearchQuery.


        :param fru_product_manufacturer: The fru_product_manufacturer of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._fru_product_manufacturer = fru_product_manufacturer

    @property
    def fru_product_part_number(self):
        """Gets the fru_product_part_number of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The fru_product_part_number of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._fru_product_part_number

    @fru_product_part_number.setter
    def fru_product_part_number(self, fru_product_part_number):
        """Sets the fru_product_part_number of this DatastoreMachineSearchQuery.


        :param fru_product_part_number: The fru_product_part_number of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._fru_product_part_number = fru_product_part_number

    @property
    def fru_product_serial(self):
        """Gets the fru_product_serial of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The fru_product_serial of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._fru_product_serial

    @fru_product_serial.setter
    def fru_product_serial(self, fru_product_serial):
        """Sets the fru_product_serial of this DatastoreMachineSearchQuery.


        :param fru_product_serial: The fru_product_serial of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._fru_product_serial = fru_product_serial

    @property
    def hardware_cpu_cores(self):
        """Gets the hardware_cpu_cores of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The hardware_cpu_cores of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: int
        """
        return self._hardware_cpu_cores

    @hardware_cpu_cores.setter
    def hardware_cpu_cores(self, hardware_cpu_cores):
        """Sets the hardware_cpu_cores of this DatastoreMachineSearchQuery.


        :param hardware_cpu_cores: The hardware_cpu_cores of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: int
        """

        self._hardware_cpu_cores = hardware_cpu_cores

    @property
    def hardware_memory(self):
        """Gets the hardware_memory of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The hardware_memory of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: int
        """
        return self._hardware_memory

    @hardware_memory.setter
    def hardware_memory(self, hardware_memory):
        """Sets the hardware_memory of this DatastoreMachineSearchQuery.


        :param hardware_memory: The hardware_memory of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: int
        """

        self._hardware_memory = hardware_memory

    @property
    def id(self):
        """Gets the id of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The id of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatastoreMachineSearchQuery.


        :param id: The id of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ipmi_address(self):
        """Gets the ipmi_address of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The ipmi_address of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._ipmi_address

    @ipmi_address.setter
    def ipmi_address(self, ipmi_address):
        """Sets the ipmi_address of this DatastoreMachineSearchQuery.


        :param ipmi_address: The ipmi_address of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._ipmi_address = ipmi_address

    @property
    def ipmi_interface(self):
        """Gets the ipmi_interface of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The ipmi_interface of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._ipmi_interface

    @ipmi_interface.setter
    def ipmi_interface(self, ipmi_interface):
        """Sets the ipmi_interface of this DatastoreMachineSearchQuery.


        :param ipmi_interface: The ipmi_interface of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._ipmi_interface = ipmi_interface

    @property
    def ipmi_mac_address(self):
        """Gets the ipmi_mac_address of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The ipmi_mac_address of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._ipmi_mac_address

    @ipmi_mac_address.setter
    def ipmi_mac_address(self, ipmi_mac_address):
        """Sets the ipmi_mac_address of this DatastoreMachineSearchQuery.


        :param ipmi_mac_address: The ipmi_mac_address of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._ipmi_mac_address = ipmi_mac_address

    @property
    def ipmi_user(self):
        """Gets the ipmi_user of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The ipmi_user of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._ipmi_user

    @ipmi_user.setter
    def ipmi_user(self, ipmi_user):
        """Sets the ipmi_user of this DatastoreMachineSearchQuery.


        :param ipmi_user: The ipmi_user of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._ipmi_user = ipmi_user

    @property
    def name(self):
        """Gets the name of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The name of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatastoreMachineSearchQuery.


        :param name: The name of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def network_asns(self):
        """Gets the network_asns of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The network_asns of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: list[int]
        """
        return self._network_asns

    @network_asns.setter
    def network_asns(self, network_asns):
        """Sets the network_asns of this DatastoreMachineSearchQuery.


        :param network_asns: The network_asns of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: list[int]
        """

        self._network_asns = network_asns

    @property
    def network_destination_prefixes(self):
        """Gets the network_destination_prefixes of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The network_destination_prefixes of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._network_destination_prefixes

    @network_destination_prefixes.setter
    def network_destination_prefixes(self, network_destination_prefixes):
        """Sets the network_destination_prefixes of this DatastoreMachineSearchQuery.


        :param network_destination_prefixes: The network_destination_prefixes of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._network_destination_prefixes = network_destination_prefixes

    @property
    def network_ids(self):
        """Gets the network_ids of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The network_ids of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._network_ids

    @network_ids.setter
    def network_ids(self, network_ids):
        """Sets the network_ids of this DatastoreMachineSearchQuery.


        :param network_ids: The network_ids of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._network_ids = network_ids

    @property
    def network_ips(self):
        """Gets the network_ips of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The network_ips of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._network_ips

    @network_ips.setter
    def network_ips(self, network_ips):
        """Sets the network_ips of this DatastoreMachineSearchQuery.


        :param network_ips: The network_ips of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._network_ips = network_ips

    @property
    def network_prefixes(self):
        """Gets the network_prefixes of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The network_prefixes of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._network_prefixes

    @network_prefixes.setter
    def network_prefixes(self, network_prefixes):
        """Sets the network_prefixes of this DatastoreMachineSearchQuery.


        :param network_prefixes: The network_prefixes of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._network_prefixes = network_prefixes

    @property
    def network_vrfs(self):
        """Gets the network_vrfs of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The network_vrfs of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: list[int]
        """
        return self._network_vrfs

    @network_vrfs.setter
    def network_vrfs(self, network_vrfs):
        """Sets the network_vrfs of this DatastoreMachineSearchQuery.


        :param network_vrfs: The network_vrfs of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: list[int]
        """

        self._network_vrfs = network_vrfs

    @property
    def nics_mac_addresses(self):
        """Gets the nics_mac_addresses of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The nics_mac_addresses of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._nics_mac_addresses

    @nics_mac_addresses.setter
    def nics_mac_addresses(self, nics_mac_addresses):
        """Sets the nics_mac_addresses of this DatastoreMachineSearchQuery.


        :param nics_mac_addresses: The nics_mac_addresses of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._nics_mac_addresses = nics_mac_addresses

    @property
    def nics_names(self):
        """Gets the nics_names of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The nics_names of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._nics_names

    @nics_names.setter
    def nics_names(self, nics_names):
        """Sets the nics_names of this DatastoreMachineSearchQuery.


        :param nics_names: The nics_names of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._nics_names = nics_names

    @property
    def nics_neighbor_mac_addresses(self):
        """Gets the nics_neighbor_mac_addresses of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The nics_neighbor_mac_addresses of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._nics_neighbor_mac_addresses

    @nics_neighbor_mac_addresses.setter
    def nics_neighbor_mac_addresses(self, nics_neighbor_mac_addresses):
        """Sets the nics_neighbor_mac_addresses of this DatastoreMachineSearchQuery.


        :param nics_neighbor_mac_addresses: The nics_neighbor_mac_addresses of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._nics_neighbor_mac_addresses = nics_neighbor_mac_addresses

    @property
    def nics_neighbor_names(self):
        """Gets the nics_neighbor_names of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The nics_neighbor_names of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._nics_neighbor_names

    @nics_neighbor_names.setter
    def nics_neighbor_names(self, nics_neighbor_names):
        """Sets the nics_neighbor_names of this DatastoreMachineSearchQuery.


        :param nics_neighbor_names: The nics_neighbor_names of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._nics_neighbor_names = nics_neighbor_names

    @property
    def nics_neighbor_vrfs(self):
        """Gets the nics_neighbor_vrfs of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The nics_neighbor_vrfs of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._nics_neighbor_vrfs

    @nics_neighbor_vrfs.setter
    def nics_neighbor_vrfs(self, nics_neighbor_vrfs):
        """Sets the nics_neighbor_vrfs of this DatastoreMachineSearchQuery.


        :param nics_neighbor_vrfs: The nics_neighbor_vrfs of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._nics_neighbor_vrfs = nics_neighbor_vrfs

    @property
    def nics_vrfs(self):
        """Gets the nics_vrfs of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The nics_vrfs of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._nics_vrfs

    @nics_vrfs.setter
    def nics_vrfs(self, nics_vrfs):
        """Sets the nics_vrfs of this DatastoreMachineSearchQuery.


        :param nics_vrfs: The nics_vrfs of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._nics_vrfs = nics_vrfs

    @property
    def partition_id(self):
        """Gets the partition_id of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The partition_id of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._partition_id

    @partition_id.setter
    def partition_id(self, partition_id):
        """Sets the partition_id of this DatastoreMachineSearchQuery.


        :param partition_id: The partition_id of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._partition_id = partition_id

    @property
    def rackid(self):
        """Gets the rackid of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The rackid of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._rackid

    @rackid.setter
    def rackid(self, rackid):
        """Sets the rackid of this DatastoreMachineSearchQuery.


        :param rackid: The rackid of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._rackid = rackid

    @property
    def sizeid(self):
        """Gets the sizeid of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The sizeid of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._sizeid

    @sizeid.setter
    def sizeid(self, sizeid):
        """Sets the sizeid of this DatastoreMachineSearchQuery.


        :param sizeid: The sizeid of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """

        self._sizeid = sizeid

    @property
    def state_value(self):
        """Gets the state_value of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The state_value of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._state_value

    @state_value.setter
    def state_value(self, state_value):
        """Sets the state_value of this DatastoreMachineSearchQuery.


        :param state_value: The state_value of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["", "LOCKED", "RESERVED"]  # noqa: E501
        if state_value not in allowed_values:
            raise ValueError(
                "Invalid value for `state_value` ({0}), must be one of {1}"  # noqa: E501
                .format(state_value, allowed_values)
            )

        self._state_value = state_value

    @property
    def tags(self):
        """Gets the tags of this DatastoreMachineSearchQuery.  # noqa: E501


        :return: The tags of this DatastoreMachineSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DatastoreMachineSearchQuery.


        :param tags: The tags of this DatastoreMachineSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if issubclass(DatastoreMachineSearchQuery, dict):
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
        if not isinstance(other, DatastoreMachineSearchQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
