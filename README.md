# Data_Acquisition-Wrangling- 

This project showcases a comprehensive data analysis project conducted in Python using Pandas, NumPy, and Seaborn libraries. The project follows a structured approach starting from data acquisition, data exploration, data cleaning, to data wrangling.
Data Acquisition: The project begins by loading multiple datasets using Pandas read_excel function. Each dataset is then printed to inspect its structure and content.
Data Exploration: Basic exploratory data analysis (EDA) techniques are employed to understand the datasets better. This includes printing the first few and last few entries, getting data type information, generating descriptive statistics, and identifying missing values using info(), head(), tail(), describe(), and isnull().sum().
Data Cleaning: Missing values are addressed through various techniques such as filling them with mean, median, or mode values using fillna() function. Outliers are detected using box plots and the interquartile range (IQR) method, and then removed from the dataset.
Data Wrangling: The datasets are combined using the merge() function and concatenated using concat() function. Necessary columns are dropped, and the combined dataset is prepared for further analysis.
Summary Statistics and Visualization: Summary statistics such as mean, median, mode, skewness, and correlation coefficients are calculated to gain insights into the data distribution and relationships between variables. Seaborn box plots are used to visualize outliers in numerical features.
Data Export: The cleaned and processed dataset is exported to a CSV file for further analysis or modeling.
