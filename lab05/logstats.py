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
    
    
