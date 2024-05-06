# metal_python.SwitchApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_switch**](SwitchApi.md#delete_switch) | **DELETE** /v1/switch/{id} | deletes an switch and returns the deleted entity
[**find_switch**](SwitchApi.md#find_switch) | **GET** /v1/switch/{id} | get switch by id
[**find_switches**](SwitchApi.md#find_switches) | **POST** /v1/switch/find | get all switches that match given properties
[**list_switches**](SwitchApi.md#list_switches) | **GET** /v1/switch | get all switches
[**notify_switch**](SwitchApi.md#notify_switch) | **POST** /v1/switch/{id}/notify | notify the metal-api about a configuration change of a switch
[**register_switch**](SwitchApi.md#register_switch) | **POST** /v1/switch/register | register a switch
[**toggle_switch_port**](SwitchApi.md#toggle_switch_port) | **POST** /v1/switch/{id}/port | toggles the port of the switch with a nicname to the given state
[**update_switch**](SwitchApi.md#update_switch) | **POST** /v1/switch | updates a switch. if the switch was changed since this one was read, a conflict is returned


# **delete_switch**
> V1SwitchResponse delete_switch(id)

deletes an switch and returns the deleted entity

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
api_instance = metal_python.SwitchApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the switch

try:
    # deletes an switch and returns the deleted entity
    api_response = api_instance.delete_switch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SwitchApi->delete_switch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the switch | 

### Return type

[**V1SwitchResponse**](V1SwitchResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_switch**
> V1SwitchResponse find_switch(id)

get switch by id

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
api_instance = metal_python.SwitchApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the switch

try:
    # get switch by id
    api_response = api_instance.find_switch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SwitchApi->find_switch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the switch | 

### Return type

[**V1SwitchResponse**](V1SwitchResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_switches**
> list[V1SwitchResponse] find_switches(body)

get all switches that match given properties

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
api_instance = metal_python.SwitchApi(metal_python.ApiClient(configuration))
body = metal_python.V1SwitchFindRequest() # V1SwitchFindRequest | 

try:
    # get all switches that match given properties
    api_response = api_instance.find_switches(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SwitchApi->find_switches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SwitchFindRequest**](V1SwitchFindRequest.md)|  | 

### Return type

[**list[V1SwitchResponse]**](V1SwitchResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_switches**
> list[V1SwitchResponse] list_switches()

get all switches

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
api_instance = metal_python.SwitchApi(metal_python.ApiClient(configuration))

try:
    # get all switches
    api_response = api_instance.list_switches()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SwitchApi->list_switches: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1SwitchResponse]**](V1SwitchResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_switch**
> V1SwitchNotifyResponse notify_switch(id, body)

notify the metal-api about a configuration change of a switch

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
api_instance = metal_python.SwitchApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the switch
body = metal_python.V1SwitchNotifyRequest() # V1SwitchNotifyRequest | 

try:
    # notify the metal-api about a configuration change of a switch
    api_response = api_instance.notify_switch(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SwitchApi->notify_switch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the switch | 
 **body** | [**V1SwitchNotifyRequest**](V1SwitchNotifyRequest.md)|  | 

### Return type

[**V1SwitchNotifyResponse**](V1SwitchNotifyResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_switch**
> V1SwitchResponse register_switch(body)

register a switch

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
api_instance = metal_python.SwitchApi(metal_python.ApiClient(configuration))
body = metal_python.V1SwitchRegisterRequest() # V1SwitchRegisterRequest | 

try:
    # register a switch
    api_response = api_instance.register_switch(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SwitchApi->register_switch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SwitchRegisterRequest**](V1SwitchRegisterRequest.md)|  | 

### Return type

[**V1SwitchResponse**](V1SwitchResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_switch_port**
> V1SwitchResponse toggle_switch_port(id, body)

toggles the port of the switch with a nicname to the given state

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
api_instance = metal_python.SwitchApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the switch
body = metal_python.V1SwitchPortToggleRequest() # V1SwitchPortToggleRequest | 

try:
    # toggles the port of the switch with a nicname to the given state
    api_response = api_instance.toggle_switch_port(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SwitchApi->toggle_switch_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the switch | 
 **body** | [**V1SwitchPortToggleRequest**](V1SwitchPortToggleRequest.md)|  | 

### Return type

[**V1SwitchResponse**](V1SwitchResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_switch**
> V1SwitchResponse update_switch(body)

updates a switch. if the switch was changed since this one was read, a conflict is returned

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
api_instance = metal_python.SwitchApi(metal_python.ApiClient(configuration))
body = metal_python.V1SwitchUpdateRequest() # V1SwitchUpdateRequest | 

try:
    # updates a switch. if the switch was changed since this one was read, a conflict is returned
    api_response = api_instance.update_switch(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SwitchApi->update_switch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SwitchUpdateRequest**](V1SwitchUpdateRequest.md)|  | 

### Return type

[**V1SwitchResponse**](V1SwitchResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

