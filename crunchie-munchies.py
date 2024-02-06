import codecademylib
import numpy as np
calorie_stats = np.genfromtxt("cereal.csv", delimiter=",")
# how much higher is the average calorie count of your competition
average_calories = np.mean(calorie_stats)
print(average_calories)

# checking if he average calorie count adequately reflect the distribution of the dataset
calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

#calculating the median
median_calories = np.median(calorie_stats)
print(median_calories)
# calculating different percentiles and print them to the terminal until I find the lowest percentile that is greater than 60 calories
percentile = np.percentile(calorie_stats, 4)
print(percentile)
# calculating the percentage of cereals that have more than 60 calories per serving
more_calories = np.mean(calorie_stats > 60)
print(more_calories)

# calculating the amount of variation (standard deviation)
calorie_std = np.std(calorie_stats)
print(calorie_std)

# calculating different percentiles and print them to the terminal until I find the lowest percentile that is greater than 60 calories
