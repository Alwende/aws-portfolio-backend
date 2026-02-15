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
    response = table.update_item(
        Key={'id': 'main_page'},
        UpdateExpression='SET #v = #v + :inc',
        ExpressionAttributeNames={'#v': 'views'},
        ExpressionAttributeValues={':inc': 1},
        ReturnValues='UPDATED_NEW'
    )

    # 3. Get the new count
    visit_count = int(response['Attributes']['views'])
    
    # 4. Return the data
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Project 4 Status: OPERATIONAL',
            'timestamp': current_time,
            'location': 'AWS Virginia Data Center (us-east-1)',
            'views': visit_count,
            'cost': '$0.00'
        }, default=str)
    }
