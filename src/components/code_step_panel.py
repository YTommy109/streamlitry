import streamlit as st
from models.code_step import CodeStep
from services import addCodeStep


def code_step_panel() -> None:
  """
  コードステップパネル
  """
  code_steps = st.session_state['CodeStep']
  if len(code_steps) > 0:
    chose: int = 0 if len(code_steps) == 1 else st.slider('Steps', min_value=0, max_value=len(code_steps)-1, value=0, step=1)
    st.code(code_steps[chose].code, language="python", line_numbers=True)

  newCode = st.text_area("Code")
  if st.button("Add Code"):
    addCodeStep(CodeStep(code=newCode, step=len(code_steps)+1, topic_id=st.session_state['topic'].id))
    st.rerun()
