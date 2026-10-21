# ---------- Task 1 ----------

def total_salary(path):
    """Return a (total, average) salary tuple read from the file."""
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                _, salary = line.split(",")
                total += int(salary)
                count += 1
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0, 0
    except (ValueError, OSError) as error:
        print(f"Cannot read file {path}: {error}")
        return 0, 0

    average = total / count if count else 0
    return total, average


# ---------- Task 2 ----------

def get_cats_info(path):
    """Return a list of dicts with cat info read from the file."""
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                cat_id, name, age = line.split(",")
                cats.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except (ValueError, OSError) as error:
        print(f"Cannot read file {path}: {error}")
        return []
    return cats

if __name__ == "__main__":
    total, average = total_salary("salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, \nСередня заробітна плата: {average}")
    print("\n")
    print(get_cats_info("cats.txt"))
