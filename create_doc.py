from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/documents']

def get_credentials():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def create_document(title, content):
    creds = get_credentials()
    service = build('docs', 'v1', credentials=creds)
    
    document = service.documents().create(body={'title': title}).execute()
    document_id = document.get('documentId')

    requests = [
        {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': content
            }
        }
    ]

    service.documents().batchUpdate(
        documentId=document_id, body={'requests': requests}).execute()

    print(f'Created document with ID: {document_id}')
    return document_id

if __name__ == '__main__':
    create_document('Automated Document', 'This is an automated Google Doc.')