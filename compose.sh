#!/bin/bash

TODAY=$(date +"%Y%m%d")

# Start Metrics : OpenStack Data collector
python3 $HOME/os-metrics/metrics/os-collector.py \
  -u $1\
  -p $2\
  -nv $3\
  -pn $4\
  -au $5 > $HOME/os-metrics/os_metrics_$TODAY.json;




## Add to the repository
cd $HOME/os-metrics/
git add $HOME/os-metrics/output/os_metrics_$TODAY.json
git commit -m "Update OpenStack metrics `$TODAY`"
git push

