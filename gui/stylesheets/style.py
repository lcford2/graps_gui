import os


class StyleSheets(object):
    def __init__(self):
        self.sheets = [
            "AMOLED", "Aqua", "ConsoleStyle",
            "ElegantDark", "ManjaroMix",
            "MaterialDark", "Ubuntu", "ExcelOffice",
            "Medize", "BreezeLight", "BreezeDark"
        ]

    def styles(self):
        return self.sheets

    def AMOLED(self):
        # broken right now
        return None
        with open(os.path.join(".", "gui", "stylesheets", "QSS", "AMOLED.qss"), "r") as sheet:
            qss = sheet.read()
        return qss

    def Aqua(self):
        with open(os.path.join(".", "gui", "stylesheets", "QSS", "Aqua.qss"), "r") as sheet:
            qss = sheet.read()
        return qss

    def ConsoleStyle(self):
        with open(os.path.join(".", "gui", "stylesheets", "QSS", "ConsoleStyle.qss"), "r") as sheet:
            qss = sheet.read()
        return qss

    def ElegantDark(self):
        with open(os.path.join(".", "gui", "stylesheets", "QSS", "ElegantDark.qss"), "r") as sheet:
            qss = sheet.read()
        return qss

    def ManjaroMix(self):
        with open(os.path.join(".", "gui", "stylesheets", "QSS", "ManjaroMix.qss"), "r") as sheet:
            qss = sheet.read()
        return qss

    def MaterialDark(self):
        with open(os.path.join(".", "gui", "stylesheets", "QSS", "MaterialDark.qss"), "r") as sheet:
            qss = sheet.read()
        return qss

    def Ubuntu(self):
        with open(os.path.join(".", "gui", "stylesheets", "QSS", "Ubuntu.qss"), "r") as sheet:
            qss = sheet.read()
        return qss

    def ExcelOffice(self):
        with open(os.path.join(".", "gui", "stylesheets", "ExcelOffice", "ExcelOffice.qss"), "r") as sheet:
            qss = sheet.read()
        return qss

    def Medize(self):
        with open(os.path.join(".", "gui", "stylesheets", "Medize", "Medize.qss"), "r") as sheet:
            qss = sheet.read()
        return qss

    def BreezeLight(self):
        with open(os.path.join(".", "gui", "stylesheets", "BreezeStyleSheets", "light.qss"), "r") as sheet:
            qss = sheet.read()
        return qss

    def BreezeDark(self):
        with open(os.path.join(".", "gui", "stylesheets", "BreezeStyleSheets", "dark.qss"), "r") as sheet:
            qss = sheet.read()
        return qss

    def __iter__(self):
        return self.sheets

    def __repr__(self):
        return "StyleSheets()"

    def __str__(self):
        return "StyleSheets()"
