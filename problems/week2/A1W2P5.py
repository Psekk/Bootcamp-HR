import re

if __name__ == "__main__":
    holidays = {
        (1, 1): "Nieuwjaarsdag",
        (4, 7): "Goede vrijdag",
        (4, 9): "Eerste paasdag",
        (4, 10): "Tweede paasdag",
        (4, 27): "Koningsdag",
        (5, 5): "Bevrijdingsdag",
        (5, 18): "Hemelvaartsdag",
        (5, 28): "Eerste pinksterdag",
        (5, 29): "Tweede pinksterdag",
        (12, 25): "Eerste kerstdag",
        (12, 26): "Tweede kerstdag",
    }

    date_input = input("Datum: ")
    regex_result = re.search("[Mm]onth:\s?(\d{1,2}),\s?[Dd]ay:\s?(\d{1,2})", date_input)
    month, day = int(regex_result.groups()[0]), int(regex_result.groups()[1])

    print(holidays[(month, day)] if (month, day) in holidays else "Geen feestdag bekend op die datum")
