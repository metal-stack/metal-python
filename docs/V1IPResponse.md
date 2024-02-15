# V1IPResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocationuuid** | **str** | a unique identifier for this ip address allocation, can be used to distinguish between ip address allocation over time. | 
**changed** | **datetime** | the last changed timestamp of this entity | [optional] 
**created** | **datetime** | the creation time of this entity | [optional] 
**description** | **str** | a description for this entity | [optional] 
**ipaddress** | **str** | the address (ipv4 or ipv6) of this ip | 
**name** | **str** | a readable name for this entity | [optional] 
**networkid** | **str** | the network this ip allocate request address belongs to | 
**projectid** | **str** | the project this ip address belongs to | 
**tags** | **list[str]** | free tags that you associate with this ip. | [optional] 
**type** | **str** | the ip type, ephemeral leads to automatic cleanup of the ip address, static will enable re-use of the ip at a later point in time | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


