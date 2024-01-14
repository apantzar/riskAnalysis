import matplotlib.pyplot as plt
import matplotlib.patches as patches

risk_categories = {
    "Technological": (1, 1),
    "Data Security": (5, 5),
    "Business Continuity": (2, 4),
    "Company Reputation": (7, 5),
    "Human Error": (9, 3),
    "Low User Engagement": (9, 7),
    "Low Provider Participation": (7, 7),
    "Application Performance": (9, 5),
    "Customer Satisfaction": (8, 8),
    "Economic": (7, 6),
    "Competition": (5, 0.5),
    "Political": (9, 1)
}

fig, ax = plt.subplots(figsize=(10, 8))

# Define the color scheme for the risk matrix areas
colors = {'low': '#B0E0E6', 'medium': '#FFDAB9', 'high': '#FA8072'}

# Create the matrix areas
ax.add_patch(patches.Rectangle((0, 0), 5, 5, color=colors['low'], label='Low Risk'))
ax.add_patch(patches.Rectangle((5, 0), 5, 5, color=colors['medium'], label='Medium Risk'))
ax.add_patch(patches.Rectangle((0, 5), 5, 5, color=colors['medium'], label='Medium Risk'))
ax.add_patch(patches.Rectangle((5, 5), 5, 5, color=colors['high'], label='High Risk'))

# Plot each risk category on the matrix
for risk, (severity, probability) in risk_categories.items():
    ax.plot(severity, probability, 'ro')
    vertical_offset = 0.3
    horizontal_offset = 0 if len(risk) <= 12 else -0.5
    ax.text(severity + horizontal_offset, probability + vertical_offset, risk, fontsize=9, ha='center', va='bottom', color='black')

# Set the axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Label the axes with 'Low', 'Medium', 'High'
ax.set_xlabel('Risk Severity', fontsize=14)
ax.set_ylabel('Probability', fontsize=14)
ax.set_xticks([2.5, 7.5])
ax.set_yticks([2.5, 7.5])
ax.set_xticklabels(['Low', 'High'], fontsize=12)
ax.set_yticklabels(['Low', 'High'], fontsize=12)

# Set the title of the plot
ax.set_title('Risk Management Analysis for MasterMind', fontsize=16)

# Show the plot
plt.tight_layout()
plt.show()
