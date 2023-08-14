from fastapi import APIRouter

router = APIRouter()


@router.put("/tasks/{task_id}/done")
async def mark_task_as_done():
    pass  # pass は「何もしない文」を表します。


@router.delete("/tasks/{task_id}/done")
async def unmark_task_as_done():
    pass  # pass は「何もしない文」を表します。
