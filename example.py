from metal_python.driver import Driver
from metal_python.api.partition_api import PartitionApi

# example works with the mini-lab!
d = Driver("http://api.0.0.0.0.nip.io:8080/metal", None, "metal-admin")
partition = PartitionApi(api_client=d.client)
print(partition.list_partitions())
