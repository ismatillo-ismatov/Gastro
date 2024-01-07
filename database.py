from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from databases import Database

import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
SQLALCHAMY_DATABASE_URL = 'mariadb+pymysql://ismatov:ismatov123@localhost/ismatov'
engine = create_engine(SQLALCHAMY_DATABASE_URL)

metadata = MetaData()



Base = declarative_base()
Session=sessionmaker()


