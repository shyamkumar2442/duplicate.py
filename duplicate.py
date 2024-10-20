def find_duplicates(numbers):
    duplicates = []
    
    for number in numbers:
        if numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)
    
    return duplicates

# Input
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
duplicates = find_duplicates(numbers)

if duplicates:
    print("Duplicate numbers:", duplicates)
else:
    print("No duplicates found.")
