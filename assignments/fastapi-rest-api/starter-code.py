from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


tasks = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Build a REST API", "completed": True},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API!"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": task.completed,
    }
    tasks.append(new_task)
    return new_task


# Add GET /tasks/{task_id}, PUT /tasks/{task_id}, and DELETE /tasks/{task_id}
# to complete the assignment.
