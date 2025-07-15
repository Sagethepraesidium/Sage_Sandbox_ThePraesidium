
from memory_module import save_conversation, save_file
from google_docs_api import create_google_doc

def log_milestone_and_create_doc(username, content, tags=None):
    # 1. Save to Supabase
    save_conversation(username, content, "milestone", tags)

    # 2. Create Google Doc
    doc_url = create_google_doc("Milestone Log", content)

    # 3. Register Google Doc in files table
    save_file(username, "Milestone Log", doc_url, tags)

    print("Milestone saved and doc created:", doc_url)

if __name__ == "__main__":
    # Sample usage
    log_milestone_and_create_doc("philip", "This is a test milestone log from orchestrator.", ["test", "milestone"])
