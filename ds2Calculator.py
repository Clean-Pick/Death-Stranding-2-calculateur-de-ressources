import math

wares = {
    "ceramique" : {
        40 : 0,
        80 : 0,
        160 : 0,
        320 : 0,
    },
    "resine": {
        40: 0,
        80: 0,
        160: 0,
        320: 0,
    },
    "metal" : {
        50 : 0,
        100 : 0,
        200 : 0,
        400 : 0,
    },
    "alliage" : {
        60 : 0,
        120 : 0,
        240 : 0,
        480 : 0,
    },
    "produit" : {
        30 : 0,
        60 : 0,
        120 : 0,
        240 : 0,
    }
}

current_structure = 1

def calculator():

    print("Combien de structures voulez-vous réparer/construire ?")
    structure_num_answer = input("> ")
    structure_num_answer = int(structure_num_answer)

    if structure_num_answer == 0:
        print("Arrêt du programme.")
        quit()
    elif structure_num_answer >= 1:
        ware_type_validation(structure_num_answer)
    else:
        print("Veuillez entrer un nombre/chiffre (1,2,3...).")
        calculator()


def ware_type_validation(structure_num):
    global  current_structure

    if structure_num == 0:
        show_results()
        return



    print(f"De quoi avez-vous besoin pour la structure {current_structure} ?")
    print("    C = Céramiques")
    print("    M = Métaux")
    print("    R = Résines")
    print("    A = Alliages Spéciaux")
    print("    P = Produits Chimiques")
    print("    Q = Je n'ai plus besoin de rien pour cette structure")
    print("N'entrez qu'une lettre avant de valider.")
    ware_type = input("> ")


    match ware_type:
        case "c" | "C":
            ware_number_validation("ceramique")
        case "m" | "M":
            ware_number_validation("metal")
        case "r" | "R":
            ware_number_validation("resine")
        case "a" | "A":
            ware_number_validation("alliage")
        case "p" | "P":
            ware_number_validation("produit")
        case "q" | "Q":
            current_structure += 1
            ware_type_validation(structure_num - 1)
            return
        case _ :
            print("Veuillez entrer une seule lettre parmis celles énoncées.")

    ware_type_validation(structure_num)

def ware_number_validation(ware_type):
    match ware_type:
        case "ceramique":
            print(f"Combien de céramique totale avez-vous besoin pour la structure {current_structure} ?")
            ware_type_answer = input("> ")
            ware_type_answer = int(ware_type_answer)
            ware_type_calculator(ware_type, ware_type_answer)
        case "metal":
            print(f"Combien de métal total avez-vous besoin pour la structure {current_structure} ?")
            ware_type_answer = input("> ")
            ware_type_answer = int(ware_type_answer)
            ware_type_calculator(ware_type, ware_type_answer)
        case "resine":
            print(f"Combien de résine totale avez-vous besoin pour la structure {current_structure} ?")
            ware_type_answer = input("> ")
            ware_type_answer = int(ware_type_answer)
            ware_type_calculator(ware_type, ware_type_answer)
        case "alliage":
            print(f"Combien d'alliages spéciaux avez-vous besoin pour la structure {current_structure} ?")
            ware_type_answer = input("> ")
            ware_type_answer = int(ware_type_answer)
            ware_type_calculator(ware_type, ware_type_answer)
        case "produit":
            print(f"Combien de produits chimiques totaux avez-vous besoin pour la structure {current_structure} ?")
            ware_type_answer = input("> ")
            ware_type_answer = int(ware_type_answer)
            ware_type_calculator(ware_type, ware_type_answer)



# Calcul :
# X = valeur totale recherchée
# Y = plus gros tas de ressource possible ne dépassant pas X | R.
# Z = résultat de la division (rapport/quotient)
# ZZ = Z arrondi à l'entier du dessous
# W = nombre de stacks à ajouter à la value de la ressource sélectionnée (la key étant Y)
# X1 = nombre de ressources réelles récupérées
#
# Ces définitions ne sont là que pour rendre la logique plus claire à un humain
#
# R = X
# début de boucle :
#   définir Y (Y étant le plus gros stack plus petit que R disponible) via : max(key for key in wares[ware_type] if key < R)
#   Z = R / Y (On calcule combien de stacks de Y on doit retirer)
#   arrondir Z à l'intégrale en dessous (Z devient ZZ, ZZ étant le nombre de stacks à enlever sans dépasser la valeur recherchée)
#   X1 = Y * ZZ (On calcule combien de ressources on a effectivement retiré)
#   (W = ZZ) alors -> wares[ware_type][Y] += W | ZZ
#   R = R - X1 (On définit combien de ressources sont encore à récupérer)
#   if R > min(wares[ware_type]):
#       ware_type_calculator(ware_type, R) (On reboucle tant que R est plus grand que le plus petit stack dispo)
#   else:
#       min_key = min(wares[ware_type]) (sinon, on cherche le plus petit stack de la ware)
#       wares[ware_type][min_key] += 1  (et on y rajoute 1 stack pour compléter et avoir X ou le minimum à avoir pour atteindre X)
#   fin de boucle


def ware_type_calculator(ware_type, wanted_total_value):

    remaining = wanted_total_value
    biggest_stack_below_remaining = max(key for key in wares[ware_type] if key < remaining)
    stacks_to_get = remaining / biggest_stack_below_remaining
    stacks_to_get = math.floor(stacks_to_get)
    num_of_wares_substracted = biggest_stack_below_remaining * stacks_to_get
    wares[ware_type][biggest_stack_below_remaining] += stacks_to_get
    remaining -= num_of_wares_substracted
    if remaining > min(wares[ware_type]):
        ware_type_calculator(ware_type, remaining)
    else:
        if remaining > 0:
            min_stack = min(wares[ware_type])
            wares[ware_type][min_stack] += 1


def show_results():
    print("Vous aurez besoin au total :")
    for material, stack in wares.items():
        for key, value in stack.items():
            if value > 0:
                print(f"[{material}] - [{key}] = {value}")
    print("Appuyez sur Entrée pour fermer le programme.")
    input("> ")

calculator()

