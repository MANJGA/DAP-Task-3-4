Earthquake Data Analysis
Project Overview
This project analyzes the "Significant Earthquakes 1965-2016" database. The dataset includes details about various earthquakes that have occurred, such as date, time, location, magnitude, and more. The aim is to clean, categorize, reshape, visualize, and extract insights from the earthquake data.

Description of Tasks
Task 1: Data Cleaning
The dataset is first cleaned by splitting the datetime column into separate date and time columns, dropping unnecessary columns, and filling missing values with appropriate measures such as the median or mean.

Task 2: Categorization
The Magnitude column is categorized into 'Low', 'Medium', and 'High' using the cut() function to simplify the analysis of earthquake magnitudes.

Task 3: Data Reshaping
Data is reshaped using the melt() and pivot_table() functions from Pandas to transform the dataset into more analyzable forms.

Task 4: Data Visualization
Four different types of charts are constructed to visualize the data:

A line chart for the magnitude of earthquakes over time.
A bar chart showing the frequency of different magnitude categories.
A scatter chart for earthquake coordinates.
A pie chart representing the distribution of earthquake types.
Task 5: Date Functions
Functions and transformations that work with dates are used to extract the year and month from the date column, and to resample the data to get the number of earthquakes each year.

Technologies Used
Python: The main programming language used for the project.
Pandas: A Python library used for data manipulation and analysis.
Matplotlib: A Python library used for creating static, animated, and interactive visualizations.
Seaborn: A Python visualization library based on matplotlib that provides a high-level interface for drawing attractive statistical graphics.
