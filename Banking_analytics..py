import pandas as pd 

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "Banking_data.csv")
df= pd.read_csv(file_path)
summary={
    "rows":len(df),
    "avg_balance": round(df["balance"].mean(), 2),
    "total_balance": round(df["balance"].sum(), 2),
    "avg_credit_score": round(df["credit_score"].mean(), 2),
    "high_churn_customers": int((df["churn_risk"] == "High").sum()),
    "medium_churn_customers": int((df["churn_risk"] == "Medium").sum()),
    "low_churn_customers": int((df["churn_risk"] == "Low").sum()),
    "top_region": df["region"].mode()[0],
    "top_account_type": df["account_type"].mode()[0],
}
print("Banking summary")
for k, v in summary.items():
 print (f"{k}:{v}")