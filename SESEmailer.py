import boto3
import datetime
from botocore.exceptions import ClientError

class SESEmailer():
    def __init__(self, sender: str, recipient: str, config_set: str, aws_region: str) -> None:
        # Replace sender@example.com with your "From" address.
        # This address must be verified with Amazon SES.
        self.SENDER = sender

        # Replace recipient@example.com with a "To" address. If your account 
        # is still in the sandbox, this address must be verified.
        self.RECIPIENT = recipient

        # Specify a configuration set. If you do not want to use a configuration
        # set, comment the following variable, and the 
        # ConfigurationSetName=CONFIGURATION_SET argument below.
        self.CONFIGURATION_SET = config_set

        # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
        self.AWS_REGION = aws_region

    def send_email(self, reports: dict, dryrun: bool = False):
        # The subject line for the email.
        SUBJECT = f"{datetime.datetime.now().date()} News Report"
        
        # The email body for recipients with non-HTML email clients.
        BODY_TEXT = f"Today's News\r\n{reports}"
                    
        # The HTML body of the email.
        BODY_HTML = f"""<html>
            <head>
                <style>
                    {self.style_str()}
                </style>
            </head>
            <body>
                <h1>Today's News</h1>
                <div class='reports'>
                    {self.reports_str(reports)}
                </div>
            </body>
        </html>
                    """            

        # The character encoding for the email.
        CHARSET = "UTF-8"

        if dryrun:
            with open("OUT.html", "w") as f:
                f.write(BODY_HTML)
            return None

        # Create a new SES resource and specify a region.
        client = boto3.client('ses',region_name=self.AWS_REGION)

        # Try to send the email.
        try:
            #Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        self.RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=self.SENDER,
                # If you are not using a configuration set, comment or delete the
                # following line
                #ConfigurationSetName=self.CONFIGURATION_SET,
            )
            return response
        # Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
            return e.response['Error']['Message']
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])
            return response['MessageId']


    @staticmethod
    def style_str() -> str:
        with open("style.css") as f:
            return ''.join(f.readlines())

    @staticmethod
    def reports_str(reports: dict) -> str:
        reports_str = ""

        for i, r in enumerate(reports["articles"]):
            r = {k: v if v else '' for k, v in r.items()}
            r["title"] = r["title"] if len(r["title"].split(" - ")) == 1 else r["title"].split(" - ")[:-1][0]
            with open("report_card.html", "r") as f:
                reports_str += ''.join(f.readlines()).format(
                    index=str(i),
                    title=r["title"],
                    desc=r["description"],
                    content=r["content"],
                    url=r["url"],
                    image=r["urlToImage"],
                    author=r["author"],
                    source=r["source"]["name"],
                    time=r["publishedAt"]
                    )
                
        return reports_str