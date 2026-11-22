# სავარჯიშო 1: მოცემული კოდი (არ შეცვალოთ)
def get_grade(score):
    """ქულას (0-100) გადაიყვანს შეფასებად."""
    if score < 0 or score > 100:
        raise ValueError("ქულა უნდა იყოს 0-დან 100-მდე")
    if score >= 91:
        return "A"
    if score >= 81:
        return "B"
    if score >= 71:
        return "C"
    if score >= 61:
        return "D"
    if score >= 51:
        return "E"
    return "F"