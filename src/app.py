# app.py
import streamlit as st
from database import SessionLocal
from models.code_step import CodeStep

session = SessionLocal()
for r in session.query(CodeStep).all():
  st.write(r.step, r.code)

st.title("app")

st.json({'foo':'bar','fu':'ba'})

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])

# You can also use "with" notation:
with tab1:
  st.radio('Select one:', [1, 2])
  st.write("this is tab 1")

with tab2:
  st.radio('Select one:', [3, 4])
  st.write("this is tab 2")