# V1NetworkCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_announcable_cid_rs** | **list[str]** | list of cidrs which are added to the route maps per tenant private network, these are typically pod- and service cidrs, can only be set for private super networks | [optional] 
**defaultchildprefixlength** | **dict(str, int)** | if privatesuper, this defines the bitlen of child prefixes per addressfamily if not nil | [optional] 
**description** | **str** | a description for this entity | [optional] 
**destinationprefixes** | **list[str]** | the destination prefixes of this network | 
**id** | **str** | the unique ID of this entity, auto-generated if left empty | 
**labels** | **dict(str, str)** | free labels that you associate with this network. | [optional] 
**name** | **str** | a readable name for this entity | [optional] 
**nat** | **bool** | if set to true, packets leaving this ipv4 network get masqueraded behind interface ip | 
**parentnetworkid** | **str** | the id of the parent network | [optional] 
**partitionid** | **str** | the partition this network belongs to | [optional] 
**prefixes** | **list[str]** | the prefixes of this network | 
**privatesuper** | **bool** | if set to true, this network will serve as a partition&#39;s super network for the internal machine networks,there can only be one privatesuper network per partition | 
**projectid** | **str** | the project id this network belongs to, can be empty if globally available | [optional] 
**shared** | **bool** | marks a network as shareable. | [optional] 
**underlay** | **bool** | if set to true, this network can be used for underlay communication | 
**vrf** | **int** | the vrf this network is associated with | [optional] 
**vrfshared** | **bool** | if set to true, given vrf can be used by multiple networks, which is sometimes useful for network partitioning (default: false) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


