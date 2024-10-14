# AutoMPG_DataProcessing
Object-Oriented Data Processing Framework for the UCI AutoMPG Dataset


## Project Overview

**Date:** 23 Jan. 2024 - 31 Jan. 2024  
**Author:** Michelle Zong
This project involves creating an object-oriented framework in Python to process and analyze fuel efficiency data from the UCI AutoMPG dataset. The focus of the project is to apply object-oriented programming (OOP) principles to clean, transform, and analyze the dataset efficiently.


## Key Features

- **Object-Oriented Design**: The project is structured around Python classes that encapsulate the data processing logic and methods for efficient data manipulation.
- **Data Parsing and Cleaning**: Handles non-standard delimiters and missing values in the dataset. Implements flexible data ingestion and transformation methods.
- **Iterable Data Structures**: Built custom iterable data structures to process the dataset in a memory-efficient manner, allowing for easy exploration and analysis of the dataset.
- **Data Comparison**: Allows data comparison between two AutoMPG objects such as equality and less than comparisons based on vehicle features (e.g., year, mpg).


## Dataset

- **Source**: [UCI Machine Learning Repository - AutoMPG Dataset](https://archive.ics.uci.edu/ml/datasets/Auto+MPG)
- **Description**: This dataset contains various characteristics of different cars from the 1970s and 1980s, including attributes such as MPG (miles per gallon), cylinders, horsepower, weight, etc.
- **Handling Missing Data**: The dataset includes missing values in some columns (e.g., horsepower). These values were cleaned using techniques such as imputation or removal based on analysis requirements.

## Project Structure
*** Edit project structure

├── README.md                 # Project documentation
├── data/                     # Raw and processed datasets
│   ├── auto-mpg.data.txt     # Original dataset
│   └── auto-mpg.clean.txt    # Standardized dataset
├── src/                      # Source code for data processing
│   ├── autompg.py            # Main script to run the analysis
│   └── __init__.py
└── tests/                    # Unit tests for the framework
    └── test_mpg.py           # Test cases for MPG data processing


## Classes

### 1. AutoMPG  
- **Responsibilities**: represents make, model, year, and mpg attributes for each record in the data set. 
- **Methods**:
  -  `__repr__()`: Outputs an unambiguous representation of the class object; for developers.
   - `__str__()`: Human-readable representation of class object; for end-users. 
   - `__eq__()`: Evaluates whether 2 AutoMPG instances are equivalent based on make, model, year, and mpg
   - `__lt__()`: Evaluates whether an AutoMPG instance is less than the other based on make, model, year, and mpg
   - `__hash__()`: Makes class hashable again after defining __eq__ method

### 2. AutoMPGData  
- **Responsibilities**: An iterable class that will read in the data file, clean it, and generate a list of AutoMPG objects.
- **Methods**:
  - `__iter__()`: makes class iterable
  - `_load_data()`: Reads in the cleaned data file, and populates self.data with AutoMPG 
    objects.
  - `_clean_data()`: Reads in messy data, standardizes data rows and stores the cleaned 
    data in auto_mpg.clean.txt. 


## How to Run

1. **Fork the Repository**:
*** check correct URL
   ```bash
   git fork https://github.com/yourusername/auto-mpg-data-processing.git
   ```

2. **Run the Project**:
   ```bash
    python src/autompg.py
   ```
