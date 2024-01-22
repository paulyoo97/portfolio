import streamlit as st
st.set_page_config(page_title="Contact", page_icon="", layout="wide")    # layout by default is centered.
st.sidebar.success("Select a page above.")

st.title("Contact \U0001F4EC")

# Understand this
def st_button(url, label, font_awesome_icon):
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)
    button_code = f'''<a href="{url}" target=_blank><i class="fa {font_awesome_icon}"></i>   {label}</a>'''
    return st.markdown(button_code, unsafe_allow_html=True)

st_button(url="paulyoo97@outlook.com", label="Email", font_awesome_icon="fa-solid fa-envelope")
st_button(url="https://www.linkedin.com/in/paul-yoo97/", label="LinkedIn", font_awesome_icon="fa-linkedin")
st_button(url="https://github.com/paulyoo97", label="Github", font_awesome_icon="fa-brands fa-github")
