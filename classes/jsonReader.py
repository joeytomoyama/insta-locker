import json

class JsonReader:
        
    def __init__(self):
        # Get heroes data from json
        with open('public/supports.json', 'r') as file:
            self.supports = json.load(file)

        with open('public/heroes.json', 'r') as file:
            self.heroes = json.load(file)
            
    def returnSupports(self):
        return self.supports
    
    def returnHeroes(self):
        return self.heroes
    
    def returnHeroesList(self):
        return self.heroes.keys()
    
    def returnTargetHero(self):
        with open('public/settings.json', 'r') as file:
            return json.load(file)['targetHero']

    def returnTargetHeroPos(self):
        with open('public/settings.json', 'r') as file:
            targetHero = json.load(file)['targetHero']

        for hero, properties in self.supports.items():
            if hero == targetHero:
                return [properties['x-index'], properties['y-index']]
            
    def setTargetHero(self, hero):
        with open('public/settings.json', 'r') as file:
            settings = json.load(file)

        settings['targetHero'] = hero

        with open('public/settings.json', 'w') as file:
            json.dump(settings, file, indent=4)

    def setHeroXY(self, hero, x, y):
        self.heroes[hero]['positionY'] = y
        self.heroes[hero]['positionX'] = x

        with open('public/heroes.json', 'w') as file:
            json.dump(self.heroes, file, indent=4)
        
    def returnActivationKey(self):
        with open('public/settings.json', 'r') as file:
            return json.load(file)['activationKey']