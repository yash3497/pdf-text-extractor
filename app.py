from flask import Flask, request, jsonify
from pypdf import PdfReader
import os

app = Flask(__name__)

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
