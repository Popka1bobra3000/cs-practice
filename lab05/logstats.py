def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError
    parts = line.split(" ", 2)
    if len(parts) != 3:
        raise ValueError
    time, level, message = parts
    if level not in {"DEBUG", "INFO", "WARNING", "ERROR"}:
        raise ValueError
    return {"time": time
            "level" level
            "message": message
    }

def count_levels(lines) -> dict:
    result = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            level = parse_event(line)["level"]
            result[lvl] = result.get(lvl, 0) + 1
        except ValueError:
            result["BROKEN"] = result.get("BROKEN",0) + 1
    return result

def top_errors(lines, n: int) -> list[list]:
    result = {}
    if n <= 0:
        return []
    for line in lines:
        if not line:
            continue
        level = parse_event(line)["level"]
        message = parse_event(line)["message"]
        try:
            if level == "ERROR":
                result(message) = result.get(message, 0) + 1
        except ValueError:
            pass
    sort = sorted(result.items(), key=lambda item: (-item[1], item[0]))
    return [[message, count] for message, count in sort[:n]]

def format_report(counts: dict, errors: list[list]) -> str
    lines = ["Отчёт по журналу", ""]
    for level in sorted(count.keys()):
        lines.append(f"{level}: {counts[level]}")
    lines.append("")
    if errors:
        for massage, count in errors:
            lines.append(f"- {massage} - {count}")
    return "\n".join(lines) + "\n"

    
    

            
