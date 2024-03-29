# allnews
Daily email report of top headlines from a range news sources

## Setup

This is designed to be run on an AWS lambda function with Python runtime. It uses newsapi-python, boto3, and airium.

```bash
git clone https://github.com/Ulthran/allnews.git
cd allnews/
mkdir package/
pip install --target package/ newsapi-python
./generate-archive.sh
```

Then upload the .zip file to a lambda function (add the NEWS_API_KEY env variable and policies to allow it to use SES and S3, maybe someday I'll add a CloudFormation template).

You'll also need to verify whatever domain/email addresses you use for sending (and receiving if you're sandboxed) emails.

## Usage

Add a trigger to the function to run daily (or at whatever increment you want).

## Dev stuff

Use `SESEmailer`'s `dryrun` flag to not send the email and just print HTML.

Use `python test_html.py` to run test set with `dryrun` flag.

Install a new package to `package/` with `pip install --target package/ package_name`