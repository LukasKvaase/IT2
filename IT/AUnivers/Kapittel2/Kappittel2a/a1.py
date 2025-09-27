import math as m
import datetime as dt
#TODO:
#1. 

class User:
    def __init__(self, name, username, email, phonenumber):
        self.name = name
        self.username = username 
        self.email = email
        self.phonenumber = phonenumber
        
user1 = User("Lukas", "lukaskvaase", "xxx@gmail.com", "+xxx")

print(user1.phonenumber)

class Planet:
    """
    Klasse for å lage planet-objekter.
    Parametre:
    navn (str): Planetens navn
    solavstand (float): Avstand fra sola i millioner km
    radius (float): Planetens radius i km
    antallRinger = 0 (int): Antall ringer rundt planeten
     """
    def __init__(self, navn:str, solavstand:float, radius:float, antallRinger:int = 0):
        """
        Konstruktør
        """
        self.navn = navn
        self.solavstand = solavstand
        self.radius = radius
        self.antallRinger = antallRinger
        
    def volum(self):
        """
        beregn volum av gitt planet
        """
        return (4/3) * m.pi * self.radius**3
    
    def overflate(self):
        """
        Beregn overflate av gitt planet
        """
        return 4 * m.pi * self.radius**2
    
    def visInfo(self):
        """
        vis info om gitt planet
        """
        print(f"Planeten {self.navn} er {self.solavstand} millioner km unna sola og har radius {self.radius} km.")
    
    def __str__(self):
        return f"__str__Planeten {self.navn} er {self.solavstand} millioner km unna sola og har radius {self.radius} km."
    
    
jupiter = Planet("Jupiter", 778.5, 69911, 4)


print(jupiter.antallRinger)
print(jupiter.volum())
print(jupiter.overflate())
jupiter.visInfo()
print(jupiter)

class Person:
    def __init__(self, name:str, sirname:str, yearBorn:int):
        self.name = name
        self.sirname = sirname
        self.yearBorn = yearBorn

Lukas = Person("Lukas", "Kvaase", 1900)

print(Lukas.name, Lukas.sirname)



# Lager objekter for fødselsdato og datoen i dag
fodseslsdato = dt.datetime(2007, 1, 2) # år, måned, dag
dagensDato = dt.datetime.now()
# Skriver ut fødselsdato på en fin måte
print(fodseslsdato.strftime("%d.%m.%Y"))
# Beregner tidsforskjell mellom de to datoene
tidsforskjell = dagensDato - fodseslsdato
# Skriver ut tidsforskjell i dager delt på 365 (finner alderen)
print(tidsforskjell.days)



class Rektangel:
  """Klasse for å representere et rektangel"""
  def __init__(self, lengde:int, bredde:int):
    """Konstruktør"""
    self.lengde = lengde
    self.bredde = bredde
  
  def areal(self):
    """Metode for å beregne areal"""
    return self.lengde * self.bredde

  def visInfo(self):
    """Skriver ut informasjon om et rektangel"""
    print(f"Rektangel med lengde {self.lengde} og bredde {self.bredde} har areal {self.areal()}")

class Kvadrat(Rektangel):
  """Klasse for å representere et kvadrat"""
  def __init__(self, sidekant:int):
    super().__init__(sidekant, sidekant)
  
  def visInfo(self):
    """Skriver ut informasjon om et kvadrat"""
    print(f"Kvadrat med sidelengde {self.lengde} har areal {self.areal()}")

# Liste som skal holde på rektangler
rektangler = []

# Lager og legger til noen rektangler
rektangler.append(Rektangel(2, 5))
rektangler.append(Rektangel(4, 3))
rektangler.append(Rektangel(5, 6))

for r in rektangler:
  r.visInfo()
  
  
class Medlem:
  medlemsnummer = 0

  def __init__(self, fornavn, etternavn):
    self.fornavn = fornavn
    self.etternavn = etternavn
    Medlem.medlemsnummer = Medlem.medlemsnummer + 1
    self.medlemsnummer = Medlem.medlemsnummer

per = Medlem("Per", "Lund")
kim = Medlem("Kim", "Svendsen")
kelly = Medlem("Kelly", "Brixton")

print(f"{per.fornavn} har medlemsnummer {per.medlemsnummer}")
print(f"{kim.fornavn} har medlemsnummer {kim.medlemsnummer}")
print(f"{kelly.fornavn} har medlemsnummer {kelly.medlemsnummer}")