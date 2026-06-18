import streamlit as st
from supabase import create_client

# ==============================
# 🔑 CONFIG SUPABASE
# ==============================
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="Mon train", layout="centered")

st.title("Mon Train")

# ==============================
# 📝 INPUT UTILISATEUR
# ==============================
trigramme = st.text_input("Entre ton trigramme (ex: ABC)").strip().upper()

# ==============================
# 🎯 PLANNING
# ==============================
planning = {
    "00": "📍 Lundi 10h — Salle 1",
    "0": "📍 Mercredi 9h — Salle 3"
}

# ==============================
# 🔍 RECHERCHE
# ==============================
if st.button("Voir l'horaire de départ"):

    if trigramme == "":
        st.warning("⚠️ Merci d'entrer un trigramme")

    else:
        try:
            # ✅ recherche stricte (recommandé)
            res = supabase.table("train") \
                .select("train_h") \
                .eq("trigramme", trigramme) \
                .execute()

            # 🔍 RESULTAT
            if res.data and len(res.data) > 0:
                train_h = res.data[0]["train_h"]

                st.success(f"✅ RDV devant les bus avec tes bagages à : {train_h}")

                # ✅ afficher planning
                if train_h in planning:
                    st.info(f"📅 {planning[train_h]}")
                else:
                    st.warning("⚠️ Sois bien à l'heure et pour plus d'infos cf WhatsApp ! ⚠️")

            else:
                st.error("❌ Aucun train trouvé pour ce trigramme")

        except Exception as e:
            st.error(f"🔥 Erreur : {e}")
