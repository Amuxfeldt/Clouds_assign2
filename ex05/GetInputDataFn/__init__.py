# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from azure.storage.blob import BlobServiceClient

def main(name: str) -> str:
    connection_string = "DefaultEndpointsProtocol=https;AccountName=clouds05;AccountKey=2IjbZs71qfA4QMY2jKuEdxLeCiKyILeE4MivQOYAIH2H4auvZZsFOOFahQpC7Y+8Z+VCM/G1EWSo+AStDuwy/g==;EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    #download
    container_client = blob_service_client.get_container_client(container="blob05")

    text = []
    for i in range(1,5):
        filename = f'mrinput-{i}.txt'
        myfile = container_client.download_blob(filename).readall()
        text += myfile.decode("utf-8").replace('\r', '').split("\n")

    return text
