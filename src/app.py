import streamlit as st
from components.code_step_panel import code_step_panel
from components.topic_panel import topic_panel

st.session_state['topic'] = None
st.session_state['CodeStep'] = []

def container() -> None:
  """
  メインコンテナ
  """
  lc, rc = st.columns((3,7))
  with lc:
    topic_panel()
  with rc:
    code_step_panel()

if __name__ == "__main__":
  container()
