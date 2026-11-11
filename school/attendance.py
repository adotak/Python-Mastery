"""Small attendance helper module."""


def attendance_rate(present: int, total: int) -> float:
    if total <= 0 or present < 0 or present > total:
        raise ValueError("Invalid attendance values")
    return present / total * 100
