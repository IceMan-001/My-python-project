import time

"""Функция для эмуляции длительности работы"""


def process_data(data):
    print(f"Processing data: {data}")
    time.sleep(2)
    print(f"Finish {data}")


def main():
    print("====Start======")
    start_time = time.time()
    process_data("Data1")
    process_data("Data2")
    process_data("Data2")

    end_time = time.time()

    print(f"Все задачи выполнены {end_time - start_time}")


if __name__ == '__main__':
    main()
