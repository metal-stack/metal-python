# V1IPAllocateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressfamily** | **str** | the addressfamily to allocate a ip address from the given network, defaults to IPv4 | [optional] 
**description** | **str** | a description for this entity | [optional] 
**machineid** | **str** | the machine id this ip should be associated with | [optional] 
**name** | **str** | a readable name for this entity | [optional] 
**networkid** | **str** | the network this ip allocate request address belongs to | 
**projectid** | **str** | the project this ip address belongs to | 
**tags** | **list[str]** | free tags that you associate with this ip. | [optional] 
**type** | **str** | the ip type, ephemeral leads to automatic cleanup of the ip address, static will enable re-use of the ip at a later point in time | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


