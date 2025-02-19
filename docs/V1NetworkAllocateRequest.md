# V1NetworkAllocateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressfamily** | **str** | the addressfamily to allocate a child network. If not specified, the child network inherits the addressfamilies from the parent. | [optional] 
**description** | **str** | a description for this entity | [optional] 
**destinationprefixes** | **list[str]** | the destination prefixes of this network | [optional] 
**labels** | **dict(str, str)** | free labels that you associate with this network. | [optional] 
**length** | **dict(str, int)** | the bit lengths of the prefix to allocate, defaults to the default child prefix lengths of the parent network | [optional] 
**name** | **str** | a readable name for this entity | [optional] 
**nat** | **bool** | if set to true, packets leaving this network get masqueraded behind interface ip | [optional] 
**parentnetworkid** | **str** | the parent network from which this network should be allocated | 
**partitionid** | **str** | the partition this network belongs to | [optional] 
**projectid** | **str** | the project id this network belongs to, can be empty if globally available | [optional] 
**shared** | **bool** | marks a network as shareable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


