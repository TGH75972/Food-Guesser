def start_game():
    print("Welcome to the Favorite Food Guesser!")
    print("I'll try to guess your favorite food based on your answers.")
    print("Answer the following questions with 'yes' or 'no'.\n")
    print("Let's begin!\n")

def is_sweet():
    answer = input("Do you prefer sweet food? (yes/no): ").strip().lower()
    return answer == "yes"

def is_spicy():
    answer = input("Do you like spicy food? (yes/no): ").strip().lower()
    return answer == "yes"

def is_healthy():
    answer = input("Do you prefer healthy food? (yes/no): ").strip().lower()
    return answer == "yes"

def is_savory():
    answer = input("Do you like savory food? (yes/no): ").strip().lower()
    return answer == "yes"

def is_vegetarian():
    answer = input("Are you a vegetarian? (yes/no): ").strip().lower()
    return answer == "yes"

def is_fruit_lover():
    answer = input("Do you love fruits? (yes/no): ").strip().lower()
    return answer == "yes"

def is_cheese_lover():
    answer = input("Do you love cheese? (yes/no): ").strip().lower()
    return answer == "yes"

def is_meat_lover():
    answer = input("Do you love meat? (yes/no): ").strip().lower()
    return answer == "yes"

def likes_pasta():
    answer = input("Do you enjoy pasta dishes? (yes/no): ").strip().lower()
    return answer == "yes"

def likes_grilled_food():
    answer = input("Do you like grilled food? (yes/no): ").strip().lower()
    return answer == "yes"

def guess_food(sweet, spicy, healthy, savory, vegetarian, fruit_lover, cheese_lover, meat_lover, pasta_lover, grilled_food):
    if sweet and not spicy:
        if healthy:
            if vegetarian:
                if fruit_lover:
                    return "Your favorite food might be a fruit salad or a smoothie bowl!"
                else:
                    return "You might love a sweet potato or a quinoa salad!"
            else:
                if meat_lover:
                    return "Your favorite food could be honey-glazed chicken or sweet salmon!"
                else:
                    return "You might enjoy a sweet and tangy chicken dish or a honey-mustard turkey!"
        else:
            if vegetarian:
                if cheese_lover:
                    return "Perhaps your favorite food is a cheesecake or a chocolate fondue!"
                else:
                    return "You probably love a decadent chocolate cake or a creamy dessert!"
            else:
                if meat_lover:
                    return "Your favorite might be a sweet BBQ rib or a honey-baked ham!"
                else:
                    return "You could enjoy sweet crepes or a caramelized dessert!"
    elif spicy and savory:
        if healthy:
            if vegetarian:
                if cheese_lover:
                    return "Your favorite food could be a spicy cheese quesadilla or a jalapeño popper!"
                else:
                    return "You might love a spicy vegetable stir-fry or a hot tofu dish!"
            else:
                if meat_lover:
                    return "You might enjoy spicy grilled chicken or a hot curry with a kick!"
                else:
                    return "Your favorite could be a spicy seafood stew or a sizzling fajita!"
        else:
            if vegetarian:
                if pasta_lover:
                    return "Perhaps you love spicy arrabbiata pasta or a zesty mac and cheese!"
                else:
                    return "You might enjoy spicy nachos or a fiery veggie burger!"
            else:
                if grilled_food:
                    return "Your favorite food could be spicy wings or a pepperoni pizza with extra chili!"
                else:
                    return "You might enjoy a spicy beef taco or a Cajun shrimp dish!"
    elif savory and not sweet:
        if healthy:
            if vegetarian:
                if pasta_lover:
                    return "You might enjoy a simple pasta primavera or a veggie stir-fry with noodles!"
                else:
                    return "Your favorite food could be a garden salad or a veggie burger!"
            else:
                if meat_lover:
                    return "You might love grilled fish or a classic chicken Caesar salad!"
                else:
                    return "You could enjoy a hearty turkey sandwich or a grilled shrimp salad!"
        else:
            if vegetarian:
                if cheese_lover:
                    return "Perhaps your favorite food is a mushroom risotto or a cheesy potato gratin!"
                else:
                    return "You might enjoy a hearty veggie stew or a savory lentil curry!"
            else:
                if grilled_food:
                    return "You could love a juicy steak or a bacon cheeseburger!"
                else:
                    return "You might enjoy a savory pot roast or a hearty beef stew!"
    else:
        return "It seems like you have a unique taste! Maybe your favorite food is something unusual like sushi with a twist or a gourmet sandwich?"

def main():
    start_game()
    
    sweet = is_sweet()
    spicy = is_spicy()
    healthy = is_healthy()
    savory = is_savory()
    vegetarian = is_vegetarian()
    fruit_lover = is_fruit_lover()
    cheese_lover = is_cheese_lover()
    meat_lover = is_meat_lover()
    pasta_lover = likes_pasta()
    grilled_food = likes_grilled_food()
    
    favorite_food = guess_food(sweet, spicy, healthy, savory, vegetarian, fruit_lover, cheese_lover, meat_lover, pasta_lover, grilled_food)
    print(f"\nBased on your answers, {favorite_food}")
    
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        print("\nRestarting the game...\n")
        main()
    else:
        print("\nThank you for playing the Favorite Food Guesser! Goodbye!")

if __name__ == "__main__":
    main()
