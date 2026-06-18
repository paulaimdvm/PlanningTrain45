import streamlit as st
from supabase import create_client

# ==============================
# 🔑 CONFIG SUPABASE
# ==============================
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="Mon planning", layout="centered")

st.title("Mon Train")

# ==============================
# 📝 INPUT UTILISATEUR
# ==============================
trigramme = st.text_input("Entre ton trigramme (ex: ABC)").upper().strip()

# ==============================
# 🎯 PLANNING (à adapter librement)
# ==============================
planning = {
    "erreur": "📍 Lundi 10h — Salle 1",
    "erreur": "📍 Mardi 14h — Salle 2",
    "erreur": "📍 Mercredi 9h — Salle 3",
    

# ==============================
# 🔍 RECHERCHE
# ==============================
if st.button("Voir l'horaire de mon train"):

    if trigramme == "":
        st.warning("⚠️ Merci d'entrer un trigramme")
    else:
        try:
            # ✅ chercher l'inscription
            res = supabase.table("train") \
                .select("*") \
                .ilike("trigramme", trigramme) \
                .execute()

            # 🔍 RESULTAT
            if res.data:
                activite = res.data[0]["train"]

                st.success(f"✅ Ton train est à : {train}")

                # ✅ afficher planning
                if activite in planning:
                    st.info(f"📅 {planning[activite]}")
                else:
                    st.warning("⚠️ Tu as rendez-vous avant au lieu pour aller vers la gare ⚠️ 
                    Sois à l'heure (cf. message Whatsapp) ! ")

            else:
                st.error("❌ Aucun train trouvé pour ce trigramme")

        except Exception as e:
            st.error(f"🔥 Erreur : {e}")
