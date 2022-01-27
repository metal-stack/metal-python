# metal_python.SizeimageconstraintApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_size_image_constraint**](SizeimageconstraintApi.md#create_size_image_constraint) | **PUT** /v1/size-image-constraint | create a sizeimageconstraint. if the given ID already exists a conflict is returned
[**delete_size_image_constraint**](SizeimageconstraintApi.md#delete_size_image_constraint) | **DELETE** /v1/size-image-constraint/{id} | deletes an sizeimageconstraint and returns the deleted entity
[**find_size_image_constraint**](SizeimageconstraintApi.md#find_size_image_constraint) | **GET** /v1/size-image-constraint/{id} | get sizeimageconstraint by id
[**list_size_image_constraints**](SizeimageconstraintApi.md#list_size_image_constraints) | **GET** /v1/size-image-constraint | get all sizeimageconstraints
[**try_size_image_constraint**](SizeimageconstraintApi.md#try_size_image_constraint) | **POST** /v1/size-image-constraint/try | try if the given combination of image and size is supported and possible to allocate
[**update_size_image_constraint**](SizeimageconstraintApi.md#update_size_image_constraint) | **POST** /v1/size-image-constraint | updates a sizeimageconstraint. if the sizeimageconstraint was changed since this one was read, a conflict is returned


# **create_size_image_constraint**
> V1SizeImageConstraintResponse create_size_image_constraint(body)

create a sizeimageconstraint. if the given ID already exists a conflict is returned

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
api_instance = metal_python.SizeimageconstraintApi(metal_python.ApiClient(configuration))
body = metal_python.V1SizeImageConstraintCreateRequest() # V1SizeImageConstraintCreateRequest | 

try:
    # create a sizeimageconstraint. if the given ID already exists a conflict is returned
    api_response = api_instance.create_size_image_constraint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SizeimageconstraintApi->create_size_image_constraint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SizeImageConstraintCreateRequest**](V1SizeImageConstraintCreateRequest.md)|  | 

### Return type

[**V1SizeImageConstraintResponse**](V1SizeImageConstraintResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_size_image_constraint**
> V1SizeImageConstraintResponse delete_size_image_constraint(id)

deletes an sizeimageconstraint and returns the deleted entity

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
api_instance = metal_python.SizeimageconstraintApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the size

try:
    # deletes an sizeimageconstraint and returns the deleted entity
    api_response = api_instance.delete_size_image_constraint(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SizeimageconstraintApi->delete_size_image_constraint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the size | 

### Return type

[**V1SizeImageConstraintResponse**](V1SizeImageConstraintResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_size_image_constraint**
> V1SizeImageConstraintResponse find_size_image_constraint(id)

get sizeimageconstraint by id

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
api_instance = metal_python.SizeimageconstraintApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the sizeimageconstraint

try:
    # get sizeimageconstraint by id
    api_response = api_instance.find_size_image_constraint(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SizeimageconstraintApi->find_size_image_constraint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the sizeimageconstraint | 

### Return type

[**V1SizeImageConstraintResponse**](V1SizeImageConstraintResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_size_image_constraints**
> list[V1SizeImageConstraintResponse] list_size_image_constraints()

get all sizeimageconstraints

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
api_instance = metal_python.SizeimageconstraintApi(metal_python.ApiClient(configuration))

try:
    # get all sizeimageconstraints
    api_response = api_instance.list_size_image_constraints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SizeimageconstraintApi->list_size_image_constraints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1SizeImageConstraintResponse]**](V1SizeImageConstraintResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **try_size_image_constraint**
> V1EmptyBody try_size_image_constraint(body)

try if the given combination of image and size is supported and possible to allocate

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
api_instance = metal_python.SizeimageconstraintApi(metal_python.ApiClient(configuration))
body = metal_python.V1SizeImageConstraintTryRequest() # V1SizeImageConstraintTryRequest | 

try:
    # try if the given combination of image and size is supported and possible to allocate
    api_response = api_instance.try_size_image_constraint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SizeimageconstraintApi->try_size_image_constraint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SizeImageConstraintTryRequest**](V1SizeImageConstraintTryRequest.md)|  | 

### Return type

[**V1EmptyBody**](V1EmptyBody.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_size_image_constraint**
> V1SizeImageConstraintResponse update_size_image_constraint(body)

updates a sizeimageconstraint. if the sizeimageconstraint was changed since this one was read, a conflict is returned

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
api_instance = metal_python.SizeimageconstraintApi(metal_python.ApiClient(configuration))
body = metal_python.V1SizeImageConstraintUpdateRequest() # V1SizeImageConstraintUpdateRequest | 

try:
    # updates a sizeimageconstraint. if the sizeimageconstraint was changed since this one was read, a conflict is returned
    api_response = api_instance.update_size_image_constraint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SizeimageconstraintApi->update_size_image_constraint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SizeImageConstraintUpdateRequest**](V1SizeImageConstraintUpdateRequest.md)|  | 

### Return type

[**V1SizeImageConstraintResponse**](V1SizeImageConstraintResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

