import sqlite3 as sql

def mostrar_menu(opciones):
    print('Menu Opciones:')
    for clave in sorted(opciones):
        print(f'{clave}) {opciones[clave][0]}')           

def leer_opcion(opciones):
    while (a := input('Opcion:')) not in opciones:
        print('Opcion incorrecta, vuelva a intentarlo')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones,opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion,opciones)
        print() # se imprime una linea en blanco para clarificar la salida en pantalla

def menu_principal():
    opciones = {
        '1':('Registrar', registrar),
        '2':('Eliminar', eliminar),
        '3':('Editar', editar),
        '4':('Listar', listar),      
        '5':('Salir', salir)
    }       

    generar_menu(opciones,'5')

def registrar():
    print('Registrado exitosamente')

def eliminar():
    print('Eliminado Correctamente')

def editar():
    print('Editado correctamente')

def listar():
    print('Lista de Productos')

def salir():
    print('Saliendo del menu\n')

if __name__== '__main__':
    menu_principal()