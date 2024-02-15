# project1 Usage Guide

Before diving into the specific files, please note that it's crucial to start the files in the order outlined below. The scripts sequentially gather data through API calls, and some processes may take longer to complete due to the volume of data being processed. Following the specified order ensures that the data flows correctly through each preparation and analysis stage.

## Getting Started

To use these files effectively, start with `geting_data.ipynb` to pull and initially prepare your dataset. Make sure you have created a `Resources` folder in your project directory before running the notebook. This folder will be used to store intermediate and final data files.

After preparing your initial dataset, proceed with `prepdata_ofns_desc.ipynb` to clean your data with a specific focus on offense types and reporting times. The cleaned data will be crucial for the analysis phase.


Finally, use any of files from Data_Analysis folder to analyze the cleaned data, focusing on identifying the most common offenses and preparing them for further predictive modeling.

By following these steps, you'll be well on your way to uncovering insights from the crime data and preparing it for comprehensive analysis and modeling.

## Overview of Files

### 1. `Data_Prep/geting_data.ipynb`

**Purpose:** Initial data preparation and understanding.

**Steps:**
- Pulls 20,000 rows from the database using an API to help us understand the data's structure and contents.
- Creates a list from the values in the `ofns_desc` column, which describes the types of offenses.
- Implements a loop to send a series of API queries for each offense type listed in `ofns_desc`.
- Choose group of columns necessery for futur research
- Saves the query results into a CSV file for further analysis.

**Output:** `Resources/final_df.csv`  
**Note:** Ensure you have a `Resources` folder in your project directory to store the output file.

### 2. `Data_Prep/prepdata_ofns_desc.ipynb`

**Purpose:** Further cleaning of the initially prepared data with a focus on offense types and reported times.

**Process:**
- Cleans the previously created `final_df.csv`, focusing on the `ofns_desc` column (offense descriptions) and the time each crime was reported.
- The cleaned data is then saved for further analysis.

**Output:** `Resources/cleaned_crime_data.csv` and  `Resources/extended_nypd_crime_data.csv` 
This file serves as the cleaned datasets, ready for in-depth analysis.

**Important Note!!!**
- Due to the fact that some research was done on similarly organized datasets and to avoid errors occurring during code execution, we will create two files in the Resource folder. 

### 3. `Data_Analysis/ofns_data_analysis.ipynb`

**Purpose:** Analysis of the most common offenses and preparation for modeling.

**Analysis:**
- Loads the `cleaned_crime_data.csv` file for analysis.
- Identifies the top 10 most common criminal offenses within the dataset.
- Prepares the identified data for next researches.

**Output:** This file readies the top 10 offenses for future modeling, aiding in understanding trends and potentially forecasting crime rates.  


### 4. `Data_Analysis/jake-prophet.ipynb`  

**Purpose:** Deep analysis of time-based crime data  

**Analysis:**  
- Loads the `extended_nypd_crime_data.csv` file into a dataframe
- Average Number of Crimes Per Month: Visualizes the monthly crime trends to identify any seasonal patterns.
- Average Number of Crimes Per Day of the Month: Helps in understanding if crimes are more frequent on specific days of the month.
- Average Number of Crimes Per Day of the Week: Analyzes weekly patterns to find out on which days crimes are more commonly reported.
- The Most Common Crime on Each Day of the Week: Identifies which types of crimes are most frequent on specific days.
- Crime Rates Based on Time of Day: Examines how crime rates vary throughout the day.
- Forecasting with Prophet: Utilizes the Prophet library to project crime rates for 2023 and analyze seasonality effects.

**Output:** Multiple graphs, dataframes, and other visualizations of the data as outlined in the Analysis.  

### 5. `Data_Analysis/10_most_common_criminal_offenses.ipynb`  

**Purpose:** Display top 10 Crime and analysis of picks  

**Analysis:**  
- Loads the `cleaned_crime_data.csv` file into a dataframe
- During the investigation of the 10 most frequent criminal cases, we noticed that CRIMINAL MISCHIEF & RELATED OF is in fourth place in terms of the number of reported cases, dominating the chart due to the pronounced peaks. Further analysis showed that there is a correlation with holidays for the highest peaks.

**Output:** Multiple graphs, dataframes, and other visualizations of the data as outlined in the Analysis.  

### 6. `Data_Analysis/crime_per_yeares.ipynb`  

**Purpose:** Display number of cases by year and trend  

**Analysis:**  
- Loads the `extended_nypd_crime_data` file into a dataframe
- A linear regression analysis on a dataset of yearly cases, converting years to numeric format, calculating regression parameters, and visualizing the trend line alongside actual case counts. 

**Output:** `Output/annual_number_of_cases_and_trend_line.png`

### 7. `Data_Analysis/trendiness.ipynb`  

**Purpose:** The trendiness of changes in criminal activities varies between different types of crime.  

**Analysis:**  
- Loads the `cleaned_crime_data.csv` file into a dataframe
- From this dataset, we can conclude that the trendiness of crime change varies across different types of crime. Positive trendiness values indicate an increase in criminal activities over time for certain crime types, while negative trendiness values suggest a decrease. These insights are crucial for policymaking and law enforcement strategies to prioritize resources effectively. 

**Output:** `Output/trendiness_of_crime_change_over_time_for_each_type_of_crime.png`
            `Output/the_overall_trendiness_of_crime_cases_over_the_years.png`

### 8. `burrough_data.ipynb`  

**Purpose:** Analysis of criminal activities by district.  

**Analysis:**  
- Loads the `extended_nypd_crime_data.csv` file into a dataframe
- By analyzing this data set, we tried to track criminal activities by Boroughs over time. This script groups the data by borough and calculates the average number of crimes reported per year for each borough.

### 9. `YearlyStats.ipynb`  

**Purpose:** Review how crime rates correlate with the time of year.  

**Analysis:**  
- Loads the `extended_nypd_crime_data.csv` file into a dataframe
- By analyzing this data set, we tried to review how crime rates correlate with the time of year..

### 10. `selektor.ipynb`  

**Purpose:** This Python code creates a user interface in Jupyter Notebook using ipywidgets to select from a list of available notebooks and then execute the chosen notebook when a button is clicked. The `run_notebook()` function defines a custom line magic command to run Jupyter notebooks using `%run`, allowing seamless integration and execution of notebooks within the Jupyter environment.

### 11. `main.py`  

**Purpose:** This Python file should be a dashboard for viewing the results that we have reached through previous analyses, but at the moment it leads the user to the powerpoint presentation of this project.


