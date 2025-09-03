import os
from dotenv import load_dotenv
from supabase import create_client, Client

def get_client() -> Client:
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    if not url or not key:
        raise RuntimeError("Missing SUPABASE_URL or SUPABASE_KEY in .env")
    return create_client(url, key)

def main():
    supabase = get_client()

    # Example: get only games released in 2017
    response_2017 = supabase.table("nintendo_games") \
    .select("title, platform, release_year") \
        .eq("release_year", 2017) \
        .execute()
    print("2017 games:", response_2017.data)

    # Replace "your_table" with a real table in your Supabase project
    # For demo purposes: SELECT * LIMIT 5
    response = supabase.table("nintendo_games").select("*").limit(5).execute()

    # response.data is a list of dict rows
    print("Rows:")
    for row in response.data:
        print(row)

if __name__ == "__main__":
    main()