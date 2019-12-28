def score(dice_values):
    if not 1 <= len(dice_values) <= 6:
        raise Exception(f'the number dice kept is not between 1 and 6: {len(dice_values)}')

    frequencies_table = dict()
    for die in dice_values:
        if die not in range(1, 7):
            raise Exception(f'die value is not in integer between range [1, 6]: {die}')
        frequencies_table[die] = frequencies_table.get(die, 0) + 1

    frequencies = list(frequencies_table.values())
    total = 0
    for die_value, frequency in sorted(frequencies_table.items(), key=lambda x: x[1], reverse=True):
        if frequency <= 2:
            if frequencies == [2, 2, 2]:
                return 1500
            if frequencies == [1, 1, 1, 1, 1, 1]:
                return 1500
            if die_value == 1:
                total += 100 * frequency
            elif die_value == 5:
                total += 50 * frequency
        elif frequency == 3:
            if frequencies == [3, 3]:
                return 2500
            total += 1000 if die_value == 1 else die_value * 100
        elif frequency == 4:
            total += 1100 if die_value == 1 else 1000
        elif frequency == 5:
            total += 2000
        else:
            return 3000

    return total
