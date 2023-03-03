import json
import random

def lambda_handler(event, context):
    # TODO implement
    
    descri = event['queryStringParameters']['description']
    
    return {
        'statusCode': 200,
        'headers': {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(encode(descri))
    }
    
def encode(arg):
    all = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','z',]
    random.shuffle(all)
    newData = []
    for ele in range(len(arg)):
        newData.append(all[ele + 4])
        yourstring = ''.join((newData))
        
    return yourstring    

