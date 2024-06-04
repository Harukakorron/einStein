import sqlite3

class stone:
    def __init__(self, Name, Formeleinheit, Verwendung, Härte, Farbe, Zugehörigkeit, Gefahr, Nummer, Oberklasse, Bild):
        self.Name = Name
        self.Verwendung = Verwendung
        self.Härte = Härte
        self.Zugehörigkeit = Zugehörigkeit
        self.Farbe = Farbe
        self.Gefahr = Gefahr
        self.Bild = Bild
        self.Nummer = Nummer
        self.Oberklasse = Oberklasse
        self.Formeleinheit = Formeleinheit

    def to_db(self):
        connection = sqlite3.connect("ding_bis_jetzt.db") # Muss vorher angelegt werden.
        cursor = connection.cursor()
        sql = f"INSERT INTO Steine (Name, Formeleinheit, Verwendung, Härte, Farbe, Zugehörigkeit, Gefahr, Nummer, Oberklasse, Bild) VALUES ('{self.Name}', '{self.Formeleinheit}', '{self.Verwendung}', '{self.Härte}', '{self.Farbe}', '{self.Zugehöhrigkeit}', '{self.Gefahr}', '{self.Nummer}', '{self.Oberklasse}', '{self.Bild}' )"
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
        return Mine(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
