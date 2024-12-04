# PDF Text Extraction API

A simple API to extract text from PDF files using Flask and PyPDF. This tool allows you to upload a PDF file and retrieve the text content from it.

## Publisher

- **Publisher Name**: Yash Gupta
- **Company Name**: CodeXcelerate
- **Website**: [www.codexcelerate.me](http://www.codexcelerate.me)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
  - [Install Dependencies](#install-dependencies)
  - [Run Locally](#run-locally)
- [API Endpoints](#api-endpoints)
  - [POST /extract-text](#post-extract-text)
- [Deployment](#deployment)
  - [Deploy on Vercel](#deploy-on-vercel)
- [Contributing](#contributing)
- [License](#license)

## Overview

The **PDF Text Extraction API** is a Python-based RESTful API that uses Flask to handle HTTP requests and **PyPDF** to extract text from PDF files. This tool is perfect for anyone needing to extract readable text from PDF documents without manual processing.

## Features

- **Text Extraction**: Upload a PDF file and extract its text.
- **Simple API**: Easy-to-use HTTP endpoint for integrating with other applications or services.
- **No dependencies for PDF parsing**: Uses `PyPDF` to handle text extraction from PDFs.

## Tech Stack

- **Flask**: Web framework for building the API.
- **PyPDF**: Python library for reading and extracting text from PDF files.
- **Vercel**: Hosting platform for deploying the API as a serverless function.

## Setup

### Install Dependencies

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yash3497/pdf-text-extractor.git
   cd pdf-text-extraction-api
   ```

2. **Create and activate a virtual environment**:
   For macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   For Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Run Locally

To run the Flask app locally:

```bash
python app.py
```

This will start the server on `http://127.0.0.1:5000`.

## API Endpoints

### POST /extract-text

This endpoint accepts a PDF file and returns the extracted text.

**Request**:

- **URL**: `/extract-text`
- **Method**: `POST`
- **Form data**: 
  - `file`: The PDF file to extract text from (must be a valid PDF).

**Example Request** (using `curl`):

```bash
curl -X POST -F "file=@path/to/your/file.pdf" http://127.0.0.1:5000/extract-text
```

**Response**:

- **Status Code**: `200 OK` (if the text extraction is successful)
- **Response Body**:
  ```json
  {
    "text": "Extracted text from the PDF"
  }
  ```

If there's an error (e.g., no file is provided or an invalid PDF is uploaded), the API will respond with an appropriate error message.

## Deployment

### Deploy on Vercel

1. **Install Vercel CLI**:
   If you don't have Vercel CLI installed, run the following command:
   ```bash
   npm install -g vercel
   ```

2. **Deploy the application**:
   - Run the following command inside the project folder:
     ```bash
     vercel
     ```
   - Follow the prompts to configure the project.
   - Vercel will deploy your application and provide a public URL for accessing the API.

   After deployment, you can use the API with the provided Vercel URL.

### Example cURL Request to Deployed API:

```bash
curl -X POST -F "file=@path/to/your/file.pdf" https://your-vercel-url.vercel.app/extract-text
```

## Contributing

We welcome contributions to improve the project. If you'd like to contribute, please fork the repository, create a new branch, and submit a pull request.

### How to Contribute

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Additional Notes

- **Error Handling**: The API includes basic error handling to catch missing files or invalid PDFs.
- **Production**: For production use, you may want to enhance error handling, add authentication, or use a cloud storage solution for file uploads.