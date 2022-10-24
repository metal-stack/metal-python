# V1FirewallResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation** | [**V1MachineAllocation**](V1MachineAllocation.md) | the allocation data of an allocated machine | [optional] 
**bios** | [**V1MachineBIOS**](V1MachineBIOS.md) | bios information of this machine | 
**changed** | **datetime** | the last changed timestamp of this entity | [optional] 
**created** | **datetime** | the creation time of this entity | [optional] 
**description** | **str** | a description for this entity | [optional] 
**events** | [**V1MachineRecentProvisioningEvents**](V1MachineRecentProvisioningEvents.md) | recent events of this machine during provisioning | 
**hardware** | [**V1MachineHardware**](V1MachineHardware.md) | the hardware of this machine | 
**id** | **str** | the unique ID of this entity | 
**ledstate** | [**V1ChassisIdentifyLEDState**](V1ChassisIdentifyLEDState.md) | the state of this chassis identify LED | 
**liveliness** | **str** | the liveliness of this machine | 
**name** | **str** | a readable name for this entity | [optional] 
**partition** | [**V1PartitionResponse**](V1PartitionResponse.md) | the partition assigned to this machine | [optional] 
**rackid** | **str** | the rack assigned to this machine | [optional] 
**size** | [**V1SizeResponse**](V1SizeResponse.md) | the size of this machine | [optional] 
**state** | [**V1MachineState**](V1MachineState.md) | the state of this machine | 
**tags** | **list[str]** | tags for this machine | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


