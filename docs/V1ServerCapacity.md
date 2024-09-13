# V1ServerCapacity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | **int** | allocated machines | [optional] 
**faulty** | **int** | machines with issues with this size | [optional] 
**faultymachines** | **list[str]** | machine ids with issues with this size | [optional] 
**free** | **int** | free machines with this size (freely allocatable) | [optional] 
**other** | **int** | machines neither phoned home nor waiting but in another provisioning state | [optional] 
**othermachines** | **list[str]** | machine ids neither allocated nor waiting with this size | [optional] 
**phoned_home** | **int** | machines in phoned home provisioning state | [optional] 
**reservations** | **int** | the amount of reservations for this size | [optional] 
**size** | **str** | the size of the machine | 
**total** | **int** | total amount of machines with size | [optional] 
**unavailable** | **int** | unavailable machines with this size | [optional] 
**usedreservations** | **int** | the amount of used reservations for this size | [optional] 
**waiting** | **int** | machines in waiting provisioning state | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


