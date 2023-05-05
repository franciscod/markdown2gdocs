"""helpers for interacting with the google docs api"""

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/documents"]


def get_service():
    creds = service_account.Credentials.from_service_account_file(
        "service_account.json", scopes=SCOPES
    )
    return build("docs", "v1", credentials=creds)


def get_doc(service, doc_id):
    return service.documents().get(documentId=doc_id).execute()


def do_batchupdate(service, doc, reqs):
    return (
        service.documents()
        .batchUpdate(documentId=doc["documentId"], body={"requests": reqs})
        .execute()
    )


def reqs_for_text(si, text):
    yield {
        "insertText": {
            "location": {
                "index": si,
            },
            "text": text,
        }
    }


def reqs_for_heading_style(si, text, level):
    yield {
        "updateParagraphStyle": {
            "range": {"startIndex": si, "endIndex": si + len(text) - 1},
            "paragraphStyle": {
                "namedStyleType": f"HEADING_{level}",
            },
            "fields": "namedStyleType",
        }
    }


def reqs_clear_doc(doc):
    ei = doc["body"]["content"][-1]["endIndex"] - 1
    if ei > 1:
        yield {
            "deleteContentRange": {
                "range": {
                    "startIndex": 1,
                    "endIndex": ei,
                }
            }
        }
