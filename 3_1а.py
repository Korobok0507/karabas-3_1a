# Глобальная переменная
function_calls = 0

# Функция определения длины строки, перевода в верхний и нижний регистр
def string_info(string):
    global function_calls
    function_calls += 1
    return (len(string), string.upper(), string.lower())

# Функция поиска строки в списке
def is_contains(string, list_to_search):
    global function_calls
    function_calls += 1
    string_lower = string.lower()
    return any(item.lower() == string_lower for item in list_to_search)

# Функция - стартовый блок
def start():
    global function_calls
    # Запрос у пользователя ключевого слово и списка слов
    keyword = input("Введите ключевое слово: ").strip()
    list_input = input("Введите список слов через пробел: ").strip()

    # Преобразование списка в Python-список
    list_to_search = list_input.split()

    # Получение информации о ключевом слове
    length, upper, lower = string_info(keyword)

    # Поиск ключевого слова в списке
    found = is_contains(keyword, list_to_search)

    # Вывод результатов
    print(f"Длина слова: {length}")
    print(f"Слово в верхнем регистре: {upper}")
    print(f"Слово в нижнем регистре: {lower}")
    print(f"Найдено ли слово в списке: {found}")
    print(f"Количество вызовов функций: {function_calls}")

# Начало выполнения стартового блока
if __name__ == "__main__":
    start()
