import random

"""Задание 1
Два списка целых заполняются случайными числами. 
Необходимо:
■ Сформировать третий список, содержащий элементы обоих списков;
■ Сформировать третий список, содержащий элементы обоих списков без повторений;
■ Сформировать третий список, содержащий элементы общие для двух списков;
■ Сформировать третий список, содержащий только уникальные элементы каждого из списков;
■ Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков"""

""""""


def elements_of_both_lists(list_1, list_2) -> list:
    # Сформировать третий список, содержащий элементы обоих списков;
    return list_1 + list_2


def elements_of_both_lists_without_repetition(list_1, list_2) -> list:
    # Сформировать третий список, содержащий элементы обоих списков без повторений;
    temp_array = list_1 + list_2
    array = []
    for number in temp_array:
        if number not in array:
            array.append(number)
    return array


def elements_are_common_to_the_two_lists(list_1, list_2) -> list:
    # Сформировать третий список, содержащий элементы общие для двух списков;
    array = []
    for number in list_1:
        if number in list_2:
            array.append(number)
    return array


def elements_common_to_the_two_lists(list_1, list_2):
    # Сформировать третий список, содержащий только уникальные элементы каждого из списков
    return list(set(list_1) ^ (set(list_2)))


def min_max_list(list_1, list_2):
    # Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков
    temp_array = list_1 + list_2

    max_number = temp_array[0]
    for i in temp_array:
        if i > max_number:
            max_number = i

    min_number = temp_array[0]
    for j in temp_array:
        if j < min_number:
            min_number = j

    return min_number, max_number


if __name__ == '__main__':
    array_size = 10
    random_array_1 = [random.randint(1, 100) for _ in range(array_size)]
    print(f"Первый массив случайных чисел: {random_array_1}")

    random_array_2 = [random.randint(1, 100) for _ in range(array_size)]
    print(f"Второй массив случайных чисел: {random_array_2}")

    print(f"Массив чисел, содержащий элементы обоих списков: "
          f"{elements_of_both_lists(random_array_1, random_array_2)}")

    print(f"Массив чисел, содержащий элементы обоих списков без повторений: "
          f"{elements_of_both_lists_without_repetition(random_array_1, random_array_2)}")

    print(f"Массив чисел, содержащий элементы общие для двух списков: "
          f"{elements_common_to_the_two_lists(random_array_1, random_array_2)}")

    print(f"Массив чисел, содержащий только уникальные элементы каждого из списков: "
          f"{elements_are_common_to_the_two_lists(random_array_1, random_array_2)}")

    answer = min_max_list(random_array_1, random_array_2)
    print(f'Максимальное число в списках: {answer[1]}, минимальное число в списках {answer[0]}')
