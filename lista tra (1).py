import os
os.system("cls")

glosa = f'''        {'LISTADO DE TRABAJADORES'}
{'-' *130}
{"Trabajador":<20} {"Cargo":<15} {"Sueldo Bruto":<20}{"Desc. Salud":<25} {"Desc. AFP":<25} {"Líquido a pagar":<25}
{'-' *130}
'''#(:<)salta espacios hasta la posocion que se le indique, permite ordenar tablas 
menu = """
1. registrar trabajador
2. lista de trabajadores
3. imprimir plantilla 
4. Salir 
"""
trabajadores = []
cargos = ["ceo","Desarrollador","analista de datos"]

def registrar():
    while True:
        try:
            nom = input("nombre: ").upper()
            #.strip()elimina los espacios de los extremos
            car = input(f"cargo {cargos}: ").strip().lower()
            sueldo = int(input("sueldo: "))
            salud = round(sueldo * 0.70)
            afp = round(sueldo * 0.12)
            liquido = round(sueldo - salud - afp)
            if len(nom)>0 and len(car)>0 and sueldo>0 and car in cargos:
                trabajadores.append([nom,car,sueldo,afp,salud,liquido])
                print(listar())
                input()
                break
            else:
                input("falta ingresar algo")
        except:
            input("exepcion: ")
def listar():
    salida = glosa #comienza copiando el texto del titulo en salida 
    for r in trabajadores:#r recupera cada pedido de la lista
        salida += f"{r[0]:<22}" #nombre 
        salida += f"{r[1]:<16}" #cargo
        salida += f"{r[2]:<20}" #sueldo 
        salida += f"{r[3]:<25}" #salud
        salida += f"{r[4]:<25}" #afp
        salida += f"{r[5]:<25}" #liquido
    return salida
    
def imprimir():
    trabajador = input(f"trabajadores {trabajadores}: ").strip().upper()
    if trabajador in trabajadores:
        with open(trabajador+".txt", "w") as archivo:
            archivo.write(listar())
    else:
        input("exepcion de impresion")

while True:
    try:
        opc = input(menu)
        if opc == "4":
            break
        if opc == "1":
            registrar()
        elif opc == "2":
            print(listar())
        elif opc == "3":
            imprimir()
    except Exception as e:
        input(f"exepcion de menu: {str(e)}")
        