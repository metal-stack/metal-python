# metal_python.ImageApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_image**](ImageApi.md#create_image) | **PUT** /v1/image | create an image. if the given ID already exists a conflict is returned
[**delete_image**](ImageApi.md#delete_image) | **DELETE** /v1/image/{id} | deletes an image and returns the deleted entity
[**find_image**](ImageApi.md#find_image) | **GET** /v1/image/{id} | get image by id
[**find_latest_image**](ImageApi.md#find_latest_image) | **GET** /v1/image/{id}/latest | find latest image by id
[**list_images**](ImageApi.md#list_images) | **GET** /v1/image | get all images
[**update_image**](ImageApi.md#update_image) | **POST** /v1/image | updates an image. if the image was changed since this one was read, a conflict is returned


# **create_image**
> V1ImageResponse create_image(body)

create an image. if the given ID already exists a conflict is returned

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.ImageApi()
body = metal_python.V1ImageCreateRequest() # V1ImageCreateRequest | 

try:
    # create an image. if the given ID already exists a conflict is returned
    api_response = api_instance.create_image(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->create_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageCreateRequest**](V1ImageCreateRequest.md)|  | 

### Return type

[**V1ImageResponse**](V1ImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image**
> V1ImageResponse delete_image(id)

deletes an image and returns the deleted entity

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.ImageApi()
id = 'id_example' # str | identifier of the image

try:
    # deletes an image and returns the deleted entity
    api_response = api_instance.delete_image(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->delete_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the image | 

### Return type

[**V1ImageResponse**](V1ImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_image**
> V1ImageResponse find_image(id)

get image by id

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.ImageApi()
id = 'id_example' # str | identifier of the image

try:
    # get image by id
    api_response = api_instance.find_image(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->find_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the image | 

### Return type

[**V1ImageResponse**](V1ImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_latest_image**
> V1ImageResponse find_latest_image(id)

find latest image by id

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.ImageApi()
id = 'id_example' # str | identifier of the image

try:
    # find latest image by id
    api_response = api_instance.find_latest_image(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->find_latest_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the image | 

### Return type

[**V1ImageResponse**](V1ImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_images**
> list[V1ImageResponse] list_images()

get all images

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.ImageApi()

try:
    # get all images
    api_response = api_instance.list_images()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->list_images: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1ImageResponse]**](V1ImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_image**
> V1ImageResponse update_image(body)

updates an image. if the image was changed since this one was read, a conflict is returned

### Example
```python
from __future__ import print_function
import time
import metal_python
from metal_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = metal_python.ImageApi()
body = metal_python.V1ImageUpdateRequest() # V1ImageUpdateRequest | 

try:
    # updates an image. if the image was changed since this one was read, a conflict is returned
    api_response = api_instance.update_image(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->update_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageUpdateRequest**](V1ImageUpdateRequest.md)|  | 

### Return type

[**V1ImageResponse**](V1ImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

