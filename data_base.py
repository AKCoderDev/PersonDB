from sqlalchemy import create_engine, ForeignKey, Column, String, CHAR, Date, Integer, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"

    passport = Column("Passport", String, primary_key=True)
    photo = Column("Photo", LargeBinary)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    gender = Column("Gender", CHAR)
    phone_number = Column("Phone number", String)
    date_of_birth = Column("Day of birth", Date)
    notes = Column("Notes", String)
    age = Column("Age", Integer)

    def calculate_age(self):
        current_year = datetime.now().year
        age = current_year - self.date_of_birth.year
        return age

    def __init__(self, passport, photo, first_name, last_name, gender, phone_number, date_of_birth, notes):
        self.passport = passport
        self.photo = photo
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.notes = notes

    def __repr__(self):
        age = self.calculate_age()
        return f"({self.passport} {self.photo} {self.first_name} {self.last_name} {self.gender} {self.phone_number} {self.date_of_birth} {self.notes})"

engine = create_engine("sqlite:///C:/projects/PersonDB/Users.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()