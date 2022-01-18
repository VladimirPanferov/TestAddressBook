from fastapi import FastAPI


app = FastAPI()


@app.post("/users")
def get_users():
    pass


@app.put("/user")
def create_user():
    pass


@app.patch("/user")
def edit_user():
    pass


@app.delete("/user")
def delete_user():
    pass
