from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

app = Flask(__name__) # En app se encuentra nuestro servidor web de Flask, app es
#el nombre recomendado. Con este trocito de codigo Flask me levanta  un servidor web
# pero dentro de mi ordenador.

#Servidor web: un servidor web es un sistema operativo de linux (habitualmente a
#nivel de servidor todo es practicamente Linux.Que despliega una serie de programas
#que hace que parte del almacenamiento de ese ordenador no sea local, si no que se
#pueda ver a traves de internet. A traves de una direcion IP. Por todo el mundo hay
#unos servidores DNS que en funcion de nuestra ubicacion geografica, nuestro movil
# se conecta al servidor DNS mas cercano, nuestro movil le pregunta al DNS
# sabes quien es google.es y te responde con el IP. movil---->DNS----->movil----->
#-->servidor web.

#OJO Vamos a programar nuestra aplicacion de manera local NO ONLINE, pero se accede
#desde nuestro navegador. Ejemplo: Jupyter, monta un servidor web y accedemos a esa
#pagina web que el crea. Está almacenada dentro de nuestro sistema, desde el esterior
#no se puede acceder.

#------>protocolo http--->navegador, uno encima del otro es la
#vinculacion que hace por nosotros, es la forma de crear URL.

# La barra (el slash) se conoce como la página de inicio (página home).
# Vamos a definir para esta ruta, el comportamiento a seguir.
@app.route('/')
def home():#------> python

    todas_las_tareas = db.session.query(Tarea).all()

    for i in todas_las_tareas:
        print(i)

    return render_template("index.html",lista_de_tareas=todas_las_tareas) #Al hacer un render_template Flask va a estar
#mirando a la carpeta template por defecto, sino nos dará un error.

@app.route("/crear-tarea",methods=["POST"])
def crear():

    tarea = Tarea(contenido=request.form["contenido_tarea"], hecha=False)
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/eliminar-tarea/<id>")
def eliminar(id):

    tarea= db.session.query(Tarea).filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/tarea-hecha/<id>')
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first() # Se obtiene la tarea que se busca
    tarea.hecha = not(tarea.hecha) # Guardamos en la variable booleana de la tarea, su contrario
    db.session.commit() # Ejecutar la operación pendiente de la base de datos
    return redirect(url_for('home')) # Esto nos redirecciona a la función home()

if __name__ == '__main__':

    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)








#El debug=True hace que cada vez que reiniciemos el
#servidor o modifiquemos codigo, el servidor de Flask se reinicie solo. Si hay
#errores nos lo muestra por consola. Con app.run arranca el servidor.

#localhost= 120.0.0.1, hace referencia a nosotros mismo siempre esta IP.
#Todo lo que tenga que ver con la web tendra un IP y un puerto, distintas puertas
#por las que podremos establecer comunicaciones, los puertos vienen de los protocolos
#de red. HTTP-->80. HTTPS---->8080.

#Una vez que hemos arrancado el servidor ya no podemos hacer nada en el terminal,
#nos aparece un listado con las codigos de error o no, el codigo 200
#es que todo ha salido bien. Pero con ctrl C cancelo esa ejecucion del servidor
#y me vuelve a aparecer el ven.






#Vamos a usar framework, que son algo mas que una libreria que nos proporcionan unas
#funcionalidades especificas, el framework tiene normas para trabajar  a diferencia
#de las librerias.

#En las paginas web no todo lo hace python sino que debe comunicarse con otras
#tecnologias abyacentes,partes para poder dar forma a la pagina web. Es dificil
#entender todas las partes de esta practica en profundidad.
#¿COMO LLEGO A LA FUNCION CREAR? ¿Lo que tengo en el input en HTML como lo leo desde Python para que ese
#input me llegue a la variable contenido? ¿puedo desde mi fichero Python leer información de mi fichero index.html?SI,
#pero no toda la información, por ejemplo, puedo leer la información que tengo dentro de los formularios. ¿Como puedo
#acceder a un elemento concreto de mi formulario? Con la variable name que acabo de crear, a traves del metodo de Flask
#request.form["nombre de variable del formulario contenido_tarea en este ejemplo"]

#Ahora como podemos trasladar la lista de objetos de nuestra consulta a HTML si en
#HTML no se puede escribir codigo sino es con lenguaje javascrip (es el que se usa
#por defecto) pues con jinja2, que nos permite escribir codigo en HTML pero cosas
#muy basicas.Ojo aqui se produce un error comun, es que cuando quiero trabajar con
#sqlalchemy y HTML le tengo que decir a la BDD que trabeje siempre en segundo plano
#trabajar en background, en el create