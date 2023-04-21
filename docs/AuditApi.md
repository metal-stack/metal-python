# metal_python.AuditApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_audit_traces**](AuditApi.md#find_audit_traces) | **POST** /v1/audit/find | find all audit traces that match given properties


# **find_audit_traces**
> list[V1AuditResponse] find_audit_traces(body)

find all audit traces that match given properties

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
api_instance = metal_python.AuditApi(metal_python.ApiClient(configuration))
body = metal_python.V1AuditFindRequest() # V1AuditFindRequest | 

try:
    # find all audit traces that match given properties
    api_response = api_instance.find_audit_traces(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->find_audit_traces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AuditFindRequest**](V1AuditFindRequest.md)|  | 

### Return type

[**list[V1AuditResponse]**](V1AuditResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

