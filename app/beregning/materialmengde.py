# app/beregning/materialmengde.py

def beregn_antall_plater(areal_m2, plate_bredde=1.2, plate_høyde=2.4, avkapp_prosent=10):
    """Beregner antall plater basert på areal og platestørrelse"""
    plate_areal = plate_bredde * plate_høyde
    antall_plater = areal_m2 / plate_areal
    antall_med_avkapp = antall_plater * (1 + avkapp_prosent / 100)
    return round(antall_med_avkapp)
