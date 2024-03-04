"""
Anàlisi dels preus de lloguer BCN 2014-2021
Author: 1rDAW ETPX
Datasets descarregats en CSV
https://opendata-ajuntament.barcelona.cat/data/ca/dataset/est-mercat-immobiliari-lloguer-mitja-mensual
"""


# 1.EXTRACCIÓN DE DATOS (DATA EXTRACTION)
def leerAno(ano):
    ficheroAnual = open(f"lloguers_clase/recursos/{ano}_lloguer_preu_trim.csv",'r',encoding='utf-8')
    datosAnuales = ficheroAnual.readlines() #dataset original
    return datosAnuales

datosAgregados = []
for ano in range(2014,2024):
    datosAnuales = leerAno(ano)
    datosAgregados += datosAnuales

# 2. MANIPULACIÓN DE LOS DATOS (DATA WRANGLING, DATA CLEANING)
datos2014Limpios = []
for linea in datosAgregados:
    linea = linea.replace('"','')
    linea = linea.replace('\n','')
    linea = linea.split(',')
    datos2014Limpios.append(linea)



# 3. ANÁLISIS DE DATOS (DATA ANALYSIS)
    
barris= ["la Vila de Gràcia","Vallcarca i els Penitents","el Coll","la Salut","el Camp d'en Grassot i Gràcia Nova"]

def calcularTrimetres(lista):
    timestres=[]
    for line in lista:
        if line[3]=='Gràcia' and line[6]=='Lloguer mitjà mensual (Euros/mes)'\
            and line[5]==barris[0]:
            timestres.append(line[0]+'\n'+line[1])
    return timestres

    
def analitzarBarri(lista,barris):
    preuLloguer=[[],[],[],[],[]]
    for line in lista:
        for i in range(5):  
            if line[3]=='Gràcia' and line[6]=='Lloguer mitjà mensual (Euros/mes)'\
            and line[5]==barris[i]:
                preuLloguer[i].append(float(line[-1]))
    return preuLloguer


# 4. VISUALIZACIÓN DE DATOS (DATA VISUALIZATION)

from matplotlib import pyplot as plt

fig,ax = plt.subplots(figsize=(15,8))

x = calcularTrimetres(datos2014Limpios)
y = ({'La Vila de Gràcia': analitzarBarri(datos2014Limpios,barris)[0],\
        'Vallcarca i els Penitents': analitzarBarri(datos2014Limpios,barris)[1],\
        'El Coll': analitzarBarri(datos2014Limpios,barris)[2],\
        'La Salut': analitzarBarri(datos2014Limpios,barris)[3],\
        "El Camp d'en Grassot i Gràcia Nova": analitzarBarri(datos2014Limpios,barris)[4]})

ax.plot(x,y['La Vila de Gràcia'],color='red', label='La Vila de Gràcia')
ax.plot(x,y['Vallcarca i els Penitents'],color='yellow', label='Vallcarca i els Penitents')
ax.plot(x,y['El Coll'] ,color='blue', label='El Coll')
ax.plot(x,y['La Salut'],color='purple', label='La Salut')
ax.plot(x,y["El Camp d'en Grassot i Gràcia Nova"] ,color='green', label="El Camp d'en Grassot i Gràcia Nova")

ax.legend()

ax.tick_params(axis='both', which='major', labelsize=7)
ax.set_title("Evolució del lloguer mitjà a Vila de Gràcia (Euros): 2014-2021")

plt.show()