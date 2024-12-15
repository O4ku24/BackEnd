from fastapi import Request, APIRouter
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from app.database import engine
from sqlalchemy import select, insert
from .models import UserModel, JornalModel
from .schemas import UserSchema, LessonSchema


url = APIRouter()
template = Jinja2Templates(directory='templates')


@url.get(path='/')
def index(request: Request):
    return template.TemplateResponse(
        request=request,
        name='home.html',
    )

@url.get(path='/auth/')
def auth(request: Request):
    return template.TemplateResponse(
        request=request,
        name='auth.html',
    )

@url.post(path='/registration/')
def add_user(request:Request, user: UserSchema):
    session = Session(engine)
    stmt = insert(UserModel).values(user_name = user.login,
                                    user_password = user.password)
    session.execute(stmt)
    session.commit()
    session.close()
    return user

@url.post(path='/add/')
def add_lesson(request:Request, lesson_req: LessonSchema):
    session = Session(engine)
    stmt = insert(JornalModel).values(user_id = lesson_req.user_id,
                                      lesson = lesson_req.lesson,
                                      title = lesson_req.title,
                                      description = lesson_req.descreption,
                                      status = lesson_req.status,
                                      data_lesson = lesson_req.data)
    session.execute(stmt)
    session.commit()
    session.close()
    return lesson_req