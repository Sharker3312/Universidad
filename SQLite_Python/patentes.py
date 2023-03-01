
import os, time, pyfiglet, time
import psycopg2
from colorama import *
###############Funciones Auxiliares##################
def clear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

def exit():
    os.system("exit")

def conectando():
    conectando=["C","o","n","e","c","t","a","n","d","o"]
    for _ in range(10):
        for spin in conectando:
            if spin=='o':
                #clear()
                print(end="\r")   
                print(spin)
                time.sleep(0.2)


            
def banner():
    def spin():
        spinner=['\\','|','/','-']
        for _ in range(10):
            for spin in spinner:
                print(spin,end="\r")
                time.sleep(0.2)

    ascii_banner=pyfiglet.figlet_format('Patentes sql')
    print(Fore.LIGHTGREEN_EX + ascii_banner)
    print("      made by"+Fore.LIGHTRED_EX+" #2_Team_TL-23")
    print(Fore.LIGHTGREEN_EX +"-" *50)
    print("Conectando con base de datos")
    print("-" *50+ Fore.YELLOW)
    spin()
    clear()

##############Consultas##############################
def listado_patentes():
    connection=psycopg2.connect(user="postgres",
                         password="postgres",
                         host="localhost",
                         port="5432",
                         database="sql_cujae")
    cursor=connection.cursor()
    cursor.execute("select nombreinventor,codigo from patentes")

    print("\nNombre del Inventor | Codigo de patente: ")
    for fila in cursor:
        print(fila)
    
    connection.close()

def listado_ayudantes():
    connection=psycopg2.connect(user="postgres",
                         password="postgres",
                         host="localhost",
                         port="5432",
                         database="sql_cujae")
    cursor=connection.cursor()
    cursor.execute("select nombre,name_ayudante from inventor")
    
    print("\nNombre inventor | Nombre ayudante: ")

    for fila in cursor:
        print(fila)
    
    connection.close()

def listado_investigadores_empresa():
    connection=psycopg2.connect(user="postgres",
                         password="postgres",
                         host="localhost",
                         port="5432",
                         database="sql_cujae")
    cursor=connection.cursor()
    cursor.execute("select name_inventor,name_ayudante from empresa")
    
    print("\nNombre inventor | Nombre ayudante: ")

    for fila in cursor:
        print(fila)
    
    connection.close()

def listado_asesores():
    connection=psycopg2.connect(user="postgres",
                         password="postgres",
                         host="localhost",
                         port="5432",
                         database="sql_cujae")
    cursor=connection.cursor()
    cursor.execute("select nombre,name_ayudante from inventor")
    
    print("\nNombre inventor | Nombre del asesorado: ")

    for fila in cursor:
        print(fila)

    connection.close()

def cantidad_patentes_empresa():
    connection=psycopg2.connect(user="postgres",
                         password="postgres",
                         host="localhost",
                         port="5432",
                         database="sql_cujae")
    cursor=connection.cursor()
    cursor.execute("select nombre,codigo_buy_patent from empresa")
    
    print("\nCodigo de patente por empresa: ")

    for fila in cursor:
        print(fila)

    connection.close()

def titulo_universitario():
    
    connection=psycopg2.connect(user="postgres",
                        password="postgres",
                        host="localhost",
                        port="5432",
                        database="sql_cujae")
    cursor=connection.cursor()
    cursor.execute("select nombre,titulo from ayudante")
    
    print("\nAyudante | Titulo Universitario: ")

    for fila in cursor:
        print(fila)
    
    connection.close()

def cant_h_invento():
    connection=psycopg2.connect(user="postgres",
                         password="postgres",
                         host="localhost",
                         port="5432",
                         database="sql_cujae")
    cursor=connection.cursor()
    cursor.execute("select nombre,hworkers from inventor")
    
    print("\nInventor | Cantidad de horas: ")

    for fila in cursor:
        print(fila)
    
    connection.close()

def fecha_contrato():
    connection=psycopg2.connect(user="postgres",
                         password="postgres",
                         host="localhost",
                         port="5432",
                         database="sql_cujae")
    cursor=connection.cursor()
    cursor.execute("select name_inventor,time_contract from empresa")
    
    print("\nInventor | Fecha de contrato: ")

    for fila in cursor:
        print(fila)
    connection.close()

def cant_inventores():
    connection=psycopg2.connect(user="postgres",
                         password="postgres",
                         host="localhost",
                         port="5432",
                         database="sql_cujae")
    cursor=connection.cursor()
    cursor.execute("select nombre,mod_super from inventor")
    
    print("\nInventor | Modalidad de superacion: ")

    for fila in cursor:
        print(fila)

    connection.close()

def ayudante():
    connection=psycopg2.connect(user="postgres",
                         password="postgres",
                         host="localhost",
                         port="5432",
                         database="sql_cujae")
    cursor=connection.cursor()
    cursor.execute("select name_ayudante,nombre from inventor")
    
    print("\nAyudante | Inventor: ")

    for fila in cursor:
        print(fila)
    connection.close()

def querys():

    clear()
    #banner()

    print("                                   Consultas")
    print("\n\n\t Selecciona una opción")
    print("\t1 - Listado de patentes por Inventor")
    print("\t2 - Listado de Ayudantes por inventor")
    print("\t3 - Listado de Investigadores contratados por empresa")
    print("\t4 - Listado de Inventores que asesoren a otro Inventor")
    print("\t5 - Cantidad de Inventores con Doctorados y Maestría")
    print("\t6 - A que inventor pertenece un ayudante")
    print("\t7 - Cantidad de patentes por empresa")
    print("\t8 - Cantidad de horas que un inventor dedicó a su invento")
    print("\t9 - Cuántos ayudantes poseen Título Universitario")
    print("\t10 - En que fecha una empresa contrató al investigador")
    print("\t11 - Atras")

    while True:

        opcionMenu=input("\nOpcion: ")

        if opcionMenu=="1":
            clear()
            listado_patentes()
            print("\n\nPresione 'f' para ir hacia atras")

        elif opcionMenu=="2":
            clear()
            listado_ayudantes()
            print("\n\nPresione 'f' para ir hacia atras")
        elif opcionMenu=="3":
            clear()
            listado_investigadores_empresa()
            print("\n\nPresione 'f' para ir hacia atras")
        elif opcionMenu=="4":
            clear()
            listado_asesores()
            print("\n\nPresione 'f' para ir hacia atras")
        elif opcionMenu=="5":
            clear()
            cant_inventores()
        elif opcionMenu=="6":
            clear()
            print("\n\nPresione 'f' para ir hacia atras")
            ayudante()
        elif opcionMenu=="7":
            clear()
            cantidad_patentes_empresa()
            print("\n\nPresione 'f' para ir hacia atras")
        elif opcionMenu=="8":
            clear()
            cant_h_invento()
            print("\n\nPresione 'f' para ir hacia atras")
        elif opcionMenu=="9":
            clear()
            titulo_universitario()
            print("\n\nPresione 'f' para ir hacia atras")
        elif opcionMenu=="10":
            clear()
            fecha_contrato()
            print("\n\nPresione 'f' para ir hacia atras")
        elif opcionMenu=="f":
            querys()
        elif opcionMenu=="11":
            Menu()
        else: 
            print("Digite una opcion correcta")
            time.sleep(1)
            querys()

#########################Insertar Datos###########################

def insert_inventor():
    clear()
    print("Cuantos Inventores desea Insertar: ")
    cant=input()
    asesora=""
    name_ayudante=""

    for i in cant:
        clear()
        print("Inventor #"+i)
        print("\nNombre: ",end="");nombre=input()
        print("DNI: ",end="");dni=input()
        print("Direccion: ",end="");direccion=input()
        print("Telefono: ",end="");telefono=input()
        print("Modalidad de superacion Profesional: ",end="");mod_super=input()
        print("Horas trabajadas en el invento: ",end="");hworked=input()
        print("Nombre del asesorado: ",end="");asesora=input()
        print("Nombre de ayudante: ",end="");name_ayudante=input()
            
        
        


        connection=psycopg2.connect(user="postgres",
                         password="postgres",
                         host="localhost",
                         port="5432",
                         database="sql_cujae")

        cursor=connection.cursor()
        
        insert="INSERT INTO Inventor(Nombre,DNI,Direccion,Telefono,Mod_super,Hworkers,name_ayudante,asesora) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            
        datos=(nombre,dni,direccion,telefono,mod_super,hworked,name_ayudante,asesora)
        cursor.execute(insert, datos)


        connection.commit()
        print("\n\nInventor #"+i+" creado con exito....")

    connection.close()
    insert()

def insert_ayudante():
    clear()
    print("Cuantos Ayudantes desea Insertar: ")
    cant=input()
    asesora=""
    name_ayudante=""

    for i in cant:
        clear()
        print("Ayudante #"+i)
        print("\nNombre: ",end="");nombre=input()
        print("DNI: ",end="");dni=input()
        print("Direccion: ",end="");direccion=input()
        print("Telefono: ",end="");telefono=input()
        print("Graduado Universitario(0/1): ",end="");titulo=input()
        print("Especialidad: ",end="");especialidad=input()
        
        connection=psycopg2.connect(user="postgres",
                         password="postgres",
                         host="localhost",
                         port="5432",
                         database="sql_cujae")

        cursor=connection.cursor()
        
        insert="INSERT INTO Ayudante(Nombre,DNI,Direccion,Telefono,Titulo,Especialidad) VALUES (%s,%s,%s,%s,%s,%s)"
            
        datos=(nombre,dni,direccion,telefono,titulo,especialidad)
        cursor.execute(insert, datos)


        connection.commit()

        print("\n\nAyudante #"+i+" creado con exito....")

    connection.close()
    insert()

def insert_empresa():
    clear()
    print("Cuantas Empresas desea insertar: ")
    cant=input()

    for i in cant:
        clear()
        print("Empresa #"+i)
        print("\nNombre: ",end="");nombre=input()
        print("Codigo: ",end="");codigo=input()
        print("Telefono: ",end="");telefono=input()
        print("Direccion: ",end="");direccion=input()
        
        print("Fecha de compra de la patente: ",end="");fecha_compra=input()
        print("Fecha de contrato del investigador: ",end="");fecha_investigador=input()
        print("Nombre del Investigador contratado: ",end="");name_inventor=input()
        print("Nombre del ayudante contratado: ",end="");name_ayudante=input()


        connection=psycopg2.connect(user="postgres",
                         password="postgres",
                         host="localhost",
                         port="5432",
                         database="sql_cujae")

        cursor=connection.cursor()
        
        insert="INSERT INTO Empresa(Nombre,Codigo,Telefono,Direccion,codigo_buy_patent,time_contract,name_inventor,name_ayudante) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            
        datos=(nombre,codigo,telefono,direccion,fecha_compra,fecha_investigador,name_inventor,name_ayudante)
        cursor.execute(insert, datos)


        connection.commit()

        print("\n\nEmpresa #"+i+" creado con exito....")

    connection.close()
    insert()

def insert_patente():
    clear()
    print("Cuantas patentes desea insertar: ")
    cant=input()

    for i in cant:
        clear()
        print("Patente #"+i)
        print("\nNombre del Inventor: ",end="");nombre_inventor=input()
        print("Codigo: ",end="");codigo=input()
        print("Fecha: ",end="");fecha=input()

        connection=psycopg2.connect(user="postgres",
                         password="postgres",
                         host="localhost",
                         port="5432",
                         database="sql_cujae")

        cursor=connection.cursor()
        
        insert="INSERT INTO Patentes(NombreInventor,Codigo,Fecha) VALUES (%s,%s,%s)"
            
        datos=(nombre_inventor,codigo,fecha)
        cursor.execute(insert, datos)


        connection.commit()

        print("\n\nPatentes #"+i+" creado con exito....")

    connection.close()
    Menu()



def insert():
    clear()

    print("                                   Insertar")
    print("\n\n\t Selecciona una opción")
    print("\t1 - Inventor")
    print("\t2 - Ayudante")
    print("\t3 - Empresa")
    print("\t4 - Patente")
    print("\t5 - Atras")

    while True:
    
        opcionMenu=input("\nOpcion: ")

        if opcionMenu=="1":
            insert_inventor()
        elif opcionMenu=="2":
            insert_ayudante()
        elif opcionMenu=="3":
            insert_empresa()
        elif opcionMenu=="4":
            insert_patente()
        elif opcionMenu=="5":
            Menu()
        else: 
            print("Digite una opcion correcta")
            time.sleep(1)
            insert()
#####MEnu#########################################
def Menu():
    
    clear()

    print("                                   Welcome")
    print("\n\n\t Selecciona una opción")
    print("\t1 - Insertar Datos")
    print("\t2 - Consultas")
    print("\t3 - Salir")

    while True:
    
        opcionMenu=input("\nOpcion: ")

        if opcionMenu=="1":
            insert()
        elif opcionMenu=="2":
            querys()
        elif opcionMenu=="3":
            break;
        else: 
            print("Digite una opcion correcta")
            Menu()
    

def connection_postgres():
    banner()
    try: 
        connection=psycopg2.connect(user="postgres",
                         password="postgres",
                         host="localhost",
                         port="5432",
                         database="sql_cujae")

        cursor=connection.cursor()
        print(connection.get_dsn_parameters(),"\n")

        cursor.execute("SELECT version();")
        record=cursor.fetchone()
        print("You are conenected to - ",record,"\n")

        connection.close()



    except(Exception, psycopg2.Error)as error:
        print("Error while connecting to PostgreSQL",error)


def create_table():
    try: 
        connection=psycopg2.connect(user="postgres",
                         password="postgres",
                         host="localhost",
                         port="5432",
                         database="sql_cujae")

        cursor=connection.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS  Empresa(
             id serial PRIMARY KEY,
             Nombre varchar(20),
             Codigo integer,
             Telefono integer,
             Direccion varchar(20),
             codigo_buy_patent varchar(20),
             time_contract varchar(20),
             name_inventor varchar(20),
             name_ayudante varchar(20)
             );
             """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS Patentes(
             id serial PRIMARY KEY,
             NombreInventor varchar(20),
             Codigo integer,
             Fecha varchar(20)
             );
             """)
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS Inventor(
            id serial PRIMARY KEY,
            Nombre varchar(20),
            DNI bigint,
            Direccion varchar(20),
            Telefono varchar(20),
            Mod_super varchar(20),
            Hworkers varchar(20),
            name_ayudante varchar(20),
            asesora boolean
            );
            """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS Ayudante(
            id serial PRIMARY KEY,
            Nombre varchar(20),
            DNI bigint,
            Direccion varchar(20),
            Telefono varchar(20),
            Titulo boolean,
            Especialidad varchar(20)
            );
            """)

        connection.commit()
        connection.close()

    except(Exception, psycopg2.Error)as error:
        print("Error while connecting to PostgreSQL",error)

####
if __name__ == '__main__':
   connection_postgres()
   time.sleep(5)
   create_table()
   Menu()

