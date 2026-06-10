from fastapi import APIRouter

from app.modelos.cliente import Cliente

router = APIRouter(
  prefix="/clientes"
)

CLIENTE_LIST = [Cliente(id_=1,nome="Paulo Corrêa",email="pslcorrea@gmail.com",telefone="125456979"),
                   Cliente(id_=2,nome="Ana Corrêa",email="ana@gmail.com",telefone="125456979"),
                   ]

@router.get("/", response_model=list[Cliente])
async def listar_clientes():
  return CLIENTE_LIST

@router.get("/{cliente_id}", response_model=Cliente | None)
async def obter_cliente(cliente_id: int):
  for cliente in CLIENTE_LIST:
    if cliente.id_ == cliente_id:
      return cliente
  return None