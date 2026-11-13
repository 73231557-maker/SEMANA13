# Semana 13 - Interfaces gráficas con Tkinter


Práctica de Construcción de Software, Universidad Continental.



En esta práctica hice dos aplicaciones de escritorio en Python con Tkinter:


**Calculadora** (calculadora.py): permite sumar, restar, multiplicar y dividir. Tiene un botón C para borrar y muestra un mensaje si la operación está mal escrita.
**Formulario de registro** (formulario.py): pide nombre, email, contraseña, edad, género y aceptar los términos. Revisa que los datos estén bien antes de registrar.
Antes de programar dibujé un wireframe de cada una (wireframe_calculadora.png y wireframe_Formulario.png) para saber cómo iba a quedar. También subí capturas de las apps funcionando.


## Cómo se ejecutan


Tkinter ya viene con Python, así que solo hay que correr:


    python calculadora.py
    python formulario.py


## Qué principios de usabilidad apliqué y por qué


**Etiquetas claras:** cada campo tiene su nombre al lado para que nadie se confunda sobre qué escribir.
**Orden con Tab:** los campos van de arriba hacia abajo, así que con la tecla Tab se avanza en un orden natural.
**Cursor listo al abrir:** el cursor aparece en el campo Nombre, para empezar a escribir sin hacer clic.
**Atajos de teclado:** con Enter se registra y con Ctrl+L se limpia. Los puse escritos en los botones para que el usuario sepa que existen.
**Errores que se ven:** si algo está mal, el campo se pinta de rojo y aparece un mensaje con todos los errores juntos. Así se corrigen de una vez y no uno por uno.
**Contraseña oculta:** se muestra con asteriscos para proteger la privacidad.
**Datos controlados:** la edad solo se acepta entre 15 y 99, y la contraseña debe tener mínimo 8 caracteres.
**Calculadora simple:** botones del mismo tamaño en una cuadrícula de 4x4, con el resultado a la derecha como en una calculadora normal.
## Cómo organicé el código


Cada aplicación es una clase. Separé la parte que dibuja la ventana (crear_widgets) de la parte que hace las acciones (validar, limpiar y click), para que el código sea más fácil de leer y de arreglar.