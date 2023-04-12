from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/price-model-land/{size}/{price}/{location}")
async def read_calculate(size: str, price: str, location: Union[int, None] = None):

    if location == 1:
        locations = 'Cercado de Lima'
    elif location == 2:
        locations = 'Ancón'
    elif location == 3:
        locations = 'Ate'
    elif location == 4:
        locations = 'Barranco'
    elif location == 5:
        locations = 'Breña'
    elif location == 6:
        locations = 'Carabayllo'
    else:
        locations = 'Sin Ubicación'

    return {"size": size, "price": price, "location": locations}

def str_value(s):
    return str('Distrito: '+s)