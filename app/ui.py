# app/ui.py

import streamlit as st
from beregning.areal import beregn_veggareal
from beregning.materialmengde import beregn_antall_plater
from beregning.materialvalg import anbefal_materiale
from beregning.bjelkelag import anbefal_bjelkedimensjon


st.set_page_config(page_title="Håndverker Assistent", layout="centered")

st.title("🔨 Håndverker Assistent")

valg = st.sidebar.selectbox("Velg funksjon:", [
    "Beregn veggareal",
    "Beregn antall gipsplater",
    "Anbefal materiale",
    "Beregn bjelkedimensjon"
])


if valg == "Beregn veggareal":
    st.header("📐 Beregn veggareal")
    bredde = st.number_input("Bredde (meter)", min_value=0.0, step=0.1)
    høyde = st.number_input("Høyde (meter)", min_value=0.0, step=0.1)
    antall = st.number_input("Antall vegger", min_value=1, step=1)
    if st.button("Beregn areal"):
        areal = beregn_veggareal(bredde, høyde, antall)
        st.success(f"Totalt veggareal: {areal:.2f} m²")

elif valg == "Beregn antall gipsplater":
    st.header("📦 Beregn antall gipsplater")
    areal = st.number_input("Oppgitt areal (m²)", min_value=0.0, step=0.1)
    if st.button("Beregn plater"):
        plater = beregn_antall_plater(areal)
        st.success(f"Du trenger ca. {plater} plater (inkl. 10 % ekstra)")

elif valg == "Anbefal materiale":
    st.header("📋 Anbefal materiale")
    konstruksjon = st.selectbox("Konstruksjonstype", ["innervegg", "yttervegg", "bærende vegg", "tak"])
    miljø = st.selectbox("Miljø", ["tørt", "våtrom", "utendørs"])
    if st.button("Få anbefaling"):
        anbefaling = anbefal_materiale(konstruksjon, miljø)
        st.info(anbefaling)
        
elif valg == "Beregn bjelkedimensjon":
    st.header("📏 Beregn bjelkedimensjon for bærende konstruksjon")
    spenn = st.number_input("Spenn (meter)", min_value=0.0, step=0.1)
    last = st.selectbox("Type last", ["Bolig", "Terrasse", "Tak eller etasjeskille"])
    if st.button("Beregn bjelker"):
        anbefaling = anbefal_bjelkedimensjon(spenn, last)
        st.success(anbefaling)
