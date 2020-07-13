# metal_python.IpApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocate_ip**](IpApi.md#allocate_ip) | **POST** /v1/ip/allocate | allocate an ip in the given network.
[**allocate_specific_ip**](IpApi.md#allocate_specific_ip) | **POST** /v1/ip/allocate/{ip} | allocate a specific ip in the given network.
[**find_i_ps**](IpApi.md#find_i_ps) | **POST** /v1/ip/find | get all ips that match given properties
[**find_ip**](IpApi.md#find_ip) | **GET** /v1/ip/{id} | get ip by id
[**free_ip**](IpApi.md#free_ip) | **POST** /v1/ip/free/{id} | frees an ip
[**list_i_ps**](IpApi.md#list_i_ps) | **GET** /v1/ip | get all ips
[**update_ip**](IpApi.md#update_ip) | **POST** /v1/ip | updates an ip. if the ip was changed since this one was read, a conflict is returned


# **allocate_ip**
> V1IPResponse allocate_ip(body)

allocate an ip in the given network.

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
api_instance = metal_python.IpApi(metal_python.ApiClient(configuration))
body = metal_python.V1IPAllocateRequest() # V1IPAllocateRequest | 

try:
    # allocate an ip in the given network.
    api_response = api_instance.allocate_ip(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpApi->allocate_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1IPAllocateRequest**](V1IPAllocateRequest.md)|  | 

### Return type

[**V1IPResponse**](V1IPResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **allocate_specific_ip**
> V1IPResponse allocate_specific_ip(ip, body)

allocate a specific ip in the given network.

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
api_instance = metal_python.IpApi(metal_python.ApiClient(configuration))
ip = 'ip_example' # str | ip to try to allocate
body = metal_python.V1IPAllocateRequest() # V1IPAllocateRequest | 

try:
    # allocate a specific ip in the given network.
    api_response = api_instance.allocate_specific_ip(ip, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpApi->allocate_specific_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| ip to try to allocate | 
 **body** | [**V1IPAllocateRequest**](V1IPAllocateRequest.md)|  | 

### Return type

[**V1IPResponse**](V1IPResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_i_ps**
> list[V1IPResponse] find_i_ps(body)

get all ips that match given properties

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
api_instance = metal_python.IpApi(metal_python.ApiClient(configuration))
body = metal_python.V1IPFindRequest() # V1IPFindRequest | 

try:
    # get all ips that match given properties
    api_response = api_instance.find_i_ps(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpApi->find_i_ps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1IPFindRequest**](V1IPFindRequest.md)|  | 

### Return type

[**list[V1IPResponse]**](V1IPResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_ip**
> V1IPResponse find_ip(id)

get ip by id

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
api_instance = metal_python.IpApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the ip

try:
    # get ip by id
    api_response = api_instance.find_ip(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpApi->find_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the ip | 

### Return type

[**V1IPResponse**](V1IPResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **free_ip**
> V1IPResponse free_ip(id)

frees an ip

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
api_instance = metal_python.IpApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the ip

try:
    # frees an ip
    api_response = api_instance.free_ip(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpApi->free_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the ip | 

### Return type

[**V1IPResponse**](V1IPResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_i_ps**
> list[V1IPResponse] list_i_ps()

get all ips

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
api_instance = metal_python.IpApi(metal_python.ApiClient(configuration))

try:
    # get all ips
    api_response = api_instance.list_i_ps()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpApi->list_i_ps: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1IPResponse]**](V1IPResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip**
> V1IPResponse update_ip(body)

updates an ip. if the ip was changed since this one was read, a conflict is returned

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
api_instance = metal_python.IpApi(metal_python.ApiClient(configuration))
body = metal_python.V1IPUpdateRequest() # V1IPUpdateRequest | 

try:
    # updates an ip. if the ip was changed since this one was read, a conflict is returned
    api_response = api_instance.update_ip(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpApi->update_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1IPUpdateRequest**](V1IPUpdateRequest.md)|  | 

### Return type

[**V1IPResponse**](V1IPResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

