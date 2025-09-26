#forskjellen på en liste og en ordbok er at en liste er verdier i en rekke. mens i en ordbok har man keys og values

#numtotext oppgave 2
def numToText(num):
    conversionTabel = {
        0: "null",
        1: "en",
        2: "to",
        3: "tre",
        4: "fire",
        5: "fem",
        6: "seks",
        7: "sju",
        8: "åtte",
        9: "ni",
        10: "ti"
    }
    return conversionTabel[num]

# num = int(input("skirv in et tall mellom 0-10: "))
# print(numToText(num))


#oppgave 3
def oppgave3():
    alphabet="abcdefghijklmnopqrstuvwxyzæøå"
    text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    text.lower()
    stats={}
    for alfabetLetter in alphabet:
        letterCount=0
        for textLetter in text:
            if alfabetLetter==textLetter:
                letterCount+=1
        stats[alfabetLetter]=letterCount
    for letter, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        print(f"{letter} - {count:02d}")


# oppgave 5
def oppgave5():
    eliteserieLag = [
    { "lag": "Lillestrøm", "seriemesterskap": [1976, 1977, 1986, 1989], "norgesmesterskap": [1977, 1978, 1981, 1985, 2007, 2017] },
    { "lag": "Molde", "seriemesterskap": [2011, 2012, 2014, 2019], "norgesmesterskap": [1994, 2005, 2013, 2014, 2021] },
    { "lag": "Viking", "seriemesterskap": [1972, 1973, 1974, 1975, 1979, 1982, 1991], "norgesmesterskap": [1979, 1989, 2001, 2019] },
    { "lag": "Strømsgodset", "seriemesterskap": [1970, 2013], "norgesmesterskap": [1969, 1970, 1973, 1991, 2010] },
    { "lag": "Aalesund", "seriemesterskap": [], "norgesmesterskap": [2009, 2011] },
    { "lag": "Rosenborg", "seriemesterskap": [1967, 1969, 1971, 1985, 1988, 1990, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2006, 2009, 2010, 2015, 2016, 2017, 2018], "norgesmesterskap": [1964, 1971, 1988, 1990, 1992, 1995, 1999, 2003, 2015, 2016, 2018] },
    { "lag": "Sarpsborg", "seriemesterskap": [], "norgesmesterskap": [] },
    { "lag": "Bodø/Glimt", "seriemesterskap": [2020, 2021], "norgesmesterskap": [1975, 1993] },
    { "lag": "Odd", "seriemesterskap": [], "norgesmesterskap": [2000] },
    { "lag": "Tromsø", "seriemesterskap": [], "norgesmesterskap": [1986, 1996] },
    { "lag": "Vålerenga", "seriemesterskap": [1965, 1981, 1983, 1984, 2005], "norgesmesterskap": [1980, 1997, 2002, 2008] },
    { "lag": "HamKam", "seriemesterskap": [], "norgesmesterskap": [] },
    { "lag": "Sandefjord", "seriemesterskap": [], "norgesmesterskap": [] },
    { "lag": "Haugesund", "seriemesterskap": [], "norgesmesterskap": [] },
    { "lag": "Jerv", "seriemesterskap": [], "norgesmesterskap": [] },
    { "lag": "Kristiansund", "seriemesterskap": [], "norgesmesterskap": [] }
    ]
    serieMestere = []
    serieMestreStats = {}
    norgesMestere = []
    serieOgNorgesMestere = []
    for i, lag in enumerate(eliteserieLag):
        if len(eliteserieLag[i]["seriemesterskap"]) >= 1:
            serieMestere.append(eliteserieLag[i]["lag"])
            serieMestreStats[eliteserieLag[i]["lag"]] = len(eliteserieLag[i]["seriemesterskap"])
        if len(eliteserieLag[i]["norgesmesterskap"]) >= 1:
            norgesMestere.append(eliteserieLag[i]["lag"])
        if len(eliteserieLag[i]["norgesmesterskap"]) >= 1 and len(eliteserieLag[i]["seriemesterskap"]) >= 1:
            serieOgNorgesMestere.append(eliteserieLag[i]["lag"])
    print(*serieMestere, sep=", ")
    print(*norgesMestere, sep=", ")
    print(*serieOgNorgesMestere, sep=", ")
    #lambda sort
    for lag, count in sorted(serieMestreStats.items(), key=lambda x: x[1], reverse=True):
        print(lag, count)
    
    #manual search
    first = None
    firstLag = None
    last = None
    lastLag = None
    for i, lag in enumerate(eliteserieLag):
        for seier in eliteserieLag[i]["seriemesterskap"]:
            if first == None or seier < first:
                first = seier
                firstLag = eliteserieLag[i]["lag"]
            if last == None or seier > last:
                last = seier
                lastLag = eliteserieLag[i]["lag"]
    print(first, firstLag)
    print(last, lastLag)
oppgave5()