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
def average_by_city(records: list[dict]):
    if not records:
        return {}
    cities = {}
    counts = {}
    for record in records:
        city = record['city']
        temp = record['temperature']
        cities[city] = cities.get(city, 0.0) + temp
        counts[city] = counts.get(city, 0) + 1
    average = {}
    for city in cities:
        average[city] = round(cities[city] / counts[city], 1)
    return average
def warmest_city(records: list[dict]):
    if not records: 
        return ''
    averages = average_by_city(records)
    if not averages: 
        return ""
    return min(averages.keys(), key=lambda city: (-averages[city], city))
