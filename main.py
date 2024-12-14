from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel

app = FastAPI()

# Gắn cứng thông tin tài khoản
VALID_USERNAME = "admin"
VALID_PASSWORD = "12345"

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username != VALID_USERNAME:
        # raise HTTPException(status_code=401, detail="Sai tên đăng nhập")
        return {"message": "Sai ten dang nhap"}
    if password != VALID_PASSWORD:
        # raise HTTPException(status_code=401, detail="Sai mật khẩu")
        return {"message": "Sai mat khau"}
    return {"message": "Dang nhap thanh cong"}
