import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    
    def __init__ (self, name, breed, id=None):
        self.id = id
        self.name = name
        self.breed = breed

# adding the init with self, name, breed, and id with self will clear first FAIL:
# FAILED Class Dog in dog.py initializes with name and breed attributes. 
# - AttributeError: 'Dog' object has no attribute 'name'


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS dogs
                (id INTEGER PRIMARY KEY,
                name TEXT,
                breed TEXT)
        """

        CURSOR.execute(sql)
        CONN.commit()
# adding the class method with def create_table passing class (cls) and using sql = """ to CREATE TABLE using CURSON and CONN
# FAILED Class Dog in dog.py contains method "create_table()" that creates table "dogs" if it does not exist. 
# - AttributeError: type object 'Dog' has no attribute 'create_table'

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS dogs
        """

        CURSOR.execute(sql)
        CONN.commit()
# adding the class method with def drop_table passing class (cls) and using sql = """ to DROP TABLE using CURSOR and CONN
# FAILED Class Dog in dog.py contains method "drop_table()" that drops table "dogs" if it exists. 
# - AttributeError: type object 'Dog' has no attribute 'drop_table'
    def save(self):
        sql = """
            INSERT INTO dogs (name, breed)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.breed))
        CONN.commit()

        # solution for bonus methods
        self.id = CURSOR.lastrowid

# def save passing self and using SQL to INSERT INTO and add VALUES using CURSOR passing name and breed and CONN 
# FAILED Class Dog in dog.py contains method "save()" that saves a Dog instance to the database. 
# - AttributeError: 'Dog' object has no attribute 'save'

    @classmethod
    def create(cls, name, breed):
        dog = cls(name, breed)
        dog.save()
        

        return dog

# create a classmeth with def create passing cls, name, and breed- sets dog = cls of name and breed and dog.save to save- return dog 
# FAILED Class Dog in dog.py contains method "create()" that creates a new row in the database and returns a Dog instance. 
# - AttributeError: type object 'Dog' has no attribute 'create'
 
    @classmethod
    def new_from_db(cls, row):
        dog = cls(
            name=row[1],
            breed=row[2],
            id=row[0]
        )

        return dog

# added classmethd of def new_form_ passing cls and row- setting dog = cls and with name as row 2, breed, row 2, and id row 1- return dog 
# FAILED Class Dog in dog.py contains method "new_from_db()" that takes a database row and creates a Dog instance. 
# - AttributeError: type object 'Dog' has no attribute 'new_from_db'

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM dogs
        """

        return [cls.new_from_db(row) for row in CURSOR.execute(sql).fetchall()]

# set classmethod of def get_all passing cls and using SQL """ to SELECT * FROM dogs and return []
# FAILED Class Dog in dog.py contains method "get_all()" that returns a list of Dog instances for every record in the database. 
# - AttributeError: type object 'Dog' has no attribute 'get_all'

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM dogs
            WHERE name = ?
            LIMIT 1
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        if not row:
            return None

        return Dog(
            name=row[1],
            breed=row[2],
            id=row[0]
        )

# FAILED Class Dog in dog.py contains method "find_by_name()" that returns a Dog instance corresponding to its database record retrieved by name. 
# - AttributeError: type object 'Dog' has no attribute 'find_by_name'

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM dogs
            WHERE id = ?
            LIMIT 1
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        if not row:
            return None

        return Dog(
            name=row[1],
            breed=row[2],
            id=row[0]
        )

# FAILED Class Dog in dog.py contains method "find_by_id()" that returns a Dog instance corresponding to its database record retrieved by id. 
# - AttributeError: type object 'Dog' has no attribute 'find_by_id'

    @classmethod
    def find_or_create_by(cls, name=None, breed=None):
        sql = """
            SELECT * FROM dogs
            WHERE (name, breed) = (?, ?)
            LIMIT 1
        """

        row = CURSOR.execute(sql, (name, breed)).fetchone()
        if not row:
            sql = """
                INSERT INTO dogs (name, breed)
                VALUES (?, ?)
            """

            CURSOR.execute(sql, (name, breed))
            return Dog(
                name=name,
                breed=breed,
                id=CURSOR.lastrowid
            )

        return Dog(
            name=row[1],
            breed=row[2],
            id=row[0]
        )

# FAILED Class Dog in dog.py contains method "find_or_create_by()" that takes a name and a breed as arguments and creates a Dog instance matching that record if it does not exist.
#  - AttributeError: type object 'Dog' has no attribute 'find_or_create_by'

    def update(self):
        sql = """
            UPDATE dogs
            SET name = ?,
                breed = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.breed, self.id))
        CONN.commit()

# FAILED Class Dog in dog.py contains a method "update()" that updates an instance's corresponding database record to match its new attribute values. 
# - AttributeError: 'Dog' object has no attribute 'update'


# ******************************************************************************************************************************************

# This code is for managing a collection of dogs using a database. Let me explain it to you in simpler terms:

# First, the code imports a library called sqlite3, which helps with working with databases.
# Then, it creates a connection to a database file called dogs.db located in a folder named lib. 
# This connection allows us to interact with the database.

# The code defines a class called Dog which represents a dog object. 
# Each dog has a name and a breed. The class has various methods that perform different operations on the database.

# Here are the main methods of the Dog class:

# create_table(): This method creates a table in the database to store dog information. 
# The table has columns for the dog's ID, name, and breed.

# drop_table(): This method deletes the table from the database if it exists.

# save(): This method saves the current dog object's information (name and breed) into the database as a new record.

# create(): This method creates a new dog object with the given name and breed, and then saves it to the database as a new record. 
# It returns the created dog object.

# new_from_db(): This method takes a row of data from the database (containing ID, name, and breed) and creates a new dog object
#  with that information.

# get_all(): This method retrieves all the dog records from the database and returns a list of dog objects.

# find_by_name(): This method searches for a dog record in the database by its name and returns the corresponding dog object if found.

# find_by_id(): This method searches for a dog record in the database by its ID and returns the corresponding dog object if found.

# find_or_create_by(): This method searches for a dog record in the database by its name and breed. 
# If a matching record is found, it returns the corresponding dog object. 
# Otherwise, it creates a new dog record in the database with the given name and breed, and returns the newly created dog object.

# update(): This method updates the dog's information (name and breed) in the database based on the current object's ID.

# Overall, this code helps us manage a collection of dogs by providing methods to create, 
# retrieve, update, and delete dog records in a database.

# ******************************************************************************************************************************************
# import sqlite3

# CONN = sqlite3.connect('lib/dogs.db')
# CURSOR = CONN.cursor()

# class Dog:
    
#     def __init__(self, name, breed, id=None):
#         self.id = id
#         self.name = name
#         self.breed = breed

#     @classmethod
#     def create_table(cls):
#         sql = """
#             CREATE TABLE IF NOT EXISTS dogs
#                 (id INTEGER PRIMARY KEY,
#                 name TEXT,
#                 breed TEXT)
#         """

#         CURSOR.execute(sql)
#         CONN.commit()

#     @classmethod
#     def drop_table(cls):
#         sql = """
#             DROP TABLE IF EXISTS dogs
#         """

#         CURSOR.execute(sql)
#         CONN.commit()

#     def save(self):
#         sql = """
#             INSERT INTO dogs (name, breed)
#             VALUES (?, ?)
#         """

#         CURSOR.execute(sql, (self.name, self.breed))
#         CONN.commit()

#         # solution for bonus methods
#         self.id = CURSOR.lastrowid

#     @classmethod
#     def create(cls, name, breed):
#         dog = cls(name, breed)
#         dog.save()
        
#         # note that this dog will not have an id
#         # the id is created for the database record, not the instance
#         # the update() bonus method will not work correctly
#         #     until this is addressed
#         return dog

#     @classmethod
#     def new_from_db(cls, row):
#         dog = cls(
#             name=row[1],
#             breed=row[2],
#             id=row[0]
#         )

#         return dog

#     @classmethod
#     def get_all(cls):
#         sql = """
#             SELECT * FROM dogs
#         """

#         return [cls.new_from_db(row) for row in CURSOR.execute(sql).fetchall()]

#     @classmethod
#     def find_by_name(cls, name):
#         sql = """
#             SELECT * FROM dogs
#             WHERE name = ?
#             LIMIT 1
#         """

#         row = CURSOR.execute(sql, (name,)).fetchone()
#         if not row:
#             return None

#         return Dog(
#             name=row[1],
#             breed=row[2],
#             id=row[0]
#         )

#     @classmethod
#     def find_by_id(cls, id):
#         sql = """
#             SELECT * FROM dogs
#             WHERE id = ?
#             LIMIT 1
#         """

#         row = CURSOR.execute(sql, (id,)).fetchone()
#         if not row:
#             return None

#         return Dog(
#             name=row[1],
#             breed=row[2],
#             id=row[0]
#         )

#     @classmethod
#     def find_or_create_by(cls, name=None, breed=None):
#         sql = """
#             SELECT * FROM dogs
#             WHERE (name, breed) = (?, ?)
#             LIMIT 1
#         """

#         row = CURSOR.execute(sql, (name, breed)).fetchone()
#         if not row:
#             sql = """
#                 INSERT INTO dogs (name, breed)
#                 VALUES (?, ?)
#             """

#             CURSOR.execute(sql, (name, breed))
#             return Dog(
#                 name=name,
#                 breed=breed,
#                 id=CURSOR.lastrowid
#             )

#         return Dog(
#             name=row[1],
#             breed=row[2],
#             id=row[0]
#         )

#     def update(self):
#         sql = """
#             UPDATE dogs
#             SET name = ?,
#                 breed = ?
#             WHERE id = ?
#         """

#         CURSOR.execute(sql, (self.name, self.breed, self.id))
#         CONN.commit()