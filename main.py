import os
import shutil
import fitz
from . import create_app
import ollama
import boto3
import os

def save_file(file, file_name):
    with open(file_name, 'wb') as f:
        f.write(file.read())
        documents_dir = 'documents'

    if not os.path.exists(documents_dir):
        os.makedirs(documents_dir)
    shutil.move(file_name, os.path.join(documents_dir, file_name))


def extract_text(path):
    pdf_document = fitz.open(f'documents/{path}')
    pdf_text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        pdf_text += page.get_text()
    return pdf_text


app, _ = create_app()

if __name__ == '__main__':
    app.run(debug=True)


def ollama_interaction(text, question):
    client = ollama.Client()
    model = "llama3:latest"
    if text == "":
        prompt = f"Question: {question}\nRéponse:"
    else :
        prompt = f"Texte: {text}\nQuestion: {question}\nRéponse:"
    result = client.generate(model=model, prompt=prompt)
    return result['response']

def s3_client():
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID', '')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY', '')
    s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    return s3_client


def get_s3_file(document_name, client):
    response = client.get_object(Bucket='privategpt-docs', Key=document_name)
    return response['Body']

def global_launch():
  client = s3_client()
  file = get_s3_file('test.pdf', client)
  save_file(file, 'test.pdf')
  texte = extract_text('test.pdf')
  response = ollama_interaction(texte, 'Quelle est la capitale de la France ?')