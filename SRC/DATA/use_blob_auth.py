import os
import uuid

from azure.identity import DefaultAzureCredential

# Import the client object from the SDK library
from azure.storage.blob import BlobClient

credential = DefaultAzureCredential()

# Retrieve the storage blob service URL, which is of the form
# https://<your-storage-account-name>.blob.core.windows.net/
storage_url = "https://timemngmt.blob.core.windows.net/time-management"

# Create the client object using the storage URL and the credential
blob_client = BlobClient(
    storage_url,
    container_name="time-management",
    blob_name=f"consultant-time-entry-{str(uuid.uuid4())[0:5]}.txt",
    credential=credential,
)

# Open a local file and upload its contents to Blob Storage
with open("./consult_time_tracking_report.txt", "rb") as data:
    blob_client.upload_blob(data)
    print(f"Uploaded consult_time_tracking_report.txt to {blob_client.url}")

