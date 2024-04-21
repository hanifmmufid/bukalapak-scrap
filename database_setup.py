from sqlalchemy import Column, Integer, String, Boolean, Enum, Float, ForeignKey, create_engine, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('postgresql+psycopg2://postgres:hanif123456@localhost:5432/bukalapak', echo=True)

class Stores(Base):
    __tablename__ = 'stores'

    store_id = Column(Integer, primary_key=True)
    store_name = Column(String, nullable=False)
    store_city = Column(String, nullable=False)
    positive_feedback = Column(Integer, nullable=False)
    total_feedback = Column(Integer, nullable=False)

    products_r = relationship("Products", back_populates="stores_r")

class Products(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey('stores.store_id'))
    Title = Column(String)
    Reviews = Column(Integer)
    Sold = Column(Float)
    Original_Price = Column(Integer)
    Description = Column(Text)
    Product_URL = Column(String)
    Brand_Category = Column(String)
    Material_casing_Category = Column(String)
    Underglow_RGB = Column(String)
    South_facing_RGB_switch = Column(String)
    Hot_swappable_5_pin = Column(String)
    Compatibility_with_mechanical_switch = Column(String)
    Magic_FN_key = Column(String)
    Software_customization = Column(String)
    Keycap_profile_Category = Column(String)
    Color_options_Category = Column(String)
    Switch_options_Category = Column(String)
    Keyboard_layout_Category = Column(String)
    Number_of_keys = Column(Integer)
    Dimensions_Length_millimeters = Column(Float)
    Dimensions_Width_millimeters = Column(Float)
    Dimensions_Height_millimeters = Column(Float)
    Weight_grams = Column(Float)
    Pre_lubed_stabilizer = Column(String)
    Include_damper_foam = Column(String)
    Detachable_Type_C = Column(String)
    Onboard_memory = Column(String)
    Anti_ghosting = Column(String)
    RGB_Per_Key = Column(String)
    Battery_capacity_mAh = Column(Float)

    stores_r = relationship("Stores", back_populates="products_r")

Base.metadata.create_all(engine)
# Session = sessionmaker(bind = engine)
# session = Session()

# stores = session.query(Stores).all()
# for store in stores:
#     print(store.store_city)
