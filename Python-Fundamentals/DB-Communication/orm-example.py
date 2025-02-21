#SQLAlchemy provides an abstraction over raw SQL queries.

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# PostgreSQL Connection
engine = create_engine("postgresql://postgres:world123@localhost:5433s/testdb")
Base = declarative_base()

# Define Model
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    salary = Column(Float, nullable=False)

# Create Table
Base.metadata.create_all(engine)

# Insert Data
Session = sessionmaker(bind=engine)
session = Session()
session.add(Employee(name="Charlie", salary=75000))
session.commit()

# Read Data
for emp in session.query(Employee).all():
    print(emp.id, emp.name, emp.salary)

session.close()
#SQLAlchemy provides an abstraction over raw SQL queries.