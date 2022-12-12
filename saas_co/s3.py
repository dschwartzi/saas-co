import boto3

#####################################

def get_object(**kargs):
    s3 = boto3.resource('s3')
    obj = s3.Object(kargs.get('bucket'), kargs.get('key'))
    return obj.get()['Body'].read().decode('utf-8') 

#####################################

def put_object(s, **kargs):
    d = kargs.get('data')
    k = kargs.get('key')
    b = kargs.get('bucket')
    r = kargs.get('region', 'us-east-1')
    s.client('s3', r).put_object(Body=d, Bucket=b, Key=k)

#####################################
