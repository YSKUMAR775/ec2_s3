from flask import Flask, jsonify
import boto3
from botocore.client import Config
import botocore

new_app = Flask('__name__')


@new_app.route('/get_urls', methods=['Get'])
def tot_get():

    ACCESS_KEY_ID = 'AKIAXB3Y4CS3GX34M5OS'
    ACCESS_SECRET_KEY = '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'
    AWS_DEFAULT_REGION = 'ap-south-1'

    s3_client = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        region_name=AWS_DEFAULT_REGION,
        config=Config(signature_version='s3v4')
    )
    my_bucket = s3_client.Bucket('kumar775')

    list_url = []
    for file in my_bucket.objects.all():
        a = file.key
        # print(a)

        my_config = Config(
            signature_version=botocore.UNSIGNED)  # instead of botocore.UNSIGNED use 's3v4' for better url
        s3_cli = boto3.client('s3', config=my_config)

        params = {"Bucket": 'kumar775', "Key": a}
        url = s3_cli.generate_presigned_url('get_object', params, ExpiresIn=3600)
        # print({a: url})

        list_url.append({a: url})

    return jsonify(list_url)


if __name__ == '__main__':
    new_app.run(host='0.0.0.0')
