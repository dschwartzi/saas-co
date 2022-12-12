import boto3
import json
import pandas as pd
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse

#####################################

def fields(args, data):
    f = args.get('fields',[])
    if not f:        return data
    #if len(f) == 1:  return [i.value for i in parse(f[0]).find(data)]
    #else:            return {je:i.value for je in f for i in parse(je).find(data)}
    return {je:i.value for je in f for i in parse(je).find(data)}

#####################################

def found(args, data):
    f = args.get('filter',[])
    if not f: return True
    for je in f:
        if [match.value for match in parse(je).find([data])]:
            return True
    return False

#####################################

class paginate():
    def __init__(self, session, **kargs):
        self.json = []
        pargs = {k:v for k,v in kargs.items() if k not in ['ep', 'service', 'fields', 'filter'] if kargs}
        for page in session.client(kargs.get('service')).get_paginator(kargs.get('ep')).paginate(**pargs):
            self.json = [fields(kargs, i.value) for i in self.jsonpath_expression().find(page) if found(kargs, i.value)]
        self.df = pd.json_normalize(self.json)

            
    def __str__(self):
        return json.dumps(self.json)

#####################################

class ec2_paginate(paginate):
    def __init__(self, session, **kargs):
        kargs.update({'ep':self.name()})
        kargs.update({'service':'ec2'})
        paginate.__init__(self, session, **kargs)

#####################################

class org_paginate(paginate):
    def __init__(self, session, **kargs):
        kargs.update({'ep':self.name()})
        kargs.update({'service':'organizations'})
        paginate.__init__(self, session, **kargs)

#####################################

class s3_paginate(paginate):
    def __init__(self, session, **kargs):
        kargs.update({'ep':self.name()})
        kargs.update({'service':'s3'})
        paginate.__init__(self, session, **kargs)

#####################################

class cw_paginate(paginate):
    def __init__(self, session, **kargs):
        kargs.update({'ep':self.name()})
        kargs.update({'service':'cloudwatch'})
        paginate.__init__(self, session, **kargs)

#####################################

class ec_paginate(paginate):
    def __init__(self, session, **kargs):
        kargs.update({'ep':self.name()})
        kargs.update({'service':'elasticache'})
        paginate.__init__(self, session, **kargs)

#####################################

class ddb_paginate(paginate):
    def __init__(self, session, **kargs):
        kargs.update({'ep':self.name()})
        kargs.update({'service':'dynamodb'})
        paginate.__init__(self, session, **kargs)

#####################################
