from sqlite3 import connect, Connection, Cursor, Row

# con = connect("static/db/products.db")
# cursor = Cursor(con)
con = connect("static/db/voyage.db")
cursor = Cursor(con)


def createTables(con: Connection):
    cursor = con.cursor()
sql = """CREATE TABLE region
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL, 
            centre TEXT NOT NULL 
          
        )"""
# cursor.execute(sql)
# con.commit()
# createTables(con)

def selectAll(con: Connection):
    cursor = Cursor(con)
    sql = """SELECT * FROM region"""
    cursor.execute(sql)
    con.commit()
    return cursor.fetchall()

def createTables(con: Connection):
    cursor = con.cursor()
sql = """CREATE TABLE type
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name_type TEXT NOT NULL,
            description TEXT NOT NULL   
        )"""
# cursor.execute(sql)
# con.commit()
# createTables(con)

def createTables(con: Connection):
    cursor = con.cursor()
sql = """CREATE TABLE tourne
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name_tourne TEXT NOT NULL, 
        description TEXT NOT NULL,
        img  TEXT NOT NULL,
        region_id INTEGER NOT NULL,
        type_id INTEGER NOT NULL,
        FOREIGN KEY (type_id) REFERENCES type(id) ON DELETE CASCADE,
        FOREIGN KEY (region_id) REFERENCES region(id) ON DELETE CASCADE  
        )"""
# cursor.execute(sql)
# con.commit()
# createTables(con)

# sql = """INSERT INTO region(name, centre) VALUES (?, ?)"""
# cursor.executemany(sql,
#                     [("Центральный", "Москва"), ("Северо-Западный", "Санкт-Петербург"), ("Южный", "Ростов-на-Дону"), ("Сибирский", "Новосибирск"), ("Дальневосточный", "Владивосток"), ("Северо-Кавказский", "Пятигорск"), ("Уральский", "Екатеринбург")])
# con.commit()


# def insertMany(con: Connection, regionsList: list):
#     cursor = Cursor(con)
#     sql = """INSERT INTO region(name, centre) VALUES (?, ?)"""
#     cursor.executemany(sql, regionsList)
#     con.commit()

# lst = [
# ("Центральный", "Москва"),
# ("Северо-Западный", "Санкт-Петербург"),
# ("Южный", "Ростов-на-Дону"),
# ("Сибирский", "Новосибирск"),
# ("Дальневосточный", "Владивосток"),
# ("Северо-Кавказский", "Пятигорск"),
# ("Уральский", "Екатеринбург")]

# insertMany(con, lst)
# print(selectAll(con))

# def insertMany(con: Connection, typesList: list):
#     cursor = Cursor(con)
#     sql = """INSERT INTO type(name_type, description) VALUES (?, ?)"""
#     cursor.executemany(sql, typesList)
#     con.commit()

# lst = [
# ("Пешеходный", "Поход выходного дня"),
# ("Автомобильный", "Автопробег"), 
# ("Велосипедный", "1 категория сложности"), 
# ("Водный", "Сплав")]

# insertMany(con, lst)
# print(selectAll(con))

def insertMany(con: Connection, tournesList: list):
    cursor = Cursor(con)
    sql = """INSERT INTO tourne(name_tourne, description, img, region_id, type_id) VALUES (?, ?, ?, ?, ?)"""
    cursor.executemany(sql, tournesList)
    con.commit()
lst = [
    ("Древний Псков", "Летне-осенний тур", "11.jpeg", 2, 1), 
    ("Романтика алых парусов", "Путешествие в Санкт-Петербург", "2.jpeg", 2, 1),
    ("Озеро Байкал", "На байдарках", "4.jpeg", 4, 4),
    ("Владивосток", "Семейное путешествие", "22.jpeg", 5, 2 ),
    ("Адыгея", "Через горы к морю", "3.jpeg", 6, 1 ),
    ("Нижегородская область", "Вдоль Волги", "container3.webp", 1, 3 )]
    
# insertMany(con, lst)
# print(selectAll(con))


class VoyageDB:
    def __init__(self, connection: Connection) -> None:
        self.__connect = connection
        self.__cursor = Cursor(connection)
        self.__cursor.row_factory = Row
    
    def getAllVoyages(self):
        sql = '''SELECT  region.name, tourne.name_tourne, tourne.description, tourne.img, 
    type.name_type, type.description FROM type INNER JOIN (region INNER JOIN tourne ON region.id = tourne.region_id) ON type.id = tourne.type_id;'''
        try:
            self.__cursor.execute(sql)
            return self.__cursor.fetchall()
        except:
            print("ошибка чтения")
            return []
        
      
        
    def getTourneFromId(self, region_id: int) -> dict | None:
        sql = '''SELECT region_id, region.name, tourne.name_tourne, tourne.description, tourne.img, 
    type.name_type, type.description 
    FROM type INNER JOIN (region INNER JOIN tourne ON region.id = tourne.region_id) ON type.id = tourne.type_id WHERE region_id = ?'''

        try:
            self.__cursor.execute(sql, (region_id,))
            return self.__cursor.fetchone()
        except:
            print("товар не найден")
            return None  

    
