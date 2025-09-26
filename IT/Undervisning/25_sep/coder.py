def translateKey(i, key):
    """Translates key. Takes key and i as iterated through text"""
    x = key["x"]
    y = key["y"]
    z = key["z"]
    return (x*i**3)+(y*i**2)+(z*i)+(x*y*z)

def safe_chr_ascii(tallkode):
    """Safe chr. Not outside range of normal Ascii"""
    return chr(32 + (tallkode % 400))


def safe_ord_ascii(char):
    """Safe ord. Not outside range of normal Ascii"""
    return (ord(char) - 32) % 400


def encode(tekst, key):
    """encodes text with a given key(save for use for decoding)"""
    nytekst = ""
    for i in range(len(tekst)):
        tallkode = safe_ord_ascii(tekst[i])  
        tallkode += (translateKey(i, key) * (i+1)) + 1
        nytekst += safe_chr_ascii(tallkode)
    return nytekst


def decode(tekst, key):
    """decodes text with a given key(same as encoded with)"""
    nytekst = ""
    for i in range(len(tekst)):
        tallkode = safe_ord_ascii(tekst[i])  
        tallkode -= (translateKey(i, key) * (i+1)) + 1
        nytekst += safe_chr_ascii(tallkode)
    return nytekst