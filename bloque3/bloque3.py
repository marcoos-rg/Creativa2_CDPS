import os, sys
import yaml

def build():
    # Si se pasa una versión como argumento, actualiza el archivo compose.yaml
    if len(sys.argv) > 2:
        version = sys.argv[2]
        state_version(version)
    else:
        print("No version specified. Using the current configuration in compose.yaml.")

    # Clonar el repositorio si no existe
    if not os.path.exists("practica_creativa2"):
        os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git')
        os.system('sudo apt install -y docker-compose')

    # Construir la aplicación Reviews
    os.chdir('practica_creativa2/bookinfo/src/reviews')
    os.system('docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build')

    # Cambiar de directorio al proyecto principal
    os.chdir('/home/rosadogonzalezmarcos2/bloque3')
    os.system('sudo docker-compose -f compose.yaml build')
    os.system('sudo docker-compose -f compose.yaml up')

def state_version(version):
    # Define los valores de entorno según la versión
    env_config = {
        "v1": {
            "ENABLE_RATINGS": "false",
            "STAR_COLOR": "black",
            "SERVICE_VERSION": "v1"
        },
        "v2": {
            "ENABLE_RATINGS": "true",
            "STAR_COLOR": "black",
            "SERVICE_VERSION": "v2"
        },
        "v3": {
            "ENABLE_RATINGS": "true",
            "STAR_COLOR": "red",
            "SERVICE_VERSION": "v1"
        }
    }

    # Verifica que la versión sea válida
    if version not in env_config:
        print(f"Error: Version '{version}' not supported. Choose from v1, v2, or v3.")
        return

    # Modifica el archivo compose.yaml
    with open("compose.yaml", "r") as file:
        compose = yaml.safe_load(file)

    compose["services"]["reviews"]["environment"] = [
        f"ENABLE_RATINGS={env_config[version]['ENABLE_RATINGS']}",
        f"STAR_COLOR={env_config[version]['STAR_COLOR']}",
        f"SERVICE_VERSION={env_config[version]['SERVICE_VERSION']}"
    ]

    with open("compose.yaml", "w") as file:
        yaml.dump(compose, file)

    print(f"Environment variables for 'reviews' updated to {version}")

def start():
    os.system('sudo docker-compose -f compose.yaml up')

def startdetached():
    os.system('sudo docker-compose -f compose.yaml up -d')

def stop():
    os.system('sudo docker-compose -f compose.yaml stop')

def delete():
    os.system('sudo docker-compose -f compose.yaml down')
    os.system('sudo rm -rf practica_creativa2/')

# Comandos del script
param = sys.argv

if len(param) > 1:
    if param[1] == "build":
        build()
    elif param[1] == "start":
        start()
    elif param[1] == "startdetached":
        startdetached()
    elif param[1] == "stop":
        stop()
    elif param[1] == "delete":
        delete()
    else:
        print("Unknown command")
else:
    print("Please provide a command: build, start, startdetached, stop, delete")
