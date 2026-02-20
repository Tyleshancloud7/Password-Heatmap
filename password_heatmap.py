# 🔐 Password Strength Heatmap Generator
# Fun, visual, and educational project for cybersecurity awareness

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from zxcvbn import zxcvbn

# Sample passwords (funny + real-world weak)
passwords = [
    '123456', 'password', 'qwerty', 'letmein', 'iloveyou',
    'monkey', 'dragon', 'admin', 
    'Tylesha2026!', 'S3cur3P@ss!', 'UltraStrongPass#42'
]

# Calculate strength score (0-4)
strength_scores = [zxcvbn(p)['score'] for p in passwords]

# Create DataFrame
df = pd.DataFrame({
    'Password': passwords,
    'Strength': strength_scores
})

# Map scores to colors for heatmap
df_pivot = df.pivot_table(index='Password', values='Strength')

# Plot heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df_pivot, annot=True, cmap='RdYlGn', cbar=True, linewidths=1, linecolor='black')
plt.title('🔥 Password Strength Heatmap – How Safe Is Your Password? 🔥', fontsize=14)
plt.xlabel('')
plt.ylabel('Password', rotation=0)
plt.xticks([])
plt.tight_layout()
plt.savefig('password_heatmap.png', dpi=300)  # Save image for LinkedIn/GitHub
plt.show()

