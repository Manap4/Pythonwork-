grocery_list = {}

while True:
    try:
        item = input("Please enter an item: ").strip().title()
        if not item:
            continue
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    except EOFError:
        break

sorted_items = sorted(grocery_list.keys())

for item in sorted_items:
    count = grocery_list[item]
    print(f"{count} {item.upper()}")