# app/beregning/materialvalg.py

def anbefal_materiale(konstruksjonstype, miljø="tørt"):
    konstruksjonstype = konstruksjonstype.lower()
    miljø = miljø.lower()

    if konstruksjonstype == "innervegg":
        if miljø == "våtrom":
            return "Anbefalt: Våtromsplater (f.eks. Litex eller ProPlate)"
        else:
            return "Anbefalt: Gipsplater eller trepanel"

    elif konstruksjonstype == "yttervegg":
        return "Anbefalt: Vindtettplate + isolasjon + kledning"

    elif konstruksjonstype == "bærende vegg":
        return "Anbefalt: Konstruksjonsvirke (f.eks. 48x148 / 48x198)"

    elif konstruksjonstype == "tak":
        return "Anbefalt: Takstoler og undertak (spon eller OSB), evt. vindsperre"

    else:
        return "Ingen anbefaling tilgjengelig for denne typen."
