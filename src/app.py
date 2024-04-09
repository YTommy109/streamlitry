import streamlit as st
from models.code_step import CodeStep
from models.topic import Topic
from services import addCodeStep, addTopic, get_all_topics, get_code_steps

st.session_state['topic'] = None
st.session_state['CodeStep'] = []

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

def topic_panel() -> None:
  """
  トピックパネル
  """
  v = st.radio("Topic", get_all_topics(), format_func=lambda x: x.topic)

  if(v):
    st.session_state['topic'] = v
    topic_id = v.id
    st.session_state['CodeStep'] = get_code_steps(topic_id)

  topic = st.text_input("Topic")
  if st.button("Add"):
    addTopic(Topic(topic=topic))
    st.rerun()

def container() -> None:
  lc, rc = st.columns((3,7))
  with lc:
    topic_panel()
  with rc:
    code_step_panel()

if __name__ == "__main__":
  container()
