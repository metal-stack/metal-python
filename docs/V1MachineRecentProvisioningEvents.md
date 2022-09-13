# V1MachineRecentProvisioningEvents

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crash_loop** | **bool** | indicates that machine is provisioning crash loop | 
**failed_machine_reclaim** | **bool** | indicates that machine reclaim has failed | 
**last_error_event** | [**V1MachineProvisioningEvent**](V1MachineProvisioningEvent.md) | the last erroneous event received | [optional] 
**last_event_time** | **datetime** | the time where the last event was received | [optional] 
**log** | [**list[V1MachineProvisioningEvent]**](V1MachineProvisioningEvent.md) | the log of recent machine provisioning events | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


