import sqlite3
import uuid
import datetime

def get_connection():
    conn = sqlite3.connect("scrap_data.db", check_same_thread=False)
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scraping_id TEXT,
            description TEXT,
            article TEXT,
            address TEXT,
            price TEXT,
            img_link TEXT,
            downloaded_at DATE
        )
    """)
    conn.commit()
    conn.close()

def save_to_db(df):
    conn = sqlite3.connect("scraped_data.db")
    scraping_id = str(uuid.uuid4()) #create unique id of scraping
    df['donwloaded_at'] = datetime.datetime.now()
    df['scraping_id'] = scraping_id
    df.to_sql("products", conn, if_exists="append", index=False)
    conn.close()
