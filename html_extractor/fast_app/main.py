from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return '<H1>You have reched home <i>Welcome</i></H1>'


