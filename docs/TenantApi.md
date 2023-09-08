# metal_python.TenantApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant**](TenantApi.md#create_tenant) | **PUT** /v1/tenant | create a tenant. if the given ID already exists a conflict is returned
[**delete_tenant**](TenantApi.md#delete_tenant) | **DELETE** /v1/tenant/{id} | deletes a tenant and returns the deleted entity
[**find_tenants**](TenantApi.md#find_tenants) | **POST** /v1/tenant/find | get all tenants that match given properties
[**get_tenant**](TenantApi.md#get_tenant) | **GET** /v1/tenant/{id} | get tenant by id
[**list_tenants**](TenantApi.md#list_tenants) | **GET** /v1/tenant | get all tenants
[**update_tenant**](TenantApi.md#update_tenant) | **POST** /v1/tenant | update a tenant. optimistic lock error can occur.


# **create_tenant**
> V1TenantResponse create_tenant(body)

create a tenant. if the given ID already exists a conflict is returned

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
api_instance = metal_python.TenantApi(metal_python.ApiClient(configuration))
body = metal_python.V1TenantCreateRequest() # V1TenantCreateRequest | 

try:
    # create a tenant. if the given ID already exists a conflict is returned
    api_response = api_instance.create_tenant(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->create_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1TenantCreateRequest**](V1TenantCreateRequest.md)|  | 

### Return type

[**V1TenantResponse**](V1TenantResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tenant**
> V1TenantResponse delete_tenant(id)

deletes a tenant and returns the deleted entity

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
api_instance = metal_python.TenantApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the tenant

try:
    # deletes a tenant and returns the deleted entity
    api_response = api_instance.delete_tenant(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->delete_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the tenant | 

### Return type

[**V1TenantResponse**](V1TenantResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_tenants**
> list[V1TenantResponse] find_tenants(body)

get all tenants that match given properties

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
api_instance = metal_python.TenantApi(metal_python.ApiClient(configuration))
body = metal_python.V1TenantFindRequest() # V1TenantFindRequest | 

try:
    # get all tenants that match given properties
    api_response = api_instance.find_tenants(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->find_tenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1TenantFindRequest**](V1TenantFindRequest.md)|  | 

### Return type

[**list[V1TenantResponse]**](V1TenantResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant**
> V1TenantResponse get_tenant(id)

get tenant by id

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
api_instance = metal_python.TenantApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the tenant

try:
    # get tenant by id
    api_response = api_instance.get_tenant(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->get_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the tenant | 

### Return type

[**V1TenantResponse**](V1TenantResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tenants**
> list[V1TenantResponse] list_tenants()

get all tenants

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
api_instance = metal_python.TenantApi(metal_python.ApiClient(configuration))

try:
    # get all tenants
    api_response = api_instance.list_tenants()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->list_tenants: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1TenantResponse]**](V1TenantResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant**
> V1TenantResponse update_tenant(body)

update a tenant. optimistic lock error can occur.

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
api_instance = metal_python.TenantApi(metal_python.ApiClient(configuration))
body = metal_python.V1TenantUpdateRequest() # V1TenantUpdateRequest | 

try:
    # update a tenant. optimistic lock error can occur.
    api_response = api_instance.update_tenant(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->update_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1TenantUpdateRequest**](V1TenantUpdateRequest.md)|  | 

### Return type

[**V1TenantResponse**](V1TenantResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

