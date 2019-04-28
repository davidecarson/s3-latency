import boto3
import botocore
import time

regions = ['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-south-1',
        'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ca-central-1',
        'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'eu-north-1', 'sa-east-1',
]

def put(s3, bucketname, key, filename):
    start_time = time.time()
    s3.Bucket(bucketname).put_object(Key=key, Body=open(filename, 'rb'))
    return time.time() - start_time

def get(s3, bucketname, key):
    start_time = time.time()
    s3.Object(bucketname, key).get()['Body'].read()
    return time.time() - start_time

def delete(s3, bucketname, key):
    start_time = time.time()
    s3.Object(bucketname, key).delete()
    return time.time() - start_time

files = ['1KB', '10KB', '1MB', '10MB']
runs = 10

#f = open("log", 'w')
for region in regions:
    session = boto3.Session(profile_name='default', region_name=region)
    s3 = session.resource('s3')
    bucketname = 'graykode-' + region
    try:
        s3.create_bucket(Bucket=bucketname)
    except:
        s3.create_bucket(
                Bucket=bucketname,
                CreateBucketConfiguration={'LocationConstraint': region},
            )

    print('-----[',region,']-----')
    #f.write('-----[%s]-----\n' % region)
    for key, file in enumerate(files):
        averput = averget = averdel = 0
        print('File Size', file)
        #f.write('File Size %s\n' % file)

        for i in range(0, runs):
            averput += put(s3, bucketname, str(key), file)
        print('\tAverage PUT latency', averput/runs)
        #f.write('\tAverage PUT latency %.6f\n' % (averput/runs))

        for i in range(0, runs):
            averget += get(s3, bucketname, str(key))
        print('\tAverage GET latency', averget / runs)
        #f.write('\tAverage GET latency %.6f\n' % (averget/runs))

        for i in range(0, runs):
            averdel += delete(s3, bucketname, str(key))
        print('\tAverage DEL latency', averdel / runs)
        #f.write('\tAverage DEL latency %.6f\n' % (averdel/runs))

    s3.Bucket(bucketname).objects.all().delete()
    s3.Bucket(bucketname).delete()

#f.close()