import boto3
import datetime
import json

class S3Uploader():
    def __init__(self) -> None:
        self.s3 = boto3.client('s3')

    def upload_report(self, report:dict):
        self.s3.put_object(
            Body=json.dumps(report),
            Bucket='allnews-reports',
            Key=f'{datetime.datetime.now().date()} Top Headlines US'
        )

