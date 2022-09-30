import mysql.connector as mysc

input("Press Enter to Initialize Database for the first time!")

'''Using connection object 'cdb' to create a new database'''

cdb=mysc.connect(host='localhost', user='root', passwd='4321')

csrdb=cdb.cursor()

csrdb.execute('DROP DATABASE IF EXISTS LibProject')

csrdb.execute('create database LibProject') 

print()
print("Initializing...")
print()

'''Using connection object 'csrdb' to create tables in the database'''

cobj=mysc.connect(host='localhost', user='root', passwd='4321', database='LibProject')

csr=cobj.cursor()   


csr.execute('''create table MainShelf
            ( Serial INT(6) AUTO_INCREMENT,
            ID INT(5) NOT NULL PRIMARY KEY, 
            Name VARCHAR(50) NOT NULL,
            Language CHAR(3) NOT NULL,
            Genre VARCHAR(10),
            Shelf INT(2),
            Status CHAR(9),
            Reader CHAR(30),
            INDEX(Serial))
            ''')

            
csr.execute('''create table Novels
            ( Serial INT(6) AUTO_INCREMENT,
            ID INT(5) NOT NULL UNIQUE, 
            Name VARCHAR(50) NOT NULL,
            Language CHAR(3) NOT NULL,
            Genre VARCHAR(10),
            Shelf INT(2),
            INDEX(Serial),
            FOREIGN KEY (ID) REFERENCES MainShelf (ID)
            ON DELETE CASCADE ON UPDATE CASCADE)
            ''')


csr.execute('''create table Reference
            ( Serial INT(6) AUTO_INCREMENT,
            ID INT(5) NOT NULL UNIQUE, 
            Name VARCHAR(50) NOT NULL,
            Language CHAR(3) NOT NULL,
            Genre VARCHAR(10),
            Shelf INT(2),
            INDEX(Serial),
            FOREIGN KEY (ID) REFERENCES MainShelf (ID)
            ON DELETE CASCADE ON UPDATE CASCADE)
            ''')

            
csr.execute('''create table Poems
            ( Serial INT(6) AUTO_INCREMENT,
            ID INT(5) NOT NULL UNIQUE, 
            Name VARCHAR(50) NOT NULL,
            Language CHAR(3) NOT NULL,
            Genre VARCHAR(10),
            Shelf INT(2),
            INDEX(Serial),
            FOREIGN KEY (ID) REFERENCES MainShelf (ID)
            ON DELETE CASCADE ON UPDATE CASCADE)
            ''')            


csr.execute('''create table English
            ( Serial INT(6) AUTO_INCREMENT,
            ID INT(5) NOT NULL UNIQUE, 
            Name VARCHAR(50) NOT NULL,
            Language CHAR(3) NOT NULL,
            Genre VARCHAR(10),
            Shelf INT(2),
            INDEX(Serial),
            FOREIGN KEY (ID) REFERENCES MainShelf (ID)
            ON DELETE CASCADE ON UPDATE CASCADE)
            ''')


csr.execute('''create table Tamil
            ( Serial INT(6) AUTO_INCREMENT,
            ID INT(5) NOT NULL UNIQUE, 
            Name VARCHAR(50) NOT NULL,
            Language CHAR(3) NOT NULL,
            Genre VARCHAR(10),
            Shelf INT(2),
            INDEX(Serial),
            FOREIGN KEY (ID) REFERENCES MainShelf (ID)
            ON DELETE CASCADE ON UPDATE CASCADE)
            ''')


csr.execute('''create table Hindi
            ( Serial INT(6) AUTO_INCREMENT,
            ID INT(5) NOT NULL UNIQUE, 
            Name VARCHAR(50) NOT NULL,
            Language CHAR(3) NOT NULL,
            Genre VARCHAR(10),
            Shelf INT(2),
            INDEX(Serial),
            FOREIGN KEY (ID) REFERENCES MainShelf (ID)
            ON DELETE CASCADE ON UPDATE CASCADE)
            ''')


print('Database and Tables Initialised succcessfully!')