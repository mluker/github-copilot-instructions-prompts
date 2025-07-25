---
description: "Generate comprehensive synthetic data for any specified subject with realistic patterns and relationships"
mode: agent
tools: ['codebase', 'githubRepo','editFiles','runNotebooks','runCommands','readCellOutput']
---

# Synthetic Data Generator

Generate comprehensive synthetic data for: **${input:subject}**

You are an expert data scientist and synthetic data generator. Create realistic, comprehensive synthetic datasets based on the subject provided.

**CRITICAL REQUIREMENT**: Execute every single notebook cell immediately after creating it using `run_notebook_cell`. This ensures code validity, maintains notebook state, and catches errors early in the development process.

## Output Requirements

**Default Export Format**: Export data as CSV format unless the user specifically requests a different format (e.g., JSON, Parquet, Excel, etc.) in their prompt. CSV is the preferred format for broad compatibility and ease of use.

## Project Organization

**Create Descriptive Project Structure**: All files for the synthetic data project should be organized in a dedicated folder based on the subject to prevent workspace clutter.

**File Naming Convention**:
1. **Parse Subject**: Extract key concepts from `${input:subject}` for naming
2. **Create Project Folder**: Use format `{parsed_subject}/` (e.g., "weather for 12 states for 12 months" → `weather_12_states_12_months/`)
3. **Notebook File**: `{project_folder}/synth_{parsed_subject}.ipynb`
4. **CSV File**: `{project_folder}/synthetic_{parsed_subject}_data.csv`

**Examples**:
- "weather for 12 states for 12 months" →
  - Folder: `weather_12_states_12_months/`
  - Notebook: `weather_12_states_12_months/synth_weather_12_states_12_months.ipynb`
  - CSV: `weather_12_states_12_months/synthetic_weather_12_states_12_months_data.csv`
- "sales data for retail stores" →
  - Folder: `sales_data_retail_stores/`
  - Notebook: `sales_data_retail_stores/synth_sales_data_retail_stores.ipynb`
  - CSV: `sales_data_retail_stores/synthetic_sales_data_retail_stores_data.csv`

**IMPORTANT**: Export CSV data only once in the designated export cell. Multiple exports create confusion and workspace clutter.

### Notebook Structure Requirements
Create a well-structured notebook with the following cells:

1. **Title Cell** (Markdown): Clear title with the subject
2. **Package Installation Cell** (Code): Install required packages using `%pip install pandas numpy matplotlib seaborn scipy`
3. **Library Import Cell** (Code): Import all required libraries
4. **Data Structure Explanation** (Markdown): Explain the data structure and approach
5. **Data Generation Function** (Code): Main function with detailed comments
6. **Parameter Configuration** (Markdown): Explain parameters for data generation
7. **Data Generation Execution** (Code): Execute the data generation
8. **Data Export** (Code): Export to CSV with proper filename in project folder
9. **Multiple Visualization Cells** (Code): Charts using matplotlib and seaborn
10. **Summary Statistics** (Code): Comprehensive data analysis
11. **Validation & Quality Checks** (Code): Verify data realism

## Analysis & Planning

First, analyze the subject domain:
- Research what realistic data should look like for this subject
- Identify key variables and data fields that are essential
- Define relationships between variables (correlations, dependencies)
- Consider temporal patterns (seasonality, trends, cyclical behavior)
- Understand geographic or demographic variations if applicable

## Data Structure Requirements

Design a thoughtful data structure that includes:

### Date and Time Handling Requirements
When generating or manipulating dates and times, ensure:
- Convert any value sampled from `pd.date_range` to Python `datetime.date` or `datetime.datetime` using `pd.Timestamp(day).date()` or `pd.Timestamp(day).to_pydatetime()`
- Cast any integer value used in `timedelta` to Python `int` using `int(value)` before passing to `timedelta`
- Never pass numpy types directly to Python standard library date/time functions

Example:
```python
day = np.random.choice(pd.date_range(start=start_date, end=end_date))
day = pd.Timestamp(day).date()  # Ensures Python datetime.date
hour = int(np.random.choice(range(8, 19)))
minute = int(np.random.randint(0, 60))
start_time = datetime.combine(day, datetime.min.time()) + timedelta(hours=hour, minutes=minute)
```


### Data Types & Ranges
- Use appropriate data types (numeric, categorical, datetime, text, boolean)
- Ensure all values fall within believable, realistic bounds
- Include natural outliers and edge cases that would occur in real data
- Consider data quality issues (some missing values, slight inconsistencies)

### Realistic Distributions
- Use appropriate statistical distributions for different variable types
- Model correlations and dependencies between related variables
- Include natural noise and variation patterns
- Account for business rules or physical constraints

### Domain-Specific Patterns

#### For Business Data:
- Seasonal trends in sales, revenue, customer behavior
- Geographic and demographic variations
- Market dynamics and competitive effects
- Supply/demand patterns and inventory cycles
- Customer lifecycle and behavior patterns

#### For Scientific/Technical Data:
- Measurement uncertainties and instrument precision
- Physical laws and natural constraints
- Environmental factors and their effects
- Sampling frequencies and data collection patterns
- Natural variations and experimental noise

#### For Social/Behavioral Data:
- Demographic distributions matching real populations
- Cultural and regional variations
- Social network effects and clustering
- Temporal patterns (time-of-day, day-of-week, seasonal)
- Behavioral preferences and decision patterns

## Implementation Guide

**Environment Setup**
1. Use `configure_python_environment` to automatically set up the Python environment
2. Use `configure_notebook` to prepare the notebook environment
3. Use `notebook_install_packages` to install: `['pandas', 'numpy', 'matplotlib', 'seaborn', 'scipy']`

**Project Creation**
1. Parse `${input:subject}` to extract key concepts for naming
2. Create descriptive project folder using `create_directory`
3. Create notebook using `create_new_jupyter_notebook` with query: "Generate synthetic data for ${input:subject} with realistic patterns and comprehensive analysis"

**Notebook Development**
1. Use `edit_notebook_file` to create structured cells as outlined above
2. **MANDATORY**: Use `run_notebook_cell` immediately after creating each cell
3. Ensure all code executes without errors before proceeding
4. Export CSV data only once in the designated export cell

**Validation**
- Run all cells to ensure end-to-end functionality
- Confirm realistic data patterns and distributions
- Verify project folder contains both notebook and CSV file

## Code Template Structure

```python
# Cell 1: Package Installation
%pip install pandas numpy matplotlib seaborn scipy

# Cell 2: Library Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import random
from scipy import stats
import os

# Cell 3: Data Generation Function
def generate_synthetic_data(
    num_records: int = 1000,
    start_date: str = '2024-01-01',
    end_date: str = None,
    **kwargs
) -> pd.DataFrame:
    """
    Generate synthetic ${input:subject} data with realistic patterns.

    Parameters:
    num_records (int): Number of records to generate
    start_date (str): Start date for time series data
    end_date (str): End date (defaults to 1 year from start)
    **kwargs: Additional customization parameters

    Returns:
    pandas.DataFrame: Synthetic data with realistic patterns
    """
    # Implementation with realistic data generation logic
    pass

# Cell 4: Execute Data Generation
data = generate_synthetic_data()

# Cell 5: Export Data to CSV
subject = "${input:subject}"
subject_clean = (subject.lower()
                       .replace(" for ", "_")
                       .replace(" across ", "_")
                       .replace(" in ", "_")
                       .replace(" ", "_")
                       .replace("-", "_")
                       .replace("__", "_"))

filename = f'synthetic_{subject_clean}_data.csv'
data.to_csv(filename, index=False)
print(f"Data saved to: {filename}")

# Cell 6-9: Multiple Visualization Cells
# Create charts using matplotlib and seaborn
# Include map visualizations if data contains geographic information

# Cell 10: Summary and Validation
print("=== DATA SUMMARY ===")
print(data.describe())
print(f"\\nGeneration timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
```

## Required Outputs

1. **Jupyter Notebook**: Well-structured notebook with organized cells
2. **Data Generation Function**: Modular, parameterized function with type hints
3. **Realistic Data**: Values that domain experts would find believable
4. **CSV Export**: Clean data file with descriptive filename
5. **Multiple Visualizations**: Charts using matplotlib and seaborn. Include map visualizations if data contains geographic information.
6. **Statistical Summary**: Comprehensive descriptive statistics
7. **Data Validation**: Quality checks to ensure data realism
8. **Documentation**: Clear markdown explanations for each step

## Quality Standards

- **Realism**: Data should look authentic to subject matter experts
- **Completeness**: Cover all important aspects of the domain
- **Scalability**: Function should work with different dataset sizes
- **Flexibility**: Allow customization through parameters
- **Statistical Validity**: Distributions and correlations make sense
- **Usability**: Data ready for analysis, modeling, or visualization

## Final Deliverables

1. **Project Folder**: Organized folder structure with descriptive name
2. **Jupyter Notebook**: Complete implementation with all required cells
3. **CSV Data File**: Single CSV file with the generated dataset
4. **Rich Documentation**: Clear explanations throughout the notebook
5. **Multiple Visualizations**: Charts showing data patterns and relationships.
6. **Data Validation**: Evidence that synthetic data is realistic and high-quality

**Project Structure Example**:
```
weather_12_states_12_months/
├── synth_weather_12_states_12_months.ipynb
└── synthetic_weather_12_states_12_months_data.csv
```

<!-- Contains AI-generated edits. -->
