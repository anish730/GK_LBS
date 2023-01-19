from sqlalchemy import create_engine, Table, Column, Integer, String, Date, VARCHAR, JSON, DECIMAL, or_, and_ 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:admin@localhost:5432/citizen')
engine.connect()

Base = declarative_base()

class User(Base):
  __tablename__ = 'unreconciled_transactions'
  txn_id = Column(Integer)
  parsed_data = Column(JSON)
  amount = Column(DECIMAL)
  type = Column(VARCHAR)
  id = Column(Integer, primary_key=True)
  txn_date = Column(Date)
 
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(User.txn_date, User.amount, User.type, User.parsed_data['clr_bal_amt']).filter(and_(User.amount <= 25.00, User.type=="D"))
# rows = query.all()
print(query)
