from typing import Optional

from pydantic import BaseModel, Field

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True
class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")
  # DB接続の際に使用する
    class Config:
      orm_mode = True