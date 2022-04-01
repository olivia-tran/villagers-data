"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    data = open(filename)
    for line in data:
        line = line.rstrip()
        villager_name, villager_species, personality, hobby, motto = line.split(
            '|')
        species.add(villager_species)
    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []
    data = open(filename)
    for line in data:
        line = line.rstrip()
        villager_name, villager_species, personality, hobby, motto = line.split(
            '|')

        if search_string == villager_species or search_string == "All":
            villagers.append(villager_name)

    # TODO: replace this with your code

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    Fitness, Nature, Education, Music, Fashion, Play = [], [], [], [], [], []

    data = open(filename)
    for line in data:
        line = line.rstrip()
        villager_name, villager_species, personality, hobby, motto = line.split(
            '|')
        if hobby == "Fitness":
            Fitness.append(villager_name)
        elif hobby == "Nature":
            Nature.append(villager_name)
        elif hobby == "Education":
            Education.append(villager_name)
        elif hobby == "Music":
            Music.append(villager_name)
        elif hobby == "Fashion":
            Fashion.append(villager_name)
        elif hobby == "Play":
            Play.append(villager_name)
    villagers_by_hobby = [sorted(Fitness), sorted(Nature), sorted(
        Education), sorted(Music), sorted(Fashion), sorted(Play)]
    # villagers_by_hobby = [Fitness, Nature,Education, Music, Fashion, Play].sort()

    return villagers_by_hobby


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    data = open(filename)
    for line in data:
        line = line.rstrip()
        villager_name, villager_species, personality, hobby, motto = line.split(
            '|')
        all_data.append((villager_name, villager_species,
                        personality, hobby, motto))

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    data = open(filename)
    for line in data:
        line = line.rstrip()
        name, villager_species, personality, hobby, motto = line.split(
            '|')
        if name == villager_name:
            return motto

    return None


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    villager_personality = None

    data = open(filename)
    for line in data:
        line = line.rstrip()
        name, villager_species, personality, hobby, motto = line.split(
            '|')
        if villager_name == name:
            villager_personality = personality
            break

    likeminded_villagers = set()

    for line in data:
        line = line.rstrip()
        name, villager_species, personality, hobby, motto = line.split(
            '|')
        if villager_personality == personality:
            likeminded_villagers.add(name)

    return likeminded_villagers


print(all_species('villagers.csv'))
print("\n")
print(get_villagers_by_species('villagers.csv', "All"))
print("\n")
print(all_names_by_hobby('villagers.csv'))

print(all_data('villagers.csv'))
print(find_motto('villagers.csv', 'Antonio'))
print(find_likeminded_villagers('villagers.csv', 'Wendy'))
