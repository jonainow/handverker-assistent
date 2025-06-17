# app/beregning/bjelkelag.py

def anbefal_bjelkedimensjon(spenn_m, lasttype):
    lasttype = lasttype.lower()

    if lasttype == "lett" or lasttype == "terrasse":
        faktor = 30
    elif lasttype == "normal" or lasttype == "bolig":
        faktor = 35
    elif lasttype == "tung" or lasttype == "tak eller etasjeskille":
        faktor = 40
    else:
        faktor = 35  # standard bolig

    anbefalt_høyde_mm = int(spenn_m * faktor)
    
    # Vanlige tilgjengelige høyder
    nærmeste = min([98, 123, 148, 173, 198, 223, 248, 273, 298],
                   key=lambda x: abs(x - anbefalt_høyde_mm))

    return f"Anbefalt bjelkedimensjon: 48 x {nærmeste} mm"
