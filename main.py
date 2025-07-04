import os 

def main():
    name = os.getenv("INPUT_NAME", "Jiyadh")
    print(f"hello, {name}! This is your Python-based Github Action.")


if __name__== "__main__":
    main()