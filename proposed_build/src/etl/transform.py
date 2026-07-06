import os
import polars as pl
from litellm import completion
from src.config import settings

def analyze_sentiment(text: str) -> str:
    """Use vendor-neutral LLM to analyze sentiment."""
    # Fallback for zero-config POC runs without API keys
    if not any(k.endswith('_API_KEY') for k in os.environ):
        return "MOCK_SENTIMENT"
        
    try:
        response = completion(
            model=settings.llm_model,
            messages=[
                {"role": "system", "content": "You are a sentiment analysis bot. Reply ONLY with POSITIVE, NEGATIVE, or NEUTRAL."},
                {"role": "user", "content": text}
            ],
            temperature=0.0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"LLM Error: {e}")
        return "ERROR"

def transform_data(df: pl.DataFrame) -> pl.DataFrame:
    """Process data with Polars and enrich with LLM."""
    # In a production system, use async or batching for LLM calls.
    # For this POC, we apply synchronously.
    sentiments = [analyze_sentiment(text) for text in df["raw_text"].to_list()]
    
    return df.with_columns(
        pl.Series("sentiment", sentiments),
        pl.lit(settings.llm_model).alias("processed_by_model")
    )
