def translateKey(i, key):
    """Translates key. Takes key and i as iterated through text"""
    x = key["x"]
    y = key["y"]
    z = key["z"]
    return (x*i**3)+(y*i**2)+(z*i)+(x*y*z)

ALLOWED_CHARS = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Uppercase
    "abcdefghijklmnopqrstuvwxyz"  # Lowercase
    "0123456789"                  # Digits
    ' .,!?;:-_()[]{}"'            # Common punctuation
    "æøåÆØÅ"                      # Norwegian letters
)

def safe_chr_ascii(tallkode):
    """Return a safe printable character including Norwegian letters."""
    return ALLOWED_CHARS[tallkode % len(ALLOWED_CHARS)]

def safe_ord_ascii(char):
    """Return the index of a safe printable character including Norwegian letters."""
    return ALLOWED_CHARS.index(char)

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