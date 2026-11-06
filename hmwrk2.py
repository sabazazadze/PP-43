import json
from dataclasses import dataclass, field, asdict


@dataclass
class Movie:
    title: str
    year: int = 2000
    rating: float = 0.0
    genres: list = field(default_factory=list)

    def __post_init__(self):
        if not 0 <= self.rating <= 10:
            raise ValueError("რეიტინგი უნდა იყოს 0-დან 10-მდე")


def best_movies(movies, min_rating):
    good = [m for m in movies if m.rating >= min_rating]
    return sorted(good, key=lambda m: m.rating, reverse=True)

m1 = Movie("მონანიება", 1984, 9.1, ["დრამა"])
m2 = Movie("გზა", 2020, 7.5)
m3 = Movie("მოგზაურობა", rating=8.2, genres=["თავგადასავალი"])

print(m1)
print(m1 == Movie("მონანიება", 1984, 9.1, ["დრამა"]))


m2.genres.append("კომედია")
print(m2.genres, m3.genres)


for m in best_movies([m1, m2, m3], 8):
    print(m.title, m.rating)


print(json.dumps(asdict(m1), ensure_ascii=False))


try:
    Movie("ცუდი", 2000, 11)
except ValueError as a:
    print("შეცდომა:", a)