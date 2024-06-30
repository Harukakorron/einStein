import sqlite3

class doitsu:
    def __init__(self, Land, Bundesland, Stein, Abbaumethode, Nummer):
        self.Land = Land
        self.Bundesland = Bundesland
        self.Stein = Stein
        self.Abbaumethode = Abbaumethode
        self.Nummer = Nummer

    def to_db(self):
        connection = sqlite3.connect("ding_bis_jetzt.db") # Muss vorher angelegt werden.
        cursor = connection.cursor()
        sql = f"INSERT INTO Deutschland (Land, Bundesland, Stein, Abbaumethode, Nummer) VALUES ('{self.Land}', '{self.Bundesland}', '{self.Stein}', '{self.Abbaumethode}', '{self.Nummer}')"
        cursor.execute(sql)
        connection.commit()
        connection.close()

    @classmethod
    def from_db(cls, Name):
        connection = sqlite3.connect("ding_bis_jetzt.db") # Muss vorher angelegt werden.
        cursor = connection.cursor()
        sql = f'SELECT Name FROM Deutschland WHERE Name = "{Name}"'
        print(sql)
        cursor.execute(sql)
        row = cursor.fetchone()
        connection.close()
        return doitsuchan(row[0], row[1], row[2], row[3], row[4], row[5])
