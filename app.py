from flask import Flask, jsonify, request
import boto3
from botocore.client import Config
import botocore


app = Flask(__name__)


@app.route('/post', methods=['Post'])
def home_1():
    info = request.get_json()

    ACCESS_KEY_ID = 'AKIAXB3Y4CS3GX34M5OS'
    ACCESS_SECRET_KEY = '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'
    AWS_DEFAULT_REGION = 'ap-south-1'
    BUCKET_NAME = 'kumar775'

    data = open(info['file_path'], "rb")

    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        region_name=AWS_DEFAULT_REGION,
        config=Config(signature_version='s3v4')
    )
    s3.Bucket(BUCKET_NAME).put_object(Key=info['file_path'], Body=data)

    my_config = Config(signature_version='s3v4')
    s3_cli = boto3.client('s3', config=my_config)
    params = {"Bucket": BUCKET_NAME, "Key": info['file_path']}
    final_url = s3_cli.generate_presigned_url('get_object', params)

    return jsonify({'url': final_url})


@app.route('/get', methods=['Get'])
def home_2():

    my_config = Config(signature_version=botocore.UNSIGNED)
    s3_cli = boto3.client('s3', config=my_config)

    params = {"Bucket": 'kumar775', "Key": 'Buddha.jpg'}
    final_url = s3_cli.generate_presigned_url('get_object', params)

    return jsonify({'url': final_url})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
