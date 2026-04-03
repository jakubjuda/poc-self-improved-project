import polars as pl

def extract_data() -> pl.DataFrame:
    """Simulate extracting data from a source system."""
    data = {
        "id": [1, 2, 3],
        "raw_text": [
            "The customer was very happy with the service.",
            "Terrible experience, the product broke after one day.",
            "It's okay, nothing special but gets the job done."
        ]
    }
    return pl.DataFrame(data)
