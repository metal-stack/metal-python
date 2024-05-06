# V1SwitchResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed** | **datetime** | the last changed timestamp of this entity | [optional] 
**connections** | [**list[V1SwitchConnection]**](V1SwitchConnection.md) | a connection between a switch port and a machine with the real nic states | 
**console_command** | **str** | command to access the console of the switch | [optional] 
**created** | **datetime** | the creation time of this entity | [optional] 
**description** | **str** | a description for this entity | [optional] 
**id** | **str** | the unique ID of this entity | 
**last_sync** | [**V1SwitchSync**](V1SwitchSync.md) | last successful synchronization to the switch | [optional] 
**last_sync_error** | [**V1SwitchSync**](V1SwitchSync.md) | last synchronization to the switch that was erroneous | [optional] 
**management_ip** | **str** | the ip address of the management interface of the switch | [optional] 
**management_user** | **str** | the user to connect to the switch | [optional] 
**mode** | **str** | the mode the switch currently has | [optional] 
**name** | **str** | a readable name for this entity | [optional] 
**nics** | [**list[V1SwitchNic]**](V1SwitchNic.md) | the list of network interfaces on the switch with the desired nic states | 
**os** | [**V1SwitchOS**](V1SwitchOS.md) | the operating system the switch currently has | [optional] 
**partition** | [**V1PartitionResponse**](V1PartitionResponse.md) | the partition in which this switch is located | 
**rack_id** | **str** | the id of the rack in which this switch is located | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


