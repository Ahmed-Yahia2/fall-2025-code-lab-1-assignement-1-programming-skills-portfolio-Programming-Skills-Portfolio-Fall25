names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search_term = "Sam"
found = False
for name in names:
    if name == search_term:
        found = True
        break
if found:
    print(f"{search_term} was found in the list!")
else:
    print(f"{search_term} was NOT found in the list.")
