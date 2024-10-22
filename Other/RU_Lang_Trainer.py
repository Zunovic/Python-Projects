import MySQLdb

connection = MySQLdb.connect(
    host="localhost",
    db="rutrainer",
    user="root", passwd=""
)
want_to_learn = True


def pick_random_vocable():
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT word, translation, spelling FROM vocable ORDER BY RAND() LIMIT 1")
        row = cursor.fetchone()
        if row:
            print("\nVokabel:", row)
        else:
            print("Keine Zeile gefunden.")
    except MySQLdb.Error as e:
        print(f"Fehler beim Abrufen der Zufallszeile: {e}")

    finally:
        cursor.close()


while want_to_learn:
    quest = input("Willst du eine Vokabel lernen? Y/N : ").lower()
    if quest == "y":
        pick_random_vocable()
    elif quest == "n":
        print("\nBis zum nächsten Mal!")
        want_to_learn = False
    else:
        print("Du hast eine falsche Eingabe getätigt.")

connection.close()
