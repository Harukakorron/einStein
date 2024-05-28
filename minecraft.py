import sqlite3

class Mine:
    def __init__(self, Name, Dimension, Höhe_mit_höchster_Wahrscheinlichkeit, Biom, Farbe, real_life, Bild):
        self.Name = Name
        self.Dimension = Dimension
        self.Höhe_mit_höchster_Wahrscheinlichkeit = Höhe_mit_höchster_Wahrscheinlichkeit
        self.Biom = Biom
        self.Farbe = Farbe
        self.real_life = real_life
        self.Bild = Bild

    def to_db(self):
        connection = sqlite3.connect("ding_bis_jetzt.db") # Muss vorher angelegt werden.
        cursor = connection.cursor()
        sql = f"INSERT INTO Minecraft (Name, Dimension, Höhe_mit_höchster_Wahrscheinlichkeit, Biom, Farbe, real_life, Bild) VALUES ('{self.Name}', '{self.Dimension}', '{self.Höhe_mit_höchster_Wahrscheinlichkeit}', '{self.Biom}', '{self.Farbe}', '{self.real_life}', '{self.Bild}' )"
        cursor.execute(sql)
        connection.commit()
        connection.close()

    @classmethod
    def from_db(cls, Name):
        connection = sqlite3.connect("ding_bis_jetzt.db") # Muss vorher angelegt werden.
        cursor = connection.cursor()
        sql = f'SELECT Name FROM Minecraft WHERE Name = "{Name}"'
        print(sql)
        cursor.execute(sql)
        row = cursor.fetchone()
        connection.close()
        return Mine(row[0], row[1], row[2], row[3], row[4], row[5], row[6])