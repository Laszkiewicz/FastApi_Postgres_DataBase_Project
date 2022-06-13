# from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Float
# from sqlalchemy.orm import relationship
# from db.base_class import Base
#
#
# class Book(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, nullable=False)
#     author = Column(String, nullable=False)
#     description = Column(String, nullable=False)
#     price = Column(Float, nullable=False)
#     books = relationship("User", back_populates="book_owner")
