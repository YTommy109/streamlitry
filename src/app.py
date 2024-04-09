# app.py
import streamlit as st
from database import SessionLocal
from models.code_step import CodeStep
from models.topic import Topic

session: SessionLocal = SessionLocal()
st.session_state['topic'] = None
st.session_state['CodeStep'] = []

def code_step_panel() -> None:
  """
  コードステップパネル
  """
  code_steps = st.session_state['CodeStep']
  if len(code_steps) > 0:
    chose: int = st.slider('Steps', min_value=0, max_value=len(code_steps)-1, value=0, step=1)
    st.code(code_steps[chose].code, language="python", line_numbers=True)

  newCode = st.text_area("Code")
  if st.button("Add Code"):
    newCodeStep = CodeStep(code=newCode, step=len(code_steps)+1, topic_id=st.session_state['topic'].id)
    session.add(newCodeStep)
    session.commit()
    st.rerun()

def topic_panel() -> None:
  """
  トピックパネル
  """
  topics = session.query(Topic).all()
  v = st.radio("Topic", topics, format_func=lambda x: x.topic)

  if(v):
    st.session_state['topic'] = v
    st.session_state['CodeStep'] = (session.query(CodeStep)
                                    .filter(CodeStep.topic_id==v.id)
                                    .order_by(CodeStep.step).all())

  topic = st.text_input("Topic")
  if st.button("Add"):
    session.add(Topic(topic=topic))
    session.commit()

lc, rc = st.columns(2)
with lc:
  topic_panel()
with rc:
  code_step_panel()

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
