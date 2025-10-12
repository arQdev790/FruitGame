import random

# Add a price for fruits
fruit_prices = {
    "strawberry": 2,
    "lemon": 1,
    "blueberry": 3,
    "banana": 2,
    "mango": 4,
    "kiwi": 2,
    "apple": 3,
    "grape": 3,
    "pear": 2,
    "pineapple": 5,
    "watermelon": 6,
    "orange": 2,
    "peach": 3,
    "plum": 2,
    "cherry": 3,
    "pomegranate": 4,
}

fruit_facts = {
    "strawberry": "Strawberries are the only fruits with seeds on the outside.",
    "lemon": "Lemons contain more sugar than strawberries.",
    "blueberry": "Blueberries are one of the only naturally blue foods.",
    "banana": "Bananas are technically berries.",
    "mango": "Mangoes are the most consumed fruits in the world.",
    "kiwi": "Kiwis are rich in vitamin C.",
    "apple": "Apples float in water because they are 25% air.",
    "grape": "Grapes explode when you put them in a microwave.",
    "pear": "Pears ripen best off the tree.",
    "pineapple": "Pineapples take two years to grow.",
    "watermelon": "Watermelons are 92% water.",
    "orange": "Oranges are a hybrid of pomelo and mandarin.",
    "peach": "Peaches are related to almonds.",
    "plum": "Plums are one of the first domesticated fruits by humans.",
    "cherry": "Cherries belong to the rose family.",
    "pomegranate": "Pomegranates have more than 600 seeds.",
}

class Fruit:
    def __init__(self, name, shape, color, is_sweet, size, texture):
        self.name = name
        self.shape = shape
        self.color = color
        self.is_sweet = is_sweet  #true, false or sometimes
        self.size = size
        self.texture = texture

    def identify(self):
        sweet_str = (
            "sweet" if self.is_sweet is True
            else "not sweet" if self.is_sweet is False
            else "sometimes sweet"
        )
        return (
            f"{self.name.capitalize()} is {self.shape}, {self.color}, "
            f"{sweet_str}, {self.size}, and {self.texture}."
        )

known_fruits = [
    Fruit("strawberry", "triangle", "red", True, "small", "rough"),
    Fruit("lemon", "oval", "yellow", False, "medium", "rough"),
    Fruit("blueberry", "round", "blue", "sometimes", "small", "smooth"),
    Fruit("banana", "crescent", "yellow", True, "medium", "smooth"),
    Fruit("mango", "oval", "orange", "sometimes", "medium", "smooth"),
    Fruit("kiwi", "oval", "brown", "sometimes", "small", "fuzzy"),
    Fruit("apple", "round", "red", "sometimes", "medium", "smooth"),
    Fruit("grape", "round", "purple", True, "small", "smooth"),
    Fruit("pear", "oval", "green", "sometimes", "medium", "smooth"),
    Fruit("pineapple", "oval", "brown", "sometimes", "large", "rough"),
    Fruit("watermelon", "round", "green", True, "large", "smooth"),
    Fruit("orange", "round", "orange", "sometimes", "medium", "rough"),
    Fruit("peach", "round", "orange", True, "medium", "fuzzy"),
    Fruit("plum", "round", "purple", True, "small", "smooth"),
    Fruit("cherry", "round", "red", True, "small", "smooth"),
    Fruit("pomegranate", "round", "red", "sometimes", "medium", "rough"),
]

def play_fruit_game():
    starting_money = 15
    money = starting_money
    fruits_to_buy = random.sample(list(fruit_prices.keys()), 3)
    bought_fruits = []

    print(f"Welcome to the Fruit Buying Game! You start with ${money}.")
    print("You need to buy these three fruits:", ", ".join(f.capitalize() for f in fruits_to_buy))
    print("Let's begin!\n")

    missing_fruits = fruits_to_buy.copy()
    while missing_fruits and money > 0:
        for target_fruit in missing_fruits[:]:
            print(f"Let's guess the characteristic of your next fruit ({target_fruit.capitalize()}):")
            user_shape = input("Enter the shape of the fruit: ").strip().lower()
            user_color = input("Enter the color of fruit: ").strip().lower()
            user_is_sweet_input = input("Is the fruit sweet? yes/no/sometimes: ").strip().lower()
            user_size = input("What is the size of your fruit? small/medium/large: ").strip().lower()
            user_texture = input("What is the texture of your fruit? smooth/rough/fuzzy: ").strip().lower()
            if user_is_sweet_input == "yes":
                user_is_sweet = True
            elif user_is_sweet_input == "no":
                user_is_sweet = False
            else:
                user_is_sweet = "sometimes"

            probabilities = []
            for fruit in known_fruits:
                prob = calculate_match_probability(fruit, user_shape, user_color, user_is_sweet, user_size, user_texture)
                probabilities.append((fruit, prob))

            best_fruit, best_prob = max(probabilities, key=lambda x: x[1])

            percent = int(best_prob * 100)
            print(f"\nThere is a {percent}% chance this is your fruit: {best_fruit.name.capitalize()}")
            print(best_fruit.identify())
            
            fruit_cost = fruit_prices.get(best_fruit.name, 1)
            if money >= fruit_cost:
                money -= fruit_cost
                bought_fruits.append(best_fruit.name)
                print(f"You bought a {best_fruit.name} for ${fruit_cost}. Remaining money: ${money}\n")
                if best_fruit.name == target_fruit:
                    missing_fruits.remove(target_fruit)
            else:
                print(f"Not enough money to buy {best_fruit.name}. Skipping purchase.\n")

        if missing_fruits and money > 0:
            print(f"You still need: {', '.join(f.capitalize() for f in missing_fruits)}")
            retry = input("You have money left. Do you want to retry for the missing fruits? (yes/no): ").strip().lower()
            if retry != "yes":
                break

    print("Game over!")
    if not missing_fruits:
        print(f"Congratulations! You have bought all required fruits: {', '.join(f.capitalize() for f in bought_fruits)}")
        print(f"Money left: ${money}")
        if bought_fruits:
            read_fruit_facts(bought_fruits)
            summarize_sweetness(bought_fruits)
    elif money == 0:
        print("You ran out of money and couldn't buy all fruits, you lose!")
        print(f"Fruits you bought: {', '.join(f.capitalize() for f in bought_fruits)}")
    else:
        print("You chose not to retry. Game over.")
        print(f"Fruits you bought: {', '.join(f.capitalize() for f in bought_fruits)}")
        print(f"Money left: ${money}")

def calculate_match_probability(fruit, shape, color, is_sweet, size, texture):
    score = 0
    total = 5

    if fruit.shape == shape:
        score += 1
    if fruit.color == color:
        score += 1
    if fruit.is_sweet == is_sweet:
        score += 1
    if fruit.size == size:
        score += 1
    if fruit.texture == texture:
        score += 1

    return score / total

def read_fruit_facts(bought_fruits):
    """Print a fact about each fruit from bought_fruits"""
    print("\nFruit Facts for your purchases: ")
    for fruit in bought_fruits:
        fact = fruit_facts.get(fruit, "No fact available for this fruit")
        print(f"- {fruit.capitalize()}: {fact}")

def summarize_sweetness(bought_fruits):
    """Print how many fruits are sweet, sour, or sometimes sweet"""
    sweet = 0
    sour = 0
    sometimes = 0
    for fruit_name in bought_fruits:
        fruit_obj = next((f for f in known_fruits if f.name == fruit_name), None)
        if fruit_obj:
            if fruit_obj.is_sweet is True:
                sweet += 1
            elif fruit_obj.is_sweet is False:
                sour += 1
            else:
                sometimes += 1
    print(f"\nSweetness Summary of your purchased fruits:")
    print(f"- Sweet: {sweet}")
    print(f"- Sour: {sour}")
    print(f"- Sometimes sweet: {sometimes}")

if __name__ == "__main__":
    play_fruit_game()