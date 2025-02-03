# Student Data Analysis

This application analyzes student data to determine the highest scorers in different subjects (Maths, Science, and Social). The script takes a list of students with their respective scores and finds the highest scorer in each subject.

## Prerequisites

- Python 3.x

## Usage

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the script:**
   ```bash
   python student_data_analysis.py
   ```

   The script will calculate and print the highest scorers in Maths, Science, and Social.

## Example

Here's an example list of students and their scores:

```python
student_1 = {'Name':'Tanmay', 'Maths': 50, "Science": 60, 'Social': 66}
student_2 = {'Name':'Dheeraj', 'Maths': 47, "Science": 87, 'Social': 58}
student_3 = {'Name':'Sooraj', 'Maths': 56, "Science": 45, 'Social': 67}
student_list = [student_1, student_2, student_3]
```

## How It Works

1. **Student List:** 
   A list of dictionaries containing the names and scores of students in Maths, Science, and Social.

2. **Calculating Highest Scores:**
   The script has three functions:
   - `calcualte_highest_in_maths(student_list)` calculates the highest scorer in Maths.
   - `calcualte_highest_in_science(student_list)` calculates the highest scorer in Science.
   - `calcualte_highest_in_social(student_list)` calculates the highest scorer in Social.

   Each function iterates through the student list, checks the scores, and determines the highest scorer in the respective subject.

3. **Output:**
   The script prints the highest scorer's name and their score in each subject.

## Disclaimer

This script is for educational purposes only. Ensure data privacy and proper handling of student data when using this script.

## License

This project is licensed under the MIT License.
