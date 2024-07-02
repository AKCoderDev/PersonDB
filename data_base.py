from sqlalchemy import create_engine, ForeignKey, Column, String, CHAR, Date, Integer, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"

    passport = Column("Passport", String, primary_key=True)
    photo = Column("photo", LargeBinary)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    phone_number = Column("phone_number", String)
    date_of_birthday = Column("Day of birthday", Date)
    notes = Column("Notes", String)
    age = Column("age", Integer)

    def calculate_age(self):
        current_year = datetime.now().year
        age = current_year - self.date_of_birthday.year
        return age

    def __init__(self, passport, photo, firstname, lastname, gender, phone_number, date_of_birthday, notes):
        self.passport = passport
        self.photo = photo
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.phone_number = phone_number
        self.date_of_birthday = date_of_birthday
        self.notes = notes

    def __repr__(self):
        age = self.calculate_age()
        return f"({self.passport} {self.photo} {self.firstname} {self.lastname} {self.gender} {self.phone_number} {self.date_of_birthday} {self.notes})"

engine = create_engine("sqlite:///C:/projects/PersonDB/Users.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()