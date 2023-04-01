# программа конвертера температуры

def celsius_to_fahrenheit(celsius):
    """Преобразование температуры из градусов Цельсия в градусы Фаренгейта"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Преобразование температуры из градусов Фаренгейта в градусы Цельсия"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# запрос ввода температуры и единицы измерения
temp = float(input("Введите температуру: "))
unit = input("Введите единицу измерения (C или F): ")

# проверка выбранной единицы измерения и вызов соответствующей функции преобразования
if unit == 'C':
    converted_temp = celsius_to_fahrenheit(temp)
    print(f"{temp} градусов Цельсия = {converted_temp} градусов Фаренгейта")
elif unit == 'F':
    converted_temp = fahrenheit_to_celsius(temp)
    print(f"{temp} градусов Фаренгейта = {converted_temp} градусов Цельсия")
else:
    print("Некорректная единица измерения")
