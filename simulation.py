import numpy as np
import pandas as pd

#1.  How likely is it that you roll doubles when rolling two dice?
n_trials = nrows = 100_000
n_dice = ncols = 2
rolls = np.random.choice([1,2,3,4,5,6], n_trials * n_dice).reshape(nrows, ncols)

(pd.DataFrame(rolls)
    .apply(lambda row: row.values[0] == row.values[1], axis=1)
    .mean())

#2. If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?
n_trials = nrows = 100_000
n_coins = ncols = 8
flips = np.random.choice([0,1], n_trials * n_coins).reshape(nrows, ncols)

heads_in_flip = flips.sum(axis=1)
exactly_3_heads = heads_in_flip == 3
exactly_3_heads.mean()
greater_than_3_heads = heads_in_flip > 3
greater_than_3_heads.mean()

#3. There are approximitely 3 web development cohorts for every 1 data science 
# cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a 
# billboard, what are the odds that the two billboards I drive past both have 
# data science students on them?
n_trials = nrows = 100_000
n_bill = ncols = 2
cohort = np.random.choice([0,1],size= n_trials * n_bill, p=[.75, .25]).reshape(nrows, ncols)
billboards = cohort.sum(axis=1)
both_ds = billboards == 2
both_ds.mean()

#4. Codeup students buy, on average, 3 poptart packages with a standard deviation 
# of 1.5 a day from the snack vending machine. If on monday the machine is 
# restocked with 17 poptart packages, how likely is it that I will be able to 
# buy some poptarts on Friday afternoon? (Remember, if you have mean and 
# standard deviation, use the np.random.normal)
n_trials = n_rows = 100_000
n_days = 4 #Monday, Tuesday, Wednesday, Thursday
tarts = pd.DataFrame(np.random.normal(3, 1.5, n_trials * n_days).reshape(n_trials, n_days))
# tarts = np.random.normal(3, 1.5, size=(100_000, 4)).round()
# tarts = np.where(purhcases < 0, 0, purchases)
tarts_left = 17 - tarts.sum(axis=1) > 0
tarts_left.mean()

# Compare Heights
#5. Men have an average height of 178 cm and standard deviation of 8cm.
# Women have a mean of 170, sd = 6cm.
# Since you have means and standard deviations, you can use np.random.normal 
# to generate observations.
# If a man and woman are chosen at random, P(woman taller than man)?
n_trials = n_rows = 100_000
men = pd.DataFrame(np.random.normal(178, 8, n_trials), columns=['men'])
women = pd.DataFrame(np.random.normal(170, 6, n_trials), columns=['women'])
comparison = pd.concat([men,women], axis=1)
woman_taller = comparison['men'] < comparison['women']
woman_taller.mean()

#6. When installing anaconda on a student's computer, there's a 1 in 250 chance that 
# the download is corrupted and the installation fails. What are the odds that 
# after having 50 students download anaconda, no one has an installation issue? 
# 100 students?
n_trials = n_rows = 100_000
n_student = 50
corrupt = pd.DataFrame(np.random.randint(0, 251, size = n_trials * n_student).reshape(n_trials, n_student))
fails = corrupt.apply(lambda row: 250 in row.values, axis=1)
no_issue = 1 - fails.mean()
no_issue
n_student = 100
corrupt = pd.DataFrame(np.random.randint(0, 251, size = n_trials * n_student).reshape(n_trials, n_student))
fails = corrupt.apply(lambda row: 250 in row.values, axis=1)
no_issue = 1 - fails.mean()
no_issue
# What is the probability that we observe an installation issue within the 
# first 150 students that download anaconda?
n_student = 150
corrupt = pd.DataFrame(np.random.randint(0, 251, size = n_trials * n_student).reshape(n_trials, n_student))
fails = corrupt.apply(lambda row: 250 in row.values, axis=1)
fails.mean()
# How likely is it that 450 students all download anaconda without an issue?
n_student = 450
corrupt = pd.DataFrame(np.random.randint(0, 251, size = n_trials * n_student).reshape(n_trials, n_student))
fails = corrupt.apply(lambda row: 250 in row.values, axis=1)
no_one = 1 - fails.mean()
no_one

#7. There's a 70% chance on any given day that there will be at least one food 
# truck at Travis Park. However, you haven't seen a food truck there in 3 days. 
# How unlikely is this?
n_trials = nrows = 100_000
n_days = ncols = 3
at_least_one = np.random.choice([0, 1], size = n_trials * n_days, p=[.3, .7]).reshape(nrows, ncols)
none_in_three = at_least_one.sum(axis=1) == 0
none_in_three.mean()

# How likely is it that a food truck will show up sometime this week?
n_days = ncols = 7
at_least_one = np.random.choice([0, 1], size = n_trials * n_days, p=[.3, .7]).reshape(nrows, ncols)
at_least_once = at_least_one.sum(axis=1) > 0
at_least_once.mean()

#8. If 23 people are in the same room, what are the odds that two of them 
# share a birthday? What if it's 20 people? 40?
n_trials = nrows = 100_000
n_people = ncols = 23
birthdays = pd.DataFrame(np.random.randint(1, 366, size= n_trials * n_people).reshape(n_trials, n_people))
uniques = birthdays.nunique(axis=1)
same = (uniques < n_people).mean()
same
n_people = 20
birthdays = pd.DataFrame(np.random.randint(1, 366, size= n_trials * n_people).reshape(n_trials, n_people))
uniques = birthdays.nunique(axis=1)
same = (uniques < n_people).mean()
same
n_people = 40
birthdays = pd.DataFrame(np.random.randint(1, 366, size= n_trials * n_people).reshape(n_trials, n_people))
uniques = birthdays.nunique(axis=1)
same = (uniques < n_people).mean()
same