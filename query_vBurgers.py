from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)

session = DBSession()

veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')

# for veggieBurger in veggieBurgers:
# 	print veggieBurger.mid
# 	print veggieBurger.restaurant.name
# 	print veggieBurger.price
# 	print "\n" 

for veggieBurger in veggieBurgers:
	if veggieBurger.price != '$2.99':
		old_price = veggieBurger.price
		veggieBurger.price = '$2.99'
		session.add(veggieBurger)
		session.commit()
		print veggieBurger.restaurant.name
		print "Old Price:", old_price
		print "New Price:", veggieBurger.price
		print "\n" 

# urbanVB = session.query(MenuItem).filter_by(mid = 10).one()
# old_price = urbanVB.price
# session.commit()
# urbanVB.price = '$2.99'

# print urbanVB.name
# print "Old Price:", old_price 
# print "New Price:", urbanVB.price


