from fastapi import FastAPI
# Celda #1 - librerias
from typing import Union, List
from pydantic import BaseModel
import numpy as np
import matplotlib.pyplot as plt
from utils import *
plt.style.use('./deeplearning.mplstyle')
np.set_printoptions(precision=2)
import json

from utils_multi import * 

# Celda #2 - Dataset
#x_train, y_train, z_train = load_data(1)

# Celda #6: Assign value the parameters w (pezo prediccion) / b (filtro inicial)
w, b = weight_bias()
#w = 1.12
#b = 30

class Prediction(BaseModel):    
    inmueble: int
    size: str
    price: str
    recommended: bool
    location: str

class Predictions(BaseModel): 
    predictions: List[Prediction]

# Definir bloque de vistas de registros
def price_index(sizemts, x_train):    
    xm2_train = np.array(x_train)
    difference_array = np.absolute(xm2_train - sizemts)    
    index = difference_array.argmin()    
    return index



app = FastAPI()

@app.get("/price_model/{sizemts}/{location}/{priceuser}")
def read_calculate(sizemts: int, location: str, priceuser: int, locariouser: Union[str, None] = None):
    x_train, y_train, z_train = load_data(location)
    xm2 = np.array(x_train)    
    indexm2 = price_index(sizemts, xm2)  
    nro = 0
    valuemessage = ''

    data = {}
    data['predictions'] = []   

    if (sizemts < 12):
            valuemessage = 'minimo 12 m^2'
    elif (sizemts > 304):
        valuemessage = 'maximo 304 m^2'
    else:
        for i in range(indexm2, indexm2+3):    
            nro = nro + 1        
            
            #if (i == price_index(sizemts, x_train) and nro == 1):                                              
            data['predictions'].append({
                'inmueble': nro,
                'size': x_train[i],
                #'price': f"$ {format(w * x_train[i] + b,'0,.2f')}",
                'price': f"$ {format(y_train[i] + b,'0,.2f')}",
                'recommended': True,
                'location': read_location(z_train[i])})

            valuemessage = 'completed process'
            
        """
        elif(i != price_index(sizemts, x_train) and nro == 2):                                              
            data['predictions'].append({
                'inmueble': nro,
                'size': x_train[i],
                'price': f"$ {format(w * x_train[i] + b,'0,.2f')}",
                'recommended': False,
                'location': read_location(z_train[i])})
            
        elif(i != price_index(sizemts, x_train) and nro == 3):                       
            data['predictions'].append({
                 'inmueble': nro,
                'size': x_train[i],
                'price': f"$ {format(w * x_train[i] + b,'0,.2f')}",
                'recommended': False,
                'location': read_location(z_train[i])})
        """ 
    with open('modelorl.json', 'w') as file:
        json.dump(data, file, indent=4)  
    return {'SizeMts': sizemts, 'PiceUser': priceuser, 'locariouser': locariouser, 'message': valuemessage, 'data': data}

@app.get("/price_same_model/{sizemts}/{location}/{priceuser}")
def read_calculate(sizemts: int, location: str, priceuser: int, locariouser: Union[str, None] = None):
    valuemessage = ''
    x_train, y_train, z_train = load_data(location)
    m = x_train.shape[0]
    nro = 0
    data = {}
    data['predictions'] = [] 
    for i in range(m):        
        if(x_train[i] == sizemts):
            nro = nro + 1 
            data['predictions'].append({
                'inmueble': nro,
                'size': x_train[i],
                'price': f"$ {format(y_train[i] + b,'0,.2f')}",
                #'price': f"$ {format(w * y_train[i] + b,'0,.2f')}",
                'recommended': True,
                'location': read_location(z_train[i])}) 
            valuemessage = 'completed process'
        #else:
            #valuemessage = 'Sin valores encontrados'
    with open('modelorl.json', 'w') as file:
        json.dump(data, file, indent=4)
    return {'SizeMts': sizemts, 'PiceUser': priceuser, 'locariouser': locariouser, 'message': valuemessage, 'data': data}


"""
def price_same(sizemts):    
    m = x_train.shape[0]
    nro = 0
    data = {}
    data['predictions'] = [] 
    for i in range(m):
        nro = nro + 1 
        if(x_train[i] == sizemts):
            data['predictions'].append({
                'inmueble': nro,
                'size': x_train[i],
                'price': f"$ {format(w * y_train[i] + b,'0,.2f')}",
                'recommended': True,
                'location': read_location(z_train[i])})
    return data

    ---------

    data['predictions'].append({
        'inmueble': 1,
        'bedrooms': x_house[1],
        'floors': x_house[2],
        'age': edad,        
        'recommended': True}) 
"""

# load house data.
Xm_train, ym_train, zm_train = load_house_data()

def zscore_normalize_features(X):    
    # find the mean of each column/feature
    mu     = np.mean(X, axis=0)                 # mu will have shape (n,)    
    sigma  = np.std(X, axis=0)                  # sigma will have shape (n,)    
    X_norm = (X - mu) / sigma      

    return (X_norm, mu, sigma)

# First, normalize out example.
@app.get("/price_house_model/{sizemts}/{location}/{age}")
def read_calculate(sizemts: int, location: int, age: int):
    #pie_cuadrado = 10.764

    data = {}
    data['characteristic'] = []

    #p = pie_cuadrado()#10.764
    sqft, iterations, alpha = pie_cuadrado()#10.764
    
    if age > 10:
         valuemessage = 'construcción del inmueble no mayor a 10 años'
    else:

        if zm_train[5] == location:

            Xm_norm, Xm_mu, Xm_sigma = zscore_normalize_features(Xm_train)
            wm_norm, bm_norm, hist = run_gradient_descent(Xm_norm, ym_train, iterations, alpha)
            
            mts = sizemts
            mts_cuadrados = mts * sqft

            #construccion = random.randint(5, 20)        
            x_house = np.array([mts_cuadrados, 4, 2, age])    
            x_house_norm = (x_house - Xm_mu) / Xm_sigma    
            x_house_predict = np.dot(x_house_norm, wm_norm) + bm_norm
            x_price = x_house_predict * 1000

            data['characteristic'].append(
                {
                'inmueble': 1,
                'size': sizemts,
                'price': f"$ {format(x_price,'0,.2f')}",
                'bedrooms': x_house[1],
                'floors': x_house[2],
                'age': age,            
                'location': read_location(location)
                })

            valuemessage = 'completed process' 
        else:        
            valuemessage = 'dataset no definido para {}'.format(read_location(location))

    return {'SizeMts': sizemts, 'message': valuemessage, 'data': data}    