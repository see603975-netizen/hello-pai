from fastapi import FastAPI
app = FastAPI() 
@app.get("/") 
def read_root():
     return {"message": "Hello 你的 ERP 之路開始了"}