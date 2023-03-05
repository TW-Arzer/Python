import argparse

parser = argparse.ArgumentParser(
    prog="Sherlock",
    description="Identifie les suspect.e.s les plus pausibles à partir de leurs traces de mobilité (issues de sources "
                "multiples inculatn les tweets géo-taggés, les traces Wi-Fi et les flux de photos géo-taggés) pour un "
                "crime spécifié par une date/heure et une localisation")
parser.add_argument("-v", "--verbose", help="affice les détails de l'éxecution du programme et les avertissements")
parser.add_argument("-s", "--suspect", help="fichier contenant la liste des suspect.e.s et les sources de données de "
                                            "localisation", required=True)
parser.add_argument("-t", "--twitter-api-key", help="clé pour l'accès à l'API Twitter (clé privée de l'application "
                                                    "Twitter)", required=True)
parser.add_argument("-u", "--twitter-api-key-secret", help="clé secrète pour l'accès à l'API Twitter", required=True)
parser.add_argument("-g", "--google-api-key", help="clé pour l'accès à l'API Google (clé privée du compte développeur "
                                                   "Google)", required=True)
parser.add_argument("-lat", "--latitude", help="latitude de la scène du crime", required=True)
parser.add_argument("-lng", "--longitude", help="longitude de la scène du crime", required=True)
parser.add_argument("-d", "--date", help="date et heure du crime (au format JJ/MM/AAAA-hh:mm, par exemple "
                                         "19/04/2019-15:02:45)", required=True)
args = parser.parse_args()

print(f"Test_msg: Opening file: {args.suspect}")