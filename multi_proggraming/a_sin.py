import asyncio
import time


async def process_data(data):
    print(f"Processing data: {data}")
    await asyncio.sleep(2)
    print(f"Finish {data}")


async def main():
    print("====Start======")
    start_time = time.time()
    tasks = [
        process_data("Data1"),
        process_data("Data2"),
        process_data("Data3")
    ]
    await asyncio.gather(*tasks)
    end_time = time.time()

    print(f"Все задачи выполнены {end_time - start_time}")

if __name__ == '__main__':
    asyncio.run(main())