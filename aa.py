# 📌 Task: Movie & TV Show Recommendation System
# 🌟 Objective:
# Create a Python application that recommends movies or TV shows to users based on their preferences, using NumPy, Pandas, CSV, SQLite, Requests, and Matplotlib.

# 🔧 Concepts Covered:
# ✅ requests - Fetch movie/TV show data from an API (e.g., TMDB API).
#  ✅ sqlite3 - Store and manage movie/show data in a local database.
#  ✅ pandas - Process and analyze user preferences.
#  ✅ numpy - Perform similarity calculations for recommendations.
#  ✅ csv - Export user history and recommendations.
#  ✅ matplotlib - Visualize movie trends and ratings.

# 📝 Task Breakdown:
# 1️⃣ Fetch Movie/TV Show Data (Using requests)
# Use the TMDB API (https://www.themoviedb.org/) to get data on:
#  ✅ Movie/show title
#  ✅ Genre
#  ✅ Ratings
#  ✅ Release date
# 2️⃣ Store Data in SQLite (Using sqlite3)
# Save user preferences and watched history in a database (movies.db).
# 3️⃣ Process & Analyze Data (Using pandas & numpy)
# Load data into a Pandas DataFrame for analysis.
# Implement a recommendation algorithm based on:
#  ✅ Genre similarity (users who like sci-fi get sci-fi recommendations).
#  ✅ Average ratings (highly rated movies recommended first).
#  ✅ Recent releases (prioritize new movies).
# 4️⃣ Export Data to CSV (Using csv & pandas)
# Save recommended movies to recommendations.csv.
# 5️⃣ Visualize Movie Trends (Using matplotlib)
# Bar chart: Show top 5 genres the user watches most.
# Pie chart: Show percentage of ratings (e.g., how many 5-star movies).
# Line graph: Show trend of movie releases per year.

import matplotlib
import requests
import pandas
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

api_key = '4351a4aeb88a636910d6de912ad3e3ae'
url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'

response = requests.get(url)
data = response.json()
 
movies = data['results']
for movie in movies:
    print(movie['title'], movie['genre_ids'], movie['vote_average'], movie['release_date'])

Base = declarative_base()
class Movies(Base):
    __tablename__="movie"
    id=Column(Integer,primary_key=True)
    title=Column(String,nullable=False)
    genre_ids=Column(Integer,nullable=False)
    average_vote=Column(Float,nullable=False)
    release_date=Column(Integer,nullable=False)

engine = create_engine('sqlite:///Recommendation.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

for movie in  movies:
    movie_entry = Movies(
        id=movie['id'],
        title=movie['title'],
        genre_ids=str(movie['genre_ids']),
        average_vote=movie['vote_average'],
        release_date=movie['release_date']
    )
    session.add(movie_entry)

session.commit()
def recommendation():
    movie_recommendation = session.query(movie_entry).filter(movie_entry.average_vote>=7).all()
    if movie_recommendation:
        for movie

session.close()