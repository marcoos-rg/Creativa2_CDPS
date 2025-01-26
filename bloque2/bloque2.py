from subprocess import call
import os, sys

# Funcion para construir la aplicacion monolitica
def build (port = '5060'):
    # Copia el repositorio e instala las dependencias necesarias
    call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])
    call(['sudo', 'apt-get', 'update'])
    call(['sudo', 'apt-get', 'install', '-y', 'python3-pip'])
    os.chdir('practica_creativa2/bookinfo/src/productpage')

    # Modifica el paquete "requests" de requirements
    requirements = 'requirements.txt'
    with open(requirements, 'r') as file:
        lines = file.readlines()
    with open(requirements, 'w') as file:
        for line in lines:
            if line.startswith('requests=='):
                file.write('requests\n')
            else:
                file.write(line)

    # Instala los requirements
    call(['pip3', 'install', '-r', 'requirements.txt'])

    # Esta linea arregla un error que saltaba con la version de json2html
    call(['pip', 'install', '--upgrade', 'json2html'])

    # Establece la variable de entorno al numero de grupo (32)
    os.environ['GROUP_NUMBER'] = '32'
    #os.environ['SERVICES_DOMAIN'] = '9080'
    #os.environ['DETAILS_HOSTNAME'] = '192.168.49.1'
    
    # Crea una copia temporal del script monolitico
    call(['mv', 'productpage_monolith.py', 'productpage_monolith_tmp.py'])

    # Abre el script original y la copia en modo escritura y lectura
    fin = open('productpage_monolith_tmp.py', 'r')
    fout = open('productpage_monolith.py', 'w')

    # Lee y modifica "productpage_monolith.py" para incluir la variable de entorno de GROUP_NUMBER
    for line in fin:
        	if 'flood_factor = 0 if (os.environ.get("FLOOD_FACTOR") is None) else int(os.environ.get("FLOOD_FACTOR"))' in line :
                	fout.write(line)
                	fout.write(os.linesep + 'groupNumber = 0 if (os.environ.get("GROUP_NUMBER") is None) else int(os.environ.get("GROUP_NUMBER"))' + os.linesep)
        	elif 'def front():' in line :
                	fout.write(line)
                	fout.write('    group = groupNumber' + os.linesep)
        	elif '\'productpage.html\',' in line :
                	fout.write(line)
                	fout.write('\tgroup=group,' + os.linesep)
        	else :
        	        fout.write(line)

    # Cierra y elimina el script temporal
    fin.close()
    fout.close()
    call(['rm', '-f', 'productpage_monolith_tmp.py'])

    # Cambia de directorio a 'templates' y crea un productpage temporal
    os.chdir('templates')
    call(['mv', 'productpage.html', 'productpage_tmp.html'])
    fin = open('productpage_tmp.html', 'r')
    fout = open('productpage.html', 'w')

    # Lee y modifica productpage para incluir el numero de grupo
    for line in fin:
       		if '{% block title %}Simple Bookstore App{% endblock %}' in line :
                	fout.write(line.replace('{% block title %}Simple Bookstore App{% endblock %}', '{% block title %}Grupo {{ group }}{% endblock %}'))
        	else :
        	        fout.write(line)

    # Cierra y elimina el temporal
    fin.close()
    fout.close()
    call(['rm', '-f', 'productpage_tmp.html'])

    # Mensaje de exito
    print("App built properly")

    # Para arrancar la aplicacion, sirve para que el Docker solo ejecute un comando
    os.chdir('..')
    call(['python3', 'productpage_monolith.py', port])

# Funcion para iniciar una vez construida la aplicación
def start(port = '5060'):
    os.chdir('practica_creativa2/bookinfo/src/productpage')
    call(['python3', 'productpage_monolith.py', port])

# Funcion para borrar el escenario
def delete():
    call(['rm', '-rf', 'practica_creativa2'])

param = sys.argv

# Comandos del script
if param[1] == "build":
    build()
elif param[1] == "delete":
    delete()
elif param[1] == "start":
    start()
elif param[1] == "startport":
    start(param[2])
else:
    print("Unknown command")
