# metal_python.HealthApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health**](HealthApi.md#health) | **GET** /v1/health | perform a healthcheck


# **health**
> RestHealthResponse health(service=service)

perform a healthcheck

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
api_instance = metal_python.HealthApi(metal_python.ApiClient(configuration))
service = 'service_example' # str | return health for this specific service only (optional)

try:
    # perform a healthcheck
    api_response = api_instance.health(service=service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->health: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| return health for this specific service only | [optional] 

### Return type

[**RestHealthResponse**](RestHealthResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

