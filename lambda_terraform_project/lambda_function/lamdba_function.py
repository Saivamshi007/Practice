import boto3
import pandas as pd
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['bucket']
    file = event['file']

    print(bucket, file)

    obj = s3.get_object(Bucket=bucket, Key = file)
    df = pd.read_csv(io.BytesIO(obj['Body'].read()))
    result = df.groupby('Pclass')['Survived'].mean().reset_index()

    outputio = io.StringIO()

    result.to_csv(outputio,index=False)

    s3.put_object(Body=outputio.getvalue(),Bucket=bucket,Key='summary.csv')

    return{
        'statusCode':200,
        'body':'Success'
    }