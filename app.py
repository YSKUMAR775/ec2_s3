from flask import Flask, jsonify, request
import boto3
from botocore.client import Config


app = Flask(__name__)


@app.route('/post', methods=['Post'])
def home_1():
    info = request.get_json()

    ACCESS_KEY_ID = 'AKIAXB3Y4CS3GX34M5OS'
    ACCESS_SECRET_KEY = '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'
    BUCKET_NAME = 'kumar776'

    # data = open('Buddha.jpg', 'rb')
    # data = open('C:/Users/Hemanth Y/Desktop/Buddha.jpg', "rb")
    # info = Path('C:/Users/Hemanth Y/Desktop/Ganesh.jpg')

    data = open(info['file_path'], 'rb')

    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )

    s3.Bucket(BUCKET_NAME).put_object(Key='Ganesh_1.jpg', Body=data)

    base_url = 'https://kumar776.s3.ap-south-1.amazonaws.com/'
    file_name = 'Ganesh_1.jpg'
    final_url = base_url + file_name

    return jsonify({'url': final_url})


@app.route('/get', methods=['Get'])
def home_2():
    base_url = 'https://kumar776.s3.ap-south-1.amazonaws.com/'
    file_name = 'Ganesh_1.jpg'
    final_url = base_url + file_name

    return jsonify({'url': final_url})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
