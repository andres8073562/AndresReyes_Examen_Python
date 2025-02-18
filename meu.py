import json

def abrirJSON():
    dicFinal = {}
    try:
        with open("./Clientes.json", 'r') as openFile:
            dicFinal = json.load(openFile)
    except FileNotFoundError:
        dicFinal = {"Clientes": []}  # If the file does not exist, create an empty "Clientes" list.
    return dicFinal

def abrirPlanes():
    dicFinal = {}
    try:
        with open("./Servicios.json", 'r') as openFile:
            dicFinal = json.load(openFile)
    except FileNotFoundError:
        dicFinal = {"Tipo de servicio": []}  # Create an empty "Tipo de servicio" list if the file doesn't exist.
    return dicFinal

def guardarJSON(dic):
    with open("./Clientes.json", 'w') as outFile:
        json.dump(dic, outFile, indent=4)  # Pretty print the JSON with indentation.

print("----Menu----")
print("Bienvenido a movistar")
print("Que deseas hacer")
print("1. Registrar nuevo usuario")
print("2. Ver planes")
print("3. Comprar planes")
print("4. Hacer un reporte")
opt = int(input(":"))

if opt == 1:
    # Register new user
    clientes = abrirJSON()
    id = int(input("Ingrese su id: "))
    Nombre = input("Ingrese su nombre: ")
    Apellidos = input("Ingrese su apellido: ")
    Direccion = input("Ingrese su dirección: ")

    # Append the new client to the "Clientes" list.
    clientes["Clientes"].append({
        "id": id,
        "Nombre": Nombre,
        "Apellido": Apellidos,
        "Direccion": Direccion
    })
    
    guardarJSON(clientes)
    print("Usuario guardado correctamente")

elif opt == 2:
    planes={}
    planes = abrirPlanes()
    for servicio in planes["Tipo de servicio"]:
        print("----Planes----")
        print(f"Plan: {servicio['Plan']}, Precio: {servicio['Precio']}")

elif opt == 3:
    
    id = int(input("Digite su id: "))
    
    clientes = abrirJSON()
    
    for cliente in clientes["Clientes"]:
       
        if cliente["id"] == id:
           
            print(f"El usuario con ID {id} ha sido encontrado.")
        
        
    else:    
        print("Perdón, el usuario no se ha encontrado. Por favor intente de nuevo.")

elif opt == 4:
    # Report an issue
    clientes = abrirJSON()
    id = int(input("Digite su id: "))
   

    for cliente in clientes["Clientes"]:
        if cliente["id"] == id:
            print(f"El usuario con ID {id} ha sido encontrado.")
            reporte = input("Cual es la causa del reporte? ")
            cliente["Reportes"] = cliente.get("Reportes", [])  
            cliente["Reportes"].append(reporte)
            guardarJSON(clientes)
            print("El reporte ha sido registrado correctamente. Perdón por las molestias.")
        
    