# coding: utf-8

"""
    metal-api

    API to manage and control plane resources like machines, switches, operating system images, machine sizes, networks, IP addresses and more  # noqa: E501

    OpenAPI spec version: v0.28.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from metal_python.api_client import ApiClient


class SizeimageconstraintApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_size_image_constraint(self, body, **kwargs):  # noqa: E501
        """create a sizeimageconstraint. if the given ID already exists a conflict is returned  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_size_image_constraint(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1SizeImageConstraintCreateRequest body: (required)
        :return: V1SizeImageConstraintResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_size_image_constraint_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_size_image_constraint_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_size_image_constraint_with_http_info(self, body, **kwargs):  # noqa: E501
        """create a sizeimageconstraint. if the given ID already exists a conflict is returned  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_size_image_constraint_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1SizeImageConstraintCreateRequest body: (required)
        :return: V1SizeImageConstraintResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_size_image_constraint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_size_image_constraint`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/v1/size-image-constraint', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1SizeImageConstraintResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_size_image_constraint(self, id, **kwargs):  # noqa: E501
        """deletes an sizeimageconstraint and returns the deleted entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_size_image_constraint(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: identifier of the size (required)
        :return: V1SizeImageConstraintResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_size_image_constraint_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_size_image_constraint_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_size_image_constraint_with_http_info(self, id, **kwargs):  # noqa: E501
        """deletes an sizeimageconstraint and returns the deleted entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_size_image_constraint_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: identifier of the size (required)
        :return: V1SizeImageConstraintResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_size_image_constraint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_size_image_constraint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/v1/size-image-constraint/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1SizeImageConstraintResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_size_image_constraint(self, id, **kwargs):  # noqa: E501
        """get sizeimageconstraint by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_size_image_constraint(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: identifier of the sizeimageconstraint (required)
        :return: V1SizeImageConstraintResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.find_size_image_constraint_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.find_size_image_constraint_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def find_size_image_constraint_with_http_info(self, id, **kwargs):  # noqa: E501
        """get sizeimageconstraint by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_size_image_constraint_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: identifier of the sizeimageconstraint (required)
        :return: V1SizeImageConstraintResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_size_image_constraint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `find_size_image_constraint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/v1/size-image-constraint/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1SizeImageConstraintResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_size_image_constraints(self, **kwargs):  # noqa: E501
        """get all sizeimageconstraints  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_size_image_constraints(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[V1SizeImageConstraintResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_size_image_constraints_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_size_image_constraints_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_size_image_constraints_with_http_info(self, **kwargs):  # noqa: E501
        """get all sizeimageconstraints  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_size_image_constraints_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[V1SizeImageConstraintResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_size_image_constraints" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/v1/size-image-constraint', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[V1SizeImageConstraintResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def try_size_image_constraint(self, body, **kwargs):  # noqa: E501
        """try if the given combination of image and size is supported and possible to allocate  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.try_size_image_constraint(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1SizeImageConstraintTryRequest body: (required)
        :return: V1EmptyBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.try_size_image_constraint_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.try_size_image_constraint_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def try_size_image_constraint_with_http_info(self, body, **kwargs):  # noqa: E501
        """try if the given combination of image and size is supported and possible to allocate  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.try_size_image_constraint_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1SizeImageConstraintTryRequest body: (required)
        :return: V1EmptyBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method try_size_image_constraint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `try_size_image_constraint`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/v1/size-image-constraint/try', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1EmptyBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_size_image_constraint(self, body, **kwargs):  # noqa: E501
        """updates a sizeimageconstraint. if the sizeimageconstraint was changed since this one was read, a conflict is returned  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_size_image_constraint(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1SizeImageConstraintUpdateRequest body: (required)
        :return: V1SizeImageConstraintResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_size_image_constraint_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_size_image_constraint_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_size_image_constraint_with_http_info(self, body, **kwargs):  # noqa: E501
        """updates a sizeimageconstraint. if the sizeimageconstraint was changed since this one was read, a conflict is returned  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_size_image_constraint_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1SizeImageConstraintUpdateRequest body: (required)
        :return: V1SizeImageConstraintResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_size_image_constraint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_size_image_constraint`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/v1/size-image-constraint', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1SizeImageConstraintResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
