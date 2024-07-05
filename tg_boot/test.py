weather = {'day_of_week': 'Пятница',
           'day_of_month': '05 июля',
           'Ночь': {'temperature': '+18°',
                    'atmosfera': 'Преимущественно облачно',
                    'weather_feeling': '+18°',
                    'probability': '13%',
                    'pressure': '768',
                    'wind': {'wind_direction': 'западный',
                             'wind_ms': '0.9', 'wind_kch':
                                 ' 3.2 км/ч'}, 'humidity': '90%'},
           'Утро': {'temperature': '+20°',
                    'atmosfera': 'Пасмурно',
                    'weather_feeling': '+20°',
                    'probability': '24%',
                    'pressure': '769',
                    'wind': {'wind_direction': 'западный',
                             'wind_ms': '1.4', 'wind_kch':
                                 ' 5 км/ч'},
                    'humidity': '70%'},
           'День': {'temperature': '+25°',
                    'atmosfera': 'Преимущественно облачно',
                    'weather_feeling': '+25°',
                    'probability': '30%',
                    'pressure': '768',
                    'wind': {'wind_direction': 'западный',
                             'wind_ms': '2.2',
                             'wind_kch': ' 7.9 км/ч'},
                    'humidity': '40%'},
           'Вечер': {'temperature': '+21°',
                     'atmosfera': 'Преимущественно облачно',
                     'weather_feeling': '+21°',
                     'probability': '27%',
                     'pressure': '767',
                     'wind': {'wind_direction': 'северо-восточный',
                              'wind_ms': '2.1', 'wind_kch': ' 7.6 км/ч'},
                     'humidity': '69%'}}

text = f"""
    Погода на {weather['day_of_month']}
    Ночью:
    Температура: {weather['Ночь']['temperature']}
    {weather['Ночь']['atmosfera']}
    Ощущается: {weather['Ночь']['weather_feeling']}
    Влажность: {weather['Ночь']['probability']}
    Давление: {weather['Ночь']['pressure']}
    Ветер: {weather['Ночь']['wind']['wind_direction']}, {weather['Ночь']['wind']['wind_kch']}
    """

if __name__ == "__main__":
    header = (f"{weather['day_of_week']} "
              f"{weather['day_of_month']}")
    result = []
    times_of_day = [x for x in weather if x != 'day_of_week' and x != 'day_of_month']
    for time_of_day in times_of_day:
        for value in weather:
            sample = (f"{weather['day_of_week']}, {weather['day_of_month']}\n "
                      f"{time_of_day}\n"
                      f"Tемпература °C {weather[time_of_day]['temperature']} "
                      f"Атмосферные явления {weather[time_of_day]['atmosfera']} "
                      f"Ощущается как °C{weather[time_of_day]['weather_feeling']} "
                      f"Вероятность осадков %{weather[time_of_day]['probability']} "
                      f"Давление мм рт. ст.{weather[time_of_day]['pressure']} "
                      f"Скорость ветра м/с {weather[time_of_day]['wind']['wind_ms']} "
                      f"{weather[time_of_day]['wind']['wind_kch']} "
                      f"{weather[time_of_day]['wind']['wind_direction']} "
                      f"Влажность воздуха {weather[time_of_day]['humidity']}")
        result.append(sample)
    print(result)
