# USGS Earthquake Database
A SQLite3 database containing earthquake events extracted from the USGS Earthquake API. Earthquake events are pulled daily, forming a database that records earthquake events from 2026-02-05 21:24:56 EST onwards. Earthquake insights regarding datetime, place, magnitude, coordinates, and depth can be gathered through SQL queries.

### api.py
Contains the code used for the API call and to convert time to the datetime format and in my local timezone (EST).

### database.py
Contains the code used to create the database and table and to insert new earthquake events. Each API call will pull earthquakes from the past week, but this is automated to be performed daily to ensure no earthquake events are missed. Earthquakes already in the database will be ignored - this is determined by the id primary key (which is a unique earthquake code for each earthquake listed in the USGS API).

### pipeline.py
Contains the script to automate the process of performing the API call to pull the data, and to insert new earthquakes into the earthquakes table. This program combines the code from api.py and database.py

## How to Use this Project
1. Clone the repository.
2. Set up a Python virtual environment.
3. Install the packages listed in requirements.txt.
4. Run database.py to create the earthquakes.db and earthquakes table, and to insert earthquake events onto the table.
5. Automate the API call and data insertion using the pipeline.py script. Use cron to schedule the script to run once per day.

### License
[![License: MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
