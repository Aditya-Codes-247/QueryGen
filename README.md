# QueryGen 

## Project Overview
Our project comprises of an advanced online SQL query generator that leverages state-of-the-art machine learning techniques to simplify SQL query creation. We fine-tuned a pre-trained BERT model using the WikiSQL and Spider datasets for DML commands. Additionally, we created a custom dataset for DDL commands through web scraping (link to custom DDL dataset). We also employed transfer learning to enhance model performance.

## Backend Technologies
The backend of the project is built using the following technologies:

- **FastAPI**: For building the API.
- **Uvicorn**: ASGI server for serving FastAPI applications.
- **Google Speech Recognition**: For converting speech to text.
- **Pytesseract**: For extracting text from images.
- **Torch**: For handling machine learning models.
- **Pydantic**: For data validation.
- **Transformers**: For implementing BERT.
- **Text-Preprocessing**: For preprocessing text data.
- **Routers**: For organizing the API endpoints.
- **Pydub**: For audio processing.

## Frontend Features
The frontend of the project is designed to provide a seamless and engaging user experience. Key features include:

- **SVG Animations**: Eye-catching animations to enhance visual appeal.
- **Smooth Navigation**: Intuitive and fluid navigation to improve usability.

## Setting Up the Project

### Prerequisites
Make sure you have the following installed on your system:
- Python 3.7+
- pip

### Steps to Set Up

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aditya-Codes-247/QueryGen.git
   cd QueryGen
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the trained ML models:**
   Place the models in the designated directory as mentioned in the repository.

4. **Run the FastAPI application:**
   ```bash
   uvicorn main:app --reload
   ```

5. **API Testing:**
   Use Curl or any other API testing tool to test the endpoints.

```

With this setup, you'll be able to deploy and test our sophisticated SQL query generator on your local machine, utilizing cutting-edge machine learning models and an intuitive, animated frontend interface.
