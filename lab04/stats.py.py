def parse_record(line: str):
    parts = line.split(";")
    if len(parts) != 3 or not parts[0].strip() or not parts[1] or not parts[2].strip():
        raise ValueError()
    try:
        q = float(parts[1])
    except ValueError:
        raise ValueError()
    result = {
                'city': parts[0].strip(),
                'temperature': q,
                'date': parts[2].strip()
                }
    return result
def read_valid(lines: list[str]):
    results = [] 
    for line in lines:
        if not line.strip(): 
            continue
        try:
            results.append(parse_record(line))
        except ValueError:
            pass
    return results
