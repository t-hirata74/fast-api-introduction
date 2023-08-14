from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.schemas.task as task_schema

# 1. 引数としてスキーマ task_create: task_schema.TaskCreate を受け取る。
# 2. これをDBモデルである task_model.Task に変換する
# 3. DBにコミットする
# 4. DB上のデータを元にTaskインスタンス task を更新する（この場合、作成したレコードの id を取得する）
# 5. 作成したDBモデルを返却する
async def create_task(
    db: AsyncSession, task_create: task_schema.TaskCreate
) -> task_model.Task:
    task = task_model.Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task