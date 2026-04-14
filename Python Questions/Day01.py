transactions = [
    100, -50, None, 200, "300", 100, -10, "invalid", 400,
    "500.5", 0, "", "700", -300, 200, "NULL"
]

"""🔹 Questions 
Q1. Remove Missing / Null-like Values
👉 Remove:
None
""
"NULL"

Pattern: Data cleaning (standardization). """

transactions = [
    100, -50, None, 200, "300", 100, -10, "invalid", 400,
    "500.5", 0, "", "700", -300, 200, "NULL"
]

cleaned = [x for x in transactions if x not in (None, "", "NULL")]
print("Q1:", cleaned)


"""
Q2. Standardize Data Types
👉 Convert:
"300" → 300
"500.5" → 500.5
👉 Ignore:
"invalid"

Pattern: Transformation + validation."""

transactions = [
    100, -50, None, 200, "300", 100, -10, "invalid", 400,
    "500.5", 0, "", "700", -300, 200, "NULL"
]

standardized = []

for x in transactions:
    if x in (None, "", "NULL"):
        continue

    if isinstance(x, str):
        try:
            if "." in x:
                x = float(x)
            else:
                x = int(x)
        except:
            continue

    standardized.append(x)

print(standardized)

"""
Q3. Keep Only Valid Numeric Records
👉 Final list should contain only:
int and float

Pattern: Data validation
"""
transactions = [
    100, -50, None, 200, "300", 100, -10, "invalid", 400,
    "500.5", 0, "", "700", -300, 200, "NULL"
]

valid_numbers = []

for x in transactions:
    if isinstance(x, (int, float)):
        valid_numbers.append(x)
    elif isinstance(x, str):
        try:
            if "." in x:
                valid_numbers.append(float(x))
            else:
                valid_numbers.append(int(x))
        except:
            pass

print(valid_numbers)

"""
Q4. Apply Business Rule Filtering
👉 Keep only values: Greater than 0

Pattern: Business filtering logic
"""

transactions = [
    100, -50, None, 200, "300", 100, -10, "invalid", 400,
    "500.5", 0, "", "700", -300, 200, "NULL"
]

filtered = []

for x in transactions:
    try:
        if isinstance(x, str):
            x = float(x) if "." in x else int(x)

        if isinstance(x, (int, float)) and x > 0:
            filtered.append(x)
    except:
        pass

print(filtered)

"""
Q5. Deduplicate Records
👉 Remove duplicates after cleaning
Pattern: Data deduplication
"""

transactions = [
    100, -50, None, 200, "300", 100, -10, "invalid", 400,
    "500.5", 0, "", "700", -300, 200, "NULL"
]

unique = []

for x in transactions:
    try:
        if isinstance(x, str):
            x = float(x) if "." in x else int(x)

        if isinstance(x, (int, float)) and x > 0:
            if x not in unique:
                unique.append(x)
    except:
        pass

print(unique)

"""
Q6. Compute Total Transaction Value
👉 Sum all cleaned values
Pattern: Aggregation
"""

transactions = [
    100, -50, None, 200, "300", 100, -10, "invalid", 400,
    "500.5", 0, "", "700", -300, 200, "NULL"
]

total = 0

for x in transactions:
    try:
        if isinstance(x, str):
            x = float(x) if "." in x else int(x)

        if isinstance(x, (int, float)) and x > 0:
            total += x
    except:
        pass

print(total)

"""
Q7. Count Records by Type
👉 Count:
how many integers
how many floats

Pattern: Basic data profiling
"""

transactions = [
    100, -50, None, 200, "300", 100, -10, "invalid", 400,
    "500.5", 0, "", "700", -300, 200, "NULL"
]

int_count = 0
float_count = 0

for x in transactions:
    try:
        if isinstance(x, str):
            if "." in x:
                x = float(x)
            else:
                x = int(x)

        if isinstance(x, int):
            int_count += 1
        elif isinstance(x, float):
            float_count += 1
    except:
        pass

print("Integers:", int_count)
print("Floats:", float_count)

"""
Q8. Identify Invalid Records (Important ⭐)
👉 Create a separate list of: invalid values ("invalid", "NULL", etc.)
Pattern: Data quality tracking
"""

transactions = [
    100, -50, None, 200, "300", 100, -10, "invalid", 400,
    "500.5", 0, "", "700", -300, 200, "NULL"
]

invalid = []

for x in transactions:
    if x in (None, "", "NULL"):
        invalid.append(x)
    elif isinstance(x, str):
        try:
            float(x)
        except:
            invalid.append(x)

print(invalid)

"""
Q9. Sort Clean Data
👉 Sort final cleaned data in ascending order
Pattern: Data preparation for reporting
"""

transactions = [
    100, -50, None, 200, "300", 100, -10, "invalid", 400,
    "500.5", 0, "", "700", -300, 200, "NULL"
]

clean = []

for x in transactions:
    try:
        if isinstance(x, str):
            x = float(x) if "." in x else int(x)

        if isinstance(x, (int, float)) and x > 0:
            if x not in clean:
                clean.append(x)
    except:
        pass

sorted_data = sorted(clean)
print(sorted_data)

"""
Q10. Build Mini Data Processing Function ⭐⭐
👉 Write a function:
def clean_transactions(data):
    return cleaned_data
👉 It should:
Handle nulls
Convert values
Remove invalid
Apply business rules
Deduplicate
"""

def clean_transactions(data):
    result = []

    for x in data:
        if x in (None, "", "NULL"):
            continue

        try:
            if isinstance(x, str):
                x = float(x) if "." in x else int(x)
        except:
            continue

        if isinstance(x, (int, float)) and x > 0:
            if x not in result:
                result.append(x)

    return result


transactions = [
    100, -50, None, 200, "300", 100, -10, "invalid", 400,
    "500.5", 0, "", "700", -300, 200, "NULL"
]

print(clean_transactions(transactions))
