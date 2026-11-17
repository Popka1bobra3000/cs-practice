import json
def csv_to_records(text: str) -> list[dict]:
    if text.strip() == "":
        return []

    lines = text.strip().split("\n")
    raw_headers = lines[0].split(",")
    headers = []
    for h in raw_headers:
        headers.append(h.strip())

    res = []
    for line in lines[1:]:
        if line.strip() == "":
            continue
        parts = line.split(",")
        row = {}
        for i in range(len(headers)):
            row[headers[i]] = parts[i].strip()
        res.append(row)

    return res


def parse_settings(lines: list[str]) -> dict:
    res = {}
    list_key = None

    for line in lines:
        if "#" in line:
            pos = line.index("#")
            line = line[:pos]

        line = line.strip()
        if line == "":
            continue

        if line.startswith("- ") and list_key is not None:
            raw_val = line[2:].strip()
            low = raw_val.lower()
            if low == "true" or low == "yes":
                val = True
            elif low == "false" or low == "no":
                val = False
            else:
                try:
                    val = int(raw_val)
                except ValueError:
                    try:
                        val = float(raw_val.replace(",", "."))
                    except ValueError:
                        val = raw_val
            res[list_key].append(val)

        elif ":" in line:
            parts = line.split(":", 1)
            k = parts[0].strip()
            raw_val = parts[1].strip()

            if raw_val == "":
                res[k] = []
                list_key = k
            else:
                list_key = None
                low = raw_val.lower()
                if low == "true" or low == "yes":
                    val = True
                elif low == "false" or low == "no":
                    val = False
                else:
                    try:
                        val = int(raw_val)
                    except ValueError:
                        try:
                            val = float(raw_val.replace(",", "."))
                        except ValueError:
                            val = raw_val
                res[k] = val

    return res



