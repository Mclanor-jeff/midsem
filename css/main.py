

eggs_per_box = 6

eggs_input = int(input("Enter the number of eggs: "))

last_uncompleted_box = (eggs_input % eggs_per_box)

if last_uncompleted_box == 0:
    print("The farmer has no eggs in the last uncompleted box")
elif last_uncompleted_box >=1:
    print(f"The farmer has {last_uncompleted_box} eggs in the last uncompleted box")

boxes_needed = eggs_input // eggs_per_box
print(boxes_needed)

if last_uncompleted_box < 6:
    print(f"The farmer requires {boxes_needed + 1} boxes")
elif last_uncompleted_box == 0:
    print("The farmer has no eggs in the last uncompleted box")
elif last_uncompleted_box >= 6:
    print(f"Number of baskets needed = {boxes_needed}")

additional_egg_needed = eggs_per_box - boxes_needed

print(f"Additional egg(s) needed: {additional_egg_needed} ")




