from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
import jwt
from jwt import PyJWTError
from pwdlib import PasswordHash

router = APIRouter(tags=["auth"])

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
SECRET_KEY = "14d0e194f16cad62eb2f966fae845984d720db01d7c72524b9f8fd82f07b45a0"

password_hash = PasswordHash.recommended()

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

# Base de datos simulada
users_db = {
    "elenarg": {
        "username": "elenarg",
        "fullname": "Elena Rivero",
        "email": "elena@prueba.es",
        "disabled": False,
        "password": password_hash.hash("123456")
    },
    "josema": {
        "username": "josema",
        "fullname": "Jose Manuel",
        "email": "jmaya@gmail.com",
        "disabled": False,
        "password": password_hash.hash("234567")
    }
}

async def authentication(token: str = Depends(oauth2)):
    try:
        username = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    user_data = users_db.get(username)
    if user_data is None:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
        
    user = User(**user_data)
    if user.disabled:
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")
    
    user = UserDB(**user_db)
    
    if not password_hash.verify(form.password, user.password):
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = {"sub": user.username, "exp": expire}
    token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)
    
    return {"access_token": token, "token_type": "bearer"}

@router.post("/register", status_code=201)
def register(user: UserDB):
    if user.username in users_db:
        raise HTTPException(status_code=409, detail="User already exists")
    
    hashed_password = password_hash.hash(user.password)
    user.password = hashed_password
    users_db[user.username] = user.model_dump()
    return user