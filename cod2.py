import boto3
import os

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
    file_name = "output.log"
    bucket = "numele-tau-bucket"
    s3_key = f"rapoarte/{file_name}"

    upload_to_s3(file_name, bucket, s3_key)
