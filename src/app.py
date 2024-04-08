# app.py
import streamlit as st
from database import SessionLocal
from models.code_step import CodeStep

session: SessionLocal = SessionLocal()

def code_step_panel(code_steps: list[CodeStep]) -> None:
  chose: int = st.slider('Steps', min_value=0, max_value=len(code_steps)-1, value=0, step=1)
  st.code(code_steps[chose].code, language="python", line_numbers=True)

def refresh_panel() -> None:
  st.session_state['CodeStep'] = session.query(CodeStep).order_by(CodeStep.step).all()
  code_step_panel(code_steps=st.session_state['CodeStep'])

refresh_panel()
newCode = st.text_area("Code")
if st.button("Add Code"):
  newCodeStep = CodeStep(code=newCode, step=len(st.session_state['CodeStep'])+1)
  session.add(newCodeStep)
  session.commit()
  st.rerun()

# st.title("app")
# st.json({'foo':'bar','fu':'ba'})

# # Insert containers separated into tabs:
# tab1, tab2 = st.tabs(["Tab 1", "Tab2"])

# # You can also use "with" notation:
# with tab1:
#   st.radio('Select one:', [1, 2])
#   st.write("this is tab 1")

# with tab2:
#   st.radio('Select one:', [3, 4])
#   st.write("this is tab 2")
