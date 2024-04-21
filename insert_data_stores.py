import csv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from database_setup import Base, Stores, Products
import pandas as pd

# Define your declarative base
Base = declarative_base()

# Define your Stores and Products classes here

# Buat koneksi ke database
engine = create_engine('postgresql+psycopg2://postgres:hanif123456@localhost:5432/bukalapak')
Base.metadata.bind = engine

# Buat sesi
DBSession = sessionmaker(bind=engine)
session = DBSession()

# class Store(Base):
#     __tablename__ = 'stores'

#     store_id = Column(Integer, primary_key=True)
#     store_name = Column(String, nullable=False)
#     store_city = Column(String, nullable=False)
#     positive_feedback = Column(Integer, nullable=False)
#     total_feedback = Column(Integer, nullable=False)

# Base.metadata.create_all(engine)

# Load the CSV file into a DataFrame
df_stores = pd.read_csv('D:\Career\QWork\chatgpt\stores.csv', delimiter=';')

for index, row in df_stores.iterrows():
    # Extract values from the row
    store_name = row['Store Name']
    store_city = row['Store City']
    positive_feedback = row['Positive Feedback']
    total_feedback = row['Total Feedback']
    
    # Create a new Stores object and add it to the session
    store = Stores(store_name=store_name, store_city=store_city, positive_feedback=positive_feedback, total_feedback=total_feedback)
    session.add(store)

# Commit the session to save changes to the database
session.commit()

# Close the session
session.close()