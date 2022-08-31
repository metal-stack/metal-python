# metal_python.PartitionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_partition**](PartitionApi.md#create_partition) | **PUT** /v1/partition | create a Partition. if the given ID already exists a conflict is returned
[**delete_partition**](PartitionApi.md#delete_partition) | **DELETE** /v1/partition/{id} | deletes a Partition and returns the deleted entity
[**find_partition**](PartitionApi.md#find_partition) | **GET** /v1/partition/{id} | get Partition by id
[**list_partitions**](PartitionApi.md#list_partitions) | **GET** /v1/partition | get all Partitions
[**partition_capacity**](PartitionApi.md#partition_capacity) | **POST** /v1/partition/capacity | get partition capacity
[**partition_capacity_compat**](PartitionApi.md#partition_capacity_compat) | **GET** /v1/partition/capacity | get partition capacity
[**update_partition**](PartitionApi.md#update_partition) | **POST** /v1/partition | updates a Partition. if the Partition was changed since this one was read, a conflict is returned


# **create_partition**
> V1PartitionResponse create_partition(body)

create a Partition. if the given ID already exists a conflict is returned

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
api_instance = metal_python.PartitionApi(metal_python.ApiClient(configuration))
body = metal_python.V1PartitionCreateRequest() # V1PartitionCreateRequest | 

try:
    # create a Partition. if the given ID already exists a conflict is returned
    api_response = api_instance.create_partition(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartitionApi->create_partition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PartitionCreateRequest**](V1PartitionCreateRequest.md)|  | 

### Return type

[**V1PartitionResponse**](V1PartitionResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_partition**
> V1PartitionResponse delete_partition(id)

deletes a Partition and returns the deleted entity

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
api_instance = metal_python.PartitionApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the Partition

try:
    # deletes a Partition and returns the deleted entity
    api_response = api_instance.delete_partition(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartitionApi->delete_partition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the Partition | 

### Return type

[**V1PartitionResponse**](V1PartitionResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_partition**
> V1PartitionResponse find_partition(id)

get Partition by id

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
api_instance = metal_python.PartitionApi(metal_python.ApiClient(configuration))
id = 'id_example' # str | identifier of the Partition

try:
    # get Partition by id
    api_response = api_instance.find_partition(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartitionApi->find_partition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the Partition | 

### Return type

[**V1PartitionResponse**](V1PartitionResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_partitions**
> list[V1PartitionResponse] list_partitions()

get all Partitions

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
api_instance = metal_python.PartitionApi(metal_python.ApiClient(configuration))

try:
    # get all Partitions
    api_response = api_instance.list_partitions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartitionApi->list_partitions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1PartitionResponse]**](V1PartitionResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partition_capacity**
> list[V1PartitionCapacity] partition_capacity(body)

get partition capacity

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
api_instance = metal_python.PartitionApi(metal_python.ApiClient(configuration))
body = metal_python.V1PartitionCapacityRequest() # V1PartitionCapacityRequest | 

try:
    # get partition capacity
    api_response = api_instance.partition_capacity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartitionApi->partition_capacity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PartitionCapacityRequest**](V1PartitionCapacityRequest.md)|  | 

### Return type

[**list[V1PartitionCapacity]**](V1PartitionCapacity.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partition_capacity_compat**
> list[V1PartitionCapacity] partition_capacity_compat()

get partition capacity

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
api_instance = metal_python.PartitionApi(metal_python.ApiClient(configuration))

try:
    # get partition capacity
    api_response = api_instance.partition_capacity_compat()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartitionApi->partition_capacity_compat: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1PartitionCapacity]**](V1PartitionCapacity.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_partition**
> V1PartitionResponse update_partition(body)

updates a Partition. if the Partition was changed since this one was read, a conflict is returned

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
api_instance = metal_python.PartitionApi(metal_python.ApiClient(configuration))
body = metal_python.V1PartitionUpdateRequest() # V1PartitionUpdateRequest | 

try:
    # updates a Partition. if the Partition was changed since this one was read, a conflict is returned
    api_response = api_instance.update_partition(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartitionApi->update_partition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PartitionUpdateRequest**](V1PartitionUpdateRequest.md)|  | 

### Return type

[**V1PartitionResponse**](V1PartitionResponse.md)

### Authorization

[HMAC](../README.md#HMAC), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

