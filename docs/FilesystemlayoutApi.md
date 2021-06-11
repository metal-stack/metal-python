# metal_python.FilesystemlayoutApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_filesystem_layout**](FilesystemlayoutApi.md#create_filesystem_layout) | **PUT** /v1/filesystemlayout | create a filesystemlayout. if the given ID already exists a conflict is returned
[**delete_filesystem_layout**](FilesystemlayoutApi.md#delete_filesystem_layout) | **DELETE** /v1/filesystemlayout/{id} | deletes an filesystemlayout and returns the deleted entity
[**get_filesystem_layout**](FilesystemlayoutApi.md#get_filesystem_layout) | **GET** /v1/filesystemlayout/{id} | get filesystemlayout by id
[**list_filesystem_layouts**](FilesystemlayoutApi.md#list_filesystem_layouts) | **GET** /v1/filesystemlayout | get all filesystemlayouts
[**match_filesystem_layout**](FilesystemlayoutApi.md#match_filesystem_layout) | **POST** /v1/filesystemlayout/matches | check if the given machine id satisfies the disk requirements of the filesystemlayout in question
[**try_filesystem_layout**](FilesystemlayoutApi.md#try_filesystem_layout) | **POST** /v1/filesystemlayout/try | try to detect a filesystemlayout based on given size and image.
[**update_filesystem_layout**](FilesystemlayoutApi.md#update_filesystem_layout) | **POST** /v1/filesystemlayout | updates a filesystemlayout. if the filesystemlayout was changed since this one was read, a conflict is returned


# **create_filesystem_layout**
> V1FilesystemLayoutResponse create_filesystem_layout(body)

create a filesystemlayout. if the given ID already exists a conflict is returned

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
api_instance = metal_python.FilesystemlayoutApi(metal_python.ApiClient(configuration))
body = metal_python.V1FilesystemLayoutCreateRequest() # V1FilesystemLayoutCreateRequest | 

try:
    # create a filesystemlayout. if the given ID already exists a conflict is returned
    api_response = api_instance.create_filesystem_layout(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesystemlayoutApi->create_filesystem_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1FilesystemLayoutCreateRequest**](V1FilesystemLayoutCreateRequest.md)|  | 

### Return type

[**V1FilesystemLayoutResponse**](V1FilesystemLayoutResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filesystem_layout**
> V1FilesystemLayoutResponse delete_filesystem_layout(id)

deletes an filesystemlayout and returns the deleted entity

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
api_instance = metal_python.FilesystemlayoutApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the filesystemlayout

try:
    # deletes an filesystemlayout and returns the deleted entity
    api_response = api_instance.delete_filesystem_layout(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesystemlayoutApi->delete_filesystem_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the filesystemlayout | 

### Return type

[**V1FilesystemLayoutResponse**](V1FilesystemLayoutResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filesystem_layout**
> V1FilesystemLayoutResponse get_filesystem_layout(id)

get filesystemlayout by id

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
api_instance = metal_python.FilesystemlayoutApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the filesystemlayout

try:
    # get filesystemlayout by id
    api_response = api_instance.get_filesystem_layout(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesystemlayoutApi->get_filesystem_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the filesystemlayout | 

### Return type

[**V1FilesystemLayoutResponse**](V1FilesystemLayoutResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_filesystem_layouts**
> list[V1FilesystemLayoutResponse] list_filesystem_layouts()

get all filesystemlayouts

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
api_instance = metal_python.FilesystemlayoutApi(metal_python.ApiClient(configuration))

try:
    # get all filesystemlayouts
    api_response = api_instance.list_filesystem_layouts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesystemlayoutApi->list_filesystem_layouts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1FilesystemLayoutResponse]**](V1FilesystemLayoutResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_filesystem_layout**
> V1FilesystemLayoutResponse match_filesystem_layout(body)

check if the given machine id satisfies the disk requirements of the filesystemlayout in question

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
api_instance = metal_python.FilesystemlayoutApi(metal_python.ApiClient(configuration))
body = metal_python.V1FilesystemLayoutMatchRequest() # V1FilesystemLayoutMatchRequest | 

try:
    # check if the given machine id satisfies the disk requirements of the filesystemlayout in question
    api_response = api_instance.match_filesystem_layout(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesystemlayoutApi->match_filesystem_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1FilesystemLayoutMatchRequest**](V1FilesystemLayoutMatchRequest.md)|  | 

### Return type

[**V1FilesystemLayoutResponse**](V1FilesystemLayoutResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **try_filesystem_layout**
> V1FilesystemLayoutResponse try_filesystem_layout(body)

try to detect a filesystemlayout based on given size and image.

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
api_instance = metal_python.FilesystemlayoutApi(metal_python.ApiClient(configuration))
body = metal_python.V1FilesystemLayoutTryRequest() # V1FilesystemLayoutTryRequest | 

try:
    # try to detect a filesystemlayout based on given size and image.
    api_response = api_instance.try_filesystem_layout(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesystemlayoutApi->try_filesystem_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1FilesystemLayoutTryRequest**](V1FilesystemLayoutTryRequest.md)|  | 

### Return type

[**V1FilesystemLayoutResponse**](V1FilesystemLayoutResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_filesystem_layout**
> V1FilesystemLayoutResponse update_filesystem_layout(body)

updates a filesystemlayout. if the filesystemlayout was changed since this one was read, a conflict is returned

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
api_instance = metal_python.FilesystemlayoutApi(metal_python.ApiClient(configuration))
body = metal_python.V1FilesystemLayoutUpdateRequest() # V1FilesystemLayoutUpdateRequest | 

try:
    # updates a filesystemlayout. if the filesystemlayout was changed since this one was read, a conflict is returned
    api_response = api_instance.update_filesystem_layout(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesystemlayoutApi->update_filesystem_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1FilesystemLayoutUpdateRequest**](V1FilesystemLayoutUpdateRequest.md)|  | 

### Return type

[**V1FilesystemLayoutResponse**](V1FilesystemLayoutResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

