import requests
import json
import pandas as pd

def usgs_api():
    '''Perform API call to extract USGS earthquake data and convert to a dataframe.'''
    try:
        url = f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"
        response = requests.get(url)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
    except requests.exceptions.HTTPError as httperror:
        print(http_error)
    except requests.exceptions.RequestException as error:
        print(error)

    if response.status_code == 200:
        json_data = response.json()["features"]
        
    #dataframe categories
    data = []
    # list of dictionaries, loop through each dictionary/event 
    for event in json_data:
        eq_event = {"id" : event["properties"]["code"],
                    "time" : event["properties"]["time"],
                    "place": event["properties"]["place"],
                    "magnitude": event["properties"]["mag"],
                    "longitude": event["geometry"]["coordinates"][0],
                    "latitude": event["geometry"]["coordinates"][1],
                    "depth": event["geometry"]["coordinates"][2],
        }
        data.append(eq_event)
    
    df = pd.DataFrame(data)
    # convert time to datetime format in EST time zone
    df["time"] = pd.to_datetime(df["time"], unit="ms", errors="coerce")
    df["time"] = df["time"].dt.tz_localize('UTC').dt.tz_convert('America/Toronto')
    df["time"] = df["time"].dt.strftime("%Y-%m-%d %H:%M:%S")

    return df


if __name__ == "__main__":
    df = usgs_api()
    print(df.head())

