if __name__ == "__main__":
    holidays = {
        "Month: 1, Day: 1": "Nieuwjaarsdag",
        "Month: 4, Day: 7": "Goede vrijdag",
        "Month: 4, Day: 9": "Eerste paasdag",
        "Month: 4, Day: 10": "Tweede paasdag",
        "Month: 4, Day: 27": "Koningsdag",
        "Month: 5, Day: 5": "Bevrijdingsdag",
        "Month: 5, Day: 18": "Hemelvaartsdag",
        "Month: 5, Day: 28": "Eerste pinksterdag",
        "Month: 5, Day: 29": "Tweede pinksterdag",
        "Month: 12, Day: 25": "Eerste kerstdag",
        "Month: 12, Day: 26": "Tweede kerstdag",
    }

    date = input("Datum: ")
    print(holidays[date] if date in holidays else "Geen feestdag bekend op die datum")
