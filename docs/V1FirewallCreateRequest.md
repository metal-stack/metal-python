# V1FirewallCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | a description for this entity | [optional] 
**ha** | **bool** | if set to true, this firewall is set up in a High Available manner | [optional] 
**hostname** | **str** | the hostname for the allocated machine (defaults to metal) | [optional] 
**imageid** | **str** | the image id to assign this machine to | 
**ips** | **list[str]** | the ips to attach to this machine additionally | [optional] 
**name** | **str** | a readable name for this entity | [optional] 
**networks** | [**list[V1MachineAllocationNetwork]**](V1MachineAllocationNetwork.md) | the networks that this machine will be placed in. | [optional] 
**partitionid** | **str** | the partition id to assign this machine to | 
**projectid** | **str** | the project id to assign this machine to | 
**sizeid** | **str** | the size id to assign this machine to | 
**ssh_pub_keys** | **list[str]** | the public ssh keys to access the machine with | 
**tags** | **list[str]** | tags for this machine | [optional] 
**user_data** | **str** | cloud-init.io compatible userdata must be base64 encoded | [optional] 
**uuid** | **str** | if this field is set, this specific machine will be allocated if it is not in available state and not currently allocated. this field overrules size and partition | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


