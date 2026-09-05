import webbrowser
import random
import streamlit as st
import pandas as pd


kanye = [
    "https://music.youtube.com/playlist?list=OLAK5uy_mvz7Tr6ZqTX0GKxE4lP5ifCaE9Sx-AEjc",
    "https://music.youtube.com/playlist?list=OLAK5uy_ljZc-x7bxToE4yodl2ujs7w0pBU9tyqKc",
    "https://music.youtube.com/playlist?list=OLAK5uy_n4negEHWAKSsnUfvxnK-hbGuYASJ1IBa4",
    "https://music.youtube.com/playlist?list=OLAK5uy_nz1xgXV49PGli0x8q3Y1XxparfuNRbe18",
    "https://music.youtube.com/playlist?list=OLAK5uy_lh6e__g89bgNq1BF7EM9GMlXMLzwvatgA",
    "https://music.youtube.com/playlist?list=OLAK5uy_muY3sZz_bPKYuLgpQT-XpRkJlg5Ic73dw",
    "https://music.youtube.com/playlist?list=OLAK5uy_kPR4FKADrZ1hZftipUfdMuBIup-mumHHE",
    "https://music.youtube.com/playlist?list=OLAK5uy_nEFBjGaOppv2c3YRocckDXUNhmD-SjPTg",
    "https://music.youtube.com/playlist?list=OLAK5uy_nR76ycGqKvEr4hl0XwHfXDLD2ThL3mT1E",
    "https://music.youtube.com/playlist?list=OLAK5uy_lJ0yXPKvCREyQl6Bcxp6I8CAfrD-yX-VA",
    "https://music.youtube.com/playlist?list=OLAK5uy_kruMNaIC1LpQ16H50h0YBrINB4jtvVUCg",
    "https://music.youtube.com/playlist?list=OLAK5uy_mo_SIUnjlx4i6w5-P_SHrA9Cib9kkclXA",
]
radiohead = [
    "https://music.youtube.com/playlist?list=OLAK5uy_nc6afxSnmK8OFML8dF9q_0D1MBMXsGnL4",
    "https://music.youtube.com/playlist?list=OLAK5uy_m59x-hBFsC789l1_qWwFXwH3gjntwy_CA",
    "https://music.youtube.com/playlist?list=OLAK5uy_lDotrFl8LXo4UMq_XeVB1areFI_b8Par8",
    "https://music.youtube.com/playlist?list=OLAK5uy_mjfZt29ZKuw9FnglSH4_LLqWBPIPicLjI",
    "https://music.youtube.com/playlist?list=OLAK5uy_lDotrFl8LXo4UMq_XeVB1areFI_b8Par8",
    "https://music.youtube.com/playlist?list=OLAK5uy_nRHRKov8jjIYbNTQXsAfx_Rr7P7lnigYU",
    "https://music.youtube.com/playlist?list=OLAK5uy_mRDhp5c2KZe2Penu4PLevXa7z5cBk4DXY",
    "https://music.youtube.com/playlist?list=OLAK5uy_kkxS8q1obnji_VjkWtpgWgpZAzAePSSA0",
    "https://music.youtube.com/playlist?list=OLAK5uy_l2JdqQ9q-aHSQmRiz3NfIkU2kkbxd1-ps"
]
tyler = [
    "https://music.youtube.com/playlist?list=OLAK5uy_lpv17dzKsIp6huLYAxQEYFw3vK8Wsd1FQ",
    "https://music.youtube.com/playlist?list=OLAK5uy_kSIbgi-WxAiBFs28kWN1cMy7bewO3-LCs",
    "https://music.youtube.com/playlist?list=OLAK5uy_lUqR8HVQWD77rRBdA5eVCNat5EJQ7P6-s",
    "https://music.youtube.com/playlist?list=OLAK5uy_nJsodC-lrLeHCE-KZNzyhdrtKNFUC3_Tc",
    "https://music.youtube.com/playlist?list=OLAK5uy_l8rapILEWWRQYoFcT_rdRoxfCuNy1yqPU",
    "https://music.youtube.com/playlist?list=OLAK5uy_mb-jIf2zXWrfTBkdLA-sQsgJEqih8aQGo",
    "https://music.youtube.com/playlist?list=OLAK5uy_kcaRWdKExi6Op8xtUMc_3h42ADIssBfdA",
    "https://music.youtube.com/playlist?list=OLAK5uy_kT-f_xh9mVxm8IW6t58HfU7uCF9uQvsnI"
    
]
vg = [
    "https://music.youtube.com/playlist?list=OLAK5uy_nVHqThCEHTYZVtf5mTHjC8PlD43CLwUFM",
    "https://music.youtube.com/playlist?list=PLwjEXrvFo-2B7iCX61eOThc_oGihi84l9",
    "https://music.youtube.com/playlist?list=OLAK5uy_m0g1k6",
    "https://music.youtube.com/playlist?list=OLAK5uy_ljXkQlhVlWyV7BxSxMMzgOLbzYS_-JPt4",
    "https://music.youtube.com/playlist?list=OLAK5uy_lhJqCASxMaouiWs66Vizl61JadKWAcupI",
    "https://music.youtube.com/playlist?list=OLAK5uy_leUaxUf5Fy9d5cllRNdNOEljXZfFU5yEA",
    "https://music.youtube.com/playlist?list=PLmOldskd2VbL7_t-NE9p6rEboq_v0AHko"

]
badmusic = ["https://music.youtube.com/playlist?list=OLAK5uy_lcDE9n6x4ySCRHAQ3xhqEAeIQQXpusa4A"]

st.title("Album Shuffler")
musicChoice = st.text_input("shuffles through an artist's albums", )
st.caption("youtube music only, name the artist or type 'video game' for video game music")
st.caption("not every artist is here, so pls suggest some if u want")
if musicChoice:
    if musicChoice == "kanye" or musicChoice == "Kanye" or musicChoice == "KANYE" or musicChoice == "Ye" or musicChoice == "ye" or musicChoice == "YE" or musicChoice == "Kanye West" or musicChoice == "kanye west" or musicChoice == "KANYE WEST" or musicChoice == "Ye West" or musicChoice == "ye" or musicChoice == "Kanye West" or musicChoice == "kanye west" or musicChoice == "KANYE WEST":
        webbrowser.open(random.choice(kanye))
    elif musicChoice == "radiohead" or musicChoice == "Radiohead" or musicChoice == "RADIOHEAD":
        webbrowser.open(random.choice(radiohead))
    elif musicChoice == "tyler" or musicChoice == "Tyler" or musicChoice == "TYLER" or musicChoice == "Tyler the Creator" or musicChoice == "tyler the creator" or musicChoice == "TYLER THE CREATOR":
        webbrowser.open(random.choice(tyler))
    elif musicChoice == "vg" or musicChoice == "VG" or musicChoice == "Vg" or musicChoice == "Video Game" or musicChoice == "video game" or musicChoice == "VIDEO GAME":
        webbrowser.open(random.choice(vg))
    elif musicChoice == "bad music" or musicChoice == "Bad Music" or musicChoice == "BAD MUSIC":
        webbrowser.open(random.choice(badmusic))
    else: 
        st.error("who????")

if st.button("wanna add albums? click here"):
    webbrowser.open("https://docs.google.com/forms/d/e/1FAIpQLScHWov8uIiYv_lZKnfjKkjdjZxGSIihmab4VLbwQvvlmmsiUw/viewform?usp=publish-editor")
#python3 -m streamlit run "albumThingy3.py" 
st.image("images/just-wanted-to-drop-by-and-say-this-is-my-favorite-gif-of-v0-jzr6kdt6bb771.gif.png")
