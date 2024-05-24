for outer in range(1, 10):
    if outer == 7:
        break
    for inner in range(1, 10):
        if inner == 3:
            continue
        print(f"Outer: {outer}, Inner: {inner}")
