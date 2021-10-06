# os-metrics
Quick script to get total CPU usage, RAM usage, etc. metrics from OpenStack to start creating a Billing system. It also provides of individual VMs statistics that were linving in some point.

## How to start

Clone this repository

````
git clone 

cd os-metrics
````

Install libraries

````
pip3 install -r requirements.txt
````

## Run metrics extraction

````
bash compose.sh USERNAME PASSWORD NOVACLIENT_VERSION OPENSTACK_PROJECT AUTH_URL
````

Example:

````
# It will extract latest metrics (last 30 minutes)
bash compose.sh mparra "mypasswd" "2.1" "srcpoll" "https://spsrc-openstack:5000"
````

Parameters:

- ``NOVACLIENT``: here we are using 2.1 for nova client api.
- ``OPENSTACK_PROJECT``: is the name of the project in OpenStack.
- ``AUTH_URL``: the API EndPoint for KeyStone in OpenStack.

## Output results

Within the ``output` directory all results for: 

- a) General statistics for the date range (1 day by default):
  - ``"total_local_gb_usage"``,
  - ``"total_vcpus_usage"``,
  - ``"total_memory_mb_usage"``, 
  - ``"total_hours"``
- b) Individual VMs instances usage:
```
{"hours": 24.0, 
"flavor": "test-flavor", 
"instance_id": "0a29f0b3-9886-4952-9fca-147c4ee9a2d8", 
"name": "singularity-builder", 
"tenant_id": "bd56a02429374556bbd43d325f351ea3", 
"memory_mb": 16384, 
"local_gb": 250, 
"vcpus": 2, 
"started_at": "2021-07-30T06:21:39.000000", 
"ended_at": null, "state": "active", 
"uptime": 5884618}
```

They are stored as: ``os_metrics.csv``.


### Structure of the JSON output

Output results generated:


```
{"tenant_id": "bd56a02429374556bbd43d325f351ea3", 
"server_usages": [
    {
     "hours": 24.0, 
     "flavor": "test-flavor", 
     "instance_id": "0a29f0b3-9886-4952-9fca-147c4ee9a2d8", 
     "name": "singularity-builder", 
     "tenant_id": "bd56a02429374556bbd43d325f351ea3", 
     "memory_mb": 16384, 
     "local_gb": 250, 
     "vcpus": 2, 
     "started_at": "2021-07-30T06:21:39.000000", "ended_at": null, 
     "state": "active", "uptime": 5884618}, 
    {
     "hours": 24.0, 
     "flavor": "multihub.c10m24", 
     "instance_id": "0b1f6831-444f-49eb-af2b-c2dd70c155ea", 
     "name": "multihub-kg2egzpbkmet-master-0", 
     "tenant_id": "bd56a02429374556bbd43d325f351ea3", 
     "memory_mb": 24576, 
     "local_gb": 50, 
     "vcpus": 10, 
     "started_at": "2021-02-12T16:52:33.000000", "ended_at": null, 
     "state": "active", "uptime": 20361964}, 
     ...
  ], 
  "total_local_gb_usage": 30000.0, 
  "total_vcpus_usage": 4608.0, 
  "total_memory_mb_usage": 22315008.0, 
  "total_hours": 456.0, 
  "start": "2021-10-05T00:00:00.000000", 
  "stop": "2021-10-06T00:00:00.000000"
}
```

Access to all the VM statistics that lived in that period:

```
results["server_usages"]  # Return all the VMs that lived in that period
```

Other general statistics for that period:

```
results["total_local_gb_usage"] 
results["total_vcpus_usage"]
...
```


## Workflow

0. Use a CRON job to run ``compose.sh``
1. App capture data: power and temperature
2. Data are append to ``output/*.json``
3. Folder ``output/*.json`` is commited to this repository to store data



