# metal_python.ProjectApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_project**](ProjectApi.md#find_project) | **GET** /v1/project/{id} | get project by id
[**find_projects**](ProjectApi.md#find_projects) | **POST** /v1/project/find | get all projects that match given properties
[**list_projects**](ProjectApi.md#list_projects) | **GET** /v1/project | get all projects


# **find_project**
> V1ProjectResponse find_project(id)

get project by id

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.ProjectApi()
id = 'id_example' # str | identifier of the project

try:
    # get project by id
    api_response = api_instance.find_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->find_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the project | 

### Return type

[**V1ProjectResponse**](V1ProjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_projects**
> list[V1ProjectResponse] find_projects(body)

get all projects that match given properties

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.ProjectApi()
body = metal_python.V1ProjectFindRequest() # V1ProjectFindRequest | 

try:
    # get all projects that match given properties
    api_response = api_instance.find_projects(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->find_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ProjectFindRequest**](V1ProjectFindRequest.md)|  | 

### Return type

[**list[V1ProjectResponse]**](V1ProjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> list[V1ProjectResponse] list_projects()

get all projects

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.ProjectApi()

try:
    # get all projects
    api_response = api_instance.list_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1ProjectResponse]**](V1ProjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

