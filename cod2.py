import boto3
import os
from datetime import datetime
import shutil

def upload_to_s3(file_path, bucket_name, s3_key):
    s3 = boto3.client('s3')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Fișierul {file_path} nu există.")

    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"{file_path} a fost urcat în S3 bucket '{bucket_name}' ca '{s3_key}'")
    except Exception as e:
        print(f"Eroare la urcarea fișierului: {e}")

if __name__ == "__main__":
    original_file_name = "output.log"

    if not os.path.exists(original_file_name):
        raise FileNotFoundError(f"Fișierul {original_file_name} nu există.")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    renamed_file = f"output_{timestamp}.log"

    shutil.copyfile(original_file_name, renamed_file)

    bucket = "tudoriliebucket"
    s3_key = f"outputs/{renamed_file}"

    upload_to_s3(renamed_file, bucket, s3_key)
