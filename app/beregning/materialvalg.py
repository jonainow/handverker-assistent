# app/beregning/materialvalg.py

def anbefal_materiale(konstruksjonstype, miljø="tørt"):
    konstruksjonstype = konstruksjonstype.lower()
    miljø = miljø.lower()

    if konstruksjonstype == "innervegg":
        if miljø == "våtrom":
            return "Anbefalt: Våtromsplater eller impregnert treverk"
        else:
            return "Anbefalt: Gipsplater, trepanel eller stålstendere"

    elif konstruksjonstype == "yttervegg":
        return "Anbefalt: Vindtettplate, isolasjon og kledning av tre eller stål"

    elif konstruksjonstype == "bærende vegg":
        return "Anbefalt: Konstruksjonsvirke eller limtre"

    elif konstruksjonstype == "tak":
        return "Anbefalt: Takstoler av tre eller stål med undertak"

    elif konstruksjonstype == "gulv":
        if miljø == "våtrom":
            return "Anbefalt: Impregnerte bjelker med gulvsponplater"
        else:
            return "Anbefalt: Bjelkelag av tre og gulvspon eller parkett"

    else:
        return "Ingen anbefaling tilgjengelig for denne typen."
