from fastapi import FastAPI

app = FastAPI()

# @ で始まるこの部分を、Pythonでは デコレータ と呼びます。
# Javaのアノテーションと似た形式ですが、Pythonのデコレータは、関数を修飾し、関数に新たな機能を追加します。
@app.get("/hello")
async def hello():
    return {"message": "hello world!"}