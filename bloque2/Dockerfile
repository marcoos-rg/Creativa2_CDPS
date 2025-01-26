# Usar Python como base (es como instalar Python en una computadora vacía)
FROM python:3.7.7-slim

# Instalar herramientas que tu script necesita, como `git` y `sudo`
RUN apt-get update && apt-get install -y git sudo

# Configurar el directorio de trabajo (el "lugar donde trabajará el contenedor")
WORKDIR /app

# Copiar tu script `bloque1.py` dentro del contenedor
COPY bloque2.py /app/

# Establecer la variable de entorno de GROUP_NUMBER
ENV GROUP_NUMBER=32

# Definir el puerto donde exponer la aplicación
EXPOSE 5060

# Definir el comando que se ejecutará cuando el contenedor inicie
CMD ["python3", "bloque2.py", "build"]
