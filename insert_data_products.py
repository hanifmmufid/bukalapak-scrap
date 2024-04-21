import csv
from sqlalchemy import create_engine, Column, Integer, String, Float, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from database_setup import Base, Stores, Products
import pandas as pd

# Define your declarative base
Base = declarative_base()

# Buat koneksi ke database
engine = create_engine('postgresql+psycopg2://postgres:hanif123456@localhost:5432/bukalapak')
Base.metadata.bind = engine

# Buat sesi
DBSession = sessionmaker(bind=engine)
session = DBSession()

# class Stores(Base):  # Pastikan Anda sudah mendefinisikan kelas Stores
#     __tablename__ = 'stores'

#     store_id = Column(Integer, primary_key=True)
#     store_name = Column(String, nullable=False)
#     store_city = Column(String, nullable=False)
#     positive_feedback = Column(Integer, nullable=False)
#     total_feedback = Column(Integer, nullable=False)

# class Products(Base):
#     __tablename__ = 'products'

#     product_id = Column(Integer, primary_key=True)
#     title = Column(String, nullable=False)
#     reviews = Column(Integer, nullable=False)
#     sold = Column(Float, nullable=False)
#     original_price = Column(Integer, nullable=False)
#     description = Column(String, nullable=False)
#     product_url = Column(String, nullable=False)
#     brand_category = Column(String)
#     material_casing_category = Column(String)
#     underglow_rgb = Column(Enum('underglow_rgb_enum', 'Yes', 'No', name='underglow_rgb_enum'))
#     south_facing_rgb_switch = Column(Enum('south_facing_rgb_switch_enum', 'Yes', 'No', name='south_facing_rgb_switch_enum'))
#     hot_swappable_5_pin = Column(Enum('hot_swappable_5_pin_enum', 'Yes', 'No', name='hot_swappable_5_pin_enum'))
#     compatibility_with_mechanical_switch = Column(String)
#     magic_fn_key = Column(Enum('magic_fn_key_enum', 'Yes', 'No', name='magic_fn_key_enum'))
#     software_customization = Column(Enum('software_customization_enum', 'Yes', 'No', name='software_customization_enum'))
#     keycap_profile = Column(String)
#     color_options = Column(String)
#     switch_options = Column(String)
#     keyboard_layout = Column(String)
#     number_of_keys = Column(Float)
#     dimensions_length_mm = Column(Float)
#     dimensions_width_mm = Column(Float)
#     dimensions_height_mm = Column(Float)
#     weight_grams = Column(Float)
#     pre_lubed_stabilizer = Column(Enum('pre_lubed_stabilizer_enum', 'Yes', 'No', name='pre_lubed_stabilizer_enum'))
#     include_damper_foam = Column(Enum('include_damper_foam_enum', 'Yes', 'No', name='include_damper_foam_enum'))
#     detachable_typec = Column(Enum('detachable_typec_enum', 'Yes', 'No', name='detachable_typec_enum'))
#     onboard_memory = Column(Enum('onboard_memory_enum', 'Yes', 'No', name='onboard_memory_enum'))
#     anti_ghosting = Column(Enum('anti_ghosting_enum', 'Yes', 'No', name='anti_ghosting_enum'))
#     rgb_per_key = Column(Enum('rgb_per_key_enum', 'Yes', 'No', name='rgb_per_key_enum'))
#     battery_capacity_mah = Column(Integer)
#     store_id = Column(Integer, ForeignKey('stores.store_id'))  # Ini merujuk ke tabel stores


# Load the CSV file into a DataFrame
df_products = pd.read_csv('D:\Career\QWork\chatgpt\products.csv')

# # Iterate over each row in the DataFrame
# for index, row in df_products.iterrows():
#     # Extract values from the row
#     title = row['Title']
#     reviews = row['Reviews']
#     sold = row['Sold']
#     original_price = row['Original Price']
#     description = row['Description']
#     product_url = row['Product URL']
#     brand_category = row['Brand (Category)']
#     material_casing_category = row['Material casing (Category)']
#     compatibility_with_mechanical_switch = row['Compatibility with mechanical switch (Category)']
#     keycap_profile = row['Keycap profile (Category)']
#     color_options = row['Color options (Category)']
#     switch_options = row['Switch options (Category)']
#     keyboard_layout = row['Keyboard layout (Category)']
#     number_of_keys = row['Number of keys (Number)']
#     dimensions_length_mm = row['Dimensions (Length) (millimeters)']
#     dimensions_width_mm = row['Dimensions (Width) (millimeters)']
#     dimensions_height_mm = row['Dimensions (Height) (millimeters)']
#     weight_grams = row['Weight (grams)']
#     battery_capacity_mah = row['Battery capacity (mAh)']

#     # Handle enum columns
#     underglow_rgb = row['Underglow RGB (Yes/No)'] if row['Underglow RGB (Yes/No)'] in ['Yes', 'No'] else None
#     south_facing_rgb_switch = row['South-facing RGB switch (Yes/No)'] if row['South-facing RGB switch (Yes/No)'] in ['Yes', 'No'] else None
#     hot_swappable_5_pin = row['Hot-swappable (5 pin) (Yes/No)'] if row['Hot-swappable (5 pin) (Yes/No)'] in ['Yes', 'No'] else None
#     magic_fn_key = row['Magic FN key (Yes/No)'] if row['Magic FN key (Yes/No)'] in ['Yes', 'No'] else None
#     software_customization = row['Software customization (Yes/No)'] if row['Software customization (Yes/No)'] in ['Yes', 'No'] else None
#     pre_lubed_stabilizer = row['Pre-lubed stabilizer (Yes/No)'] if row['Pre-lubed stabilizer (Yes/No)'] in ['Yes', 'No'] else None
#     include_damper_foam = row['Include damper foam (Yes/No)'] if row['Include damper foam (Yes/No)'] in ['Yes', 'No'] else None
#     detachable_type_c = row['Detachable Type-C (Yes/No)'] if row['Detachable Type-C (Yes/No)'] in ['Yes', 'No'] else None
#     onboard_memory = row['Onboard memory (Yes/No)'] if row['Onboard memory (Yes/No)'] in ['Yes', 'No'] else None
#     anti_ghosting = row['Anti-ghosting (Yes/No)'] if row['Anti-ghosting (Yes/No)'] in ['Yes', 'No'] else None
#     rgb_per_key = row['RGB Per-Key (Yes/No)'] if row['RGB Per-Key (Yes/No)'] in ['Yes', 'No'] else None

#     # Create a new Products object and add it to the session
#     product = Products(title=title, reviews=reviews, sold=sold, original_price=original_price,
#                        description=description, product_url=product_url, brand_category=brand_category,
#                        material_casing_category=material_casing_category, underglow_rgb=underglow_rgb,
#                        south_facing_rgb_switch=south_facing_rgb_switch,
#                        hot_swappable_5_pin=hot_swappable_5_pin,
#                        compatibility_with_mechanical_switch=compatibility_with_mechanical_switch,
#                        keycap_profile=keycap_profile, color_options=color_options,
#                        switch_options=switch_options, keyboard_layout=keyboard_layout,
#                        number_of_keys=number_of_keys, dimensions_length_mm=dimensions_length_mm,
#                        dimensions_width_mm=dimensions_width_mm, dimensions_height_mm=dimensions_height_mm,
#                        weight_grams=weight_grams, battery_capacity_mah=battery_capacity_mah,
#                        pre_lubed_stabilizer=pre_lubed_stabilizer, include_damper_foam=include_damper_foam,
#                        detachable_typec=detachable_type_c, onboard_memory=onboard_memory,
#                        anti_ghosting=anti_ghosting, rgb_per_key=rgb_per_key)
#     session.add(product)



# # Commit the session to save changes to the database
# session.commit()
file_path = 'D:\Career\QWork\chatgpt\mechanical-keyboard-full.csv'
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        product = Products(
            # product_id=int(row['product_id']),
            store_id = row['store_id'],
            Title=row['Title'],
            Reviews=int(row['Reviews']),
            Sold=float(row['Sold']),
            Original_Price=int(row['Original Price']),
            Description=row['Description'],
            Product_URL=row['Product URL'],
            Brand_Category=row['Brand (Category)'],
            Material_casing_Category=row['Material casing (Category)'],
            Underglow_RGB=row['Underglow RGB (Yes/No)'],
            South_facing_RGB_switch=row['South-facing RGB switch (Yes/No)'],
            Hot_swappable_5_pin=row['Hot-swappable (5 pin) (Yes/No)'],
            Compatibility_with_mechanical_switch=row['Compatibility with mechanical switch (Category)'],
            Magic_FN_key=row['Magic FN key (Yes/No)'],
            Software_customization=row['Software customization (Yes/No)'],
            Keycap_profile_Category=row.get('Keycap profile (Category)', None),
            Color_options_Category=row.get('Color options (Category)', None),
            Switch_options_Category=row.get('Switch options (Category)', None),
            Keyboard_layout_Category=row.get('Keyboard layout (Category)', None),
            Number_of_keys=int(row['Number of keys (Number)']) if row['Number of keys (Number)'] else None,
            Dimensions_Length_millimeters=float(row['Dimensions (Length) (millimeters)']) if row['Dimensions (Length) (millimeters)'] else None,
            Dimensions_Width_millimeters=float(row['Dimensions (Width) (millimeters)']) if row['Dimensions (Width) (millimeters)'] else None,
            Dimensions_Height_millimeters=float(row['Dimensions (Height) (millimeters)']) if row['Dimensions (Height) (millimeters)'] else None,
            Weight_grams=float(row['Weight (grams)']) if row['Weight (grams)'] else None,
            Pre_lubed_stabilizer=row['Pre-lubed stabilizer (Yes/No)'],
            Include_damper_foam=row['Include damper foam (Yes/No)'],
            Detachable_Type_C=row['Detachable Type-C (Yes/No)'],
            Onboard_memory=row['Onboard memory (Yes/No)'],
            Anti_ghosting=row['Anti-ghosting (Yes/No)'],
            RGB_Per_Key=row['RGB Per-Key (Yes/No)'],
            Battery_capacity_mAh=float(row['Battery capacity (mAh)']) if row['Battery capacity (mAh)'] else None,
        )
        session.add(product)
    session.commit()

# Close the session
session.close()