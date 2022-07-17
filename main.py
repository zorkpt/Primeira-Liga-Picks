
Clubes = ["Arouca", "Benfica", "Boavista", "Casa Pia","Chaves", "Estoril", "Famalicão","Gil Vicente", "Maritimo", "P. Ferreira", "Portimonense", "Porto", "Rio Ave", "Santa Clara", "Braga", "Sporting", "Vitoria SC", "Vizela"]


from os import sched_get_priority_max
from pprint import pprint as pp

def make_day(num_teams, day):
    # using circle algorithm, https://en.wikipedia.org/wiki/Round-robin_tournament#Scheduling_algorithm
    assert not num_teams % 2, "Number of teams must be even!"
    # generate list of teams
    lst = Clubes
    # rotate
    day %= (num_teams - 1)  # clip to 0 .. num_teams - 2
    if day:                 # if day == 0, no rotation is needed (and using -0 as list index will cause problems)
        lst = lst[:1] + lst[-day:] + lst[1:-day]
    # pair off - zip the first half against the second half reversed
    half = num_teams // 2
    return list(zip(lst[:half], lst[half:][::-1]))

def make_schedule(num_teams):
    jornada = []
    """
    Produce a double round-robin schedule
    """
    # number of teams must be even
    if num_teams % 2:
        num_teams += 1  # add a dummy team for padding

    # build first round-robin
    schedule = [make_day(num_teams, day) for day in range(num_teams - 1)]
    # generate second round-robin by swapping home,away teams
    swapped = [[(away, home) for home, away in day] for day in schedule]
    jornada = [schedule + swapped]
    return jornada

def main():
    num_teams = len(Clubes)
    schedule = make_schedule(num_teams)
    

    for i in schedule:
        for a in i:
            for b in a:
                print(f" {b[0]} - {b[1]} ")
            print('',sep='\n')
    

if __name__ == "__main__":
    main()