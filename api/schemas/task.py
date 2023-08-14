from typing import Optional

from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")

class Task(BaseModel): # BaseModel はFastAPIのスキーマモデルであることを表すので、このクラスを継承して Task クラスを作成しています。
    id: int
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    done: bool = Field(False, description="完了フラグ")