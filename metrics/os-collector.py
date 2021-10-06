#!/bin/env python

import argparse
from novaclient import client
from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client
import datetime
import json
import datetime as DT

def connect_nova_api(user=None,password=None,nova_api=None,project_name=None,auth_url=None):
  """
  Connect with the NOVA API
  """
  loader = loading.get_plugin_loader('password')
  auth = loader.load_from_options(auth_url=auth_url,
                                 username=user,
                                 password=password,
                                 project_name=project_name, 
                                 user_domain_id="default", 
                                 project_domain_id="default"
                                    )
  sess = session.Session(auth=auth)
  nova = client.Client(nova_api, session=sess)
  return nova

def show_usage(n=None,start_date=None,end_date=None):
  """
  Get the list of usage items by date
  """
  instances_summary=n.usage.list(detailed=True,start=start_date,end=end_date)
  return instances_summary[0]._info

def main():
    """
    Body of the os-collector
    """
    parser = argparse.ArgumentParser(description='Get OpenStack usage stats')
    parser.add_argument(
        'action', choices=['show', 'store'], help='Show and Store Openstack usage data')
    parser.add_argument(
        '-u', '--user', required=True, type=str, help='Username')
    parser.add_argument(
        '-p', '--password', required=True, type=str, help='User password')
    parser.add_argument(
        '-nv', '--nova_api', required=True, type=str, help='Nova API version')
    parser.add_argument(
        '-pn', '--project_name', required=True, type=str, help='Project name')
    parser.add_argument(
        '-au', '--auth_url', required=True, type=str, help='Authentication URL')
    parser.add_argument(
        '-sd', '--start_date', required=False, type=str, help='Start date')
    parser.add_argument(
        '-ed', '--end_date', required=False, type=str, help='End date')
    
    args = parser.parse_args()

    if args.action == "show":
      cn=connect_nova_api(user=args.user,
                          password=args.password,
                          nova_api=args.nova_api,
                          project_name=args.project_name,
                          auth_url=args.auth_url)
      if args.start_date == None:
        end_c = DT.date.today()
        end = datetime.datetime(end_c.year,end_c.month,end_c.day)
        start_c = end_c - DT.timedelta(days=1)
        start = datetime.datetime(start_c.year,start_c.month,start_c.day)
      else:
        start=datetime.datetime.strptime(args.start_date, "%Y-%m-%d")
        end=datetime.datetime.strptime(args.end_date, "%Y-%m-%d")
     
      # Start getting usage
      results = show_usage(n=cn,
                           start_date=start,
                           end_date=end)

      print(results)
    

    elif args.action == "store":
      pass
      

if __name__ == "__main__":
    main()
