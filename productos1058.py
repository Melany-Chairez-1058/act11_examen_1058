#Zona de clases
class productos1058:
    #zona de atributos
    id_pro=0
    precio=0
    stock=0
    descripcion=" "
    nom_flores=""
    categoria=""
    nombre_pro=""
    #zona de  funciones
    def mostrar_datos(self):
        print(f"DATOS DEL PRODUCTO \nID:{prod.id_pro} \nPrecio:{prod.precio} \nStock:{prod.stock} \nDescripcion:{prod.descripcion}\nFlores:{prod.nom_flores} \nCategoria:{prod.categoria} \nNombre:{prod.nombre_pro}")
        
    def lista_prod(self):
        list_prod=["Jazmin","Rosas","Girasol","Orquidea","clavel"]
        print(" \n LISTA DE PRODUCTOS")
        for x in list_prod:
            print(x)
    def tupla_prod(self):
        list_prod=["Flor individual","Ramo pequeño","Ramo grande","Ramo y chocolates","Ramo con mensaje"]
        print("\n TUPLA DE PRODUCTOS")
        for x in list_prod:
            print(x)   
    def dicc_prod(self):
        dicc_prod={"Jazmin":"15 pesos","Ramo grande":"560 pesos","Girasol":"60 pesos","Ramo con mensaje":"600 pesos","clavel":"25 pesos"}
        print(" \n DICCIONARIO DE PRODUCTOS")
        for x,y in dicc_prod.items():
            print(x,y) 
    def alta(self):
        print(" \n El nuevo producto se ha dado de alta correctamente")   
    def baja(self):
        print(" \n El producto se ha dado de baja correctamente")
#zona de objetos       
prod= productos1058()
prod.id_pro=166
prod.precio=580
prod.stock=32
prod.descripcion="Ramo grande con 60 unidades de flores"
prod.nom_flores="Girasoles, tulipanes y rosas"
prod.categoria="Ramo grande"
prod.nombre_pro="Amor Infnito"
#llamado de funciones
prod.mostrar_datos()
prod.lista_prod() 
prod.tupla_prod()  
prod.dicc_prod()    
prod.alta()
prod.baja()
    