import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv("ENDPOINT-DOC-INT")
    KEY = os.getenv("KEY")
    AZURE_ST_CONNECTION_STRING = os.getenv("STORAGE-CONNECTION-STRING")
    CONTAINER = os.getenv("CONTAINER-NAME")

