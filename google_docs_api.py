from google.oauth2 import service_account
from googleapiclient.discovery import build

# Initialize Google Docs service
def init_google_docs_service():
    SCOPES = ['https://www.googleapis.com/auth/documents']
    SERVICE_ACCOUNT_FILE = 'path/to/your/credentials.json'  # Redacted for public repo

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build('docs', 'v1', credentials=credentials)
    return service

# Create a new Google Doc
def create_google_doc(title, content):
    service = init_google_docs_service()
    body = {'title': title}
    doc = service.documents().create(body=body).execute()
    doc_id = doc.get('documentId')

    # Insert content into the document
    requests = [
        {
            'insertText': {
                'location': {'index': 1},
                'text': content
            }
        }
    ]
    service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()

    doc_url = f"https://docs.google.com/document/d/{doc_id}/edit"
    return doc_url
