import os

PATH = "app.log"

if not os.path.exists(PATH):
    print('No log file exist')
else:
    with open(PATH) as file:
        lines = file.readlines()

    logData = []
    total_lines = 0
    level_count = {}
    error_messages = []

    for line in lines:
        total_lines += 1
        a1, a2, a3, a4 = line.split(" ", 3)

        logData.append({
            "date": a1,
            "time": a2,
            "type": a3,
            "message": a4.strip()
        })

        level_count[a3] = level_count.get(a3, 0) + 1

        if a3 == "ERROR":
            error_messages.append(a4.strip())

    print("\nTotal log lines:", total_lines)

    print("\nLog level counts:")
    for level, count in level_count.items():
        print(f"{level}: {count}")

    print("\nError messages:")
    if error_messages:
        for msg in error_messages:
            print("-", msg)
    else:
        print("No errors found")
