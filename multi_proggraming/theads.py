import threading
import time


def process_data(data):
    print(f"Processing data: {data}")
    time.sleep(2)
    print(f"Finish {data}")


def main():
    print("====Start======")
    start_time = time.time()
    data = ['Data1', 'Data2', 'Data3']
    threads = []

    for item in data:
        # создаем поток - передаем ему функцию и параметры функции
        thread = threading.Thread(target=process_data, args=(item,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    print(f"Все задачи выполнены {end_time - start_time}")


if __name__ == '__main__':
    main()
