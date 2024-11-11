import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ElasticsearchException
import os

# Elasticsearch connection
es = Elasticsearch(["http://localhost:9200"])
index_name = "cv-transcriptions"

# Load the CSV data
csv_file = "../asr/cv-valid-dev.csv"
df = pd.read_csv(csv_file)

# Define mappings for the index
mappings = {
    "properties": {
        "filename": {"type": "keyword"},
        "text": {"type": "text"},
        "up_votes": {"type": "integer"},
        "down_votes": {"type": "integer"},
        "age": {"type": "keyword"},
        "gender": {"type": "keyword"},
        "accent": {"type": "keyword"},
        "generated_text": {"type": "text"}
    }
}

# Create index with mappings if it doesn't exist
if not es.indices.exists(index=index_name):
    try:
        es.indices.create(index=index_name, body={"mappings": mappings})
        print(f"Index '{index_name}' created with mappings.")
    except ElasticsearchException as e:
        print(f"Error creating index: {e}")
        exit(1)

# Clean up the data (remove missing rows, convert fields to appropriate types)
df = df.dropna(subset=["text", "generated_text", "filename"])  # Remove rows with missing important fields
df["up_votes"] = df["up_votes"].fillna(0).astype(int)  # Fill NaN with 0 and convert to int
df["down_votes"] = df["down_votes"].fillna(0).astype(int)  # Fill NaN with 0 and convert to int

# Clean text fields to remove newlines, excess spaces, and special characters
def clean_text(text):
    return text.replace("\n", " ").replace("\r", "").strip()

df["text"] = df["text"].apply(clean_text)
df["generated_text"] = df["generated_text"].apply(clean_text)

# Index the data into Elasticsearch
def index_data(row):
    # Prepare the document for indexing, with empty fields set to None
    doc = {
        "filename": row["filename"],
        "text": row["text"],
        "up_votes": int(row["up_votes"]) if pd.notnull(row["up_votes"]) else 0,
        "down_votes": int(row["down_votes"]) if pd.notnull(row["down_votes"]) else 0,
        "age": row["age"] if pd.notnull(row["age"]) and row["age"] != "" else None,
        "gender": row["gender"] if pd.notnull(row["gender"]) and row["gender"] != "" else None,
        "accent": row["accent"] if pd.notnull(row["accent"]) and row["accent"] != "" else None,
        "generated_text": row["generated_text"]
    }
    
    # Index the document
    try:
        es.index(index=index_name, document=doc)
        print(f"Document indexed: {row['filename']}")
    except ElasticsearchException as e:
        print(f"Error indexing document '{row['filename']}': {e}")

# Iterate over the rows of the DataFrame and index them into Elasticsearch
for index, row in df.iterrows():
    index_data(row)

print("Data indexing complete.")
