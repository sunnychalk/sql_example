import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

sql_command = 'CREATE TABLE IF NOT EXISTS Users (ID INTEGER PRIMARY KEY, FIRST_NAME VARCHAR(50) NOT NULL, LAST_NAME VARCHAR(50) NOT NULL, ADRESS VARCHAR(100), PHONE INTEGER NOT NULL);'
cursor.execute(sql_command)
sql_command = 'INSERT INTO Users VALUES (1,"Dima", "Dmitriev", "My adress", 03);'
cursor.execute(sql_command)
sql_command = 'INSERT INTO Users VALUES (2,"Ivan", "Ivanov", "My adress2", 02);'
cursor.execute(sql_command)
sql_command = 'INSERT INTO Users VALUES (3,"Peter", "Petrov", "My adress3", 01);'
cursor.execute(sql_command)
sql_command = 'INSERT INTO Users VALUES (4,"Michael", "Johnson", "My adress4", 04);'
cursor.execute(sql_command)
conn.commit()

sql_command = 'CREATE TABLE IF NOT EXISTS Pizza (ID INTEGER PRIMARY KEY, NAME VARCHAR(50) NOT NULL, PRICE INTEGER NOT NULL);'
cursor.execute(sql_command)
sql_command = 'INSERT INTO Pizza VALUES (1, "Chicken", 5.00);'
cursor.execute(sql_command)
sql_command = 'INSERT INTO Pizza VALUES (2, "Vegan", 4.00);'
cursor.execute(sql_command)
sql_command = 'INSERT INTO Pizza VALUES (3, "Hawaii", 6.00);'
cursor.execute(sql_command)
sql_command = 'INSERT INTO Pizza VALUES (4, "Super", 10.00);'
cursor.execute(sql_command)
conn.commit()


sql_command = 'CREATE TABLE IF NOT EXISTS Orders (ID INTEGER PRIMARY KEY, USERS_ID INTEGER, FOREIGN KEY (USERS_ID) REFERENCES Users(ID), PIZZA_ID INTEGER, FOREIGN KEY (PIZZA_ID) REFERENCES Pizza(ID));'
cursor.execute(sql_command)
sql_command = 'INSERT INTO Orders VALUES (1, 2, 1);'
cursor.execute(sql_command)
sql_command = 'INSERT INTO Orders VALUES (2, 3, 4);'
cursor.execute(sql_command)
sql_command = 'INSERT INTO Orders VALUES (3, 4, 2);'
cursor.execute(sql_command)
sql_command = 'INSERT INTO Orders VALUES (4, 1, 3);'
cursor.execute(sql_command)
conn.commit()


class Users():

	def __init__(self, id, first_name, last_name, adress, phone):
		self.id = id
		self.first_name = first_name
		self.last_name = last_name
		self.adress = adress
		self.phone = phone

	def get_all(self):
		sql_command = 'SELECT * FROM Users;'
		return cursor.execute(sql_command)


	def add_new_object(id, first_name, last_name, adress, phone):
		sql_command = 'INSERT INTO Users VALUES(id, first_name, last_name, adress, phone);'
		return cursor.execute(sql_command)


	def get_object_by_id(self, id):
		sql_command = 'SELECT first_name, last_name FROM Users WHERE id = self.id;'
		return cursor.execute(sql_command)

	def get_list_sorted_by_first_name(self):
		sql_command = 'SELECT * FROM Users ORDER BY FIRST_NAME;'
		return cursor.execute(sql_command)
		
		
Users.get_all()
Users.get_object_by_id(3)
Users.add_new_object(5, "Oleg", "Anisimov", "My adress5", 06)
Users.get_list_sorted_by_first_name()

cursor.close()
conn.close()