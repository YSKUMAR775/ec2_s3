from flask import Flask, jsonify, request
import boto3
from botocore.client import Config

app = Flask(__name__)


@app.route("/sai", methods=['Post'])
def home_1():
    info = request.get_json()

    ACCESS_KEY_ID = 'AKIAXB3Y4CS3GX34M5OS'
    ACCESS_SECRET_KEY = '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'
    BUCKET_NAME = 'kumar775'

    # data = open("C:/Users/Hemanth Y/Desktop/Ganesh.jpg", 'rb')
    data = open(info['path'], "rb")

    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )

    s3.Bucket(BUCKET_NAME).put_object(Key='Lord_Ganesh.jpg', Body=data)

    base_url = 'https://kumar775.s3.ap-south-1.amazonaws.com/'
    file_name = 'Lord_Ganesh.jpg'
    final_url = base_url + file_name

    return jsonify({'url': final_url})


@app.route("ias", methods=['Get'])
def home_2():

    base_url = 'https://kumar775.s3.ap-south-1.amazonaws.com/'
    file_name = 'Buddha.jpg'
    final_url = base_url + file_name

    return jsonify({'my_url': final_url})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
