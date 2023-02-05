import os
from newsapi import NewsApiClient
from SESEmailer import SESEmailer
from S3Uploader import S3Uploader

def lambda_handler(event, context):
    # Init
    news_api_key = os.environ.get('NEWS_API_KEY')
    newsapi = NewsApiClient(api_key=news_api_key)

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(country='us')

    uploader = S3Uploader()

    uploader.upload_report(top_headlines)

    emailer = SESEmailer(
        "Charlie <news@charliebushman.com>",
        "ctbushman@gmail.com",
        "ConfigSet",
        "us-east-1",
    )

    email_ret_code = emailer.send_email(top_headlines)

    return { 
        'email_ret_code' : email_ret_code,
        'top_headlines' : top_headlines,
    }