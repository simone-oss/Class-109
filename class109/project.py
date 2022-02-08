import pandas as pd
import statistics
import csv
df = pd.read_csv("project.csv")
reading_list = df["reading score"].to_list()
#Mean for reading and Weight
reading_mean = statistics.mean(reading_list)
#Median for reading and weight
reading_median = statistics.median(reading_list)
#Mode for reading and weight
reading_mode = statistics.mode(reading_list)
#Printing mean, median and mode to validate
print("Mean, Median and Mode of reading is {}, {} and {} respectively".format(reading_mean, reading_median, reading_mode))
print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(weight_mean, weight_median, weight_mode))
#Standard deviation for reading and weight
reading_std_deviation = statistics.stdev(reading_list)
#1, 2 and 3 Standard Deviations for reading
reading_first_std_deviation_start, reading_first_std_deviation_end = reading_mean-reading_std_deviation, reading_mean+reading_std_deviation
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_mean-(2*reading_std_deviation), reading_mean+(2*reading_std_deviation)
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_mean-(3*reading_std_deviation), reading_mean+(3*reading_std_deviation)
#1, 2 and 3 Standard Deviations for weight
#Percentage of data within 1, 2 and 3 Standard Deviations for reading
reading_list_of_data_within_1_std_deviation = [result for result in reading_list if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end]
reading_list_of_data_within_2_std_deviation = [result for result in reading_list if result > reading_second_std_deviation_start and result < reading_second_std_deviation_end]
reading_list_of_data_within_3_std_deviation = [result for result in reading_list if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end]
#Percentage of data within 1, 2 and 3 Standard Deviations for Weightend]
#Printing data for reading and weight (Standard Deviation)
print("{}% of data for reading lies within 1 standard deviation".format(len(reading_list_of_data_within_1_std_deviation)*100.0/len(reading_list)))
print("{}% of data for reading lies within 2 standard deviations".format(len(reading_list_of_data_within_2_std_deviation)*100.0/len(reading_list)))
print("{}% of data for reading lies within 3 standard deviations".format(len(reading_list_of_data_within_3_std_deviation)*100.0/len(reading_list)))
