Certainly! Below is a simple Python script for a command-line tool called `data-cleaner-cli`. This tool can automate basic steps of data cleansing and preprocessing such as handling missing values, removing duplicates, and encoding categorical variables. It uses the `pandas` library, so you need to ensure that `pandas` is installed in your Python environment.

Here's the script:

```python
import pandas as pd
import argparse
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Load data from a CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Successfully loaded data from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        sys.exit(1)

def handle_missing_values(df, strategy='drop', fill_value=None):
    """
    Handle missing values in the dataset.
    strategy: 'drop', 'fill' - drop missing or fill with specific value.
    fill_value: Value to fill missing data with if strategy is 'fill'.
    """
    if strategy not in ['drop', 'fill']:
        logging.error("Invalid strategy for handling missing values. Choose 'drop' or 'fill'.")
        sys.exit(1)
    
    try:
        if strategy == 'drop':
            df = df.dropna()
            logging.info("Dropped missing values")
        elif strategy == 'fill':
            if fill_value is None:
                logging.error("No fill_value provided while strategy is 'fill'.")
                sys.exit(1)
            df = df.fillna(fill_value)
            logging.info("Filled missing values")
    except Exception as e:
        logging.error(f"Error handling missing values: {e}")
        sys.exit(1)
    
    return df

def remove_duplicates(df):
    """
    Remove duplicate rows from the dataset.
    """
    try:
        df = df.drop_duplicates()
        logging.info("Removed duplicate rows")
    except Exception as e:
        logging.error(f"Error removing duplicates: {e}")
        sys.exit(1)
    
    return df

def encode_categorical(df):
    """
    Encode categorical features using one-hot encoding.
    """
    try:
        df = pd.get_dummies(df, drop_first=True)
        logging.info("Encoded categorical variables")
    except Exception as e:
        logging.error(f"Error encoding categorical variables: {e}")
        sys.exit(1)
    
    return df

def save_data(df, file_path):
    """
    Save the processed dataset to a CSV file.
    """
    try:
        df.to_csv(file_path, index=False)
        logging.info(f"Successfully saved processed data to {file_path}")
    except Exception as e:
        logging.error(f"Error saving data: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Data Cleaner CLI')
    parser.add_argument('input_file', help='Path to input CSV file')
    parser.add_argument('output_file', help='Path to output CSV file')
    parser.add_argument('--missing_strategy', choices=['drop', 'fill'], default='drop', help='Strategy to handle missing values')
    parser.add_argument('--fill_value', type=str, default=None, help='Fill value if missing_strategy is set to fill')
    
    args = parser.parse_args()
    
    # Load data
    df = load_data(args.input_file)
    
    # Handle missing values
    df = handle_missing_values(df, strategy=args.missing_strategy, fill_value=args.fill_value)
    
    # Remove duplicates
    df = remove_duplicates(df)
    
    # Encode categorical variables
    df = encode_categorical(df)
    
    # Save processed data
    save_data(df, args.output_file)
    
if __name__ == '__main__':
    main()
```

### Instructions to run the script:

1. **Install Required Packages**: Make sure you have `pandas` installed. If not, you can install it using `pip`:
   ```bash
   pip install pandas
   ```

2. **Run the Script**:
   You can run the script from the command line. Below is an example of how to use the tool:

   ```bash
   python data_cleaner_cli.py input.csv output.csv --missing_strategy fill --fill_value 0
   ```

   This command will load `input.csv`, fill missing values with `0`, remove duplicate rows, encode categorical variables, and save the cleaned data to `output.csv`.

### What the Script Does:

- Loads data from a CSV file.
- Handles missing values using chosen strategy.
- Removes duplicate rows.
- Encodes categorical variables using one-hot encoding.
- Saves the cleaned data to a new CSV file.
- Provides error handling and logging for each step to ensure the process is straightforward and provides useful feedback.