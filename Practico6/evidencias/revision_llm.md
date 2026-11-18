# Revisión independiente con Codex

## Prompt enviado

Revisá la seguridad del código de los cinco ejercicios en las copias locales main (tmp/dss-practico6-repo) y Practico-2 (tmp/dss-practico6-corregido). Leé solo el código y la configuración de las aplicaciones. Explicá qué problemas encontraste, dónde aparecen y qué cambia entre las dos ramas. Indicá si algo depende de la configuración. Respondé en español y de forma breve.

## Respuesta final

Practico-2 corrige la inyección SQL del ejercicio 1, el XSS almacenado del 2 y la evaluación de expresiones del 4. En el 5 reemplaza el cifrado reversible con clave fija por BCrypt.

Quedan dos problemas concretos. El buscador del ejercicio 2 todavía interpola texto del usuario en SQL. En el ejercicio 3, el servidor genera el nombre del archivo y limita las extensiones, pero sigue sin verificar que el contenido sea una imagen.

En ambas ramas, los ejercicios 1 y 2 arrancan con depuración habilitada por defecto cuando se ejecutan con python app.py. La exposición efectiva depende de la configuración del despliegue.
