import streamlit as st

def style_background_home():
    st.markdown("""
            <style>
                    .stApp{
                        background-color: #5865f2 !important;
                }
                    .stApp div[data-testid="stColumn"]{
                        background-color:#E0E3FF !important;
                        padding: 2.5rem !important;
                        border-radius: 5rem !important;
                }
            </style>  
                """, unsafe_allow_html=True)
def style_background_dashboard():
    st.markdown("""
            <style>
                    .stApp{
                        background-color: #E0E3FF !important;
                }
            </style>  
                """, unsafe_allow_html=True)
def style_base_layout():
    st.markdown("""
            <style>
            

               /*hide top tool bar of streamlit*/
                    #MainMenu, footer,header{
                     visibility:hidden;
                }
                .block-container{
                    padding-top:1.5rem !important;
                }h1{
                    font-size:3.5rem !important;
                    line-height:1.1 !important;
                    margin-bottom:0rem !important;
                    color:white !important;
                }
                h2{
                    
                    font-size:0 rem !important;
                    line-height:0.7 !important;
                    margin-bottom:0rem !important;
                    color:black !important;
                }
               
                h3, h4, p {
                font-family: 'Outfit', sans-serif;    
                }
                
                button{
                    border-radius:1.5rem !important;
                    background-color:#800080 !important;
                    color:white !important;
                    padding:10px, 20px !important;
                    border:none !important;
                    transition:transform 0.25s ease-in-out !important;
                }
                button[kind="secondary"]{
                    border-radius:1.5rem !important;
                    background-color:#EB459E !important;
                    color:black !important;
                    padding:10px, 20px !important;
                    border:none !important;
                    transition:transform 0.25s ease-in-out !important;
                }
                button[kind="tertiary"]{
                    border-radius:1.5rem !important;
                    background-color:#EBA7EC !important;
                    color:black !important;
                    padding:10px, 20px !important;
                    border:none !important;
                    transition:transform 0.25s ease-in-out !important;
                }
                button:hover{
                transform:scale(1.05)
                }
                
                 
            </style>  
                """, unsafe_allow_html=True)