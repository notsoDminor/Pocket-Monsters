import json
import requests
data = requests.get("https://raw.githubusercontent.com/yorkcshub/Miscellanous/master/effectiveness.json")
data_json = json.loads(data.text)

power_convertor = {"super effective": 2, "normal effective": 1, "not very effective": 0.5, "no effect": 0}

def power_counter(fighter1, fighter2):
    for power in data_json:
        if fighter1 in data_json[power]:
            if fighter2 in data_json[power].get(fighter1):
                return power_convertor.get(power)

def attack(x, y, pokemons):
    warriors1 = []
    warriors2 = []
    warriors = pokemons.split(",")
    for i in range(x):
        warriors1.append(warriors[i])
    for i in range(x, y + x):
        warriors2.append(warriors[i])
    score1 = round(vs(warriors1, warriors2), 1)
    score2 = round(vs(warriors2, warriors1), 1)
    if score2 < score1:
        output = (score1, score2, "ME")
    elif score1 < score2:
        output = (score1, score2, "FOE")
    elif score1 == score2:
        output = (score1, score2, "EQUAL")
    print(output)


def vs(warriors1, warriors2):
    score = 0
    for w1 in warriors1:
        if " " in w1:
            w1 = w1.split(" ")
            for w2 in warriors2:
                if " " in w2:
                    w2 = w2.split(" ")
                    score += max(power_counter(w1[0], w2[0]) * power_counter(w1[0], w2[1]), power_counter(w1[1], w2[0]) * power_counter(w1[1], w2[1]))
                else:
                    score += max((power_counter(w1[0], w2)), (power_counter(w1[1], w2)))
        else:
            for w2 in warriors2:
                if " " in w2:
                    w2 = w2.split(" ")
                    score += (power_counter(w1, w2[0]) * power_counter(w1, w2[1]))
                else:
                    score += (power_counter(w1, w2))
    return score

attack(2,6,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug")
