import json

class HeroSelection:
    # def __init__(self):
    #     pass

    def initialize(self):
        with open('heroes.json', 'r') as file:
            data = json.load(file)
            print(data)
            print(data.items())

        # for hero, properties in data.items():
        #     # print(hero['x-index'])
        #     print(hero)
        #     print(properties)
