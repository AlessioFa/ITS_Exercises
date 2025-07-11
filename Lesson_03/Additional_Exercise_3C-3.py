objects: list[str] = []

while True:
    your_object = input("Enter some objects:").lower()
    
    if your_object == "stop":
        break
    
    objects.append(your_object)


match objects:

    case ["penna", "matita", "quaderno"]:
        print(f"['penna', 'matita', 'quaderno']\nSchool supplies")
    
    case ["pane", "latte", "uova"]:
        print(f"['pane', 'latte', 'uova']\nProdotti alimentari")
    
    case ["sedia", "tavolo", "armadio"]:
        print(f"['sedia', 'tavolo', 'armadio']\nMobili")
    
    case ["telefono", "computer", "tablet"]:
        print("['telefono', 'computer', 'tablet']\nDispositivi elettronici")
    
    case _:
        print(f"{object}\nCategory not recognised")
