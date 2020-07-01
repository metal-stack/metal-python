# metal_python.HealthApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health**](HealthApi.md#health) | **GET** /v1/health | perform a healthcheck


# **health**
> RestStatus health()

perform a healthcheck

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.HealthApi()

try:
    # perform a healthcheck
    api_response = api_instance.health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RestStatus**](RestStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

