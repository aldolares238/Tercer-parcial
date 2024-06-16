#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Proyecto IA CHATBOT

El presente proyecto se programó y ejecutó desde un entorno virtual de anaconda.
La versión recomendada de python es la 3.6
conda create -n Chatbot2 python=3.6 

Una vez creado el entorno, podremos abrirlo con el comando: 
conda activate Chatbot2

Se procede a clonar el repositorio de github con las librerias y comandos necesarios
En este repositorio encontraremos todo lo necesario para correr el entrenamiento

git clone --recursive https://github.com/daniel-kukiela/nmt-chatbot

Se instalaron los requerimientos necesarios del repositorio clonado
pip install -r requirements.txt

Cada usuario deberá elegir los datos con los que entrenará a su chatbot, en mi caso usé algunos meses de comentarios de reddit con respuestas unitarias, es decir, una pregunta, una respuesta. Esta información deberá ser procesada mediante el código anexo llamado "chatbot_database".
Hecho esto, se procede a correr el siguiente codigo anexado llamado "create_training_data" para terner listos los datos del entrenamiento. 

Se regresa al entorno virtual, para correr el comando que prepara la información dentro de la carpeta llamada "setup"
python prepare_data.py

Debera dejarse entrenar tanto tiempo sea necesario, en mi caso, fueron 4000 epocas de entrenamiento.
Para interactuar con el bot podemos hacerlo mientras sigue entrenando para ir probando, mediante el comando:
python inference.py
