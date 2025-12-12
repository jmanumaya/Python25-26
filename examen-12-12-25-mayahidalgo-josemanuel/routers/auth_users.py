
from  datetime import datetime, timedelta, timezone
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException

import jwt
from jwt import PyJWTError
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Definimos el algoritmo de encriptación
ALGORITHM = "HS256"

# Duracion del token
ACCESS_TOKEN_EXPIRE_MINUTES = 1

# Clvae que se utilizará como semilla para generar el token
# openssl rand -hex 32
SECRET_KEY = "14d0e194f16cad62eb2f966fae845984d720db01d7c72524b9f8fd82f07b45a0"

# Objeto que se utilizará para el cálculo del hash y la verificación de las contraseñas
password_hash = PasswordHash.recommended()

router = APIRouter()

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "josema": {
        "username" : "josema",
        "fullname" : "Jose Manuel",
        "email" : "jmaya@gmail.com",
        "disabled" : False,
        "password" : "234567"
    }
}

@router.post("/register", status_code=201)
def register(user: UserDB):
    if user.username not in users_db:
        hashed_password = password_hash.hash(user.password)
        user.password = hashed_password
        users_db[user.username] = user.model_dump()
        return user
    else:
        raise HTTPException(status_code=409, detail="User already exists")
    
@router.post("/login")
async def login (form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if user_db:
        # Si el usuario existe en la base de datos
        # Comprobamos las contraseñas
        # Creamos el usuario de tipo UserDB
        user = UserDB(**users_db[form.username])
        try:
            if password_hash.verify(form.password, user.password):
                expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
                access_token = {"sub" : user.username, "exp" : expire}
                # Generamos token
                token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)
                return {"access_token": token, "token_type": "bearer"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error en la autenticación: {e}")
    raise HTTPException(status_code=401, detail="Usuario o contraseña icorrectos")

async def authentication(token: str = Depends(oauth2)):
    try:
        username = jwt.decode(token, SECRET_KEY, algorithm=ALGORITHM).get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Credenciales de autenticacion invalidas",
                                headers={"WWW-Authenticate" : "Bearer"})
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Credenciales de autenticacion invalidas",
                                headers={"WWW-Authenticate" : "Bearer"})
    
    user = User(**users_db[username])

    if user.disabled:
        # Si el usuario está deshabilitado lanzamos execption
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    
    #Retornamos un usuario correcto y habilitado
    return user
