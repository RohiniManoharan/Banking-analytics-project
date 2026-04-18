# Banking Analytics Project with AI Insights

## Overview
This project analyzes banking data to identify customer behavior, account trends, churn risk, and business insights. It combines Python-based data analysis with AI-generated natural-language insights to create a practical and recruiter-friendly portfolio project.

The project demonstrates:
- Data cleaning and analysis
- Banking domain understanding
- Python scripting
- AI-assisted(Deepseek model using openAI SDK-Microsoft foundry) insight generation
- Business reporting and storytelling

## Business Objective
Banks need to understand customer activity, account patterns, and churn risk to improve retention and decision-making. This project helps answer those business questions by analyzing a banking dataset and generating AI-driven insights from the results.

## Dataset
The dataset includes customer and account-level banking information such as:

- Customer ID
- Age
- Gender
- Account Type
- Balance
- Transaction Count
- Last Transaction Days
- Loan Amount
- Credit Score
- Churn Risk
- Income
- Region

## Project Files

- `src/banking_analytics.py`  
  Loads the dataset, performs analysis, and generates summary metrics.

- `src/chats.py`  
  Sends the summary output to an AI model(Deepseek using OpenAI SDK) and returns insights in natural language.

- `data/banking_data.csv`  
  Contains the banking dataset used for analysis.

## Tools and Technologies

- Python
- Pandas
- Microsoft Foundry
- AI model integration
- VS Code
- GitHub

## Project Workflow

1. Load the banking dataset.
2. Clean and inspect the data.
3. Generate summary statistics.
4. Pass the summary to an AI model using `chats.py`.
5. Receive business insights and recommendations.
6. Save the code and outputs to GitHub.

## Analysis Performed

The project focuses on:

- Customer segmentation
- Balance analysis
- Credit score patterns
- Churn risk analysis
- Region-wise trends
- Account type comparison
- AI-generated business recommendations

## Example Insights Generated
The AI model can provide insights such as:

- Which customers are at higher churn risk.
- Which account types have the highest balances.
- What the average credit score looks like.
- Which region has the strongest banking activity.
- What actions the bank can take to improve retention.

## Project Structure

```bash
banking-analytics-project/
├── data/
│   └── banking_data.csv
├── src/
│   ├── banking_analytics.py
│   └── chats.py
├── output.txt
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/banking-analytics-project.git
cd banking-analytics-project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the analytics script
```bash
python src/banking_analytics.py
```

### 4. Run the AI insight script
```bash
python src/chats.py
```

## Sample Output
The project produces outputs such as:

- Total rows analyzed
- Average balance
- Total balance
- Average credit score
- High, medium, and low churn customer counts
- AI-generated business insights

## Future Improvements

- Add predictive churn modeling
- Add fraud detection analysis
- Create interactive dashboards
- Expand the dataset with historical transactions
- Improve AI prompts for deeper recommendations
- Add automated report generation

## Why This Project Matters
This project demonstrates a mix of:
- Banking domain knowledge
- Data analytics
- Python scripting
- AI integration
- Practical business storytelling

It is especially useful for AI Engineer, Data Analyst, and AI-focused analytics roles.

## Author
Rohini Manoharan
LinkedIn: www.linkedin.com/in/rohini-manoharan
GitHub: https://github.com/RohiniManoharan/
