#task- 2
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Store(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    genre=Column(String,nullable=False)
    author=Column(String,nullable=False)
    rating=Column(Integer,nullable=False)

engine = create_engine('sqlite:///favourites.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_book1=Store(genre="Horror",author="Ray Mon",rating=3.5)
new_book2=Store(genre="RomCom",author="Helena",rating=5)
new_book3=Store(genre="Anime",author="My",rating=2.1)
new_book4=Store(genre="Self-development",author="Richard ho",rating=4.1)
session.add_all([new_book1,new_book2,new_book3,new_book4])
session.commit()
session.delete(new_book3)

def search_book(search_author):
    books= session.query(Store).filter(Store.author==search_author).first()
    if books:
        print(f"Book is Found{books.genre} ,{books.author} and rating{books.rating}")

    
    else:
        print("Book is not found")
search_author="Helena"
search_book(search_author)