from pydantic import BaseModel


""" class TaskCreateSchema(BaseModel):
    title:str
    description:str

class TaskSchema(BaseModel):
    title: str
    description:str
    status: bool

class TaskUpdateSchema(BaseModel):
    title: str
    description:str
    status: bool """

class UserSchema(BaseModel):
    login: str
    password: str

class LessonSchema(BaseModel):
    user_id: int
    lesson: str
    title: str
    descreption: str
    status: bool
    data: str 