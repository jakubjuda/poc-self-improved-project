import duckdb
import polars as pl
from src.config import settings

def load_data(df: pl.DataFrame) -> None:
    """Load Polars DataFrame into DuckDB."""
    conn = duckdb.connect(settings.db_path)
    
    # Register Polars DataFrame as a virtual table in DuckDB
    conn.register("df_view", df)
    
    # Create table if it doesn't exist
    conn.execute('''
        CREATE TABLE IF NOT EXISTS sentiment_analysis AS 
        SELECT * FROM df_view WHERE 1=0
    ''')
    
    # Insert new records (Idempotent-ish for POC)
    conn.execute('''
        INSERT INTO sentiment_analysis 
        SELECT * FROM df_view 
        WHERE id NOT IN (SELECT id FROM sentiment_analysis)
    ''')
    
    print(f"\n[SUCCESS] Data successfully loaded into {settings.db_path}")
    
    # Verify and display
    result = conn.execute("SELECT * FROM sentiment_analysis").df()
    print("\n--- Current DuckDB State ---")
    print(result)
    print("----------------------------\n")
    
    conn.close()
