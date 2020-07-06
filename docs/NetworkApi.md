# metal_python.NetworkApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocate_network**](NetworkApi.md#allocate_network) | **POST** /v1/network/allocate | allocates a child network from a partition&#39;s private super network
[**create_network**](NetworkApi.md#create_network) | **PUT** /v1/network | create a network. if the given ID already exists a conflict is returned
[**delete_network**](NetworkApi.md#delete_network) | **DELETE** /v1/network/{id} | deletes a network and returns the deleted entity
[**find_network**](NetworkApi.md#find_network) | **GET** /v1/network/{id} | get network by id
[**find_networks**](NetworkApi.md#find_networks) | **POST** /v1/network/find | get all networks that match given properties
[**free_network**](NetworkApi.md#free_network) | **POST** /v1/network/free/{id} | free a network
[**list_networks**](NetworkApi.md#list_networks) | **GET** /v1/network | get all networks
[**update_network**](NetworkApi.md#update_network) | **POST** /v1/network | updates a network. if the network was changed since this one was read, a conflict is returned


# **allocate_network**
> V1NetworkResponse allocate_network(body)

allocates a child network from a partition's private super network

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: HMAC
configuration = metal_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt
configuration = metal_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = metal_python.NetworkApi(metal_python.ApiClient(configuration))
body = metal_python.V1NetworkAllocateRequest() # V1NetworkAllocateRequest | 

try:
    # allocates a child network from a partition's private super network
    api_response = api_instance.allocate_network(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->allocate_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkAllocateRequest**](V1NetworkAllocateRequest.md)|  | 

### Return type

[**V1NetworkResponse**](V1NetworkResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network**
> V1NetworkResponse create_network(body)

create a network. if the given ID already exists a conflict is returned

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: HMAC
configuration = metal_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt
configuration = metal_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = metal_python.NetworkApi(metal_python.ApiClient(configuration))
body = metal_python.V1NetworkCreateRequest() # V1NetworkCreateRequest | 

try:
    # create a network. if the given ID already exists a conflict is returned
    api_response = api_instance.create_network(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->create_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkCreateRequest**](V1NetworkCreateRequest.md)|  | 

### Return type

[**V1NetworkResponse**](V1NetworkResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network**
> V1NetworkResponse delete_network(id)

deletes a network and returns the deleted entity

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: HMAC
configuration = metal_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt
configuration = metal_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = metal_python.NetworkApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the network

try:
    # deletes a network and returns the deleted entity
    api_response = api_instance.delete_network(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->delete_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the network | 

### Return type

[**V1NetworkResponse**](V1NetworkResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_network**
> V1NetworkResponse find_network(id)

get network by id

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: HMAC
configuration = metal_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt
configuration = metal_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = metal_python.NetworkApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the network

try:
    # get network by id
    api_response = api_instance.find_network(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->find_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the network | 

### Return type

[**V1NetworkResponse**](V1NetworkResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_networks**
> list[V1NetworkResponse] find_networks(body)

get all networks that match given properties

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: HMAC
configuration = metal_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt
configuration = metal_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = metal_python.NetworkApi(metal_python.ApiClient(configuration))
body = metal_python.V1NetworkFindRequest() # V1NetworkFindRequest | 

try:
    # get all networks that match given properties
    api_response = api_instance.find_networks(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->find_networks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkFindRequest**](V1NetworkFindRequest.md)|  | 

### Return type

[**list[V1NetworkResponse]**](V1NetworkResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **free_network**
> V1NetworkResponse free_network(id)

free a network

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: HMAC
configuration = metal_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt
configuration = metal_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = metal_python.NetworkApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the network

try:
    # free a network
    api_response = api_instance.free_network(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->free_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the network | 

### Return type

[**V1NetworkResponse**](V1NetworkResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_networks**
> list[V1NetworkResponse] list_networks()

get all networks

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: HMAC
configuration = metal_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt
configuration = metal_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = metal_python.NetworkApi(metal_python.ApiClient(configuration))

try:
    # get all networks
    api_response = api_instance.list_networks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->list_networks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1NetworkResponse]**](V1NetworkResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network**
> V1NetworkResponse update_network(body)

updates a network. if the network was changed since this one was read, a conflict is returned

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: HMAC
configuration = metal_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt
configuration = metal_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = metal_python.NetworkApi(metal_python.ApiClient(configuration))
body = metal_python.V1NetworkUpdateRequest() # V1NetworkUpdateRequest | 

try:
    # updates a network. if the network was changed since this one was read, a conflict is returned
    api_response = api_instance.update_network(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->update_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetworkUpdateRequest**](V1NetworkUpdateRequest.md)|  | 

### Return type

[**V1NetworkResponse**](V1NetworkResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

