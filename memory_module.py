# memory_module.py
# Public-safe version — Supabase memory logging

import os
import datetime
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL", "<YOUR_SUPABASE_URL>")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "<YOUR_SUPABASE_API_KEY>")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_conversation(username, content, entry_type="conversation", tags=None):
    data = {
        "username": username,
        "content": content,
        "entry_type": entry_type,
        "timestamp": datetime.datetime.now().isoformat(),
        "tags": tags or []
    }
    response = supabase.table("conversations").insert(data).execute()
    print("Saved conversation:", response)

def save_file(username, filename, file_url, tags=None):
    data = {
        "username": username,
        "filename": filename,
        "file_url": file_url,
        "timestamp": datetime.datetime.now().isoformat(),
        "tags": tags or []
    }
    response = supabase.table("files").insert(data).execute()
    print("Saved file:", response)
