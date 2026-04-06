def ask_city():
    city =  input("¿Donde Vivis?")
    if len(city) > 0:
        return city
    else:
        ask_city()

def greetings(city: str):
    print(f"Bienvenido a {city.strip()}")


greetings(ask_city())
