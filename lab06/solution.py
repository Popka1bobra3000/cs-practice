def count_by_extension(paths):
    res = {}
    for p in paths:
        parts = p.split("/")
        filename = parts[-1]
        if "." in filename:
            ext = filename.split(".")[-1].lower()
        else:
            ext = ""
        if ext in res:
            res[ext] += 1
        else:
            res[ext] = 1
    return res


def deepest_path(paths):
    if len(paths) == 0:
        return ""
    
    best = paths[0]
    best_slashes = best.count("/")

    for p in paths[1:]:
        slashes = p.count("/")
        if slashes > best_slashes:
            best_slashes = slashes
            best = p
        elif slashes == best_slashes:
            if p < best:
                best = p

    return best


def human_size(n_bytes):
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    val = float(n_bytes)
    idx = 0
    
    while val >= 1024 and idx < len(units) - 1:
        val = val / 1024
        idx += 1
        
    if idx == 0:
        return str(int(val)) + " Б"
    
    return f"{round(val, 1):.1f} {units[idx]}"
