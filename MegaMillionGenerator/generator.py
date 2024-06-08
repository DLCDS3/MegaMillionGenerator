import random

class Generator:
    def __init__(self, number_of_draw: int, avoid_numbers_white: list, avoid_numbers_yellow: list, duplicate_number: bool = False):
        if not duplicate_number and number_of_draw >= 14:
            raise ValueError("Cannot generate 14 or more unique draws without allowing duplicate numbers.")
        
        self.number_of_draw = number_of_draw
        self.duplicate_number = duplicate_number
        self.avoid_numbers_white = avoid_numbers_white
        self.avoid_numbers_yellow = avoid_numbers_yellow
        self.generated_draws_white = []
        self.generated_draws_yellow = []

        

    def generate(self):
            for draw in range(0,self.number_of_draw):
                generated_white = []

                # White Ball Generation
                while len(generated_white) < 5:
                    num = random.randint(1, 70)
                    if num not in generated_white and num not in self.avoid_numbers_white and not (self.duplicate_number and any(num in draw for draw in self.generated_draws_white)):
                        generated_white.append(num)
                
                # Yellow Ball Generation
                while True:
                    yellow_num = random.randint(1,25)
                    if yellow_num not in self.avoid_numbers_yellow and not (self.duplicate_number and yellow_num in self.generated_draws_yellow):
                        break

                self.generated_draws_white.append(generated_white)
                self.generated_draws_yellow.append(yellow_num)

            # Putting results together
            self.resulting_draws = [self.generated_draws_white[draw] + [self.generated_draws_yellow[draw]] for draw in range(self.number_of_draw)]
                
            return self.resulting_draws