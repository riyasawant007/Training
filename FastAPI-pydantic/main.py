from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/users/")
async def create_user(user: User):  # Use async for better async handling
    return {"message": f"User {user.name} created", "user_data": user}
