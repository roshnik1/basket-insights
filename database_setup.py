from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the PostgreSQL connection details from environment variables
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Create the database connection URL
db_url = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'

# Define the base class for declarative models
Base = declarative_base()

# Define the Aisles table
class Aisle(Base):
    __tablename__ = 'aisles'

    aisle_id = Column(Integer, primary_key=True, autoincrement=True)
    aisle = Column(String(255), nullable=False)

# Define the Departments table
class Department(Base):
    __tablename__ = 'deparkemts'

    department_id = Column(Integer, primary_key=True, autoincrement=True)
    department = Column(String(255), nullable=False)

# Define the Order Products table
class OrderProduct(Base):
    __tablename__ = 'order_products'

    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    add_to_cart_order = Column(Integer)
    reordered = Column(Integer)

# Define the Orders table
class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, autoincrement=False)
    user_id = Column(Integer, nullable=False)
    order_number = Column(Integer, nullable=False)
    order_dow = Column(Integer, nullable=False)  # Day of the week
    order_hour_of_day = Column(Integer, nullable=False)
    days_since_prior_order = Column(Integer)

# Define the Products table
class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(255), nullable=False)
    aisle_id = Column(Integer, nullable=False)
    department_id = Column(Integer, nullable=False)

# Create the Database and Tables
def create_database(db_url):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

create_database(db_url)

# Create a Session
Session = sessionmaker(bind=create_engine(db_url))
session = Session()