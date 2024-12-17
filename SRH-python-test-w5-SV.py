# Big Data Programming: Pyhton Module Test
# Instructions ...
# Please consider good style & naming while developing the code when necessary,
#  such as Docstring, linting, etc. it is considered in the grading process!
# Use this file for the solution only. Jupyter notebook(.ipynb) not acceptable!
# Push the solution to a remote repo of name "SRH-Python-Test", and send me the link of the repo as DM
#  on Ms Teams for assessment.
# The duration of this test is 1 hour.

# Q1: What is the main difference between the list and Tuple?
# Tuple:
# A tuple is an ordered, immutable objects
# Immutable means that once a tuple is created, you cannot
#List:
#List are mutable objects
#list syntax uses square brackets.

# Q2: why should list indexing be used Python?
#The index() function is a powerful tool in Python as it simplifies the process of finding the index of an element in a sequence, eliminating the need for writing loops or conditional statements. This function is especially useful when working with large datasets or complex structures, where manual searching could be time-consuming and error-prone.


# Q3: You have two lists (string_list, values_list) below. Write a function of
#  a name count_car. The function returns a dictionary.
#  The expected return of the function should print out this dictionary:
#  {'Audi_Q5': 2, 'Honda_civic': 4, 'Mercedes_200E': 5, 'BMW_720': 7, 'VW_passat': 2}
string_list = ['Audi_Q5', 'Honda_civic', 'Mercedes_200E', 'Honda_civic',
               'BMW_720', 'VW_passat']

value_list = [2, 4, 5, 7, 2]

# Your code here ...


# Q4: Write a function of a name double_even_numbers. The function squares the
#  even numbers only. Also, the function leaves the first element of the input
#  as is without getting squared regardless being even or odd number.
#  The function has one argument which is a numpy array of 100 elements of
#  integer type between 0-10.
#  The function returns an array. Use list comprehension in your answer.

# Your code here ...


# Q5: Read "movies.csv" file, a file is provided. Create a function
#  returns only table of elements before 2000 with score 7 and above, then save
#  the elements in a new csv file with a name "dest_csv". 

def filter_and_save_csv(file_path, output_path='dest_csv.csv'):
    try:
        # Step 1: Read the CSV file
        df = pd.read_csv('movies.csv')
        
        # Step 2: Filter movies before 2000 with score >= 7
        filtered_df = df[(df['year'] < 2000) & (df['score'] >= 7)]
        
        # Step 3: Save the filtered DataFrame to a new CSV file
        filtered_df.to_csv(output_path, index=False)
        
        print(f"Filtered CSV file saved as '{output_path}'")
        return filtered_df
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Use your specific file path
file_path = r'C:\Users\franc\OneDrive\Desktop\Big Data\New folder\movies.csv'
output_path = r'C:\Users\franc\OneDrive\Desktop\Big Data\New folder\dest_csv.csv'

# Call the function
filter_and_save_csv(file_path, output_path)


# Q6: Write a function of a name div_func. It returns the divsion of elements
#  in a list in reversed order. The function should pass the two lists below
#  without errors.

import random
random.seed(42)
short_list = [1, 0, 2, 2, 20]
long_list = [random.randrange(0, 10, 1) for i in range(15)]

# Your code here ...
