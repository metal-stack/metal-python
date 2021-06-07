# V1MachineAllocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boot_info** | [**V1BootInfo**](V1BootInfo.md) | information required for booting the machine from HD | [optional] 
**created** | **datetime** | the time when the machine was created | 
**description** | **str** | a description for this machine | [optional] 
**hostname** | **str** | the hostname which will be used when creating the machine | 
**image** | [**V1ImageResponse**](V1ImageResponse.md) | the image assigned to this machine | [optional] 
**name** | **str** | the name of the machine | 
**networks** | [**list[V1MachineNetwork]**](V1MachineNetwork.md) | the networks of this machine | 
**project** | **str** | the project id that this machine is assigned to | 
**reinstall** | **bool** | indicates whether to reinstall the machine | 
**ssh_pub_keys** | **list[str]** | the public ssh keys to access the machine with | 
**succeeded** | **bool** | if the allocation of the machine was successful, this is set to true | 
**user_data** | **str** | userdata to execute post installation tasks | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


