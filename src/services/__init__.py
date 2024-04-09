from database import SessionLocal
from models.code_step import CodeStep
from models.topic import Topic

session: SessionLocal = SessionLocal()

def addTopic(topic: Topic) -> None:
    session.add(topic)
    session.commit()

def addCodeStep(code_step: CodeStep) -> None:
    session.add(code_step)
    session.commit()

def get_code_steps(topic_id: int) -> list[CodeStep]:
    return (session.query(CodeStep)
            .filter(CodeStep.topic_id==topic_id)
            .order_by(CodeStep.step).all())

def get_all_topics() -> list[Topic]:
    return session.query(Topic).all()