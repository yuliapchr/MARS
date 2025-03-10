from data.users import User
from data import db_session

db_session.global_init('database/mars_explorer.db')
session = db_session.create_session()

capitan = User()
capitan.surname = 'Scott'
capitan.name = 'Ridley'
capitan.age = 21
capitan.position = 'capitan'
capitan.speciality = 'research engineer'
capitan.address = 'module_1'
capitan.hashed_password = 'qwerty'
capitan.email = 'scott_chief@mars.org'

peop1 = User()
peop1.surname = 'Scot'
peop1.name = 'Ridey'
peop1.age = 20
peop1.position = 'people'
peop1.speciality = 'engineer'
peop1.address = 'module_1'
peop1.hashed_password = 'qwertyu'
peop1.email = 'scott_chief1@mars.org'

peop2 = User()
peop2.surname = 'Sot'
peop2.name = 'Riey'
peop2.age = 22
peop2.position = 'people'
peop2.speciality = 'engineer'
peop2.address = 'module_2'
peop2.hashed_password = 'qwertyui'
peop2.email = 'scott_chief2@mars.org'

peop3 = User()
peop3.surname = 'Scot'
peop3.name = 'Ridey'
peop3.age = 30
peop3.position = 'people'
peop3.speciality = 'engineer'
peop3.address = 'module_3'
peop3.hashed_password = 'qwertyuio'
peop3.email = 'scott_chief3@mars.org'

session.add(capitan)
session.add(peop1)
session.add(peop2)
session.add(peop3)

session.commit()
