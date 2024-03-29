import json

class JsonReader:
        
    def __init__(self):
        # Get heroes data from json
        with open('public/supports.json', 'r') as file:
            self.heroes = json.load(file)
            
    def returnHeroes(self):
        return self.heroes

    def returnTargetHero(self):
        with open('public/settings.json', 'r') as file:
            targetHero = json.load(file)['targetHero']

        for hero, properties in self.heroes.items():
            if hero == targetHero:
                return [properties['x-index'], properties['y-index']]
        
    def returnActivationKey(self):
        with open('public/settings.json', 'r') as file:
            return json.load(file)['activationKey']