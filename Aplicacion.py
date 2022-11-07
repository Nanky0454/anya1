import sqlite3 as sql
#Metodos del menu
def mostrar_menu(opciones):

    print('Menu opciones:')
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
        '2':('Eliminar',eliminar),
        '3':('Editar', editar),
        '4':('Listar', listar),      
        '5':('Salir', salir)
    }       

    generar_menu(opciones,'5')
#---------------------------------------------------------------------------------------

#Metodos de opciones


def registrar():
    print('opcion registrar')
def eliminar():
    print('opcion eliminar')
def editar():
    print('opcion editar')
def listar():
    print('opcion listar')
def salir():
    print('opcion salir')

#-------------------------------------------------------
#Metodos Base de Datos
def crearBD():
    conn = sql.connect("Arones_Bravo_Huanuco_Nanquen_almacen.db")
    conn.commit()
    conn.close()
    
def crearTabla():
    conn = sql.connect("Arones_Bravo_Huanuco_Nanquen_almacen.db")
    cursor = conn.cursor()
    cursor.execute(
    """CREATE TABLE Producto (
        idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo text,
        nombre text,
        precio float 
    )"""
    )
    conn.commit()
    conn.close()










if __name__ == "__main__" :
    #menu_principal()
    #crearBD()
    #crearTabla()
    pass

    










      