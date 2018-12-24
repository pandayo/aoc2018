def create_army(at, line, ID, boost = 1):
    army = {}
    army["ID"] = ID
    army["at"] = at
    # Weaknesses
    army["weak"] = []
    army["immune"] = []
    if "(" in line:
        wi = line.split("(")[1].split(")")[0].split("; ")
        if len(wi) > 1:
            for info in wi:
                parseWeaknessInfo(army, info)
        else:
            parseWeaknessInfo(army, wi[0])
    # Numbers
    numbers = line.split(" ")
    army["HP"] = int(numbers[4])
    army["number"] = int(numbers[0])
    army["ini"] = int(numbers[-1])
    army["att"] = int(numbers[-6])
    if at == "imm":
        army["att"] *= boost
    # damage type
    army["damage"] = numbers[-5]
    army["target"] = None
    return(army)

def effective_power(army):
    return(army["att"]*army["number"])

def parseWeaknessInfo(army, wi):
    if wi.split(" ")[0] == "weak":
        army["weak"].extend(wi[8:].split(", "))
    else:
        army["immune"].extend(wi[10:].split(", "))

def calculate_dmg(army, target):
    if army["damage"] in target["immune"]:
        return(0)
    elif army["damage"] in target["weak"]:
        return(2*army["att"]*army["number"])
    else:
        return(army["att"]*army["number"])

def select_target(army, targets, already_targeted):
    best_target = None
    best_damage = 0
    best_ep = 0
    best_ini = 0
    for target in targets:
        if target["ID"] not in already_targeted:
            dmg = calculate_dmg(army, target)
##            print("Army {0} would deal army {1} {2} damage.".
##                  format(army["ID"], target["ID"], dmg))
            if dmg > best_damage:
                best_target = target["ID"]
                best_ep = effective_power(target)
                best_ini = target["ini"]
                best_damage = dmg
            elif dmg == best_damage:
                if best_ep < effective_power(target):
                    best_target = target["ID"]
                    best_ep = effective_power(target)
                    best_ini = target["ini"]
                    best_damage = dmg
                elif best_ep == effective_power(target):
                    if best_ini < target["ini"]:
                        best_target = target["ID"]
                        best_ep = effective_power(target)
                        best_ini = target["ini"]
                        best_damage = dmg
    return(best_target)

def attack(army, armies):
    if army["number"] > 0:
        for target in armies:
            if target["ID"] == army["target"]:
                dmg = calculate_dmg(army, target)
                dying = dmg // target["HP"]
                alive = target["number"]
                target["number"] = max(0, target["number"] - dying)
##                print("Army {0} dealt {1} dmg to army {2} killing {3} units."
##                      .format(army["ID"], dmg, target["ID"],
##                              min(alive, dying)))
                return
##    else:
##        print("Army {0} already is dead.".format(army["ID"]))


lines = open("input.txt").read().splitlines()

armytype = None
armies = []
group = 1

for line in lines:
    if line == "Immune System:":
        armytype = "Imm"
    elif line == "Infection:":
        armytype = "Inf"
    elif line != "":
        army = create_army(armytype, line, group)
        armies.append(army)
        group += 1

imm = [army for army in armies if army["at"] == "Imm" and army["number"] > 0]
inf = [army for army in armies if army["at"] == "Inf" and army["number"] > 0]

counter = 1

while imm and inf:
    armies = sorted(armies, key = lambda a: (effective_power(a), a["ini"]),
                    reverse = True)

##    print("-----Round {0:5d}-----".format(counter))

##    print("Immune System:")
##    for army in imm:
##        print("{0} contains {1} units.".format(army["ID"], army["number"]))
##    
##    print("Infection:")
##    for army in inf:
##        print("{0} contains {1} units.".format(army["ID"], army["number"]))

    #print("Target Selection:")
    
    target_ids = set()
    for army in armies:
        #print(army)
        if army["at"] == "Imm":
            army["target"] = select_target(army, inf, target_ids)
            target_ids.add(army["target"])
        else:
            army["target"] = select_target(army, imm, target_ids)
            target_ids.add(army["target"])
##    print("Attacking:")
    
    armies = sorted(armies, key = lambda a: a["ini"], reverse = True)
    for army in armies:
        if not army["target"] is None:
            attack(army, armies)
        #else:
        #    print("No valid target for this army")
    narmies = [target for target in armies if target["number"] > 0]
    armies = narmies
    
    imm = sorted([army for army in armies if army["at"] == "Imm"
                  and army["number"] > 0],
                 key = lambda a: a["ID"])
    inf = sorted([army for army in armies if army["at"] == "Inf"
                  and army["number"] > 0],
                 key = lambda a: a["ID"])

    counter += 1

    

winner = 0

for army in armies:
    winner += army["number"]

print(winner)
        
