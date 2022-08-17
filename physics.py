from math import prod
from matplotlib import pyplot as plt


def chance_for(n, out_of=35, revealed=5):
    """
    example - imagine a set of 10 questions, 3 completed as shown by *
    [1 2 3* 4* 5* 6 7 8 9 10]

    what is chance of 3 random unique selections all *?

    chance of selecting a completed one is 3/10
    now set looks something like this
    [1 2 4* 5* 6 7 8 9 10]

    chance of next random selection among completed is 2/9
    set becomes something like
    [1 2 4* 6 7 8 9 10]

    final selection now has 1/8 chance of success (ie) choosing 4*

    so we end up with a computation like (3/10) * (2/9) * (1/8)

    :return: float within [0, 1]
    """
    chance = prod((n - i) / (out_of - i) for i in range(revealed))
    return chance


# assume 35 total questions and reveal 5 at random
questions_completed = list(range(5, 35 + 1))
chances = [chance_for(n) for n in questions_completed]

# convert the decimal probabilities to percent
chances = [c * 100 for c in chances]

# graph
fig = plt.figure(figsize=(7.2, 4.05))
plt.plot(questions_completed, chances, 'r-')
plt.title('Chance of Success Assuming n Completed out of 35')
plt.xlabel('Questions Completed (n)')
plt.ylabel('% Chance')
plt.grid(True)
plt.show()

# notice even with 20 questions complete there is ~95% chance of failure
# (ie) only ~5% chance of all 5 randomly selected numbers being among the 20
