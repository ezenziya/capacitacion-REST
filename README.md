# Patron Repositorio Rest

Implimentacion de un patron repositorio en REST

## Armar un entorno virtual para Python

Altamente recomendado para no tener conflicto entre las librerias...y siempre hay conflicto entre las liberias de Python

```sh
python -m pip install virtualenv
virtualenv venv
source venv/bin/activate 
```

## Instalando Librerias

Para esta API se utilizan:
- Uvicorn: como servidor web
- databases: como conector con la DB
- SQLite: como DB autonoma
- fastapi-crudrouter: Como mapeador entre objeto python <=> DB


```sh
#si tienen windows es venv\Scripts\activate
python -m pip install --upgrade pip
#Instalar librerias
python -m pip install fastapi
python -m pip install "uvicorn[standard]"
python -m pip install "databases[sqlite]"
python -m pip install "fastapi-crudrouter"
```

## Para ejecutar el servicio

Y luego ejecutamos el servidor:

```sh
uvicorn main:app --reload
```

y listo, probar el endpoint!
