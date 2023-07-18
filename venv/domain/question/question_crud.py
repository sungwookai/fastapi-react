from models import Question
from sqlalchemy.orm import Session

# create
# read
# update
# delete
def get_question_list(db: Session): ## read
    question_list = db.query(Question)\
        .order_by(Question.create_date.desc())\
        .all()
    return question_list
