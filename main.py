import streamlit as st
import app

st.set_page_config(page_title="Wong Kito AI", page_icon="🌉")
st.title("🌉 Wong Kito AI")

# Input
text_input = st.text_area("Nak ngomong apo?", placeholder="Contoh: Saya mau makan pempek")

# Tombol
if st.button("Terjemahkan"):
    if not text_input:
        st.warning("Isi dulu lor!")
    else:
        with st.spinner("Bentar lor..."):
            # --- MEMANGGIL FUNGSI DARI FILE SEBELAH ---
            hasil = app.get_palembang_translation(text_input)
            
            # Cek apakah hasil balikan berupa error atau bukan
            if "Error:" in hasil:
                st.error(hasil)
            else:
                st.success("Ini basonyo:")
                st.markdown(f"### {hasil}")