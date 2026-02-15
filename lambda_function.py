import json
import boto3
import datetime

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCount')

def lambda_handler(event, context):
    # 1. Get current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 2. Update the Visitor Count (Atomic Counter)
    try:
        response = table.update_item(
            Key={'id': 'main_page'},
            UpdateExpression='SET #v = #v + :inc',
            ExpressionAttributeNames={'#v': 'views'},
            ExpressionAttributeValues={':inc': 1},
            ReturnValues='UPDATED_NEW'
        )
        visit_count = int(response['Attributes']['views'])
    except Exception as e:
        print(e)
        visit_count = 0
    
    # 3. Return the data
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Project 5 Status: AUTOMATED',
            'timestamp': current_time,
            'location': 'AWS Virginia Data Center (us-east-1)',
            'views': visit_count,
            'cost': '$0.00'
        }, default=str)
    }
