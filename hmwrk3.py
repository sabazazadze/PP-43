# import asyncio
# import time
#
#
# async def load_user(user_id):
#     await asyncio.sleep(1)
#     return {"id": user_id, "name": f"მომხმარებელი {user_id}"}
#     # შეცდომა: time.sleep ბლოკავდა event loop-ს; საჭიროა await asyncio.sleep
#
# async def main():
#     start = time.perf_counter()
#     users = await asyncio.gather(*(load_user(user_id) for user_id in (1, 2, 3)))
#     elapsed = time.perf_counter() - start
#     print(users)
#     print(f"დრო: {elapsed:.1f} წმ")
#     # შეცდომა: load_user(...) მხოლოდ კორუტინის ობიექტს ქმნიდა და არ სრულდებოდა gather
#
# asyncio.run(main()) # შეცდომა: main() პირდაპირ გამოძახება კორუტინას არ ასრულებს საჭიროა asyncio.run



# ===== მოცემული კოდი: სავარჯიშო 3 (კოდი შეცდომებით) =====
# import asyncio
# import time
#
#
# async def load_user(user_id):
#     time.sleep(1)  # მომხმარებლის ჩატვირთვას ვასახიერებთ
#     return {"id": user_id, "name": f"მომხმარებელი {user_id}"}
#
#
# async def main():
#     users = []
#     for user_id in (1, 2, 3):
#         user = load_user(user_id)
#         users.append(user)
#     print(users)
#
#
# main()