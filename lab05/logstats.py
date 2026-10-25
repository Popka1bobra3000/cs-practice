VALID_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError
    parts = line.split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError
    time, level, message = parts
    if level not in VALID_LEVELS:
        raise ValueError
    return {
        "time": time,
        "level": level,
        "message": message
    }


def count_levels(lines) -> dict:
    result = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            level = event["level"]
            result[level] = result.get(level, 0) + 1
        except ValueError:
            result["BROKEN"] = result.get("BROKEN", 0) + 1
    return result


def top_errors(lines, n: int) -> list[list]:
    if n <= 0:
        return []
    result = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                message = event["message"]
                result[message] = result.get(message, 0) + 1
        except ValueError:
            pass  # Битая строка просто пропускается
            
    sort = sorted(result.items(), key=lambda item: (-item[1], item[0]))
    return [[message, count] for message, count in sort[:n]]


def format_report(counts: dict, errors: list[list]) -> str:
    lines = ["Отчёт по журналу", ""]
    for level in sorted(counts.keys()):
        lines.append(f"{level}: {counts[level]}")
    lines.append("")
    lines.append("Частые ошибки:")
    if errors:
        for message, count in errors:
            lines.append(f"- {message} — {count}")
    return "\n".join(lines) + "\n"
