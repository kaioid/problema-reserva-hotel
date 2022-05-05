from src.hotel import Hotel


def get_cheapest_hotel(lista):   #DO NOT change the function's name
    # iniciando tratamento da entrada
    global entrada
    entrada = []
    corte1 = lista.split(':')
    tipo_cliente = corte1[0]
    entrada.append(tipo_cliente)
    aux = corte1[1]

    corte2 = aux.split('(')
    for par in corte2:
        if ')' in par:
            entrada.append(par.split(')')[0])   # separando dados da entrada em uma lista

    aux = total_value()     # variável auxiliar para armazenar lista com os valores de reserva em cada hotel
    rating_list = [hotel1.rating, hotel2.rating, hotel3.rating]     # lista com classificação de cada hotel
    hotel_list = [hotel1, hotel2, hotel3]   # lista com endereços de memória de cada hotel

    minimo = min(aux)   # guardando o valor mínimo em uma variável
    count = 0   # contador para guardar índice dos menores valores em caso de repetição
    indice = []     # lista para armazenar índices de menor valor (só terá mais de um item se houver repetições
    for mini in aux:
        if mini == minimo:
            indice.append(count)
            count += 1
        else:
            count += 1
    lista = []
    for i in indice:
        lista.append(rating_list[i])
    melhor = max(lista)     # definindo maior classificação

    for cheapest_hotel in hotel_list:
        if cheapest_hotel.rating == melhor:
            return cheapest_hotel.name  # retornando o hotel mais barato e o de maior classificação em caso de empate 


def type_day():
    count = 0
    for day in entrada:
        if day == "sat" or day == "sun":
            count = count + 1
    cart = [(len(entrada)-count-1), count]
    return cart     # retornando lista com quantidade de weekdays e weekends, respectivamente


def value_list():
    global hotel1, hotel2, hotel3
    if entrada[0] == "Rewards":
        hotel1 = Hotel("Lakewood", 3, {"Weekday": 80, "Weekend": 80})
    elif entrada[0] == "Regular":
        hotel1 = Hotel("Lakewood", 3, {"Weekday": 110, "Weekend": 90})

    if entrada[0] == "Rewards":
        hotel2 = Hotel("Bridgewood", 4, {"Weekday": 110, "Weekend": 50})
    elif entrada[0] == "Regular":
        hotel2 = Hotel("Bridgewood", 4, {"Weekday": 160, "Weekend": 60})

    if entrada[0] == "Rewards":
        hotel3 = Hotel("Ridgewood", 5, {"Weekday": 100, "Weekend": 40})
    elif entrada[0] == "Regular":
        hotel3 = Hotel("Ridgewood", 5, {"Weekday": 220, "Weekend": 150})
    # Instanciando hoteis de acordo com o tipo de cliente (Regular ou Rewards)
    return [hotel1.price_card, hotel2.price_card, hotel3.price_card]    # retornando lista com listas contendo os preços para weekdays e weekends


def total_value():
    lista_wday = []
    lista_wend = []
    soma = []
    for item in value_list():
        lista_wday.append(type_day()[0]*item[0])
    for item in value_list():
        lista_wend.append(type_day()[1]*item[1])

    for x in range(len(lista_wday)):
        soma.append(lista_wday[x]+lista_wend[x])

    return soma  # retornando lista com valor total com base nos dias da reserva




