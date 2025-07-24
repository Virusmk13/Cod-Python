import datetime

def generate_output():
    now = datetime.datetime.now()
    output = f"[{now}] Exemplu de output generat de cod1\n"
    output += "Linia 1: Hello World!\n"
    output += "Linia 2: Aceasta este o demonstrație.\n"

    with open("output.log", "w") as f:
        f.write(output)

    print("Fișierul output.log a fost generat.")

if __name__ == "__main__":
    generate_output()
