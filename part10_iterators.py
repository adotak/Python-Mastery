# Ahmad, Roll No: __________, 2026-11-11
"""Generators and decorators."""
from functools import wraps
from time import perf_counter
from typing import Any, Callable, Iterator


def countdown(number: int) -> Iterator[int]:
    while number > 0:
        yield number
        number -= 1


def evens(limit: int) -> Iterator[int]:
    yield from range(0, limit + 1, 2)


def read_lines(path: str) -> Iterator[str]:
    with open(path, encoding="utf-8") as file:
        yield from file


def only_errors(lines: Iterator[str]) -> Iterator[str]:
    for line in lines:
        if "ERROR" in line:
            yield line


def timer(function: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        started = perf_counter()
        result = function(*args, **kwargs)
        print(f"{function.__name__} took {perf_counter() - started:.6f}s")
        return result
    return wrapper


def log_calls(function: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"{function.__name__}{args}{kwargs}")
        return function(*args, **kwargs)
    return wrapper


@timer
@log_calls
def sum_to(number: int) -> int:
    return sum(range(1, number + 1))


if __name__ == "__main__":
    print(list(countdown(5)), list(evens(10)), sum_to(1_000_000))
