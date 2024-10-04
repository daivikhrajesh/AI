# SQL Query Generator with Retrieval-Augmented Generation (RAG)

This project is a Retrieval-Augmented Generation (RAG) application that generates SQL queries based on a provided database schema and a user question. It uses a transformer-based model to generate queries without requiring an OpenAI API key, making it completely free to use.

## Features
- Automatically extracts schema information from a database.
- Generates SQL queries based on user-provided questions and the extracted schema.
- Powered by a transformer model (`gpt2`) for generating the SQL queries.
- Fully functional with Streamlit as the user interface.

## Project Structure

```
Advanced-chat-with-db
    ├── app.py                    # Main Streamlit application file
    ├── db_schema_logic.py         # Logic for extracting schema and generating SQL queries
    ├── new.db                     # SQLite database file
    ├── Readme.md                  # Project documentation
    └── requirements.txt           # Project dependencies
```

## Installation

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/daivikhrajesh/AI/tree/main/Advanced-chat-with-db.git
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment (optional but recommended).

```bash
# For Windows:
python -m venv venv
venv\Scripts\activate

# For macOS/Linux:
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Prepare the Database

Make sure you have an SQLite database (or modify the code to use a different one) in the root directory. The provided database file (`new.db`) is used for the application. You can replace it with your own.

### 5. Run the Application

To run the Streamlit application:

```bash
streamlit run app.py
```

## Usage

1. **Schema Extraction**: The app will automatically extract the schema from the provided database and display it.
2. **Query Generation**: Input your question about the database (e.g., "Select all users from the Users table"), and the transformer model will generate a corresponding SQL query.
3. **View SQL**: The generated SQL query will be shown in the app, ready for you to execute in your database environment.


## Technologies Used

- **Python**: Programming language used for the backend logic.
- **Streamlit**: Framework used to create the user interface.
- **Transformers (Hugging Face)**: Model used to generate SQL queries.
- **SQLite**: Database used for schema extraction and testing.
- **SQLAlchemy**: ORM used to interact with the database.

## Modifications

This project originally required an OpenAI API key, but it has been modified to use a free transformer (`gpt2`) to avoid API costs and make it more accessible. The model generates queries based on the extracted schema and user input.

## Future Improvements

- Enhance SQL generation accuracy by fine-tuning the transformer model.
- Add support for additional databases beyond SQLite.
- Improve UI for more user-friendly interactions.
- Add validation of generated SQL queries before displaying them.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

If you would like to contribute to this project, feel free to open a pull request or issue on GitHub. Contributions are always welcome!

---

Feel free to customize the `README.md` file further, especially under the "Contributing" section or the repository link, based on your needs. 
