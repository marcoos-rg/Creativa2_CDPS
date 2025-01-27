# **Practica Creativa 2 Grupo 32**
  - ### ***[Guillermo Peláez Cañizáres](https://github.com/Guillepc)***
  - ### ***[Marcos Rosado González](https://github.com/marcoos-rg)***
---
## **Bloque 1: Despliegue de la aplicación en máquina virtual pesada**

Iniciar la instancia `bloque1` en la pestaña *Instancias de VM* de la terminal de Google Cloud y conectar con SSH

### **Uso del Script**

| Comando         | Descripción                                  |
| --------------- | -------------------------------------------- |
| `build`         | Construir la aplicación   |
| `start`         | Iniciar la aplicación (Puerto por defecto 9080). |
| `startport <port>` | Iniciar la aplicación en un puerto seleccionado.   |
| `stop`          | Detiene sin eliminar los contenedores.       |
| `delete`        | Borrar la aplicación.          |

Ejemplo de comando de construcción de la aplicación
```bash
python3 bloque1.py build
```

La aplicación será visible en `http://<IP_PUBLICA>:9080`

---
## **Bloque 2: Despliegue de una aplicación monolítica usando docker**
### **Arranque del escenario**

Entrar en la pestaña *Container Registry* en la terminal de Google Cloud, y navegar hasta el final en la imagen de `product-page`. Implementar en *Cloud Run*, con las opciones marcadas.

![image](https://github.com/user-attachments/assets/e7409507-1fac-4d1f-ba95-0c7e0f28b179)
![image](https://github.com/user-attachments/assets/b57b08f1-b933-4c07-adba-26868f6d0f25)
![image](https://github.com/user-attachments/assets/585ab17d-18cc-4471-b2b8-fa23062872c8)
![image](https://github.com/user-attachments/assets/2549a512-8565-416d-b8b9-cb0b61e75998)

La aplicación es ahora visible en la URL publica del servicio.

---
## **Bloque 3: Segmentación de una aplicación monolítica en microservicios utilizando docker-compose**

Iniciar la instancia `bloque1` en la pestaña *Instancias de VM* de la terminal de Google Cloud y conectar con SSH

### Uso del script

| Comando         | Descripción                                  |
| --------------- | -------------------------------------------- |
| `build <version>`         | Clona, compila y levanta los contenedores.   |
| `start`         | Inicia los contenedores en modo interactivo. |
| `startdetached` | Inicia los contenedores en segundo plano.    |
| `stop`          | Detiene sin eliminar los contenedores.       |
| `delete`        | Detiene y elimina los contenedores.          |

Ejemplo de comando de construcción de la aplicación
```bash
python3 bloque3.py build v1
```

La aplicación será visible en `http://<IP_PUBLICA>:9080`

---
## **Bloque 4: Despliegue de una aplicación basada en microservicios utilizando Kubernetes**

Abrir una terminal de *Cloud Shell* en la esquina superior derecha de la Terminal de Google Cloud y navegar al directorio `bloque4`. Crear la aplicacion con los siguientes comandos:

```Shell
kubectl apply -f productpage.yaml
kubectl apply -f details.yaml
kubectl apply -f ratings.yaml
kubectl apply -f reviews-svc.yaml
kubectl apply -f reviews-v1-deployment.yaml
```

![image](https://github.com/user-attachments/assets/1a640c7b-0840-4b59-ba4c-f356b1f3d2ea)

Se puede ver la aplicación en la IP Externa del servicio `productpage`, en `http://<EXTERNAL_IP>:9080`



