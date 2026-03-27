from __future__ import annotations


def average_ratios(numbers: list[float]) -> float:
    """Return the average of 100 divided by each number in the list.

    Raises:
        ValueError: If the input list is empty or contains zero.
    """
    if not numbers:
        raise ValueError("numbers must contain at least one element")

    total = 0.0
    for index, value in enumerate(numbers):
        if value == 0:
            raise ValueError(f"division by zero at index {index}")
        total += 100.0 / value

    return total / len(numbers)


if __name__ == "__main__":
    try:
        print(average_ratios([10, 5, 0]))
    except ValueError as error:
        print(f"Unable to compute average ratios: {error}")
