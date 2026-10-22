from logstats import count_levels, top_errors, format_report

filename = input().strip()

with open(filename, "r", encoding="utf-8") as file:
    counts = count_levels(file)

total_parsed = sum(counts.values())
error_count = counts.get("ERROR", 0)
broken_count = counts.get("BROKEN", 0)

print(total_parsed)
print(error_count)
print(broken_count)

with open(filename, "r", encoding="utf-8") as file:
    errors = top_errors(file, 3)

report_text = format_report(counts, errors)

with open("report.txt", "w", encoding="utf-8") as rep:
    rep.write(report_text)
