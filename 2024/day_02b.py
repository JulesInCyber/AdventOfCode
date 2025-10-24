def base_check(report):
    # Basic check stays the same
    increasing = all(x < y for x, y in zip(report, report[1:]))
    decreasing = all(x > y for x, y in zip(report, report[1:]))
    diff = [x - y for x, y in zip(report, report[1:])]
    safe = all(abs(d) < 4 for d in diff)

    if safe and (increasing or decreasing):
        return True
    else:
        return False

def advanced_check(report):
    for i in range(len(report)):
        tmp = report.pop(i)
        dampener = base_check(report)
        if dampener == True:
            break
        report.insert(i, tmp)
    return dampener

# Test Data
test_data = [
    [7, 6, 4, 2, 1], # Safe
    [1, 2, 7, 8, 9], # Unsafe
    [9, 7, 6, 2, 1], # Unsafe
    [1, 3, 2, 4, 5], # Safe
    [8, 6, 4, 4, 1], # Safe
    [1, 3, 6, 7, 9]  # Safe
]

if __name__ == '__main__':
    safe_reports = 0
    for t in test_data:
        result = advanced_check(t)
        if result == True:
            safe_reports += 1

    print(safe_reports)