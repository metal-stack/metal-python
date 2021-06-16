# V1NetworkImmutable

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinationprefixes** | **list[str]** | the destination prefixes of this network | 
**nat** | **bool** | if set to true, packets leaving this network get masqueraded behind interface ip | 
**parentnetworkid** | **str** | the id of the parent network | [optional] 
**prefixes** | **list[str]** | the prefixes of this network | 
**privatesuper** | **bool** | if set to true, this network will serve as a partition&#39;s super network for the internal machine networks,there can only be one privatesuper network per partition | 
**underlay** | **bool** | if set to true, this network can be used for underlay communication | 
**vrf** | **int** | the vrf this network is associated with | [optional] 
**vrfshared** | **bool** | if set to true, given vrf can be used by multiple networks, which is sometimes useful for network partioning (default: false) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


