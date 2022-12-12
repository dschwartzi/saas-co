from jsonpath_ng import parse
from .paginate import cw_paginate

from datetime import datetime as dt
from datetime import timedelta as td

#####################################

class get_metric_data(cw_paginate):
    def name(self): return __class__.__name__        
    def jsonpath_expression(self): return parse('MetricDataResults[*]')

#####################################

def _get_metric_stat(**kargs):

  stat = kargs.get('Stat')

  try:
      md = kargs.get('session').client('cloudwatch').get_metric_statistics(
                                                        StartTime=dt.now() - td(days=kargs.get('days')), 
                                                        EndTime=dt.now(), 
                                                        Namespace=f"AWS/{kargs.get('Namespace')}",
                                                        MetricName=kargs.get('MetricName'),
                                                        Dimensions=[kargs.get('Dimensions')],
                                                        Period=kargs.get('Period'), 
                                                        Statistics=[stat])
      return md['Datapoints'][0][stat] if len(md['Datapoints']) > 0 else None
  except Exception as e:
        print(e)
        return None

#####################################
# Utility
#####################################

def _get_metric_data(**kargs):

    try:
        return get_metric_data(kargs.get('session'), 
            StartTime=dt.now()-td(days=kargs.get('days')), 
            EndTime=dt.now(), 
            MetricDataQueries=kargs.get('MetricDataQueries'),
            fields=kargs.get('fields',[]));
    except Exception as e:
        print(e)
        return None
    
#####################################

def _get_metric_data_queries(**kargs):
    dims = kargs.get('Dimensions')
    return [{
         "Id": f"{metric}_{dims['Value']}", 
         "MetricStat": {
             "Metric": {
                 "Namespace": f"AWS/{kargs.get('Namespace')}",
                 "MetricName": metric,
                 "Dimensions": [dims]
             },
             "Period": kargs.get('Period'), 
             "Stat": kargs.get('Stat'),
             "Unit": kargs.get("Unit"),
         },
         'Label': metric
      } for metric in kargs.get('MetricNames')]
