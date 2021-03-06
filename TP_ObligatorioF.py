import numpy as np
import os
from pyrecord import Record




# Una entidad bancaria tiene organizada su información en los siguientes vectores de registros:
# CUENTAS datos de los clientes
# CAJEROS datos de los cajeros automáticos 

#creo el tipo de dato "cliente"
cliente=Record.create_type("cliente","numeroCuenta","apellido","nombre","dni","tipoCuenta","saldo","estado",
                           numeroCuenta=0,
                           apellido="",
                           nombre="",
                           dni="",
                           tipoCuenta=0,
                           saldo=0.0,
                           estado=False)


# #creo el tipo de dato "cajero"
cajero=Record.create_type("cajero","numeroCajero","ubicacion","movimientos",
                          numeroCajero=0,
                          ubicacion="",
                          movimientos=0)


# #creo vector "vcuentas" sobredimensionado para poder agregar mas clientes
# vcuentas=np.array([cliente]*650)
# #Guardo en el campo "Numero de cuenta" del primer registro la cantidad util de vector, con la que voy a pode modificar su cantidad util segun agregue clientes.(no voy a quitar clientes porque solo se desactivan, no se borran)
# vcuentas[0].numeroCuenta=600

# #creo vector de cajeros 
# vcajeros=np.array([cajero]*120)

#Funciones.....................................................................................................................................................................

# hace una pausa poniendo un cartel
def pausa():
    print()
    print(" "*20,end=" ")
    input(" Presione Enter para continuar...")

def mensaje(m):
    print()
    print(" "*20,m+'...')

#  Esto sirve para detectar el Sist Operativo
#  Y envía la orden de limpiar la pantalla según corresponda.
#  'posix' (sistemas POSIX y distribuciones de Linux).
#  'nt' (Windows).
def limpiar_pantalla():
    if (os.name)=='posix':
        os.system('clear')
    if (os.name)=='nt':
        os.system('cls')
    return None
    
# Permite elegir opciones de menú
# Validando entre 0 y el pasado por parámetro
# Y retornando la opción elegida 
def elegir(ultimo):
    print()
    print(" "*22,end=" ")
    opc=input(" Elija una opción: ")
    opc=valiDigito2(opc)
    opc=int(opc)
    while((opc>ultimo) or (opc<0)):
        print(" "*20,"Lo siento, la Opción es inválida")
        print(" "*22,end=" ")
        opc=input(" Elija una opción: ")
        opc=valiDigito2(opc)
        opc=int(opc)
        
    return opc

#valido que la entrada sea un digito
def valiDigito2(n):
    
    while not(n.isdigit()) and not(n=="0"):
            print(" "*20,"Lo siento, la Opción es inválida")
            print(" "*22,end=" ")
            n=input(" Elija una opción: ")
    return n

#Creo los vectores en esta funcion para poder asignarlos a una variable local dentro de la ejecucion principal.
def crearVectoresR():
    cliente=Record.create_type("cliente","numeroCuenta","apellido","nombre","dni","tipoCuenta","saldo","estado",
                           numeroCuenta=0,
                           apellido="",
                           nombre="",
                           dni="",
                           tipoCuenta=0,
                           saldo=0.0,
                           estado=False)


    #creo el tipo de dato "cajero"
    cajero=Record.create_type("cajero","numeroCajero","ubicacion","movimientos",
                            numeroCajero=0,
                            ubicacion="",
                            movimientos=0)


    #creo vector "vcuentas" sobredimensionado para poder agregar mas clientes
    vcuentas=np.array([cliente]*650)
    #Guardo en el campo "Numero de cuenta" del primer registro la cantidad util de vector, con la que voy a pode modificar su cantidad util segun agregue clientes.(no voy a quitar clientes porque solo se desactivan, no se borran)
    vcuentas[0].numeroCuenta=601

    #creo vector de cajeros 
    vcajeros=np.array([cajero]*121)
    return vcuentas,vcajeros


#1)
#Carga el vector de registros con el archivo "cuentas.txt"
def cargoClientes(vector):
    
    
    
    a1=open('cuentas.txt','r')
       
    linea=a1.readline().strip()
    i=1
    
    while linea!='':
        s=linea.split(',')
        numeroCuenta=int(s[0])
        apellido=s[1]
        nombre=s[2]
        dni=s[3]
        tipoCuenta=int(s[4])
        saldo=float(s[5])
        estado=bool(s[6])
        
        
        vector[i]=cliente()
        vector[i].numeroCuenta=numeroCuenta
        vector[i].apellido=apellido
        vector[i].nombre=nombre
        vector[i].dni=dni
        vector[i].tipoCuenta=tipoCuenta
        vector[i].saldo=saldo
        vector[i].estado=estado    
        
        
       
        i+=1
        linea=a1.readline().strip()
        
    
    a1.close()  
 
#Carga el vector de registros con el archivo "cajeros.txt"       
def cargoCajeros(vector):
    
    
    
    a1=open('cajeros.txt','r')
       
    linea=a1.readline().strip()
    i=1
    
    while linea!='':
        s=linea.split(',')
        numeroCajero=int(s[0])
        ubicacion=s[1]
        movimientos=int(s[2])
        
        
        vector[i]=cajero()
        vector[i].numeroCajero=numeroCajero
        vector[i].ubicacion=ubicacion
        vector[i].movimientos=movimientos
          
        
        
        
        i+=1
        linea=a1.readline().strip()
    a1.close()    
 
#consulta el numero de cuenta a buscar y valida su tipo y que sea una cuenta existente 
def consultaCuenta(vector):
    cuenta=input("ingrese el numero de cuenta que desea consultar: ")
    limpiar_pantalla()
        
    validodigito(cuenta)
    
    cuenta=int(cuenta)
    while (cuenta<1000 or cuenta>((vector[0].numeroCuenta)+999)) and not(cuenta==0):
        print("el numero de cuenta es inexistente")
        print("intente nuevamente o ingrese 0 para salir")
        cuenta=input()
        cuenta=validodigito(cuenta)
        cuenta=int(cuenta)
        limpiar_pantalla()
    
    
    return cuenta

#valida que la entrada solo contenga digitos
def validodigito(numero):    
        while not(numero.isdigit()) and not(numero=="0"):
            print("su numero de cuenta no debe contener letras")
            print("intente nuevamente o ingrese 0 para salir: ")
            numero=input()
            limpiar_pantalla()
        return numero

#Devuelve los datos de la cuenta con pasarle un numero de cuenta valido   
def buscoCuenta(vector,numero): 

    if not(numero==0):
        j=numero-999
        
        apellido=vector[j].apellido
        nombre=vector[j].nombre
        dni=vector[j].dni
        tipoCuenta=vector[j].tipoCuenta
        saldo=vector[j].saldo
        estado=vector[j].estado
    
        

            
            
        
        print(f'numero de cuenta: {numero}')
        print(nombre," ",apellido)
        print("Dni: ",dni)
        print("Tipo de cuenta: ",tipoCuenta)
        print("$",saldo)
            
        if vector[j].estado==False:
            print("La cuenta se encuentra inactiva") 
        return estado   


#2)
def corteDeControl(vcuentas):
    
    a1 = open('operaciones.txt','r')
    # leo una línea antes de entrar y cargo las variables
    linea=a1.readline().strip()  # Uso strip para quitar el fin de linea \n
    s=linea.split(',') # divido la línea leida usando el separador coma
    
    cuenta=int(s[0])     # Tomo numero de cuenta para cargar cuenta  anterior
    vMovCajeros=np.array([0]*121)
    
    i=0
    while linea!='': # cuando línea sea vacía '' finalizó el archivo
        suma=0.0
        cont=0
        print()
        print(f"                      Cuenta Nro {cuenta}")
        anterior=cuenta
        while linea!='' and cuenta==anterior:  # cuando línea sea vacía '' finalizó el archivo
            # Acumulo y cuento
            cuenta=int(s[0])
            año=int(s[1])
            mes=int(s[2])
            dia=int(s[3])
            numeroCajero=int(s[4])
            tipoMovimiento=int(s[5])
            monto=float(s[6])
            
            #sumo o resto los movimientos de la cuenta
            if tipoMovimiento==1:
                suma+=monto
            elif tipoMovimiento==2:
                suma-=monto 
            
            #sumo la cantidad de movimientos de los cajeros
            vMovCajeros[numeroCajero]+=1
            
           
            
            
            

            
            
            linea=a1.readline().strip() # Leo una nueva línea y cargo las variables
            if linea!='':
                s=linea.split(',') # divido la línea leida usando el separador coma
                cuenta=int(s[0])     # Tomo carrera para cargar comparar con carrera anterior

        
         #actualizo saldo de las cuentas
            
        vcuentas[cuenta-999].saldo+=suma
            
               
        
        #Muestro el saldo anual de los movimientos
        print(f"El saldo de los movimientos anuales de la cuenta es: {round(suma,2)}")
        
        # Y vuelvo a empezar
    a1.close() # cierro el archivo
    actualizado=True
    return vMovCajeros,actualizado


def mayorCajero(v):
    mayor=0
    cant=0
    for i in range(len(v)):
        if v[i]>cant:
            cant=v[i]
            mayor=i
    return mayor,cant
        
def actualizarCajeros(vcajeros,vMovCajeros,actCajeros):
    if actCajeros==False:    
        for i in range(1,len(vcajeros)):
            
            vcajeros[i].movimientos+=vMovCajeros[i] 
    else:
        print("Los cajeros ya han sido actualizados anteriormente")
    actCajeros=True
    return actCajeros


def mostrarCajero(vcajeros): 
    
    for i in range(1,len(vcajeros)):
        
        print(vcajeros[i].numeroCajero,      vcajeros[i].ubicacion,          vcajeros[i].movimientos)
    
     

              
    





#3)
#Pregunta un numero de Dni, busca si esta, si no esta pregunta los datos que faltan para dar de alta la cuenta. Si esta activa lo informa, y si esta inactiva 
def alta(vector):
    dni=input("ingrese numero de documento: ")
    dni=validoDni(dni)
    dni=str(dni)
    i=1
    esta=False
    util=vector[0].numeroCuenta
    while i<=(vector[0].numeroCuenta):
        
        
        if dni==vector[i].dni:
            esta=True
            if vector[i].estado==True:
                print("la cuenta se encuentra activa")
                print(f'numero de cuenta: {vector[i].numeroCuenta}')
                print(vector[i].nombre," ",vector[i].apellido)
                print("Dni: ",vector[i].dni)
                print("Tipo de cuenta: ",vector[i].tipoCuenta)
                print("$",vector[i].saldo)
            else:
                print("Este DNI ya tuvo una cuenta existente,pero esta inactiva")
                print(f'numero de cuenta: {vector[i].numeroCuenta}')
                print(vector[i].nombre," ",vector[i].apellido)
                print("Dni: ",vector[i].dni)
                print("Tipo de cuenta: ",vector[i].tipoCuenta)
                print("$",vector[i].saldo)
                print()
                print("La cuenta será dada de alta")
                print("si desea modificar datos , busque en el menu principal -4 Modificar datos")
                
                #aelegir entre activar o modificar datos 
        
        i+=1
    if esta==False:
        vector[util+1].dni=dni
        vector[util+1].nombre=input("ingrese nombre: ")
        vector[util+1].apellido=input("ingrese apellido: ")
        tipoCuenta=input("ingrese tipo de cuenta")
        vector[util+1].tipoCuenta=validoTipoCuenta(tipoCuenta)
        vector[util+1].saldo=0.0
        vector[util+1].estado=True
        print("")
        print("La cuenta fue dada de alta")
        vector[0].numeroCuenta+=1
    
def validoDni(numero):    
        while not(numero.isdigit()) and not(numero=="0"):
            print("su numero de Dni no debe contener letras")
            print("intente nuevamente o ingrese 0 para salir: ")
            numero=input()
            limpiar_pantalla
        return numero

def validoTipoCuenta(numero):    
        while not(numero.isdigit()) and not(numero=="0"):
            print("su tipo de cuenta debe ser un numero")
            print("intente nuevamente o ingrese 0 para salir: ")
            numero=input()
            
        
        numero=int(numero)
            
        while numero<1 or numero>15:
            print("su tipo de cuenta debe ser un numero entre 1 y 15")
            print("intente nuevamente o ingrese 0 para salir: ")
            numero=input()
            numero=validoTipoCuenta(numero)
            
            
            
            
        return numero



#valida que la cuenta a dar de baja sea una cuenta existente
def borrarCuenta(vector):
    cuenta=input("ingrese el numero de cuenta que desea dar de baja: ")
    limpiar_pantalla()
        
    validodigito(cuenta)
    
    cuenta=int(cuenta)
    while (cuenta<1000 or cuenta>((vector[0].numeroCuenta)+999)) and not(cuenta==0):
        print("el numero de cuenta es inexistente")
        print("intente nuevamente o ingrese 0 para salir")
        cuenta=input()
        cuenta=validodigito(cuenta)
        cuenta=int(cuenta)
        limpiar_pantalla()
    
    
    return cuenta

#pide un numero de cuenta y valida que este sea existente.Si esta activo lo muestra y pone inactivo.Si esta inactivo lo informa.
def baja(vector):
    cuenta=borrarCuenta(vector)
    estado=buscoCuenta(vector,cuenta)
    if estado==True:
        print("La cuenta será dada de baja")
    
    if not(cuenta==0):
        vector[cuenta-999].estado=False
       
#valida que la cuenta a modificar sea una cuenta existente
def modificarCuenta(vector):
    cuenta=input("ingrese el numero de cuenta que desea modificar: ")
    limpiar_pantalla()
        
    validodigito(cuenta)
    
    cuenta=int(cuenta)
    while (cuenta<1000 or cuenta>((vector[0].numeroCuenta)+999)) and not(cuenta==0):
        print("el numero de cuenta es inexistente")
        print("intente nuevamente o ingrese 0 para salir")
        cuenta=input()
        cuenta=validodigito(cuenta)
        cuenta=int(cuenta)
        limpiar_pantalla()
    
    
    return cuenta


#submenu modificar datos
def modificarDatos(v):
    #valido que la cuenta sea existente
    n=modificarCuenta(v)
    
    #traigo los datos de la cuenta
    buscoCuenta(v,n)
    print(" "*25,"Cual campo deseas modificar?")
    print()
    print(" "*25,"1 Nombre")
    print(" "*25,"2 Apellido")
    print(" "*25,"3 DNI")
    print(" "*25,"4 Tipo de cuenta")
    print()
    print(" "*28,"0 Salir")
    op=elegir(4)
    if op==1:
        v[n-999].nombre=input("ingrese nombre y presione enter para finalizar: ")
    elif op==2:
        v[n-999].apellido=input("ingrese apellido y presione enter para finalizar: ")
    elif op==3:
        dni=input("ingrese DNI y presione enter para finalizar: ")    
        dni=validoDni(dni)
        v[n-999].dni=dni
    elif op==4:
        tipo=input("ingrese tipo de cuenta y presione enter para finalizar: ")    
        tipo=validoTipoCuenta(tipo)
        v[n-999].tipoCuenta=tipo
    return n
        

#.................................................................................................................................................................................





def menuPrincipal():

    
    vcuentas,vcajeros=crearVectoresR()
    cargoClientes(vcuentas)
    cargoCajeros(vcajeros)
    vMovcajeros=np.array([0]*121)
    actualizado=False
    actCajeros=False
    seguir=True
    while seguir:
        limpiar_pantalla()
        print(" "*25,"Menú Principal")
        print()
        print(" "*25,"1 Consultar saldo con numero de cuenta")
        print(" "*25,"2 Dar de alta una cuenta")
        print(" "*25,"3 Dar de baja una cuenta")
        print(" "*25,"4 Modificar los datos de una cuenta")
        print(" "*25,"5 Actualizacion de cuentas")
        print(" "*25,"6 Cajero con mayor cantidad de movimientos anual")
        print(" "*25,"7 Actualizacion de cajeros")
        # print(" "*25,"8 mostrar cajeros")
        print()
        print(" "*28,"0 Salir")
        op=elegir(7)
        if op==1:
            limpiar_pantalla()
            numeroCuenta=consultaCuenta(vcuentas)
            buscoCuenta(vcuentas,numeroCuenta)
            pausa()
        elif op==2:
            limpiar_pantalla()
            alta(vcuentas)
            pausa()
        elif op==3:
            limpiar_pantalla()
            baja(vcuentas)
            pausa()
        elif op==4:
            limpiar_pantalla()
            cuenta_modificada=modificarDatos(vcuentas)
            limpiar_pantalla()
            buscoCuenta(vcuentas,cuenta_modificada)
            pausa()
        elif op==5:
            limpiar_pantalla()
            if actualizado==False:
                vMovcajeros,actualizado=corteDeControl(vcuentas)
            else:
                print("Las cuentas ya han sido actualizadas anteriormente")
            pausa()
        elif op==6:
            limpiar_pantalla()
            if actualizado==True:
                mayorC,cant=mayorCajero(vMovcajeros)
                print(f"El cajero con mayor cantidad de movimientos en el año es el numero: {mayorC}")
                print(f"Cantidad de movimientos: {cant}")
            else:
              print("Para ver esta informacion primero debe actualizar las cuentas")
            pausa()    
        elif op==7:
            limpiar_pantalla()
            actCajeros=actualizarCajeros(vcajeros,vMovcajeros,actCajeros)
            pausa()
        #para  debugear y ver el estado de los cajeros se puede descomentar esta opcion, y poner 8 en el parametro de elegir
        # elif op==8:
        #     limpiar_pantalla()
        #     mostrarCajero(vcajeros)        
        #     pausa()
        
                  
        else:
            limpiar_pantalla()
            print(" "*25,"Nos vemos la próxima...")
            pausa()
            seguir=False
            limpiar_pantalla()
            




menuPrincipal()








            








