#!/bin/bash

date = $(date '+%Y-%m-%d')

# Start Metrics : OpenStack Data collector
python3 $HOME/os-metrics/metrics/os-collector.py \
  -u $1\
  -p $2\
  -nv $3\
  -pn $4\
  -au $5 > os_metrics_$date.json;



## Add to the repository
cd $HOME/os-metrics/
git add $HOME/os-metrics/output/os_metrics_$date.json
git commit -m "Update OpenStack metrics `$date`"
git push

