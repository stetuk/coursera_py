import boto3
import os
import json





BUCKET=os.environ['Bucket']
TABLENAME=os.environ['TableName']




client=boto3.client('s3')

response = client.get_object(
    Bucket=BUCKET,
   
    Key='files/data.json'
  )
print(response)
data=json.load(response['Body'])
print(data)

dynamoDb=boto3.client('dynamodb')

dynamoDb.put_item(
    TableName=TABLENAME,
    Item={
        'id':{'N':data['id']},
        'name':{'S':data['name']},
        'course':{'S':data['course']}
        'enrolled':{'BOOL':data['enrolled'] }
    }
    )


# Get the service resource.
# dynamodb = boto3.resource('dynamodb')
# for bucket in s3.buckets.all():
#     print(bucket.OS)
# table.put_item(
#    Item={
#         'id': '1234',
#         'name': 'Diego',
#         'course': 'Restart',
#         'enrolled': True
#     }
)

  