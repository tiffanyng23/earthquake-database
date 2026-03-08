from api import usgs_api
import pandas as pd
from sqlalchemy import create_engine,text

# create database
engine = create_engine("sqlite:///earthquakes.db")
#create earthquakes table where earthquake id is a primary key
with engine.connect() as conn:
    conn.execute(text('''
        CREATE TABLE IF NOT EXISTS earthquakes (
            id TEXT PRIMARY KEY,
            time TEXT,
            place TEXT,
            magnitude FLOAT,
            longitude FLOAT,
            latitude FLOAT,
            depth FLOAT
        )
    '''))

def main():
    #insert new data
    add_data()
    #Sample query for data
    print(pd.read_sql("SELECT COUNT(*) FROM earthquakes WHERE magnitude > 6", engine))


def add_data():
    # extract dataframe from usgs api call
    df = usgs_api()
    #convert to dictionary - orient in records form [{one earthquakes data}, {next earthquake data}]
    records = df.to_dict(orient="records")

    #insert new data to earthquake database, ignore data already in df - check using primary key
    with engine.begin() as conn:
        conn.execute(text("""
                INSERT OR IGNORE INTO earthquakes
                (id, time, place, magnitude, longitude, latitude, depth)
                VALUES(:id, :time, :place, :magnitude, :longitude, :latitude, :depth)
        """),
        records
        )

if __name__=="__main__":
    main()






