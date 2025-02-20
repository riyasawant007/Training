from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.name} created", "user_data": user}
