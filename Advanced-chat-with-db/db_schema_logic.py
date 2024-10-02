from transformers import pipeline
from sqlalchemy import create_engine, inspect

def extract_schema(db_url):
    """Extract schema from the database without accessing data."""
    engine = create_engine(db_url)
    inspector = inspect(engine)
    
    schema_info = []
    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        schema_info.append(f"Table: {table_name}")
        for column in columns:
            schema_info.append(f"  - {column['name']} ({column['type']})")
    
    return "\n".join(schema_info)

def setup_llm_chain():
    """Set up the Hugging Face model for text generation."""
    generator = pipeline('text-generation', model='gpt2')
    return generator

def generate_sql_query(chain, schema, question):
    """Generate SQL query based on the schema and question."""
    prompt = chain.prompt.format(schema=schema, question=question)
    # Adjust the text generation parameters
    result = chain.llm(prompt, max_new_tokens=50)  # Generate up to 50 new tokens
    return result
