# 🔐 Password Strength Heatmap Generator

Ever wondered how safe your passwords really are? 🤔  
This Python project generates a **fun heatmap** of password strength — weak passwords are red, strong ones are green.

## How It Works
- Uses `zxcvbn` to score password strength (0-4)  
- Plots a heatmap with `seaborn`  
- Shows weak, medium, and strong passwords visually

## How to Run
```bash
pip3 install pandas seaborn matplotlib zxcvbn
python3 password_heatmap.py
