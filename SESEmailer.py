import boto3
import datetime
from airium import Airium
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

        self.airium = Airium()

    def send_email(self, reports: dict, dryrun: bool = False):
        # The subject line for the email.
        SUBJECT = f"{datetime.datetime.now().date()} News Report"
        
        # The email body for recipients with non-HTML email clients.
        BODY_TEXT = f"Today's News\r\n{reports}"
        
        self.airium('<!DOCTYPE html>')
        with self.airium.html(lang="en"):
            with self.airium.head():
                self.airium.meta(charset="utf-8")
                self.airium.title(_t="Ctbus News")

            with self.airium.body():
                with self.airium.h1():
                    self.airium("Top Headlines")
                with self.airium.table(style="border: 1px solid black; padding-inline: 15px;"):
                    reports_by_source = {source: [r for r in reports["articles"] if r["source"]["name"] == source] for source in list(set([r["source"]["name"] for r in reports["articles"]]))}
                    
                    for source, reports_list in reports_by_source.items():
                        with self.airium.tr():
                            with self.airium.td():
                                self.airium.h3(_t=f"{source}")
                        with self.airium.tr():
                            with self.airium.td():
                                with self.airium.table(style="padding-inline: 15px;"):
                                    for r in reports_list:
                                        with self.airium.tr():
                                            r["title"] = r["title"] if len(r["title"].split(" - ")) == 1 else r["title"].split(" - ")[:-1][0]
                                            display_str = f"{r['title']}"
                                            if r["author"]:
                                                display_str += f" - {r['author']}"
                                            with self.airium.td():
                                                self.airium.a(_t=display_str, href=r["url"])

        # The character encoding for the email.
        CHARSET = "UTF-8"

        if dryrun:
            with open("OUT.html", "w") as f:
                f.write(str(self.airium))
            return None

        # Create a new SES resource and specify a region.
        client = boto3.client('ses', region_name=self.AWS_REGION)

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
                            'Data': str(self.airium),
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

