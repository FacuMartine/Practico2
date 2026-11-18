# Cómo mostrar el práctico 6 en Kali

Esta guía permite repetir el análisis estático y abrir las evidencias. No hace falta levantar las aplicaciones ni Docker.

## 1 Preparar la terminal

El proyecto y el entorno ya están instalados en esta computadora:

```bash
cd ~/DSS-Practico6
source .venv/bin/activate
cd Practico2
semgrep --version
git status --short
```

## 2 Analizar main

Los resultados se guardan fuera del repositorio para conservarlos al cambiar de rama. Se excluye la carpeta de evidencias si también se copió dentro del repositorio.

```bash
mkdir -p ../evidencias
git switch main
git branch --show-current
semgrep scan --config auto --oss-only --exclude evidencias --json-output ../evidencias/main.json --text-output ../evidencias/main.txt 2>&1 | tee ../evidencias/main.log
```

Esperar el mensaje de finalización. En la ejecución realizada hubo 11 alertas. Las reglas auto se descargan de Internet y pueden cambiar; si una nueva ejecución da otro resultado, conservarlo y revisar la diferencia.

## 3 Analizar Practico-2

```bash
git switch Practico-2
git branch --show-current
semgrep scan --config auto --oss-only --exclude evidencias --json-output ../evidencias/Practico-2.json --text-output ../evidencias/Practico-2.txt 2>&1 | tee ../evidencias/Practico-2.log
```

En la ejecución realizada hubo 9 alertas. Desaparecieron las dos de AES/ECB del ejercicio 5.


## 4 Mostrar por qué desaparecieron dos alertas

```bash
git diff main Practico-2 -- Ejercicio5/src/main/java/com/cinebuscador/config/EncryptionService.java
```

Las líneas con menos se quitaron y las de más se agregaron. Se reemplazó el cifrado reversible por BCrypt. Salir con q si Git abre el visor.

## 5 Mostrar un falso negativo

```bash
git show Practico-2:Ejercicio2/app.py | nl -ba | sed -n '23,45p'
```

La búsqueda y el sentido de orden llegan del usuario y se insertan en el SQL. Semgrep no señaló esa SQLi. El LLM sí la identificó en la revisión del código. La corrección del XSS de este ejercicio no corrige su buscador.

## 6 Mostrar la alerta SpEL que permanece

```bash
git diff main Practico-2 -- Ejercicio4/src/main/java/com/cinebuscador/controller/FuncionController.java
```

El controlador corregido ya no llama al evaluador. La clase permanece y Semgrep la señala, pero eso solo no demuestra que la entrada del buscador siga llegando a ella.

