# metal_python.MachineApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_reinstall_machine**](MachineApi.md#abort_reinstall_machine) | **POST** /v1/machine/{id}/abort-reinstall | abort reinstall this machine
[**add_provisioning_event**](MachineApi.md#add_provisioning_event) | **POST** /v1/machine/{id}/event | adds a machine provisioning event
[**allocate_machine**](MachineApi.md#allocate_machine) | **POST** /v1/machine/allocate | allocate a machine
[**chassis_identify_led_off**](MachineApi.md#chassis_identify_led_off) | **POST** /v1/machine/{id}/power/chassis-identify-led-off/{description} | sends a power-off to the chassis identify LED
[**chassis_identify_led_on**](MachineApi.md#chassis_identify_led_on) | **POST** /v1/machine/{id}/power/chassis-identify-led-on | sends a power-on to the chassis identify LED
[**chassis_identify_led_on_0**](MachineApi.md#chassis_identify_led_on_0) | **POST** /v1/machine/{id}/power/chassis-identify-led-on/{description} | sends a power-on to the chassis identify LED
[**finalize_allocation**](MachineApi.md#finalize_allocation) | **POST** /v1/machine/{id}/finalize-allocation | finalize the allocation of the machine by reconfiguring the switch, sent on successful image installation
[**find_ipmi_machine**](MachineApi.md#find_ipmi_machine) | **GET** /v1/machine/{id}/ipmi | returns a machine including the ipmi connection data
[**find_ipmi_machines**](MachineApi.md#find_ipmi_machines) | **POST** /v1/machine/ipmi/find | returns machines including the ipmi connection data
[**find_machine**](MachineApi.md#find_machine) | **GET** /v1/machine/{id} | get machine by id
[**find_machines**](MachineApi.md#find_machines) | **POST** /v1/machine/find | find machines by multiple criteria
[**free_machine**](MachineApi.md#free_machine) | **DELETE** /v1/machine/{id}/free | free a machine
[**get_provisioning_event_container**](MachineApi.md#get_provisioning_event_container) | **GET** /v1/machine/{id}/event | get the current machine provisioning event container
[**ipmi_report**](MachineApi.md#ipmi_report) | **POST** /v1/machine/ipmi | reports IPMI ip addresses leased by a management server for machines
[**list_machines**](MachineApi.md#list_machines) | **GET** /v1/machine | get all known machines
[**machine_bios**](MachineApi.md#machine_bios) | **POST** /v1/machine/{id}/power/bios | boots machine into BIOS on next reboot
[**machine_off**](MachineApi.md#machine_off) | **POST** /v1/machine/{id}/power/off | sends a power-off to the machine
[**machine_on**](MachineApi.md#machine_on) | **POST** /v1/machine/{id}/power/on | sends a power-on to the machine
[**machine_reset**](MachineApi.md#machine_reset) | **POST** /v1/machine/{id}/power/reset | sends a reset to the machine
[**register_machine**](MachineApi.md#register_machine) | **POST** /v1/machine/register | register a machine
[**reinstall_machine**](MachineApi.md#reinstall_machine) | **POST** /v1/machine/{id}/reinstall | reinstall this machine
[**set_chassis_identify_led_state**](MachineApi.md#set_chassis_identify_led_state) | **POST** /v1/machine/{id}/chassis-identify-led-state | set the state of a chassis identify LED
[**set_machine_state**](MachineApi.md#set_machine_state) | **POST** /v1/machine/{id}/state | set the state of a machine
[**wait_for_allocation**](MachineApi.md#wait_for_allocation) | **GET** /v1/machine/{id}/wait | wait for an allocation of this machine


# **abort_reinstall_machine**
> V1BootInfo abort_reinstall_machine(id, body)

abort reinstall this machine

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.MachineApi()
id = 'id_example' # str | identifier of the machine
body = metal_python.V1MachineAbortReinstallRequest() # V1MachineAbortReinstallRequest | 

try:
    # abort reinstall this machine
    api_response = api_instance.abort_reinstall_machine(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->abort_reinstall_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1MachineAbortReinstallRequest**](V1MachineAbortReinstallRequest.md)|  | 

### Return type

[**V1BootInfo**](V1BootInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_provisioning_event**
> V1MachineRecentProvisioningEvents add_provisioning_event(id, body)

adds a machine provisioning event

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.MachineApi()
id = 'id_example' # str | identifier of the machine
body = metal_python.V1MachineProvisioningEvent() # V1MachineProvisioningEvent | 

try:
    # adds a machine provisioning event
    api_response = api_instance.add_provisioning_event(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->add_provisioning_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1MachineProvisioningEvent**](V1MachineProvisioningEvent.md)|  | 

### Return type

[**V1MachineRecentProvisioningEvents**](V1MachineRecentProvisioningEvents.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# create an instance of the API class
api_instance = metal_python.MachineApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chassis_identify_led_off**
> V1MachineResponse chassis_identify_led_off(id, description, body)

sends a power-off to the chassis identify LED

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.MachineApi()
id = 'id_example' # str | identifier of the machine
description = 'description_example' # str | reason why the chassis identify LED has been turned off
body = metal_python.V1EmptyBody() # V1EmptyBody | 

try:
    # sends a power-off to the chassis identify LED
    api_response = api_instance.chassis_identify_led_off(id, description, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->chassis_identify_led_off: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **description** | **str**| reason why the chassis identify LED has been turned off | 
 **body** | [**V1EmptyBody**](V1EmptyBody.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chassis_identify_led_on**
> V1MachineResponse chassis_identify_led_on(id, body)

sends a power-on to the chassis identify LED

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.MachineApi()
id = 'id_example' # str | identifier of the machine
body = metal_python.V1EmptyBody() # V1EmptyBody | 

try:
    # sends a power-on to the chassis identify LED
    api_response = api_instance.chassis_identify_led_on(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->chassis_identify_led_on: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1EmptyBody**](V1EmptyBody.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chassis_identify_led_on_0**
> V1MachineResponse chassis_identify_led_on_0(id, description, body)

sends a power-on to the chassis identify LED

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.MachineApi()
id = 'id_example' # str | identifier of the machine
description = 'description_example' # str | reason why the chassis identify LED has been turned on
body = metal_python.V1EmptyBody() # V1EmptyBody | 

try:
    # sends a power-on to the chassis identify LED
    api_response = api_instance.chassis_identify_led_on_0(id, description, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->chassis_identify_led_on_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **description** | **str**| reason why the chassis identify LED has been turned on | 
 **body** | [**V1EmptyBody**](V1EmptyBody.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finalize_allocation**
> V1MachineResponse finalize_allocation(id, body)

finalize the allocation of the machine by reconfiguring the switch, sent on successful image installation

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.MachineApi()
id = 'id_example' # str | identifier of the machine
body = metal_python.V1MachineFinalizeAllocationRequest() # V1MachineFinalizeAllocationRequest | 

try:
    # finalize the allocation of the machine by reconfiguring the switch, sent on successful image installation
    api_response = api_instance.finalize_allocation(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->finalize_allocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1MachineFinalizeAllocationRequest**](V1MachineFinalizeAllocationRequest.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

No authorization required

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

# create an instance of the API class
api_instance = metal_python.MachineApi()
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

No authorization required

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

# create an instance of the API class
api_instance = metal_python.MachineApi()
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

No authorization required

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

# create an instance of the API class
api_instance = metal_python.MachineApi()
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

No authorization required

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

# create an instance of the API class
api_instance = metal_python.MachineApi()
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

No authorization required

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

# create an instance of the API class
api_instance = metal_python.MachineApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provisioning_event_container**
> V1MachineRecentProvisioningEvents get_provisioning_event_container(id)

get the current machine provisioning event container

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.MachineApi()
id = 'id_example' # str | identifier of the machine

try:
    # get the current machine provisioning event container
    api_response = api_instance.get_provisioning_event_container(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->get_provisioning_event_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 

### Return type

[**V1MachineRecentProvisioningEvents**](V1MachineRecentProvisioningEvents.md)

### Authorization

No authorization required

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

# create an instance of the API class
api_instance = metal_python.MachineApi()
body = metal_python.V1MachineIpmiReport() # V1MachineIpmiReport | 

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
 **body** | [**V1MachineIpmiReport**](V1MachineIpmiReport.md)|  | 

### Return type

[**V1MachineIpmiReportResponse**](V1MachineIpmiReportResponse.md)

### Authorization

No authorization required

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

# create an instance of the API class
api_instance = metal_python.MachineApi()

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **machine_bios**
> V1MachineResponse machine_bios(id, body)

boots machine into BIOS on next reboot

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.MachineApi()
id = 'id_example' # str | identifier of the machine
body = metal_python.V1EmptyBody() # V1EmptyBody | 

try:
    # boots machine into BIOS on next reboot
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

No authorization required

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

# create an instance of the API class
api_instance = metal_python.MachineApi()
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

No authorization required

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

# create an instance of the API class
api_instance = metal_python.MachineApi()
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

No authorization required

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

# create an instance of the API class
api_instance = metal_python.MachineApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_machine**
> V1MachineResponse register_machine(body)

register a machine

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.MachineApi()
body = metal_python.V1MachineRegisterRequest() # V1MachineRegisterRequest | 

try:
    # register a machine
    api_response = api_instance.register_machine(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->register_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1MachineRegisterRequest**](V1MachineRegisterRequest.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

No authorization required

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

# create an instance of the API class
api_instance = metal_python.MachineApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_chassis_identify_led_state**
> V1MachineResponse set_chassis_identify_led_state(id, body)

set the state of a chassis identify LED

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.MachineApi()
id = 'id_example' # str | identifier of the machine
body = metal_python.V1ChassisIdentifyLEDState() # V1ChassisIdentifyLEDState | 

try:
    # set the state of a chassis identify LED
    api_response = api_instance.set_chassis_identify_led_state(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->set_chassis_identify_led_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 
 **body** | [**V1ChassisIdentifyLEDState**](V1ChassisIdentifyLEDState.md)|  | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

No authorization required

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

# create an instance of the API class
api_instance = metal_python.MachineApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wait_for_allocation**
> V1MachineResponse wait_for_allocation(id)

wait for an allocation of this machine

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.MachineApi()
id = 'id_example' # str | identifier of the machine

try:
    # wait for an allocation of this machine
    api_response = api_instance.wait_for_allocation(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineApi->wait_for_allocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the machine | 

### Return type

[**V1MachineResponse**](V1MachineResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

