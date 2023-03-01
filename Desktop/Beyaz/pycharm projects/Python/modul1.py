Programlara_dili = ["Python", "C", "Java"]
def faktoriyel(a):
    """
İçine Girdiğiniz Sayının Faktoriyelini bulur.
Negatif sayı girmeyiniz.

"""
    fakt = 1
    if ( a == 1 or a == 0 ):
        return 1
    else:
        while(1<a):
            fakt *= a
            a -= 1
        return fakt
    print(fakt)


