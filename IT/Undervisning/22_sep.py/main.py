myDict = {
    "klasse_1STD":{
        "elev1": "Arne",
        "elve2": "Per",
        "nyListe": [1, 2, 3,{"navn": "Åke"}]}
}

print(myDict["klasse_1STD"]["nyListe"][3]["navn"])

for klasse in myDict:
    print(klasse)
    for elev in myDict[klasse]:
        print(elev)
        for ting in myDict[klasse][elev]:
            print(ting)
            if type(ting) == dict:
                for tulleTing in ting:
                    print(ting[tulleTing]) 
         
