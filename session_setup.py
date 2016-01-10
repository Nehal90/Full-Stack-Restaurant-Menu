from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)

session = DBSession()

# fourthRestaurant = Restaurant(name = "Pizza Shop", rid = 4)

# session.add(fourthRestaurant)

# session.commit()

# cheesePizza = MenuItem(name = "Cheese Pizza", description = "Made with Cheese", course = "Entree", price = "$7.99", restaurant = fourthRestaurant)

# session.add(cheesePizza)

# session.commit()

# session.query(MenuItem).all()

