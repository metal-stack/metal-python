# V1PartitionUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootconfig** | [**V1PartitionBootConfiguration**](V1PartitionBootConfiguration.md) | the boot configuration of this partition | [optional] 
**description** | **str** | a description for this entity | [optional] 
**dns_servers** | [**list[V1DNSServer]**](V1DNSServer.md) | the dns servers for this partition | 
**id** | **str** | the unique ID of this entity | 
**labels** | **dict(str, str)** | free labels that you associate with this partition | [optional] 
**mgmtserviceaddress** | **str** | the address to the management service of this partition | [optional] 
**name** | **str** | a readable name for this entity | [optional] 
**ntp_servers** | [**list[V1NTPServer]**](V1NTPServer.md) | the ntp servers for this partition | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


