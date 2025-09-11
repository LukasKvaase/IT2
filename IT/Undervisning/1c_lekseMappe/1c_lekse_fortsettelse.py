from random import randint

def oppgave5():
    #variabler
    alfabet = "abcdefghijklmnopqrstuvwxyzæøå"
    text = """
    Fotografi er en permanent gjengivelse av et bilde ved hjelp av lys, optikk og lysfølsomme materiale som kan lagre bildeinformasjonen. Gjengivelsen kan være monokromatisk (sort/hvitt) eller flerfarget.

    Et fotografisk bilde dannes ved å eksponere en lysfølsom overflate, for eksempel en film eller en lysfølsom bildebrikke, for lysstråler gjennom et optisk system (kamera). Det optiske systemet kan være så enkelt som et hull, en optisk linse eller et objektiv, som er et sett av linseelementer som samler og fokuserer lysstrålene.

    Et fotografi er, i motsetning til maleri, grafikk eller andre former for bilder, en eksakt gjengivelse av motivet som dannes i eksponeringsøyeblikket.[omstridt – diskuter] Men ønsker man et mer kunstnerisk uttrykk eller av annen årsak å endre på fotoet kan man etterbehandle det enten, med manuell fargelegging, retusjering, redigering eller etterbehandling ved hjelp av forskjellig programvare.

    Fotografier har være viktige for å dokumentere historiske hendelser og dagliglivet tilbake i historien.

    """
    stats = [] # oppretter en liste for statistikk
    
    text = text.lower() # gjør alt om til små bokstaver
    
    # for alfabetChar in alfabet: # itererer gjennom hele alfabetet
    #     charCount = 0 # setter/resetter tellingen på antall bokstaver av en gitt type
    #     for textChar in text: # iterer gjennom aller tegnene i teksten
    #         if textChar == alfabetChar: # hvis bokstaven er lik boksaven som søkes legges det til i count
    #             charCount+=1
    #     stats.append([alfabetChar, charCount]) # legger til bokstav og antall inn i liste som legges i liste
        

    for alfabetChar in alfabet: # itererer gjennnom hele alfabetet
        stats.append([alfabetChar, text.count(alfabetChar)]) # legger til bokstav og antall ved hjelp av innebygd funksjon count
            
    stats.sort(key=lambda x: x[1], reverse=True) # sorterer listen med lamda funksjon for å hente antall. reverserer for å ha synkende
    
    print(f"{"Letter":8}{"count":>8}") # formatert header
    for letters in stats: # itererer gjennom statistikk
        print(f"{letters[0]:8}{letters[1]:>8}") # formatert sting for pen fremføring av data
    


def oppgave6():
    running = True
    while running: # while loop
        number = randint(1,10) # generer et tilfeldig tall mellom 1 - 10
        guess = None
        maxCount = 4
        count = 0
        while number != guess: # while som kjører så lenge gjettet tall ikke er likt som tall
            guess = input("\ngjett et tall fra 1 til 10: ")
            if guess == "e": # brexit funksjon
                running = False
                break
            if guess == number:
                print(f"\nRiktig! \n\nLa oss spille igjen, eller skriv (e) for exit.  count: {count}\n") 
            elif count > maxCount:
                print(f"\n Du gjetter for mange ganger!  count: {count}\n")
                break
            elif guess < number:
                print(f"\nDu gjettet for lavt :( count: {count}\n")
            elif guess > number:
                print(f"\nDu gjettet for høyt  count: {count}:(\n")
            else:
                print("\nUgyldig svar.\n") 
            count+=1
    
        
def oppgave7():
    n, last, current = int(input("\nn: ")), 0, 1
    for i in range(n):
        print(f"{i+1:<6}{current:>8}")
        current += last
        last = current-last
        

while True:
    print("\n--- Meny ---")
    print("5: Oppgave 5")
    print("6: Oppgave 6")
    print("7: Oppgave 7")
    print("0: Avslutt")

    valg = input("Velg oppgave: ")
    if valg == "5":
        oppgave5()
    elif valg == "6":
        oppgave6()
    elif valg == "7":
        oppgave7()
    elif valg == "0":
        print("Avslutter programmet...")
        break
    else:
        print("Ugyldig valg, prøv igjen.")