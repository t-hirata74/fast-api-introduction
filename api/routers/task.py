from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks")
async def list_tasks():
    pass  # pass は「何もしない文」を表します。


@router.post("/tasks")
async def create_task():
    pass  # pass は「何もしない文」を表します。


@router.put("/tasks/{task_id}")
async def update_task():
    pass  # pass は「何もしない文」を表します。


@router.delete("/tasks/{task_id}")
async def delete_task():
    pass  # pass は「何もしない文」を表します。
