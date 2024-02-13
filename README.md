# project1# Branch Usage Guide

Before diving into the specific files, please note that it's crucial to start the files in the order outlined below. The scripts sequentially gather data through API calls, and some processes may take longer to complete due to the volume of data being processed. Following the specified order ensures that the data flows correctly through each preparation and analysis stage.

## Getting Started

To use these files effectively, start with `geting_data.ipynb` to pull and initially prepare your dataset. Make sure you have created a `Resources` folder in your project directory before running the notebook. This folder will be used to store intermediate and final data files.

After preparing your initial dataset, proceed with `prepdata_ofns_desc.ipynb` to clean your data with a specific focus on offense types and reporting times. The cleaned data will be crucial for the analysis phase.

Finally, use `ofns_data_analysis.ipynb` to analyze the cleaned data, focusing on identifying the most common offenses and preparing them for further predictive modeling.

By following these steps, you'll be well on your way to uncovering insights from the crime data and preparing it for comprehensive analysis and modeling.

## Overview of Files

### 1. `geting_data.ipynb`

**Purpose:** Initial data preparation and understanding.

**Steps:**
- Pulls 20,000 rows from the database using an API to help us understand the data's structure and contents.
- Creates a list from the values in the `ofns_desc` column, which describes the types of offenses.
- Implements a loop to send a series of API queries for each offense type listed in `ofns_desc`.
- Choose group of columns necessery for futur research
- Saves the query results into a CSV file for further analysis.

**Output:** `Resources/final_df.csv`  
**Note:** Ensure you have a `Resources` folder in your project directory to store the output file.

### 2. `prepdata_ofns_desc.ipynb`

**Purpose:** Further cleaning of the initially prepared data with a focus on offense types and reported times.

**Process:**
- Cleans the previously created `final_df.csv`, focusing on the `ofns_desc` column (offense descriptions) and the time each crime was reported.
- The cleaned data is then saved for further analysis.

**Output:** `Resources/cleaned_crime_data.csv`  
This file serves as the cleaned dataset, ready for in-depth analysis.

### 3. `ofns_data_analysis.ipynb`

**Purpose:** Analysis of the most common offenses and preparation for modeling.

**Analysis:**
- Loads the `cleaned_crime_data.csv` file for analysis.
- Identifies the top 10 most common criminal offenses within the dataset.
- Prepares the identified data for predictive modeling using the Prophet model.

**Output:** This file readies the top 10 offenses for future modeling, aiding in understanding trends and potentially forecasting crime rates.

