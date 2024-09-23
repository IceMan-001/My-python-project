import random


class Tasklist:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def elements_of_both_lists(self):
        # Сформировать третий список, содержащий элементы обоих списков;
        print(f"Массив чисел, содержащий элементы обоих списков: {sorted(self.value1 + self.value2)}")

    def elements_of_both_lists_without_repetition(self):
        # Сформировать третий список, содержащий элементы обоих списков без повторений;
        temp_array = self.value1 + self.value2
        array = []
        for number in temp_array:
            if number not in array:
                array.append(number)
        print(f"Массив чисел, содержащий элементы обоих списков без повторений: {sorted(array)}")

    def elements_are_common_to_the_two_lists(self):
        # Сформировать третий список, содержащий элементы общие для двух списков;
        array = []
        for number in self.value1:
            if number in self.value2:
                array.append(number)
        print(f"Массив чисел, содержащий элементы общие для двух списков: {sorted(array)}")

    def elements_common_to_the_two_lists(self):
        # Сформировать третий список, содержащий только уникальные элементы каждого из списков
        print(f"Массив чисел, содержащий только уникальные элементы каждого из списков: "
              f"{sorted(list(set(self.value1) ^ set(self.value2)))}")

    def min_max_list(self):
        # Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков
        temp_array = self.value1 + self.value2

        max_number = temp_array[0]
        for i in temp_array:
            if i > max_number:
                max_number = i

        min_number = temp_array[0]
        for j in temp_array:
            if j < min_number:
                min_number = j

        print(f'Максимальное число в списках: {max_number}, минимальное число в списках {min_number}')


if __name__ == '__main__':
    array_size = 10
    random_array_1 = [random.randint(1, 100) for _ in range(array_size)]
    print(f"Первый массив случайных чисел: {random_array_1}")

    random_array_2 = [random.randint(1, 100) for _ in range(array_size)]
    print(f"Второй массив случайных чисел: {random_array_2}")

    answer = Tasklist(random_array_1, random_array_2)
    answer.elements_of_both_lists()
    answer.elements_of_both_lists_without_repetition()
    answer.elements_are_common_to_the_two_lists()
    answer.elements_common_to_the_two_lists()
    answer.min_max_list()
