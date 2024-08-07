# metal_python.SizeApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_size**](SizeApi.md#create_size) | **PUT** /v1/size | create a size. if the given ID already exists a conflict is returned
[**delete_size**](SizeApi.md#delete_size) | **DELETE** /v1/size/{id} | deletes an size and returns the deleted entity
[**find_size**](SizeApi.md#find_size) | **GET** /v1/size/{id} | get size by id
[**list_size_reservations**](SizeApi.md#list_size_reservations) | **POST** /v1/size/reservations | get all size reservations
[**list_sizes**](SizeApi.md#list_sizes) | **GET** /v1/size | get all sizes
[**suggest**](SizeApi.md#suggest) | **POST** /v1/size/suggest | from a given machine id returns the appropriate size
[**update_size**](SizeApi.md#update_size) | **POST** /v1/size | updates a size. if the size was changed since this one was read, a conflict is returned


# **create_size**
> V1SizeResponse create_size(body)

create a size. if the given ID already exists a conflict is returned

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
api_instance = metal_python.SizeApi(metal_python.ApiClient(configuration))
body = metal_python.V1SizeCreateRequest() # V1SizeCreateRequest | 

try:
    # create a size. if the given ID already exists a conflict is returned
    api_response = api_instance.create_size(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SizeApi->create_size: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SizeCreateRequest**](V1SizeCreateRequest.md)|  | 

### Return type

[**V1SizeResponse**](V1SizeResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_size**
> V1SizeResponse delete_size(id)

deletes an size and returns the deleted entity

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
api_instance = metal_python.SizeApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the size

try:
    # deletes an size and returns the deleted entity
    api_response = api_instance.delete_size(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SizeApi->delete_size: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the size | 

### Return type

[**V1SizeResponse**](V1SizeResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_size**
> V1SizeResponse find_size(id)

get size by id

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
api_instance = metal_python.SizeApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the size

try:
    # get size by id
    api_response = api_instance.find_size(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SizeApi->find_size: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the size | 

### Return type

[**V1SizeResponse**](V1SizeResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_size_reservations**
> list[V1SizeReservationResponse] list_size_reservations(body)

get all size reservations

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
api_instance = metal_python.SizeApi(metal_python.ApiClient(configuration))
body = metal_python.V1SizeReservationListRequest() # V1SizeReservationListRequest | 

try:
    # get all size reservations
    api_response = api_instance.list_size_reservations(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SizeApi->list_size_reservations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SizeReservationListRequest**](V1SizeReservationListRequest.md)|  | 

### Return type

[**list[V1SizeReservationResponse]**](V1SizeReservationResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sizes**
> list[V1SizeResponse] list_sizes()

get all sizes

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
api_instance = metal_python.SizeApi(metal_python.ApiClient(configuration))

try:
    # get all sizes
    api_response = api_instance.list_sizes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SizeApi->list_sizes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1SizeResponse]**](V1SizeResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suggest**
> list[V1SizeConstraint] suggest(body)

from a given machine id returns the appropriate size

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
api_instance = metal_python.SizeApi(metal_python.ApiClient(configuration))
body = metal_python.V1SizeSuggestRequest() # V1SizeSuggestRequest | 

try:
    # from a given machine id returns the appropriate size
    api_response = api_instance.suggest(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SizeApi->suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SizeSuggestRequest**](V1SizeSuggestRequest.md)|  | 

### Return type

[**list[V1SizeConstraint]**](V1SizeConstraint.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_size**
> V1SizeResponse update_size(body)

updates a size. if the size was changed since this one was read, a conflict is returned

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
api_instance = metal_python.SizeApi(metal_python.ApiClient(configuration))
body = metal_python.V1SizeUpdateRequest() # V1SizeUpdateRequest | 

try:
    # updates a size. if the size was changed since this one was read, a conflict is returned
    api_response = api_instance.update_size(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SizeApi->update_size: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SizeUpdateRequest**](V1SizeUpdateRequest.md)|  | 

### Return type

[**V1SizeResponse**](V1SizeResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

