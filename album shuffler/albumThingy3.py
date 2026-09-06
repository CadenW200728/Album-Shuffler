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
    "https://music.youtube.com/playlist?list=OLAK5uy_nhQ2EVQRbH-uWJbaesYXRQGZMzinN0qqg",
    "https://music.youtube.com/playlist?list=OLAK5uy_ljXkQlhVlWyV7BxSxMMzgOLbzYS_-JPt4",
    "https://music.youtube.com/playlist?list=OLAK5uy_lhJqCASxMaouiWs66Vizl61JadKWAcupI",
    "https://music.youtube.com/playlist?list=OLAK5uy_leUaxUf5Fy9d5cllRNdNOEljXZfFU5yEA",
    "https://music.youtube.com/playlist?list=PLmOldskd2VbL7_t-NE9p6rEboq_v0AHko",
    "https://music.youtube.com/playlist?list=OLAK5uy_nnY0s7ogC6wEI85M_C9NrMLLv6lWOQxqY"

]

movie = ["https://music.youtube.com/playlist?list=PLpRjkOHBe_TgmznCle__jWDhoV4aFgCjw",
        "https://music.youtube.com/playlist?list=OLAK5uy_mE5qofGJLnPOnR-msAa-lIoYPuzCJsbqg",
        "https://music.youtube.com/playlist?list=OLAK5uy_kuK1ARRMlYf4cu68la2kIUz8Ji2KIoT0c",
        "https://music.youtube.com/playlist?list=OLAK5uy_k8XkxQFGZhSX8gENqaH6pg1xz8vOTnzQs",
        "https://music.youtube.com/playlist?list=PLy7D1yMoeOF6TG5G6-RCuzgClxXGsFB0U",
        "https://music.youtube.com/playlist?list=OLAK5uy_nufJ7u7NEq73QyRj78Bsr60c4Fl9xHfhw",
        "https://music.youtube.com/playlist?list=OLAK5uy_n90Ggeh_hENyTJCiF0bD6y914EN5WTDcI",
        "https://music.youtube.com/playlist?list=OLAK5uy_myCew62AQBU-0W19WPM133HicoHJUxQII",
         ]

daft = ["https://music.youtube.com/playlist?list=OLAK5uy_mfg6NA2Q6rWf2THgxCy4kLKAu7gSy0OrA",
        "https://music.youtube.com/playlist?list=OLAK5uy_mz6eafmqdRHSaR4IwG0ll6J6rgv0_ZpGw",
        "https://music.youtube.com/playlist?list=OLAK5uy_mEC7F1xzswzJY4ljJCZxhq_l3ZKVwdAE0",
        "https://music.youtube.com/playlist?list=OLAK5uy_kNhM2yaBTOVwrcZJepB1C9P3-n5_Sfy5c"]

badmusic = ["https://music.youtube.com/playlist?list=OLAK5uy_lcDE9n6x4ySCRHAQ3xhqEAeIQQXpusa4A"]

kdot = [
    "https://music.youtube.com/playlist?list=OLAK5uy_ltzpNncYEZXvj2j59gFt303ciBHYBdVHg",
    "https://music.youtube.com/playlist?list=OLAK5uy_mP3LkB5O8-7fbX4X5eRBKU1cLXMwG2Bm8",
    "https://music.youtube.com/playlist?list=OLAK5uy_k5mTVnRXWZS09BKOn7_zelGY5k0beDga4",
    "https://music.youtube.com/playlist?list=OLAK5uy_lONzr2WDx7bOXJWJNC1YloDy76sCBUHyw",
    "https://music.youtube.com/playlist?list=OLAK5uy_kqTVP9PZstmXkaT9gXjuTXdXwxM9_Jroc",
    "https://music.youtube.com/playlist?list=OLAK5uy_m_zl1RNdUJwiB2Yi1ExSwNQ0Vh3U0-LBQ",

]

beatles = ["https://music.youtube.com/playlist?list=OLAK5uy_mSQvIHDf7UlQDi_TcmXbq_7aY8-7-99W8",
           "https://music.youtube.com/playlist?list=OLAK5uy_mM7D2y0gEKaLqXbK-nWgih4f-YHCmU-Ac",
           "https://music.youtube.com/playlist?list=OLAK5uy_kNANFuHzr_3bZH3S5aXxOT4X1ouKnjY4k",
           "https://music.youtube.com/playlist?list=OLAK5uy_lY9ogwwjXTNY47v6bolSPmWE5gihcV8aQ",
           "https://music.youtube.com/playlist?list=OLAK5uy_lJlBwY8J0ezSODyk5eXLUlq8wCBVGybD4",
           "https://music.youtube.com/playlist?list=OLAK5uy_lirCIxLpU2odTVLZ_Sbo1wZaeu5IStivs",
           "https://music.youtube.com/playlist?list=OLAK5uy_kNH5_0dq0SINuzQFBDRKoCCcO0aTcGxoo",
           "https://music.youtube.com/playlist?list=OLAK5uy_k0N28ttgCjdEqyy02W7h0v1Kg78hs9AnM",
           "https://music.youtube.com/playlist?list=OLAK5uy_kxk_lSv8ZOf-eZeqp627XdaEIOozc34Ec",
           "https://music.youtube.com/playlist?list=OLAK5uy_ngFkZaiOccd84mOWCf4mZKbJrvsPzm8BE",
           "https://music.youtube.com/playlist?list=OLAK5uy_nd7utIrpWh7bhjrtPLbtuWzbZ5o9u48fU",
           "https://music.youtube.com/playlist?list=OLAK5uy_lqcFZTOPHGwcnP0nYMzNuY0IES0fl7Fe4",
           "https://music.youtube.com/playlist?list=OLAK5uy_nt1EGRLs8dljkOjozHvbrbSy_QEzn316s"]

nirvana = ["https://music.youtube.com/playlist?list=OLAK5uy_l33lV-pSSSn7IHoVBPYrblCO9mLI5ICVc",
           "https://music.youtube.com/playlist?list=OLAK5uy_nswo1jp2sgcPk7n2cCRlEiEMfA6xLEqHE",
           "https://music.youtube.com/playlist?list=OLAK5uy_nbu8EUmXmbBb24DoOx_H7NBV_PKlo3Ku8"]

pinkfloyd = ["https://music.youtube.com/playlist?list=OLAK5uy_nCBf4OZxhktV5fD5m1MSPW-MT5Q5X1M3Y",
              "https://music.youtube.com/playlist?list=OLAK5uy_n-lE02j8pQkwGhsL5JLAPvbBAoAmxh9n8",
              "https://music.youtube.com/playlist?list=OLAK5uy_lcQR3_itj5ZqeRVJZiu-nqsAiVIyFQohg",
              "https://music.youtube.com/playlist?list=OLAK5uy_mGR_R8SnyfX250Oy5Z3FVWmkESuCN_nVU",
              "https://music.youtube.com/playlist?list=OLAK5uy_nM82AUr-l5OxTITeZBbC6MqZpk9JxD_OE",
              "https://music.youtube.com/playlist?list=OLAK5uy_lrCrcAdxFG4aMzMrebs7o9TU384xyF240",
              "https://music.youtube.com/playlist?list=OLAK5uy_klU9jB4SMO5SqEyFazPAVbDek2j0JVQxY",
              "https://music.youtube.com/playlist?list=OLAK5uy_k6DQIzfcQ94K-SZ2nlQicUOafxFeTCRaQ",
              "https://music.youtube.com/playlist?list=OLAK5uy_loKmzl_a690GUTO3O3irATW-Q60Czk9BI",
              "https://music.youtube.com/playlist?list=OLAK5uy_lPp-jqBS8UtWe9J4F_uADQZzFXr8JoOGA",
              "https://music.youtube.com/playlist?list=OLAK5uy_lWz_Ssalk7J_B0jX5efv9bOrOiMTIVPIw",
              "https://music.youtube.com/playlist?list=OLAK5uy_n_fyQF2s8mD_vYN-7uQyvNgwXd5xZNrFY",
              "https://music.youtube.com/playlist?list=OLAK5uy_kynAU1oQ9BgUqD1N9TujSDfcwA_s_dfK0",
              "https://music.youtube.com/playlist?list=OLAK5uy_mz6yoUOJXZzgMr4WLF2y0FX3nfQnhioco",
              "https://music.youtube.com/playlist?list=OLAK5uy_kIzCuwkECvcJgM0awvX4ACzkt3EvPydqI"]

foofighters = ["https://music.youtube.com/playlist?list=OLAK5uy_lWAJFIKQJKBnaVplK6ywu6U5HQQifQJHY",
               "https://music.youtube.com/playlist?list=OLAK5uy_keHNwGuJwFejyBIaVLfXlsRA-kPl2MXTQ",
               "https://music.youtube.com/playlist?list=OLAK5uy_mW9ozOeQDl63XvRyc-L9LewDnqu_ZfZI0",
               "https://music.youtube.com/playlist?list=OLAK5uy_n-cqA721qq5Va8PRNHK2jmNUYdxTF7CfI",
               "https://music.youtube.com/playlist?list=OLAK5uy_lkxVUNUmQt2cXv8zeQIW9qpBdU4le13yg",
               "https://music.youtube.com/playlist?list=OLAK5uy_nxn8Zv2ewQJB-bOHbholRKxn_-3-zaTx0",
               "https://music.youtube.com/playlist?list=OLAK5uy_kPx0BRDUEVby17Y40h2KOC9Cfwvr1dM_k",
               "https://music.youtube.com/playlist?list=OLAK5uy_ntJojboFE3gTUB4vppIK8N6_LwsGrTtGA",
               "https://music.youtube.com/playlist?list=OLAK5uy_mTM3fbXnDfIyUwOOSvCTi5dJvRNTP1bqE",
               "https://music.youtube.com/playlist?list=OLAK5uy_k4xx-4vNuW2YGFFBjA5az4MAxEPinuAQo",
               "https://music.youtube.com/playlist?list=OLAK5uy_lBzRHIupm6Em5U6sjeDEnhSwjQg7Yi3Wk",
               "https://music.youtube.com/playlist?list=OLAK5uy_mK_-lq7b_lUQJK_H0PoIQZIsIl6a4Gkrg"]
drake = ["https://music.youtube.com/playlist?list=OLAK5uy_mtzMkd37EtMYa866S5deO_g8IHoHwm5WY",
         "https://music.youtube.com/playlist?list=OLAK5uy_lcDE9n6x4ySCRHAQ3xhqEAeIQQXpusa4A",
         "https://music.youtube.com/playlist?list=OLAK5uy_mDJQ6HxsusQs5OIRkgyF9zixrv1PHhowE",
         "https://music.youtube.com/playlist?list=OLAK5uy_mOGt00VGQtgn7VM3LyVC5gIAUsx6Gd9XU",
         "https://music.youtube.com/playlist?list=OLAK5uy_kY8dtv44revO4EYCIUOAgYfrWo9a_DQu0",
         "https://music.youtube.com/playlist?list=OLAK5uy_nASZ91BLkwjQyVGZYqyYxfNafT5Np5g8A",
         "https://music.youtube.com/playlist?list=OLAK5uy_mohWCfICkz2hGDpW37VfU5BhNGBp__g8E",
         "https://music.youtube.com/playlist?list=OLAK5uy_na_qnYnNCbsE864dnFpM8S78rZxBM9ksA",
         "https://music.youtube.com/playlist?list=OLAK5uy_nXeJmdRleb0huIiqiajJHNwU1nQyxJ4jg",
         "https://music.youtube.com/playlist?list=OLAK5uy_lKouR3b3iarfXfc31uj52NU9wcVKfZ5Yg",
         "https://music.youtube.com/playlist?list=OLAK5uy_mfmtfL0TzphJF46gDiCIyj2Lwk23eibtY",
         "https://music.youtube.com/playlist?list=OLAK5uy_mmdeqCJfSAiPkcJiowuR220YCy-9zIN2c",
         "https://music.youtube.com/playlist?list=OLAK5uy_lKHB7W1HFDIXp0CQDja4KOlR5HNSeYG6U",
         "https://music.youtube.com/playlist?list=OLAK5uy_lDzklZqvl-Xyh-qotlTUozpaMDUPKr1Y8",
         "https://music.youtube.com/playlist?list=OLAK5uy_mXmZ7g86CVTU7i1_zrXw_KRLPFwxGJq1E"]
mj = ["https://music.youtube.com/playlist?list=OLAK5uy_kcoRvXuX8AWWr5W2HyOPnwp4i11UfdryY",
      "https://music.youtube.com/playlist?list=OLAK5uy_lQq3vGlP81JruELvDx3izUej85ZXIhoLA",
      "https://music.youtube.com/playlist?list=OLAK5uy_l1U925dsiDi2DqlG-KCbODG6BaibpxbQE",
      "https://music.youtube.com/playlist?list=OLAK5uy_m9ELAPGUnHtlIMV6T_bDb6YsiSKu5cI7M",
      "https://music.youtube.com/playlist?list=OLAK5uy_nsZm9AscLdmJf4wE2Af8D3JvFzfPCKdEs",
      "https://music.youtube.com/playlist?list=OLAK5uy_kUDpgk4yWnyIVfpftIeU0icvhlKAROmx0"
      ]

badmusic = ["https://music.youtube.com/playlist?list=OLAK5uy_lcDE9n6x4ySCRHAQ3xhqEAeIQQXpusa4A"]

st.title("Album Shuffler")
musicChoice = st.text_input("shuffles through an artist's albums", )
st.caption("youtube music only, name the artist or type 'video game' for video game music")
st.caption("project will get constantly updated with album suggestions from u guys, so rn it doesn't have too many albums outside of my favorite artists")
if musicChoice:
    choice = musicChoice.lower().strip()
    
if musicChoice:
    choice = musicChoice.lower().strip()
    
    if choice in ["kanye", "ye", "kanye west", "ye west"]:
        url = random.choice(kanye)
    elif choice == "radiohead":
        url = random.choice(radiohead)
    elif choice in ["tyler", "tyler the creator"]:
        url = random.choice(tyler)
    elif choice in ["vg", "video game"]:
        url = random.choice(vg)
    elif choice == "bad music":
        url = random.choice(badmusic)
    elif choice in ["kdot", "kendrick", "kendrick lamar"]:
        url = random.choice(kdot)
    elif choice in ["beatles", "the beatles"]:
        url = random.choice(beatles)
    elif choice in ["nirvana"]:
        url = random.choice(nirvana)
    elif choice in ["pink floyd", "pinkfloyd"]:
        url = random.choice(pinkfloyd)
    elif choice in ["foo fighters", "foofighters"]:
        url = random.choice(foofighters)
    elif choice in ["daft punk", "daftpunk"]:
        url = random.choice(daft)
    elif choice in ["drake"]:
        url = random.choice(drake)
    elif choice in ["mj", "michael jackson", "michaeljackson"]:
        url = random.choice(mj)
    else:
        url = None
        
    if url:
        st.link_button("click here pls", url)
    else:
        st.error("who????")

st.link_button("wanna add albums? click here", "https://docs.google.com/forms/d/e/1FAIpQLScHWov8uIiYv_lZKnfjKkjdjZxGSIihmab4VLbwQvvlmmsiUw/viewform?usp=header")
#python3 -m streamlit run "albumThingy3.py" 
st.markdown("![kirbee](https://media.tenor.com/ZLHdbFbs26sAAAAj/kirby-cute.gif)")
