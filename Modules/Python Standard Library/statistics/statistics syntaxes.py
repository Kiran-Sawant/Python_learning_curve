import statistics as stat
import xlwings as xl

# Getting data from excel file
book = xl.Book('dor.xlsx')
qqq = book.sheets('QQQ')

open2open = qqq.range('F10:F974').options().value
# print(open2open)

#________________Statistical operations___________________#
# mean() returns the arithmetic mean of data
print(f'mean(): {stat.mean(open2open) * 100:.3f}%')
print(f"harmonic mean: {stat.harmonic_mean(range(0, 100)) * 100:.3f}%\n")

# median() returns the middle value of the data
print(f"median(): {stat.median(open2open) * 100:.3f}%")
# median_grouped() returns the 50th percentile of data
print(f"Grouped median: {stat.median_grouped(open2open) * 100:.3f}%")
# median_high() returns the high median of data
print(f"High Median: {stat.median_high(open2open) * 100:.3f}%")
# median_low() returns the low median of data
print(f"Low median: {stat.median_high(open2open) * 100:.3f}%\n")

# mode() returns the most commonly occuring value in the data
print(f"mode(): {stat.mode(open2open) * 100:.3f}%\n")

# stddev() returns the standard deviation of sample
print(f"standard deviation: {stat.stdev(open2open) * 100:.3f}%")
# pstddev() returns the standard deviation of the population
print(f"Population stddev(): {stat.pstdev(open2open) * 100:.3f}%\n")

# variance() returns the sample varience
print(f"Sample Variance: {stat.variance(open2open) * 100:.3f}%")
# pvarience() returns the varience of population
print(f"Population Variance{stat.pvariance(open2open) * 100:.3f}%")
