import sys
from stats import parse_record, average_by_city, warmest_city
lines = sys.stdin.read().splitlines()
valid_records = []
errors = 0
for line in lines:
    if not line.strip(): continue
    try:
        record = parse_record(line)
        valid_records.append(record)
    except ValueError:
        errors += 1
valid_count = len(valid_records)
city = warmest_city(valid_records)
averages = average_by_city(valid_records)
print(f"правильных записей  - {valid_count}")
print(f"ошибок - {errors}")
if city:
    print(f"самый теплый город - {city}")
else:
    print("бубубубебебе")
    
    
        
    
