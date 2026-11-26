from datetime import date


def clean_text(raw, field_name, min_len=1, max_len=100):
    if not isinstance(raw, str):
        raise ValueError(f"{field_name}: უნდა იყოს ტექსტი.")

    text = " ".join(raw.strip().split())

    if not text:
        raise ValueError(f"{field_name} ვერ იქნება ცარიელი.")
    if len(text) < min_len:
        raise ValueError(f"{field_name} ძალიან მოკლეა (მინ. {min_len} სიმბოლო).")
    if len(text) > max_len:
        raise ValueError(f"{field_name} ძალიან გრძელია (მაქს. {max_len} სიმბოლო).")
    if not any(ch.isalnum() for ch in text):
        raise ValueError(f"{field_name} უნდა შეიცავდეს მინიმუმ ერთ ასოს ან ციფრს.")

    return text


def clean_year(raw):
    text = str(raw).strip()

    if not text:
        raise ValueError("წელი ვერ იქნება ცარიელი.")
    if not text.isdigit():
        raise ValueError("წელი უნდა შეიცავდეს მხოლოდ ციფრებს (მაგ. 1998).")

    year = int(text)
    current = date.today().year
    if not (1000 <= year <= current):
        raise ValueError(f"წელი უნდა იყოს 1000-სა და {current}-ს შორის.")

    return year


def normalize(text):
    return " ".join(text.strip().split()).casefold()
