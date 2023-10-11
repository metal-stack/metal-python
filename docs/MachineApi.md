# metal_python.MachineApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocate_machine**](MachineApi.md#allocate_machine) | **POST** /v1/machine/allocate | allocate a machine
[**chassis_identify_led_off**](MachineApi.md#chassis_identify_led_off) | **POST** /v1/machine/{id}/power/chassis-identify-led-off | sends a power-off to the chassis identify LED
[**chassis_identify_led_on**](MachineApi.md#chassis_identify_led_on) | **POST** /v1/machine/{id}/power/chassis-identify-led-on | sends a power-on to the chassis identify LED
[**delete_machine**](MachineApi.md#delete_machine) | **DELETE** /v1/machine/{id} | deletes a machine from the database
[**find_ipmi_machine**](MachineApi.md#find_ipmi_machine) | **GET** /v1/machine/{id}/ipmi | returns a machine including the ipmi connection data
[**find_ipmi_machines**](MachineApi.md#find_ipmi_machines) | **POST** /v1/machine/ipmi/find | returns machines including the ipmi connection data
[**find_machine**](MachineApi.md#find_machine) | **GET** /v1/machine/{id} | get machine by id
[**find_machines**](MachineApi.md#find_machines) | **POST** /v1/machine/find | find machines by multiple criteria
[**free_machine**](MachineApi.md#free_machine) | **DELETE** /v1/machine/{id}/free | free a machine
[**get_machine_console_password**](MachineApi.md#get_machine_console_password) | **GET** /v1/machine/consolepassword | get consolepassword for machine by id
[**ipmi_report**](MachineApi.md#ipmi_report) | **POST** /v1/machine/ipmi | reports IPMI ip addresses leased by a management server for machines
[**issues**](MachineApi.md#issues) | **POST** /v1/machine/issues/evaluate | returns machine issues
[**list_issues**](MachineApi.md#list_issues) | **GET** /v1/machine/issues | returns the list of issues that exist in the API
[**list_machines**](MachineApi.md#list_machines) | **GET** /v1/machine | get all known machines
[**machine_bios**](MachineApi.md#machine_bios) | **POST** /v1/machine/{id}/power/bios | boots machine into BIOS
[**machine_cycle**](MachineApi.md#machine_cycle) | **POST** /v1/machine/{id}/power/cycle | sends a power cycle to the machine
[**machine_disk**](MachineApi.md#machine_disk) | **POST** /v1/machine/{id}/power/disk | boots machine from disk
[**machine_off**](MachineApi.md#machine_off) | **POST** /v1/machine/{id}/power/off | sends a power-off to the machine
[**machine_on**](MachineApi.md#machine_on) | **POST** /v1/machine/{id}/power/on | sends a power-on to the machine
[**machine_pxe**](MachineApi.md#machine_pxe) | **POST** /v1/machine/{id}/power/pxe | boots machine from PXE
[**machine_reset**](MachineApi.md#machine_reset) | **POST** /v1/machine/{id}/power/reset | sends a reset to the machine
[**reinstall_machine**](MachineApi.md#reinstall_machine) | **POST** /v1/machine/{id}/reinstall | reinstall this machine
[**set_machine_state**](MachineApi.md#set_machine_state) | **POST** /v1/machine/{id}/state | set the state of a machine
[**update_firmware**](MachineApi.md#update_firmware) | **POST** /v1/machine/update-firmware/{id} | sends a firmware command to the machine
[**update_machine**](MachineApi.md#update_machine) | **POST** /v1/machine | updates a machine. if the machine was changed since this one was read, a conflict is returned


# **allocate_machine**
> V1MachineResponse allocate_machine(body)

allocate a machine

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
body = metal_python.V1MachineAllocateRequest() # V1MachineAllocateRequest | 

try:
    # allocate a machine
    api_response = api_instance.allocate_machine(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->allocate_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1MachineAllocateRequest**](V1MachineAllocateRequest.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chassis_identify_led_off**
> V1MachineResponse chassis_identify_led_off(id, body, description=description)

sends a power-off to the chassis identify LED

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the machine
body = metal_python.V1EmptyBody() # V1EmptyBody | 
description = 'description_example' # str | reason why the chassis identify LED has been turned off (optional)

try:
    # sends a power-off to the chassis identify LED
    api_response = api_instance.chassis_identify_led_off(id, body, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->chassis_identify_led_off: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1EmptyBody**](V1EmptyBody.md)|  | 
 **description** | **str**| reason why the chassis identify LED has been turned off | [optional] 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chassis_identify_led_on**
> V1MachineResponse chassis_identify_led_on(id, body, description=description)

sends a power-on to the chassis identify LED

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the machine
body = metal_python.V1EmptyBody() # V1EmptyBody | 
description = 'description_example' # str | identifier of the machine (optional)

try:
    # sends a power-on to the chassis identify LED
    api_response = api_instance.chassis_identify_led_on(id, body, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->chassis_identify_led_on: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1EmptyBody**](V1EmptyBody.md)|  | 
 **description** | **str**| identifier of the machine | [optional] 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_machine**
> V1MachineResponse delete_machine(id)

deletes a machine from the database

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the machine

try:
    # deletes a machine from the database
    api_response = api_instance.delete_machine(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->delete_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_ipmi_machine**
> V1MachineIPMIResponse find_ipmi_machine(id)

returns a machine including the ipmi connection data

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the machine

try:
    # returns a machine including the ipmi connection data
    api_response = api_instance.find_ipmi_machine(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->find_ipmi_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 

### Return type

[**V1MachineIPMIResponse**](V1MachineIPMIResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_ipmi_machines**
> list[V1MachineIPMIResponse] find_ipmi_machines(body)

returns machines including the ipmi connection data

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
body = metal_python.V1MachineFindRequest() # V1MachineFindRequest | 

try:
    # returns machines including the ipmi connection data
    api_response = api_instance.find_ipmi_machines(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->find_ipmi_machines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1MachineFindRequest**](V1MachineFindRequest.md)|  | 

### Return type

[**list[V1MachineIPMIResponse]**](V1MachineIPMIResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_machine**
> V1MachineResponse find_machine(id)

get machine by id

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the machine

try:
    # get machine by id
    api_response = api_instance.find_machine(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->find_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_machines**
> list[V1MachineResponse] find_machines(body)

find machines by multiple criteria

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
body = metal_python.V1MachineFindRequest() # V1MachineFindRequest | 

try:
    # find machines by multiple criteria
    api_response = api_instance.find_machines(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->find_machines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1MachineFindRequest**](V1MachineFindRequest.md)|  | 

### Return type

[**list[V1MachineResponse]**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **free_machine**
> V1MachineResponse free_machine(id)

free a machine

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the machine

try:
    # free a machine
    api_response = api_instance.free_machine(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->free_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_machine_console_password**
> V1MachineConsolePasswordResponse get_machine_console_password(body)

get consolepassword for machine by id

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
body = metal_python.V1MachineConsolePasswordRequest() # V1MachineConsolePasswordRequest | 

try:
    # get consolepassword for machine by id
    api_response = api_instance.get_machine_console_password(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->get_machine_console_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1MachineConsolePasswordRequest**](V1MachineConsolePasswordRequest.md)|  | 

### Return type

[**V1MachineConsolePasswordResponse**](V1MachineConsolePasswordResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipmi_report**
> V1MachineIpmiReportResponse ipmi_report(body)

reports IPMI ip addresses leased by a management server for machines

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
body = metal_python.V1MachineIpmiReports() # V1MachineIpmiReports | 

try:
    # reports IPMI ip addresses leased by a management server for machines
    api_response = api_instance.ipmi_report(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->ipmi_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1MachineIpmiReports**](V1MachineIpmiReports.md)|  | 

### Return type

[**V1MachineIpmiReportResponse**](V1MachineIpmiReportResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issues**
> list[V1MachineIssueResponse] issues(body)

returns machine issues

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
body = metal_python.V1MachineIssuesRequest() # V1MachineIssuesRequest | 

try:
    # returns machine issues
    api_response = api_instance.issues(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1MachineIssuesRequest**](V1MachineIssuesRequest.md)|  | 

### Return type

[**list[V1MachineIssueResponse]**](V1MachineIssueResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_issues**
> list[V1MachineIssue] list_issues()

returns the list of issues that exist in the API

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))

try:
    # returns the list of issues that exist in the API
    api_response = api_instance.list_issues()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->list_issues: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1MachineIssue]**](V1MachineIssue.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_machines**
> list[V1MachineResponse] list_machines()

get all known machines

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))

try:
    # get all known machines
    api_response = api_instance.list_machines()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->list_machines: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1MachineResponse]**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **machine_bios**
> V1MachineResponse machine_bios(id, body)

boots machine into BIOS

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the machine
body = metal_python.V1EmptyBody() # V1EmptyBody | 

try:
    # boots machine into BIOS
    api_response = api_instance.machine_bios(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->machine_bios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1EmptyBody**](V1EmptyBody.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **machine_cycle**
> V1MachineResponse machine_cycle(id, body)

sends a power cycle to the machine

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the machine
body = metal_python.V1EmptyBody() # V1EmptyBody | 

try:
    # sends a power cycle to the machine
    api_response = api_instance.machine_cycle(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->machine_cycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1EmptyBody**](V1EmptyBody.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **machine_disk**
> V1MachineResponse machine_disk(id, body)

boots machine from disk

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the machine
body = metal_python.V1EmptyBody() # V1EmptyBody | 

try:
    # boots machine from disk
    api_response = api_instance.machine_disk(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->machine_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1EmptyBody**](V1EmptyBody.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **machine_off**
> V1MachineResponse machine_off(id, body)

sends a power-off to the machine

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the machine
body = metal_python.V1EmptyBody() # V1EmptyBody | 

try:
    # sends a power-off to the machine
    api_response = api_instance.machine_off(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->machine_off: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1EmptyBody**](V1EmptyBody.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **machine_on**
> V1MachineResponse machine_on(id, body)

sends a power-on to the machine

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the machine
body = metal_python.V1EmptyBody() # V1EmptyBody | 

try:
    # sends a power-on to the machine
    api_response = api_instance.machine_on(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->machine_on: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1EmptyBody**](V1EmptyBody.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **machine_pxe**
> V1MachineResponse machine_pxe(id, body)

boots machine from PXE

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the machine
body = metal_python.V1EmptyBody() # V1EmptyBody | 

try:
    # boots machine from PXE
    api_response = api_instance.machine_pxe(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->machine_pxe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1EmptyBody**](V1EmptyBody.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **machine_reset**
> V1MachineResponse machine_reset(id, body)

sends a reset to the machine

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the machine
body = metal_python.V1EmptyBody() # V1EmptyBody | 

try:
    # sends a reset to the machine
    api_response = api_instance.machine_reset(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->machine_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1EmptyBody**](V1EmptyBody.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reinstall_machine**
> V1MachineResponse reinstall_machine(id, body)

reinstall this machine

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the machine
body = metal_python.V1MachineReinstallRequest() # V1MachineReinstallRequest | 

try:
    # reinstall this machine
    api_response = api_instance.reinstall_machine(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->reinstall_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1MachineReinstallRequest**](V1MachineReinstallRequest.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_machine_state**
> V1MachineResponse set_machine_state(id, body)

set the state of a machine

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the machine
body = metal_python.V1MachineState() # V1MachineState | 

try:
    # set the state of a machine
    api_response = api_instance.set_machine_state(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->set_machine_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1MachineState**](V1MachineState.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firmware**
> V1MachineResponse update_firmware(id, body)

sends a firmware command to the machine

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the machine
body = metal_python.V1MachineUpdateFirmwareRequest() # V1MachineUpdateFirmwareRequest | 

try:
    # sends a firmware command to the machine
    api_response = api_instance.update_firmware(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->update_firmware: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1MachineUpdateFirmwareRequest**](V1MachineUpdateFirmwareRequest.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_machine**
> V1MachineResponse update_machine(body)

updates a machine. if the machine was changed since this one was read, a conflict is returned

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
api_instance = metal_python.MachineApi(metal_python.ApiClient(configuration))
body = metal_python.V1MachineUpdateRequest() # V1MachineUpdateRequest | 

try:
    # updates a machine. if the machine was changed since this one was read, a conflict is returned
    api_response = api_instance.update_machine(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->update_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1MachineUpdateRequest**](V1MachineUpdateRequest.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

