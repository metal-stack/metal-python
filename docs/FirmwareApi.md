# metal_python.FirmwareApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_firmwares**](FirmwareApi.md#list_firmwares) | **GET** /v1/firmware | returns all firmwares (for a specific machine)
[**remove_firmware**](FirmwareApi.md#remove_firmware) | **DELETE** /v1/firmware/{kind}/{vendor}/{board}/{revision} | remove given firmware
[**upload_firmware**](FirmwareApi.md#upload_firmware) | **PUT** /v1/firmware/{kind}/{vendor}/{board}/{revision} | upload given firmware


# **list_firmwares**
> V1FirmwaresResponse list_firmwares(machine_id=machine_id, kind=kind, vendor=vendor, board=board)

returns all firmwares (for a specific machine)

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
api_instance = metal_python.FirmwareApi(metal_python.ApiClient(configuration))
machine_id = 'machine_id_example' # str | restrict firmwares to the given machine (optional)
kind = 'kind_example' # str | the firmware kind [bios|bmc] (optional)
vendor = 'vendor_example' # str | the vendor (optional)
board = 'board_example' # str | the board (optional)

try:
    # returns all firmwares (for a specific machine)
    api_response = api_instance.list_firmwares(machine_id=machine_id, kind=kind, vendor=vendor, board=board)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmwareApi->list_firmwares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **machine_id** | **str**| restrict firmwares to the given machine | [optional] 
 **kind** | **str**| the firmware kind [bios|bmc] | [optional] 
 **vendor** | **str**| the vendor | [optional] 
 **board** | **str**| the board | [optional] 

### Return type

[**V1FirmwaresResponse**](V1FirmwaresResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_firmware**
> remove_firmware(kind, vendor, board, revision, body)

remove given firmware

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
api_instance = metal_python.FirmwareApi(metal_python.ApiClient(configuration))
kind = 'kind_example' # str | the firmware kind [bios|bmc]
vendor = 'vendor_example' # str | the vendor
board = 'board_example' # str | the board
revision = 'revision_example' # str | the firmware revision
body = metal_python.V1EmptyBody() # V1EmptyBody | 

try:
    # remove given firmware
    api_instance.remove_firmware(kind, vendor, board, revision, body)
except ApiException as e:
    print("Exception when calling FirmwareApi->remove_firmware: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**| the firmware kind [bios|bmc] | 
 **vendor** | **str**| the vendor | 
 **board** | **str**| the board | 
 **revision** | **str**| the firmware revision | 
 **body** | [**V1EmptyBody**](V1EmptyBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_firmware**
> upload_firmware(kind, vendor, board, revision, file=file)

upload given firmware

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
api_instance = metal_python.FirmwareApi(metal_python.ApiClient(configuration))
kind = 'kind_example' # str | the firmware kind [bios|bmc]
vendor = 'vendor_example' # str | the vendor
board = 'board_example' # str | the board
revision = 'revision_example' # str | the firmware revision
file = '/path/to/file.txt' # file | the firmware file (optional)

try:
    # upload given firmware
    api_instance.upload_firmware(kind, vendor, board, revision, file=file)
except ApiException as e:
    print("Exception when calling FirmwareApi->upload_firmware: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**| the firmware kind [bios|bmc] | 
 **vendor** | **str**| the vendor | 
 **board** | **str**| the board | 
 **revision** | **str**| the firmware revision | 
 **file** | **file**| the firmware file | [optional] 

### Return type

void (empty response body)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

