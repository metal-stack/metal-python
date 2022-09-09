# metal_python.VpnApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vpn_auth_key**](VpnApi.md#get_vpn_auth_key) | **POST** /v1/vpn/authkey | create auth key to connect to project&#39;s VPN


# **get_vpn_auth_key**
> V1VPNResponse get_vpn_auth_key(body)

create auth key to connect to project's VPN

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
api_instance = metal_python.VpnApi(metal_python.ApiClient(configuration))
body = metal_python.V1VPNRequest() # V1VPNRequest | 

try:
    # create auth key to connect to project's VPN
    api_response = api_instance.get_vpn_auth_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VpnApi->get_vpn_auth_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1VPNRequest**](V1VPNRequest.md)|  | 

### Return type

[**V1VPNResponse**](V1VPNResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

