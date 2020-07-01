# metal_python.VersionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info**](VersionApi.md#info) | **GET** /v1/version | returns the current version information of this module


# **info**
> RestVersion info()

returns the current version information of this module

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.VersionApi()

try:
    # returns the current version information of this module
    api_response = api_instance.info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RestVersion**](RestVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

