# Topsis-Anoushka-102203560
The TOPSIS package is a robust Python library designed to simplify the implementation of the TOPSIS multi-criteria decision-making method. This technique is widely used to rank and select alternatives by comparing them to an ideal solution. 
 It reads data from a CSV file, applies the TOPSIS algorithm, and saves the results to another CSV file.

## Example Usage

pip install topsis-anoushka-102203560

python -m topsis <input_file.csv> <weights> <impacts> <result_file.csv>

## Parameters

### `input_file`
- **Description**: name of the input CSV file.  
- **Requirements**:  
  - The file must contain at least 3 columns: one for alternatives and at least two for criteria.  
  - The first column is treated as the identifiers of the alternatives.

### `weights`
- **Description**: A comma-separated string of numeric weights corresponding to the criteria columns.  
- **Purpose**: Weights determine the importance of each criterion.

### `impacts`
- **Description**: A comma-separated string of impacts (`+` or `-`) for each criterion.  
- **Details**:  
  - `+` indicates a criterion is **beneficial** (higher values are better).  
  - `-` indicates a criterion is **non-beneficial** (lower values are better).

### `result_file`
- **Description**: name of the CSV file where the results will be saved.  
- **Output**:  
  - The output file includes the original data, a `"Topsis Score"` column, and a `"Rank"` column.


The link to the package on pypi:
https://pypi.org/project/Topsis-Anoushka-102203560/1.0.0/
