# metal_python.FirewallApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocate_firewall**](FirewallApi.md#allocate_firewall) | **POST** /v1/firewall/allocate | allocate a firewall
[**find_firewall**](FirewallApi.md#find_firewall) | **GET** /v1/firewall/{id} | get firewall by id
[**find_firewalls**](FirewallApi.md#find_firewalls) | **POST** /v1/firewall/find | find firewalls by multiple criteria
[**list_firewalls**](FirewallApi.md#list_firewalls) | **GET** /v1/firewall | get all known firewalls


# **allocate_firewall**
> V1FirewallResponse allocate_firewall(body)

allocate a firewall

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
api_instance = metal_python.FirewallApi(metal_python.ApiClient(configuration))
body = metal_python.V1FirewallCreateRequest() # V1FirewallCreateRequest | 

try:
    # allocate a firewall
    api_response = api_instance.allocate_firewall(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->allocate_firewall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1FirewallCreateRequest**](V1FirewallCreateRequest.md)|  | 

### Return type

[**V1FirewallResponse**](V1FirewallResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_firewall**
> V1FirewallResponse find_firewall(id)

get firewall by id

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
api_instance = metal_python.FirewallApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the firewall

try:
    # get firewall by id
    api_response = api_instance.find_firewall(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->find_firewall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the firewall | 

### Return type

[**V1FirewallResponse**](V1FirewallResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_firewalls**
> list[V1FirewallResponse] find_firewalls(body)

find firewalls by multiple criteria

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
api_instance = metal_python.FirewallApi(metal_python.ApiClient(configuration))
body = metal_python.V1FirewallFindRequest() # V1FirewallFindRequest | 

try:
    # find firewalls by multiple criteria
    api_response = api_instance.find_firewalls(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->find_firewalls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1FirewallFindRequest**](V1FirewallFindRequest.md)|  | 

### Return type

[**list[V1FirewallResponse]**](V1FirewallResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_firewalls**
> list[V1FirewallResponse] list_firewalls()

get all known firewalls

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
api_instance = metal_python.FirewallApi(metal_python.ApiClient(configuration))

try:
    # get all known firewalls
    api_response = api_instance.list_firewalls()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->list_firewalls: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1FirewallResponse]**](V1FirewallResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

