# s3-ppms-file-trigger-integrateio-api-example

## Pre-requsites
- S3 bucket
- AWS Python 3.7 Lambda Function
- AWS Trigger installed on the Lambda function (in Triggers for the Lambda function) set to Trigger on Object PUT (this is what s3 uses even tho you'd think it'd be POST)
- Use the pre-fab AWS defaults for a new Role.
- An existing Xplenty package and it's ID to Trigger, along with a Package Variable for the filename, I'm using UPLOADED_FILENAME in my Xplenty Package, so that is what I pass in the payload in the Lambda function.

## Usage
Change out YOUR_API_KEY and YOUR_PACKAGE_ID_HERE as noted.
