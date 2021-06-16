# V1FilesystemLayoutBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraints** | [**V1FilesystemLayoutConstraints**](V1FilesystemLayoutConstraints.md) | constraints which must match that this layout is taken, if sizes and images are empty these are develop layouts | 
**disks** | [**list[V1Disk]**](V1Disk.md) | list of disks that belong to this layout | [optional] 
**filesystems** | [**list[V1Filesystem]**](V1Filesystem.md) | list of filesystems to create | [optional] 
**logicalvolumes** | [**list[V1LogicalVolume]**](V1LogicalVolume.md) | list of logicalvolumes to create | [optional] 
**raid** | [**list[V1Raid]**](V1Raid.md) | list of raid arrays to create | [optional] 
**volumegroups** | [**list[V1VolumeGroup]**](V1VolumeGroup.md) | list of volumegroups to create | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


