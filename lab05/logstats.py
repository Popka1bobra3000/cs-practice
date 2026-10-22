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

            
