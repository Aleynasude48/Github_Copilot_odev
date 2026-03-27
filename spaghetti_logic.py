from __future__ import annotations

LOG_FILE: str = "log.txt"
VAT_RATE: float = 0.15


def calculate_totals(values: list[float]) -> list[float]:
    """Apply VAT to each value and return the computed totals."""
    return [value * (1 + VAT_RATE) for value in values]


def format_total(value: float) -> str:
    """Format a total value for display."""
    return f"Total: {value:.2f}"


def append_to_log_file(totals: list[float], path: str = LOG_FILE) -> None:
    """Write the list of totals into the log file."""
    with open(path, "a", encoding="utf-8") as output_file:
        output_file.write(f"{totals}\n")


def process_data(data: list[float]) -> list[float]:
    """Compute totals, print formatted results, log them, and return the totals."""
    totals = calculate_totals(data)
    for total in totals:
        print(format_total(total))
    append_to_log_file(totals)
    return totals
