def header(title):
    print("=" * 60)
    print(title.center(60))
    print("=" * 60)

def menu(options):
    for k, v in options.items():
        print(f"{k} - {v}")
    print("-" * 60)

def pause():
    input("Press Enter to continue...")
