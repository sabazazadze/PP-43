import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def crud_tour():
    new_post = {"title": "ახალი პოსტი", "body": "ტექსტი", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    response.raise_for_status()

    new_id = response.json()["id"]
    print(f"CREATE: {response.status_code}, id={new_id}")

    response = requests.get(f"{BASE_URL}/posts/{new_id}")
    print(f"READ:{new_id}, {response.status_code}")

    full_post = {
        "id": 1,
        "title": "სრულად შეცვლილი",
        "body": "ახალი ტექსტი",
        "userId": 1,
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=full_post)
    print(f"UPDATE(PUT): {response.status_code}, title={response.json()['title']}")

    patch_data = {"title": "ნაწილობრივ შეცვლილი"}
    response = requests.patch(f"{BASE_URL}/posts/{new_id}", json=patch_data)
    print(f"UPDATE(PATCH): {response.status_code}, title={response.json()['title']}")

    response = requests.delete(f"{BASE_URL}/posts/1")
    # response.raise_for_status()
    print(f"DELETE: {response.status_code}, {response.json()}")





crud_tour()