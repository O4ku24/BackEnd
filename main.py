import uvicorn
from app.database import  engine
from fastapi import FastAPI
from app.models import  UserModel, JornalModel
from app.urls import url
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Top Wey",
    version="0.0.1"
)

app.include_router(url)
app.mount("/static", StaticFiles(directory='static'), name='static')


if __name__ == '__main__':
    UserModel.metadata.create_all(engine)
    JornalModel.metadata.create_all(engine)
    print('Start Server')
    uvicorn.run('main:app', port = 8000, host='127.0.0.1', reload=True)
    print('Server Stop')

