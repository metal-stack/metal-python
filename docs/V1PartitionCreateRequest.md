# V1PartitionCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootconfig** | [**V1PartitionBootConfiguration**](V1PartitionBootConfiguration.md) | the boot configuration of this partition | 
**description** | **str** | a description for this entity | [optional] 
**dns_servers** | [**list[MetalDNSServer]**](MetalDNSServer.md) | the dns servers for this partition | [optional] 
**id** | **str** | the unique ID of this entity | 
**labels** | **dict(str, str)** | free labels that you associate with this partition | [optional] 
**mgmtserviceaddress** | **str** | the address to the management service of this partition | [optional] 
**name** | **str** | a readable name for this entity | [optional] 
**ntp_servers** | [**list[MetalNTPServer]**](MetalNTPServer.md) | the ntp servers for this partition | [optional] 
**privatenetworkprefixlength** | **int** | the length of private networks for the machine&#39;s child networks in this partition, default 22 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


