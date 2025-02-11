import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="digital_media_store",
        user=os.environ['postgres'],
        password=os.environ['postgres'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Insert database operations here that aren't covered in the create database tables script digitalmediastore.sql.

conn.commit()

cur.close()
conn.close()
