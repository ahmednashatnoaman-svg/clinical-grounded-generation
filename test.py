import sys
sys.path.append(".")
import config
from ingest import load_pdfs, chunk_documents, build_index
from query import retrieve

pages = load_pdfs(config.DATA_DIR)
chunks = chunk_documents(pages)
vectordb = build_index(chunks)

question = "What is the recommended screening interval for breast cancer in average-risk women?"
results = retrieve(vectordb, question, k=3)
if results:
    print(results[0][1])
