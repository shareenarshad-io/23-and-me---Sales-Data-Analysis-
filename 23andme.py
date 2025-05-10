'''
Please answer the questions below based on the data provided:
'''
# import libraries 
import pandas as pd
import matplotlib.pyplot as plt 
import glob
#Plot daily sales for all 50 weeks.

# assign a constant figure size and use it in plotting to make plots larger
FIG_SIZE = (8,6)

# get all filenames under the data directory 
l = [pd.read_csv(filename) for filename in glob.glob("/Users/shareenarshad/Desktop/datasets/datasets-4/*.csv")]

# check the list size to understand how many files will be read
# should be equal to 50
print(len(l))

#  create the dataset using all files under the data directory
df = pd.concat(l, axis=0)
print(df.head())

#To extract the sale day (year - month - day) from a complete timestamp (year - month - day hour-second-millisecond) we need to convert the column datatype to DateTime. Pandas library provides several functions to conveniently manipulate timestamps.

sale_day = pd.to_datetime(df['sale_time'])

daily_sales_df = sale_day.groupby(sale_day.dt.floor('d')).size().reset_index(name='sales_amount')
daily_sales_df.rename(columns={'sale_time':'sale_day'},inplace=True)
daily_sales_df.head()

#  to use index in plotting make sale_day index
daily_sales_df.index = daily_sales_df['sale_day']
daily_sales_df.drop(columns=['sale_day'], inplace=True)

#  plot daily sales for all 50 weeks
daily_sales_df.plot(figsize=FIG_SIZE, title = "Daily sales over 50 weeks")
plt.show()

#It looks like there has been a sudden change in daily sales. What date did it occur?





#Is the change in daily sales at the date you selected statistically significant? If so, what is the p-value?
#Does the data suggest that the change in daily sales is due to a shift in the proportion of male-vs-female customers? Please use plots to support your answer (a rigorous statistical analysis is not necessary).
#Assume a given day is divided into four dayparts: night (12:00AM - 6:00AM), morning (6:00AM - 12:00PM), afternoon (12:00PM - 6:00PM) and evening (6:00PM - 12:00AM). What is the percentage of sales in each daypart over all 50 weeks?
