raw_username = "  Super_Coder_2026  "
username = raw_username.strip().lower().replace("_", "-")
print("მომხმარებლის სახელი:", username)
print("სიგრძე: " f"{len(username)}")
print("იწყება 'super'-ით:", username.startswith("super"))
print("ტირეების რაოდენობა:",username.count("-"))
username1 = username.replace("-", "")
print("მხოლოდ ასოები და ციფრები:", "-" not in username1)
