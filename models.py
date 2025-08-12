from sqlalchemy import Integer, Text, Column, ForeignKey, String, DateTime, func
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Users(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	brand = Column(String, unique=True, nullable=False)
	password = Column(String, nullable=False)
	email_list = relationship("EmailList", back_populates="brand")
	sequence = relationship("Sequence", back_populates="belongs_to")
	sequence_id = Column(Integer, ForeignKey("sequence.id"))

class EmailList(Base):
	__tablename__ = "emaillist"

	id = Column(Integer, primary_key=True, index=True)
	email = Column(String, nullable=False)
	first_name = Column(String)
	last_name = Column(String)
	brand = relationship("Users", back_populates="email_list")
	brand_id = Column(Integer, ForeignKey("users.id"))
	added = Column(
		DateTime(timezone=True),
		server_default=func.now(),
		nullable=False
	)

class Emails(Base):
	__tablename__ = "emails"

	id = Column(Integer, primary_key=True, index=True)
	email = Column(Text, nullable=False)
	sequence_id = Column(Integer, ForeignKey("sequence.id"))

class Sequence(Base):
	__tablename__ = "sequence"

	