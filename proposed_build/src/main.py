import os
from dotenv import load_dotenv
from src.etl.extract import extract_data
from src.etl.transform import transform_data
from src.etl.load import load_data

def main():
    load_dotenv()
    print("Starting Vendor-Neutral LLM ETL Pipeline...\n")
    
    print("1. Extracting data...")
    df = extract_data()
    print(df)
    
    print("\n2. Transforming data (LLM Enrichment)...")
    if not any(k.endswith('_API_KEY') for k in os.environ):
        print("WARNING: No API keys found in environment. Using mock LLM responses.")
        print("To use real models, add OPENAI_API_KEY, ANTHROPIC_API_KEY, etc. to a .env file.")
        
    transformed_df = transform_data(df)
    print(transformed_df)
    
    print("\n3. Loading data into DuckDB...")
    load_data(transformed_df)
    
    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
