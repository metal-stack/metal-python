from metal_python.driver import Driver
from metal_python.api.partition_api import PartitionApi

d = Driver("http://api.0.0.0.0.xip.io:8080/metal", None, "metal-admin")
partition = PartitionApi(api_client=d.client)
print(partition.list_partitions())
