# Celda #1 - librerias
import numpy as np
import matplotlib.pyplot as plt
from utils import *
plt.style.use('./deeplearning.mplstyle')
np.set_printoptions(precision=2)
import json

# Celda #2 - Dataset
x_train, y_train = load_data()

# Celda #6: Assign value the parameters w (pezo prediccion) / b (filtro inicial)
w = 1200
b = 300

# Definir bloque de vistas de registros
async def price_index(sizemts, x_train):    
    xm2_train = np.array(x_train)
    difference_array = np.absolute(xm2_train - sizemts)    
    index = difference_array.argmin()    
    return index

async def prices_model_output(sizemts):
    xm2 = np.array(x_train)    
    indexm2 = price_index(sizemts, xm2)  
    nro = 0

    data_string = []

    for i in range(indexm2, indexm2+3):
        nro = nro + 1
        if (i == price_index(sizemts, x_train)):            
            #print(f"['index:'{i}, 'price:' $ {format(w * x_train[i] + b,'0,.2f')}, 'size:' {x_train[i]:.0f} m^2, 'recommended: true']")                        
            data_string = {'inmueble': nro, 'size': x_train[i], 'price': f"$ {format(w * x_train[i] + b,'0,.2f')}", 'recommended': 'true'}
            print(data_string)
            #print(json.dumps(data_string, sort_keys=True, indent=6))
        else:
            #print(f"['index:'{i}, 'price:' $ {format(w * x_train[i] + b,'0,.2f')}, 'size:' {x_train[i]:.0f} m^2, 'recommended: false']")                        
            data_string = {'inmueble': nro, 'size': x_train[i], 'price': f"$ {format(w * x_train[i] + b,'0,.2f')}", 'recommended': 'false'}
            print(data_string)
            #print(json.dumps(data_string, sort_keys=True, indent=2))
        #return data_string