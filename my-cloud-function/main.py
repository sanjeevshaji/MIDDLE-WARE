from firebase_admin import credentials, storage, initialize_app
from queue import Queue

cred = credentials.Certificate("./smarthire-285b9-firebase-adminsdk-frtth-fee212ac40.json")
initialize_app(cred, {"storageBucket": "smarthire-285b9.appspot.com"})
bucket = storage.bucket()

def download_files():
    queue = Queue()
    blobs = bucket.list_blobs()

    for blob in blobs:
        queue.put(blob)

    while not queue.empty():
        blob = queue.get()
        destination_path = f"./{blob.name}"
        blob.download_to_filename(destination_path)

    print(f"Documents downloaded from Firebase Storage and saved to {destination_path}.")

download_files()
