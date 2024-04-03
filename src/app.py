# app.py
import streamlit as st
from database import SessionLocal
from models.code_step import CodeStep

def code_step_panel(labels: list[str]) -> None:
  col1, col2 = st.columns([1, 5])

  with col1:
    chose: int = st.radio('Steps:', options=range(len(labels)), format_func=labels.__getitem__)

  with col2:
    st.code(code_steps[chose].code, language="python", line_numbers=True)

session: SessionLocal = SessionLocal()
code_steps: list[CodeStep] = session.query(CodeStep).order_by(CodeStep.step).all()
code_step_panel([f"Step {i.step}" for i in code_steps])

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
