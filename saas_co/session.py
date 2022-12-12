import boto3

#####################

def session_from_credentials(creds, region):
    try:
        return boto3.session.Session(
            region_name=region,
            aws_access_key_id=creds["AccessKeyId"],
            aws_secret_access_key=creds["SecretAccessKey"],
            aws_session_token=creds["SessionToken"]
        )
    except:
        return None

#####################

def assume_role(**params):
    region = params.get('region', 'us-east-1')
    access_key_id = params.get('access_key_id')
    secret_access_key = params.get('secret_access_key') 
 
    account_id = params.get('accountId')
    role_name = params.get('roleName')
    session_name = params.get('sessionName','tmp')
    role_arn = f'arn:aws:iam::{account_id}:role/{role_name}'

    try:
        if access_key_id:
            sts = boto3.client('sts', 
                               region_name=region,
                               aws_access_key_id=access_key_id,                
                               aws_secret_access_key=secret_access_key)
        else:
            sts = boto3.client('sts')
        assumed_role = sts.assume_role(RoleArn=role_arn, 
                                       RoleSessionName=session_name)
        credentials = assumed_role.get('Credentials')
    except Exception as e:
        print(account_id, 'Assume error')
        credentials = None

    return session_from_credentials(credentials, region)

############################################

def get_account_regions(accounts):
    account_regions = list(set([(a['account_id'], a['region']) for a in accounts]))
    return [{'account_id':a[0], 'region':a[1]} for a in account_regions]

#####################

def get_session(a, **args):
    reg = a.get('region')
    aid = a.get('account_id')
    sessions = args.get('sessions')
    if not sessions: 
        for ar in args.get('account_regions'): sessions.update({ar['account_id']:{}})
    s = sessions.get(aid,{}).get(reg,None)
    if not s: sessions[aid][reg] = assume_role(access_key_id = args.get('key'), 
                                               secret_access_key = args.get('secret'),
                                               roleName = args.get('role'),
                                               accountId = aid, region=reg)
        
#####################

def get_sessions(accounts, **kargs):
    account_regions = get_account_regions(accounts)
    kargs.update({'account_regions': account_regions, 'sessions':{}})
    [get_session(a, **kargs) for a in accounts]
    return kargs['sessions']
