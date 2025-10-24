'''
https://adventofcode.com/2024/day/2
Safe Data:
- All increasing or Decreasing
- max difference 3
'''

def check_safety(report):
    # Check if all increasing or decreasing
    increasing = all(x < y for x,y in zip(report, report[1:]))
    decreasing = all(x > y for x,y in zip(report, report[1:]))
    
    # Checking difference
    diff = [x - y for x,y in zip(report, report[1:])]
    safe = all(abs(d) < 4 for d in diff)

## alternatife: using a loop
    # for e in diff:
    #     # Using the absolute of each entry
    #     if abs(e) < 4:
    #         safe = True
    #     else:
    #         safe = False
    #         break #Breaking loop if any entry is False

    if safe and (increasing or decreasing):
        return "Safe"
    else:
        return "Unsafe"

test_data = [
[7, 6, 4, 2, 1], # Safe
[1, 2, 7, 8, 9], # Unsafe
[9, 7, 6, 2, 1], # Unsafe
[1, 3, 2, 4, 5], # Unsafe
[8, 6, 4, 4, 1], # Unsafe
[1, 3, 6, 7, 9]  # Safe
]

safe_reports = 0
for report in test_data:
    result = check_safety(report)
    if result == "Safe":
        safe_reports += 1

print(safe_reports)