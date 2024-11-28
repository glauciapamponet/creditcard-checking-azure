import os
import streamlit as st
from utils.config import Config
from azure.storage.blob import BlobServiceClient

def upload_blob(file, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_ST_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER, blob=file_name)
        blob_client.upload_blob(file)
        return blob_client.url
    except Exception as e:
        st.error(f'Erro ao enviar o arquivo ao blob storage: {e}')
        return None
