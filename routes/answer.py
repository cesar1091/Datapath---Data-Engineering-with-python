from fastapi import APIRouter
from config.db import conn
from models.answer import answer1,answer2,answer3,answer4
from schemas.answer import Answer1,Answer2,Answer3,Answer4

answer = APIRouter()

@answer.get('/answer1',response_model=list[Answer1],tags=['answer'])
def get_answer1():
    return conn.execute(answer1.select()).fetchall()

@answer.get('/answer2',response_model=list[Answer2],tags=['answer'])
def get_answer2():
    return conn.execute(answer2.select()).fetchall()

@answer.get('/answer3',response_model=list[Answer3],tags=['answer'])
def get_answer3():
    return conn.execute(answer3.select()).fetchall()

@answer.get('/answer4',response_model=list[Answer4],tags=['answer'])
def get_answer4():
    return conn.execute(answer4.select()).fetchall()

