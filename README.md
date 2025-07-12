# Steps

### Para correr el programa seguir las siguientes instrucciones
#### Para el proyecto de juego
```sh
-> cd juego
-> python3 rock_paper_scissors.py 
```

#### Para el proyecto de request
```sh
-> git clone
-> cd web_server
-> python3 -m venv env
-> source env/bin/activate
-> pip3 install -r requirements.txt
-> python3 main.py
```

#### Para el proyecto de request pero desde docker
```sh
-> git clone
-> cd web_server
-> python3 -m venv env
-> source env/bin/activate
-> deactivate
-> pip3 install -r requirements.txt
# recordar tener instalado y activado docker
-> docker-compose build
-> docker-compose up -d
-> docker-compose ps
# para acceder, ir al navegador e ingresar localhost y usar los endpoint ubicados en main
```

