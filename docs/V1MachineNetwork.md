# V1MachineNetwork

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** | ASN number for this network in the bgp configuration | 
**destinationprefixes** | **list[str]** | the destination prefixes of this network | 
**ips** | **list[str]** | the ip addresses of the allocated machine in this vrf | 
**nat** | **bool** | if set to true, packets leaving this network get masqueraded behind interface ip | 
**networkid** | **str** | the networkID of the allocated machine in this vrf | 
**networktype** | **str** | the network type, types can be looked up in the network package of metal-lib | 
**prefixes** | **list[str]** | the prefixes of this network | 
**private** | **bool** | indicates whether this network is the private network of this machine | 
**underlay** | **bool** | if set to true, this network can be used for underlay communication | 
**vrf** | **int** | the vrf of the allocated machine | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


