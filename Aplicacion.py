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
    Codigo = input('Ingrese el codigo del nuevo producto: ')
    Nombre = input('Ingrese el nombre del nuevo prodcuto: ')
    Precio = input('Ingrese el Precio del nuevo producto: ')
    nuevo_producto(Codigo,Nombre,Precio)
    print('Producto registrado exitosamente')
def eliminar():
    print('opcion eliminar')
def editar():
    print('opcion editar')
def listar():
    print('Lista de Productos:\nidpro\tcodigo\tnombre\tprecio ')
    listar_productos()
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

def nuevo_producto(codigo,nombre ,precio):
    conn = sql.connect("Arones_Bravo_Huanuco_Nanquen_almacen.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO Producto(codigo,nombre,precio) VALUES ('{codigo}','{nombre}',{precio})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def registrar10(lista_productos):
    conn = sql.connect("Arones_Bravo_Huanuco_Nanquen_almacen.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO Producto(codigo,nombre,precio) VALUES (?,?,?)"
    cursor.executemany(instruccion,lista_productos)
    conn.commit()
    conn.close()



def listar_productos():
    conn = sql.connect("Arones_Bravo_Huanuco_Nanquen_almacen.db")
    cursor = conn.cursor()
    instruccion = f"SELECT idproducto FROM Producto"
    cursor.execute(instruccion)
    listid = cursor.fetchall()
    instruccion = f"SELECT codigo FROM Producto"
    cursor.execute(instruccion)
    listcod = cursor.fetchall()
    instruccion = f"SELECT nombre FROM Producto"
    cursor.execute(instruccion)
    listna = cursor.fetchall()
    instruccion = f"SELECT precio FROM Producto"
    cursor.execute(instruccion)
    listpr = cursor.fetchall()
    conn.commit()
    conn.close()
    i = 0
    while i < len(listid):
        print(f'{listid[i][0]}\t{listcod[i][0]}\t{listna[i][0]}\t{listpr[i][0]}')       
        i +=1   






if __name__ == "__main__" :
    lista_productos = [
       ("PRO01","Impresora L3210",699),
       ("PRO02","Colchon Brave 2 Plazas",589),
       ("PRO03","Silla gamer rojo",339),
       ("PRO04","Mesa de Centro Tabaco",329),
       ("PRO05","Escritorio Plegable Walnut", 129),
       ("PRO06","Arroz Extra Costero 5kg", 24.45),
       ("PRO07","Aceite de Soya Sao 900ml", 8.9),
       ("PRO08","Sal de Mesa Marina Emsal Bolsa 1kg",2),
       ("PRO09","Arveja Verde Tesoro Del Campo Bolsa 500g",3.7),
       ("PRO10","Lomos de atun campomar en agua y sal 150g",6.3)
    ]
    #registrar10(lista_productos)
    #crearBD()
    #crearTabla()
    menu_principal()
    pass