import streamlit as st
from models.topic import Topic
from services import addTopic, get_all_topics, get_code_steps


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
