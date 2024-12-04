from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from pypdf import PdfReader
import os
from docx import Document
import subprocess

app = Flask(__name__)

@app.route('/extract-text-doc', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        temp_path = os.path.join('/tmp', file.filename)
        file.save(temp_path)

        try:
            if file.filename.endswith('.docx'):
                text = extract_text_from_docx(temp_path)
            elif file.filename.endswith('.doc'):
                text = extract_text_from_doc(temp_path)
            else:
                os.remove(temp_path)
                return jsonify({'error': 'Unsupported file type. Only .doc and .docx files are supported.'}), 400

            os.remove(temp_path)  # Clean up the file
            return jsonify({'text': text}), 200
        except Exception as e:
            os.remove(temp_path)
            return jsonify({'error': str(e)}), 500

def extract_text_from_docx(filepath):
    """Extract text from a .docx file."""
    doc = Document(filepath)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

def extract_text_from_doc(filepath):
    """Convert .doc to .docx and extract text."""
    try:
        # Generate a new .docx file path
        converted_path = filepath + '.docx'
        # Convert using unoconv
        subprocess.run(['unoconv', '-f', 'docx', '-o', converted_path, filepath], check=True)

        # Extract text from the converted .docx
        text = extract_text_from_docx(converted_path)
        os.remove(converted_path)  # Clean up the converted file
        return text
    except Exception as e:
        raise Exception(f"Failed to process .doc file: {e}")


@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the file to a temporary location
    temp_path = os.path.join('/tmp', file.filename)
    file.save(temp_path)

    try:
        # Create PdfReader object and extract text
        reader = PdfReader(temp_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        
        # Return extracted text as JSON response
        return jsonify({"text": text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Clean up: delete the temp file
        os.remove(temp_path)

if __name__ == "__main__":
    app.run(debug=True)
