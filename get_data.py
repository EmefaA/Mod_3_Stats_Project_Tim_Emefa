#import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats

# get data and small data cleaning
df = pd.read_csv('athlete_events.csv')
df2 = pd.read_csv('noc_regions.csv')
df = df.merge(df2, on = 'NOC')
new_df = df.dropna(subset = ['Age', 'Height', 'Weight'])

# separate out the women from the men
all_women = new_df[new_df['Sex'] == 'F'].copy()

#get BMI's of women
all_women['Height(m)'] = all_women['Height'].map(lambda x: x/100)
all_women['BMI'] = (all_women['Weight']/(all_women['Height(m)']**2)).round(1)

#select all the ladies from 1996
all_women_1996 = all_women[all_women['Year'] == 1996]

#select all the ladies from 2016
all_women_2016 = all_women[all_women['Year'] == 2016]

#Z-testing analysis for question 1

#mean and std of BMI
pop_mean_1996_bmi = all_women_1996['BMI'].mean()
pop_std_1996_bmi = all_women_1996['BMI'].std()

# Taking sample of year 2016 for comparison
sample_of_all_women_2016_bmi = all_women_2016['BMI'].sample(n=30)
sample_of_all_women_2016_mean_bmi = np.mean(sample_of_all_women_2016_bmi)
sample_of_all_women_2016_se_bmi = pop_std_1996_bmi/np.sqrt(len(sample_of_all_women_2016_bmi))

#mean of population and sample
pop_mean_1996_bmi
sample_of_all_women_2016_mean_bmi

#results
z1 = (sample_of_all_women_2016_mean_bmi - pop_mean_1996_bmi)/sample_of_all_women_2016_se_bmi
p1 = 1 - stats.norm.sf(z1)

#Z-testing analysis for question 2

#mean and std of Age
pop_mean_1996_age = all_women_1996['Age'].mean()
pop_std_1996_age = all_women_1996['Age'].std()

# Taking sample of year 2016 for comparison
sample_of_all_women_2016_age = all_women_2016['Age'].sample(n=30)
sample_of_all_women_2016_mean_age = np.mean(sample_of_all_women_2016_age)
sample_of_all_women_2016_se_age = pop_std_1996_age/np.sqrt(len(sample_of_all_women_2016_age))

#mean of population and sample
pop_mean_1996_age
sample_of_all_women_2016_mean_age 

#results
z2 = (sample_of_all_women_2016_mean_age - pop_mean_1996_age)/sample_of_all_women_2016_se_age
p2 = 1 - stats.norm.sf(z2)

