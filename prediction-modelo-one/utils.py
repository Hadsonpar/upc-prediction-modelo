import numpy as np
import os# para manipular rutas

def weight_bias():
    w = 3050
    b = 300
    #w = 1200
    #b = 300
    return w, b

# Load dataset according to locations
# function start
def load_data(locations: str):
    location = locations  
    values = ''

    file_path = 'data/MRL01/locations/dataset{}.txt'.format(location)

    if os.path.exists(file_path) == True:
        data = np.loadtxt(file_path, delimiter=',')
    
        x = data[:,0]
        y = data[:,1]
        z = data[:,2]

        values = x, y, z
    else:
        values = 'Dataset no definido'

    return values
# function end

def load_location():
    data = np.loadtxt("data/LOCATION/location-lima-metropolitana.txt", delimiter=',')    
    id = data[:,0]
    lo = data[:,1]
    return id, lo

def percent_location(code):
    if (code == 1):
        values = 0.0040
    elif(code == 2):
        values = 0.0020
    elif(code == 3):
        values = 0.0012
    elif(code == 4):
        values = 0.0050
    elif(code == 5):
        values = 0.0040
    elif(code == 6):
        values = 0.0037
    elif(code == 7):
    	values = 0.0027
    elif(code == 8):
        values = 0.0018
    elif(code == 9):
        values = 0.0050
    elif(code == 10):
        values = 0.0035
    elif(code == 11):
        values = 0.0050
    elif(code == 12):
        values = 0.0056
    elif(code == 13):
        values = 0.0038
    elif(code == 14):
        values = 0.0042
    elif(code == 15):
        values = 0.0051
    elif(code == 16):
        values = 0.0016
    elif(code == 17):
        values = 0.0040
    elif(code == 18):
        values = 0.0070
    elif(code == 19):
        values = 0.0030
    elif(code == 20):
        values = 0.0025
    elif(code == 21):
        values = 0.0050
    elif(code == 22):
        values = 0.0030
    elif(code == 23):
        values = 0.0016
    elif(code == 24):
        values = 0.0059
    elif(code == 25):
        values = 0.0020
    elif(code == 26):
        values = 0.0060
    elif(code == 27):
        values = 0.0070
    elif(code == 28):
        values = 0.0050
    elif(code == 29):
        values = 0.0040
    elif(code == 30):
        values = 0.0050
    elif(code == 31):
        values = 0.0050
    elif(code == 32):
        values = 0.0056
    elif(code == 33):
        values = 0.0070
    elif(code == 34):
        values = 0.0050
    elif(code == 35):
        values = 0.0030
    elif(code == 36):
        values = 0.0040
    elif(code == 37):
        values = 0.0050
    elif(code == 38):
        values = 0.0030
    elif(code == 39):
        values = 0.0065
    elif(code == 40):
        values = 0.0050
    elif(code == 41):#'San Borja'
        values = 0.0070
    elif(code == 42):
        values = 0.0042
    elif(code == 43):
        values = 0.0050
    elif(code == 44):
        values = 0.0068
    elif(code == 45):
        values = 0.0052
    elif(code == 46):
        values = 0.0036
    elif(code == 47):
        values = 0.0054
    elif(code == 48):
        values = 0.0060
    elif(code == 49):
        values = 0.0046    
    
    return values

def read_location(code: int):
    if (code == 1):
        values = 'Cercado de Lima'
    elif(code == 2):
        values = 'Ancón'
    elif(code == 3):
        values = 'Ate'
    elif(code == 4):
        values = 'Barranco'
    elif(code == 5):
        values = 'Breña'
    elif(code == 6):
        values = 'Carabayllo'
    elif(code == 7):
        values = 'Comas'
    elif(code == 8):
        values = 'Chaclacayo'
    elif(code == 9):
        values = 'Chorrillos'
    elif(code == 10):
        values = 'El Agustino'
    elif(code == 11):
        values = 'Jesús María'
    elif(code == 12):
        values = 'La Molina'
    elif(code == 13):
        values = 'La Victoria'
    elif(code == 14):
        values = 'Lince'
    elif(code == 15):
        values = 'Lurigancho'
    elif(code == 16):
        values = 'Lurín'
    elif(code == 17):
        values = 'Magdalena'
    elif(code == 18):
        values = 'Miraflores'
    elif(code == 19):
        values = 'Pachacamac'
    elif(code == 20):
        values = 'Pucusana'
    elif(code == 21):
        values = 'Pueblo Libre'
    elif(code == 22):
        values = 'Puente Piedra'
    elif(code == 23):
        values = 'Punta Negra'
    elif(code == 24):
        values = 'Punta Hermosa'
    elif(code == 25):
        values = 'Rímac'
    elif(code == 26):
        values = 'San Bartolo'
    elif(code == 27):
        values = 'San Isidro'
    elif(code == 28):
        values = 'Independencia'
    elif(code == 29):
        values = 'San Juan de Miraflores'
    elif(code == 30):
        values = 'San Luis'
    elif(code == 31):
        values = 'San Martín de Porres'
    elif(code == 32):
        values = 'San Miguel'
    elif(code == 33):
        values = 'Santiago de Surco'
    elif(code == 34):
        values = 'Surquillo'
    elif(code == 35):
        values = 'Villa María del Triunfo'
    elif(code == 36):
        values = 'San Juan de Lurigancho'
    elif(code == 37):
        values = 'Santa María del Mar'
    elif(code == 38):
        values = 'Santa Rosa'
    elif(code == 39):
        values = 'Los Olivos'
    elif(code == 40):
        values = 'Cieneguilla'
    elif(code == 41):
        values = 'San Borja'
    elif(code == 42):
        values = 'Villa el Salvador'
    elif(code == 43):
        values = 'Santa Anita'
    elif(code == 44):
        values = 'Callao'
    elif(code == 45):
        values = 'Bellavista'
    elif(code == 46):
        values = 'Carmen de la Legua'
    elif(code == 47):
        values = 'La Perla'
    elif(code == 48):
        values = 'La Punta'
    elif(code == 49):
        values = 'Ventanilla'
    else:
        values = 'Sin Identificar'
    return values
    
def price_same(x_train, y_train, z_train, sizemts: int):
    m = x_train.shape[0]
    data = []
    for i in range(m):
        if(x_train[i] == sizemts):
            data.append({x_train[i], y_train[i], z_train[i]})
    return data 

def is_list_empty(list):
    if len(list) != 0:        
        return True    
    return False