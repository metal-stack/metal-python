# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.24.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from metal_python.api_client import ApiClient


class FirmwareApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_firmwares(self, **kwargs):  # noqa: E501
        """returns all firmwares (for a specific machine)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_firmwares(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str machine_id: restrict firmwares to the given machine
        :param str kind: the firmware kind [bios|bmc]
        :param str vendor: the vendor
        :param str board: the board
        :return: V1FirmwaresResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_firmwares_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_firmwares_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_firmwares_with_http_info(self, **kwargs):  # noqa: E501
        """returns all firmwares (for a specific machine)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_firmwares_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str machine_id: restrict firmwares to the given machine
        :param str kind: the firmware kind [bios|bmc]
        :param str vendor: the vendor
        :param str board: the board
        :return: V1FirmwaresResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['machine_id', 'kind', 'vendor', 'board']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_firmwares" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'machine_id' in params:
            query_params.append(('machine-id', params['machine_id']))  # noqa: E501
        if 'kind' in params:
            query_params.append(('kind', params['kind']))  # noqa: E501
        if 'vendor' in params:
            query_params.append(('vendor', params['vendor']))  # noqa: E501
        if 'board' in params:
            query_params.append(('board', params['board']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HMAC', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/v1/firmware', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1FirmwaresResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_firmware(self, kind, vendor, board, revision, body, **kwargs):  # noqa: E501
        """remove given firmware  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_firmware(kind, vendor, board, revision, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str kind: the firmware kind [bios|bmc] (required)
        :param str vendor: the vendor (required)
        :param str board: the board (required)
        :param str revision: the firmware revision (required)
        :param V1EmptyBody body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_firmware_with_http_info(kind, vendor, board, revision, body, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_firmware_with_http_info(kind, vendor, board, revision, body, **kwargs)  # noqa: E501
            return data

    def remove_firmware_with_http_info(self, kind, vendor, board, revision, body, **kwargs):  # noqa: E501
        """remove given firmware  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_firmware_with_http_info(kind, vendor, board, revision, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str kind: the firmware kind [bios|bmc] (required)
        :param str vendor: the vendor (required)
        :param str board: the board (required)
        :param str revision: the firmware revision (required)
        :param V1EmptyBody body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kind', 'vendor', 'board', 'revision', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_firmware" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kind' is set
        if ('kind' not in params or
                params['kind'] is None):
            raise ValueError("Missing the required parameter `kind` when calling `remove_firmware`")  # noqa: E501
        # verify the required parameter 'vendor' is set
        if ('vendor' not in params or
                params['vendor'] is None):
            raise ValueError("Missing the required parameter `vendor` when calling `remove_firmware`")  # noqa: E501
        # verify the required parameter 'board' is set
        if ('board' not in params or
                params['board'] is None):
            raise ValueError("Missing the required parameter `board` when calling `remove_firmware`")  # noqa: E501
        # verify the required parameter 'revision' is set
        if ('revision' not in params or
                params['revision'] is None):
            raise ValueError("Missing the required parameter `revision` when calling `remove_firmware`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `remove_firmware`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'kind' in params:
            path_params['kind'] = params['kind']  # noqa: E501
        if 'vendor' in params:
            path_params['vendor'] = params['vendor']  # noqa: E501
        if 'board' in params:
            path_params['board'] = params['board']  # noqa: E501
        if 'revision' in params:
            path_params['revision'] = params['revision']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HMAC', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/v1/firmware/{kind}/{vendor}/{board}/{revision}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload_firmware(self, kind, vendor, board, revision, **kwargs):  # noqa: E501
        """upload given firmware  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_firmware(kind, vendor, board, revision, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str kind: the firmware kind [bios|bmc] (required)
        :param str vendor: the vendor (required)
        :param str board: the board (required)
        :param str revision: the firmware revision (required)
        :param file file: the firmware file
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upload_firmware_with_http_info(kind, vendor, board, revision, **kwargs)  # noqa: E501
        else:
            (data) = self.upload_firmware_with_http_info(kind, vendor, board, revision, **kwargs)  # noqa: E501
            return data

    def upload_firmware_with_http_info(self, kind, vendor, board, revision, **kwargs):  # noqa: E501
        """upload given firmware  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_firmware_with_http_info(kind, vendor, board, revision, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str kind: the firmware kind [bios|bmc] (required)
        :param str vendor: the vendor (required)
        :param str board: the board (required)
        :param str revision: the firmware revision (required)
        :param file file: the firmware file
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kind', 'vendor', 'board', 'revision', 'file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_firmware" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kind' is set
        if ('kind' not in params or
                params['kind'] is None):
            raise ValueError("Missing the required parameter `kind` when calling `upload_firmware`")  # noqa: E501
        # verify the required parameter 'vendor' is set
        if ('vendor' not in params or
                params['vendor'] is None):
            raise ValueError("Missing the required parameter `vendor` when calling `upload_firmware`")  # noqa: E501
        # verify the required parameter 'board' is set
        if ('board' not in params or
                params['board'] is None):
            raise ValueError("Missing the required parameter `board` when calling `upload_firmware`")  # noqa: E501
        # verify the required parameter 'revision' is set
        if ('revision' not in params or
                params['revision'] is None):
            raise ValueError("Missing the required parameter `revision` when calling `upload_firmware`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'kind' in params:
            path_params['kind'] = params['kind']  # noqa: E501
        if 'vendor' in params:
            path_params['vendor'] = params['vendor']  # noqa: E501
        if 'board' in params:
            path_params['board'] = params['board']  # noqa: E501
        if 'revision' in params:
            path_params['revision'] = params['revision']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HMAC', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/v1/firmware/{kind}/{vendor}/{board}/{revision}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
