import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    mask = df["sex"] == "Male"
    average_age_men = round(df[mask]["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    mask = df["education"] == "Bachelors"
    percentage_bachelors = round(df[mask]["education"].value_counts() / df["education"].value_counts().sum() * 100, 1)[0]

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    education = ["Bachelors", "Masters", "Doctorate"]

    higher_education = df[df.education.isin(education) == True]
    lower_education = df[df.education.isin(education) == False]

    # percentage with salary >50K
    higher_education_rich = round(higher_education["salary"].str.contains(">").sum() / len(higher_education.index) * 100, 1)
    lower_education_rich = round(lower_education["salary"].str.contains(">").sum() / len(lower_education.index) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df["hours-per-week"] == df["hours-per-week"].min()].index)
    num_min_workers_rich = df[df["hours-per-week"] == df["hours-per-week"].min()]["salary"].str.contains(">").sum()

    rich_percentage = num_min_workers_rich / num_min_workers * 100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_countries =  df[df["salary"].str.contains(">50")]["native-country"].value_counts()
    totals_by_country = df["native-country"].value_counts()
    percentage_rich_by_country = (round(highest_earning_countries / totals_by_country * 100, 1)).sort_values(ascending=False)
    highest_earning_country = percentage_rich_by_country.index[0]
    highest_earning_country_percentage = percentage_rich_by_country[0]

    # Identify the most popular occupation for those who earn >50K in India.
    mask_1 = df["native-country"] == "India"
    mask_2 = df["salary"].str.contains(">50")

    rich_indians = df[mask_1 & mask_2]
    top_IN_occupation = rich_indians["occupation"].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
