class Animals:
    head = 1
    body = 1
    tail = 1
    weight = 10.0
    single_calorie_consumption = 0.5
    voice_var = 'Mumbling...'

    def walk(self):
        if self.weight > (self.single_calorie_consumption * 10):
            print('Walking...')
            self.weight -= self.single_calorie_consumption
        else:
            print('I can''t walk, need more food...')

    def sleep(self):
        print('Z-z-z...')
        self.weight -= self.single_calorie_consumption

    def eat(self):
        print('Munch-Munch...')
        self.weight += self.single_calorie_consumption

    def drink(self):
        print('Slurping...')

    def voice(self):
        print(self.voice_var)


class FourLegAnimal(Animals):
    weight = 50
    single_calory_consumption = 1
    legs = 4
    horns = True

    def sit(self):
        print('Sitting...')


class Birds(Animals):
    weight = 0.5
    single_calory_consumption = 0.05
    legs = 2
    wings = True

    def fly(self):
        print('Flying...')


class Cow(FourLegAnimal):
    weight = 700
    voice_var = 'Moo!'


class Goat(FourLegAnimal):
    weight = 30
    voice_var = 'Baaaaahh!'


class Sheep(FourLegAnimal):
    weight = 50
    voice_var = 'Baa!'


class Pig(FourLegAnimal):
    weight = 60
    horns = False
    voice_var = 'Oink!'


class Duck(Birds):
    weight = 0.7
    voice_var = 'Quack!'


class Chicken(Birds):
    weight = 0.6
    voice_var = 'Co-co!'


class Goose(Birds):
    weight = 1.2
    voice_var = 'Quack!'
