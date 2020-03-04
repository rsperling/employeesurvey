import sys


class Questionnaire:
    def __init__(self):
        self.name = ""
        self.location = ""
        self.cocktail = ""
        self.music = ""
        self.hobby = ""
        self.pet_peeve = ""
        self.num1 = ""
        self.book = ""
        self.bucket_list = ""
        self.adjective = ""

    def ask_me_stuff(self):
        print("I'm going to ask you some questions...\n")

        self.name = input("What is your nombre? ")
        self.location = input("Where are you from? ")
        self.cocktail = input("Favorite happy hour beverage: ")
        self.music = input("What genre of music do you listen to? ")
        self.hobby = input("Favorite thing to do: ")
        self.pet_peeve = input("What is your biggest pet peeve?: ")
        self.num1 = input("How many pairs of shoes do you own?: ")
        self.book = input("What types of books do you like to read?: ")
        self.bucket_list = input("What is at the top of your bucket list?: ")
        self.adjective = input("One word to best describe you: ")

        print("\n\n")

    def about_me(self):
        print(f"Hello! my nombre is {self.name}")
        print(f"My roots are based in {self.location}")
        print(f"When I go to happy hour, I LOVE to drink {self.cocktail}")
        print(f"I love to rock out to {self.music} in the shower every morning")
        print(f"When I am not at work, I like to {self.hobby}")
        print(f"My coworkers may not know it, but I REALLY cannot stand {self.pet_peeve}")
        print(f"I am a closet hoarder of approximately {self.num1} pairs of shoes")
        print(f"When I am not reading Bocchi's novel length emails, I love to read {self.book}")
        print(f"One thing I really hope to do in the near future is {self.bucket_list}")
        print(f"Many would describe me as {self.adjective}")


if __name__ == "__main__":
    q = Questionnaire()
    q.ask_me_stuff()
    q.about_me()
    sys.exit(0)