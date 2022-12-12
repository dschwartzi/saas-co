def call_endpoint(accounts, sessions, **kargs):
    data = {'accounts':accounts, 'sessions':sessions}
    return [run_func(a, data, **kargs) for a in accounts]

def run_func(a, data, **kargs):
    aid = a.get('account_id')
    region = a.get('region')
    s = data['sessions'].get(aid,{}).get(region,None)
    if s: 
        kargs.update({'row':a})
        a.update({kargs.get('key'): kargs.get('func')(s, **kargs)})
        return a
    return None     
