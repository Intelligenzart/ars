 
import streamlit as st
import st_player
st.title("Ars Europa Channel")


tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10= st.tabs(["Home", "Immortali", "Decameron", "Simboli nell'Arte", "Sacrum", "Capolavori", "Historica", "Cultural Heritage", "Principi della Poesia", "Simboli, miti e leggende"])

with tab1:
   st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVE2Onr5TDiuvdWMTJAD6dC7V4etiVO6XrBYTQnOoAtHiKFkFfxVK1vQS3jsilaMjPHK7FydecZY2YnHZQEv-U9dQ9j3Jl4KLF4q8VuIoIrpzg_iLcLXavCHXSUJGC7iIHxLpmSzakUYOWDLALxuQbvKPsetm-eegh4w76DUZiW6DTLxRA_JCZmAEKRg/s2028/PROMO5.jpg", width=400)
   st.markdown("<h2 style='text-align: center; color: white;'>Video e documentari di Arte, Storia, Cultura</h2>", unsafe_allow_html=True)
   st.markdown("<h5 style='text-align: justify; color: white;'>Arte, Storia, Cultura, Formazione e Comunicazione nella nuova Era Digitale. </h5>", unsafe_allow_html=True)
   st.markdown("<h5 style='text-align: justify; color: white;'>Questi sono gli ingredienti della nostra attività, questa la nostra alchimia. Scopri le nostre produzioni video, assapora il piacere della Cultura. </h5>", unsafe_allow_html=True)
   st.markdown("<h5 style='text-align: justify; color: white;'>Ogni 5 giorni una nuova opera.</h5>", unsafe_allow_html=True)
  

with tab2:
   st.header("Immortali - la tragedia greca illustrata")
   st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEQg7e37bXap_mqdykKlgd5kgkkcqkhxp-KN9Fj-RRa7UESHe7QkM1GF2VnLdDNsoyEPOz1zZvMLGE0aamvrIhT0jmicCeSib3QnYwqFtnWzOWvFzN_PcOgC8c0UoXEAmDs1E00g_22e8LNugEgLLsP3V9ja2QH8-Vm8OMbH5rOmNQhDguNOqZ/s320/immortali.jpg", width=400)
   if st.button('Guarda le tragedie greche illustrate'):
    st_player("https://www.youtube.com/playlist?list=PL9Z4DZPRiAHIwr1341rsiU57K-6qXrKp7")
   else:
    st.write('La tragedia greca narrata, animata e illustrata con immagini iperrealistiche, con la spiegazione finale dei significati di ciascuna opera.')


with tab3:
   st.header("Decameron - le novelle di Boccaccio illustrate")
   st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMl7-Zvt5nNG5AjW_SbySRtD0vIJ-yvExOLxtVXeZvm5kuzWk6j-Rb6LK8VqqfZXzVIQu6nFKLjuNf_oZwjPE4OLibB-IxPnBMq_IZYVs2B5bRIJDSan8gxP9mo_BuYwgnLB3-U5iO2YYuFcSKg5RKMaPX-yRjVHia8J1_bB52hVZdYMc1eTWg/s320/decameron.jpg", width=400)
   if st.button('Guarda il DECAMERON illustrato'):
    st_player("https://www.youtube.com/playlist?list=PL9Z4DZPRiAHKUw44W1OAaLtsc8I4LHDy3, height=int")
   else:
    st.write('Le novelle del Decameron illustrate, animate e narrate, in modo semplice, divertente, talvolta malizioso, ironico o giocoso, ma sempre profondo.')

with tab4:
   st.header("Simboli nell'arte - i significati nascosti nei capolavori")
   st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3VAykz4BfaNDVpKDd2VuUN_P4jkp8VVu9JrSkjC_kU63U--s5XuISbO14zY16yhxUNapLkoIy3DYMYjZye3DsJs6x0SiQkAYWPWdgCsyjG-XP_FIcUtMdCWir-gDF9xpRWXHckcICIFMwKv-n8p10wIyW21VRiozI3IOMxue-U_z5MRRmEdZc/s320/simboli%20arte.jpg", width=400)
   if st.button('Guarda i documentari di simbologia artistica'):
    st_player("https://www.youtube.com/playlist?list=PL9Z4DZPRiAHJwfgf0zDT-z2GzAPkduaLI")
   else:
    st.write('I simboli celati nelle più grandi opere artistiche e la spiegazione del loro significato')

with tab5:
   st.header("SACRUM - i simboli nelle religioni")
   st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1OLMcgeStxXT3ar2ItD0g33JBPLnP6WyQd5oQ0C5QXb27OBggmhb5Yu93Wuh8nKsxQE9w43AFzU-kJbwllGya86CAhhhEkXwCVdkFLER1YUyO4wkvcF8X4OtPp-EcoYv80Mdl_n7o9GUa6EyIkl-HrvTQUqHDEDBoh6bqQw5sgwvLOa6BrxIq/s1920/SACRUM.jpg", width=400)
   if st.button('Guarda i documentari di simbologia religiosa'):
    st_player("https://www.youtube.com/playlist?list=PL9Z4DZPRiAHKrVGywpn_dXBozaUdby7UM")
   else:
    st.write('I simboli nelle antiche religioni e la spiegazione del loro significato')


with tab6:
   st.header("Capolavori")
   st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjU10883eE5sKQOO1PaMyJUiz2AlvMkNbUwp7J5EeMnOZKeswoPXg0cx7cU9mxU1mykS_5mnvPce-0W8SRTb4vufD6V05a_QVv3V8qE3cc4_Ql2cEWspkJFdordOJuME_ubMQdSyeBlIE65v4irOKvIJlWCJX5F3sud26NakczUz3E2aJQHkuhG/s1920/capolavori.jpg", width=400)
   if st.button('Guarda le più belle opere pittoriche'):
    st_player("https://youtu.be/55aKom1mDB0?list=PL9Z4DZPRiAHLnibjEHEjFgfc7KPpAqV-K")
   else:
    st.write('I capolavori del Passato')

with tab7:
   st.header("Historica")
   st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYsa4MBY68SHIIlfK8Er3Q-I7NVjVbeK83_X2udKLr1X6tgLHtoMr7QSeOqdLPwDhAl54SJK-vaqXLMWjLPA5KNUZyBVd1VcVp1HZn6kUSpzZV73yQjSDWOldQKW1Ck9w_rSlo8PGYRr7TzJ_XKIft9hTq9DcA4lZzg4RKdSdpuFgqyH7CE3lG/s1920/Historica.jpg", width=400)
   if st.button('Guarda i documentari di Storia'):
    st_player("https://www.youtube.com/playlist?list=PL9Z4DZPRiAHLeiX7ETj1m7viYhvIuBHA2")
   else:
    st.write('La Storia antica e medievale e i suoi significati')

with tab8:
   st.header("Cultural Heritage")
   st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEignL_gZlYceDHRHlve_EMnIj5g1qq8wO56Ne-P314frmvX03gXJ1kbQ_KPKU4ra06-M1j1FW7XIiNBzK3xN---EPRJuiQA8OWolFG_LBeHRvauwNCraza0TNSfraLNlY6MXMofWNLAKd4q28MMyytQ36avx6cXwyo9ZmwOw7Kr_nRhLx6rQ-wU/s1920/Cultural%20Heritage.jpg", width=400)
   if st.button('Guarda i i luoghi, i simboli, la Storia'):
    st_player("https://www.youtube.com/playlist?list=PL9Z4DZPRiAHL7Uu39EvWF9seH7Yd2uXtd")
   else:
    st.write('I luoghi artistici e le bellezze dateci in eredità')


with tab9:
   st.header("Principi della Poesia")
   st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgns-Yhqjh_bZ-Y8uFkxserCYOZW4tj87WagMTL5D2yPDVLjjQSeLyANfBiBIkf6-kLDOAK5JcGTBoCknko8x-yOmc6pWY7qTqLVb6lSoalmbHs4geaFWg5SdCLGe4MF4G-AKNXOkotDdw-ALcFYu67YORDvyL8gWGwth5A2ABxqGVRWhX2g0Y3/s1920/principi%20letteratura.jpg", width=400)
   if st.button('Guarda i Principi della Poesia'):
    st_player("https://www.youtube.com/playlist?list=PL9Z4DZPRiAHIbBsd8BnGvOHSgoe7TybEK")
   else:
    st.write('I più grandi personaggi della Letteratura')


with tab10:
   st.header("Simboli, miti e leggende")
   st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKLLuHfMeqjOf8Qdy97sSaPyzROjEiyvzWHuFBNgpPdLKe0_ev_O8DBsw6530yQChAvQbYzZXNjQbu9d7M1E1EMUxb6KgkxLnvrGVUeBbXnzE3smghHN1EJ3W3fha6baDon6x_4MuV_GEdGoSgT_9vS0cBLc-LIBMCRD8jEM81opbN-aUN2pg5/s1920/simboli,%20miti%20e%20leggende.jpg", width=400)
   if st.button('Guarda Simboli, miti e leggende'):
    st_player("https://www.youtube.com/playlist?list=PL9Z4DZPRiAHJw9zJ__X8814oCLVA8dSiN")
   else:
    st.write('I più grandi personaggi della mitologia greca')







