class Crime:

    def __init__(self, location, date):
        self.__suspect = []
        self.__location = str(location)
        self.__date = str(date)

    def __str__(self):
        result = f"Crime ayant eu lieu à {self.__location}, le {self.__date}.\n"
        result += "Les suspect.e.s sont:\n"
        for i in self.__suspect:
            result += f"- {i}\n"
        return result

    def set_location(self, location):
        self.__location = location

    def set_date(self, date):
        self.__date = date

    def get_location(self):
        return self.__location

    def get_date(self):
        return self.__date

    def get_suspects(self):
        return self.__suspect

    def ajouter_suspect(self, suspect):
        self.__suspect.append(suspect)


if __name__ == "__main__":
    c1 = Crime("Bahnhofstrasse 12, 8001 Zürich", "05/03/2023")
    c1.ajouter_suspect("Peter")
    c1.ajouter_suspect("Fritz")
    c1.ajouter_suspect("Maria")

    print(c1)
