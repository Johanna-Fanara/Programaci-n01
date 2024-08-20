#clase 3
#listas avanzadas

lst = [1, 2, 3]
lst.append(4)
print(f"append(): {lst}")


lista=[1,2]
lista.extend([3, 4])
print(f"extend():{lista}")


lista1= [1, 2, 3]
lista1.inser(1, 1.5) # (posicion, valor)
print(f"insert():{lista1}")


lista2=[1, 2, 2, 3]
lista2.remove(2) #borra el primer resultado que encuentra con ese valor
print(f"remove(): {lista2}") # [1, 2, 3]


lista3=[1, 2, 3]
popped_element= lista3.pop()
print(f"pop(): (Elemento: {popped_element}, lista:{lista3})")


lista4=[1, 2, 3]
index_element = lista4.index(2)
print(f"index(): {index_element}") #Te devuelve la posicion del primer valor que ecuentra 

count_element = lst.count(2) #cuenta cuatos elementos hay

lst.sort() #ordena con algun metodo de ordenamiento de menor a mayor

lst.reverse() #invierte la lista

#Slicing
lista5=[1,2,3,4]
print(f"lista5[1:3]: {lista5[1:3]}") # [2, 3] posicion 1 incluida, posicion 3 no icluida, por eso retorna 2(1) y 3(2)

#Concatenacion de listas
lst1=[1, 2]
lst2= [3, 4]
print(f"lst1 + lst2: {lst1+lst2}") #[1, 2, 3, 4]


#Copia de lista
lst3=[1, 2]
lst3_copy = lst3.copy()
print(f"lst3.copy():{lst3_copy}")


lst3_copy_slicing = lst3[:] #Asi se copia una lista tambien


#Desempaquetamiento
a, b, c = [1, 2, 3]
print(f"desempaquetado: a = {a}, b = {b}, c = {c}")


#Funciones comunes

sum() #suma

min() #minimo

max() #maximo

list() #devuelve lista