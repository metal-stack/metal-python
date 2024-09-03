# V1NetworkUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_announcable_cid_rs** | **list[str]** | list of cidrs which are added to the route maps per tenant private network, these are typically pod- and service cidrs, can only be set for private super networks | [optional] 
**description** | **str** | a description for this entity | [optional] 
**destinationprefixes** | **list[str]** | the destination prefixes of this network | [optional] 
**id** | **str** | the unique ID of this entity | 
**labels** | **dict(str, str)** | free labels that you associate with this network. | [optional] 
**name** | **str** | a readable name for this entity | [optional] 
**prefixes** | **list[str]** | the prefixes of this network | [optional] 
**shared** | **bool** | marks a network as shareable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


