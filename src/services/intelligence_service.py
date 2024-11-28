from certifi.core import contents
from utils.config import Config
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

def analise_card(file_url):
    try:
        credential = AzureKeyCredential(Config.KEY)
        doc_intelligence_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)
        url_request = AnalyzeDocumentRequest(url_source=file_url)
        card_info = doc_intelligence_client.begin_analyze_document("prebuilt-creditCard", url_request)
        result = card_info.result()

        for doc in result.documents:
            fields = doc.get('fields', {})
            return {
                "card_name": fields.get('CardHolderName', {}).get('content'),
                "card_number": fields.get('CardNumber', {}).get('content'),
                "expiry_date": fields.get('ExpirationDate', {}).get('content'),
                "bank_name": fields.get('IssuingBank', {}).get('content')
            }

    except Exception as e:
        raise Exception(e)
