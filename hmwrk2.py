import asyncio
import time

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

async def square(number):
    await asyncio.sleep(1)
    return number * number

async def main():
    start = time.perf_counter()
    squares = await asyncio.gather(*(square(n) for n in numbers))
    elapsed= time.perf_counter() - start
    for i in range(len(numbers)):
        print(f"{numbers[i]}: {squares[i]}")
    print(f"ჯამი: {sum(squares)}")
    print(f"დრო: {elapsed:.1f}")

asyncio.run(main())
# 4. დრო დაახლოებით 1 წამია და არა 8 რადგან ყველა 1 წამიანი ლოდინი ერთდროულად მიმდინარეობს (gather მათ event loop ში ერთად უშვებს) ამიტომ ისინი არ იკრიბება და საერთო დრო ერთი ლოდინის ტოლია