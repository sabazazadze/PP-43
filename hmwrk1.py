import asyncio
import time

orders = [("შეკვეთა #1", 1.0), ("შეკვეთა #2", 1.5), ("შეკვეთა #3", 2.0)]


async def deliver(order, seconds):
    print(f"{order}: გაიგზავნა")
    await asyncio.sleep(seconds)
    print(f"{order}: მიტანილია")


async def main():
    start = time.perf_counter()
    for order, seconds in orders:
        await deliver(order, seconds)
    sequential = time.perf_counter() - start
    print(f"ზედიზედ: {sequential:.1f} წმ")

    start = time.perf_counter()
    await asyncio.gather(*(deliver(o, s) for o, s in orders))
    concurrent = time.perf_counter() - start
    print(f"ერთდროულად: {concurrent:.1f} წმ")

    print(f"დაჩქარება: {sequential / concurrent:.1f}x")

asyncio.run(main())


#სამივე ლოდინი ერთდროულად მიმდინარეობს და gather მთავრდება მაშინ როცა ყველაზე ნელი (2 წმ) დასრულდება