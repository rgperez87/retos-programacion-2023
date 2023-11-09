import random

def set_initial_weather_conditions():
    init_temp = int(input("Introduce la temperatura inicial: "))
    init_rain = int(input("Introduce el porcentaje de lluvia: "))
    return init_temp, init_rain

def simulate_conditions(temp: int, rain: int):

    rand = random.randint(1,100)
    masomenos = random.randint(0,1)

    if rand <= 10:
        if masomenos == 1:
            temp += 2
        else: temp -= 2
    if temp > 25:
        rain = min(100, rain+20)
    if temp < 5:
        rain = max(0, rain-20)
    if rain == 100:
        temp -= 1

    return temp, rain

def weather_simulation(simDays: int):
    init_temp, init_rain = set_initial_weather_conditions()
    today_temp = init_temp
    today_rain = init_rain
    max_temp = -25
    min_temp = 40
    total_raindays = 0
    
    for day in range(simDays):
        today_temp, today_rain = simulate_conditions(today_temp, today_rain)
        print("### Día " + str(day+1))
        print("Hoy tenemos una temperatura de " + str(today_temp) + "º y una probabilidad de lluvia del " + str(today_rain) + "%")

        max_temp = max(max_temp, today_temp)
        min_temp = min(min_temp, today_temp)
        if today_rain == 100: total_raindays += 1

    print("### Resumen del periodo")
    print("Durante estos " + str(simDays) + " días, la temperatura mínima ha sido de " + str(min_temp) + "º y la temperatura máxima ha sido de " + str(max_temp) + "º.")
    print("Además, ha llovido un total de " + str(total_raindays) + " días.")

    return

init_simDays = int(input("Introduce el número de días a simular:"))
weather_simulation(init_simDays)