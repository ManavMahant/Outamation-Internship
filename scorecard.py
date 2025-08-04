import numpy as np
import matplotlib.pyplot as plt

overs = np.arange(5, 51, 5)

np.random.seed()

team_a_increment = np.random.randint(25, 46, size=len(overs))
team_b_increment = np.random.randint(25, 46, size=len(overs))

team_a_scores = np.cumsum(team_a_increment)
team_b_scores = np.cumsum(team_b_increment)

plt.figure(figsize=(10, 6))
plt.plot(overs, team_a_scores, color='blue', marker='o', label='Team A')
plt.plot(overs, team_b_scores, color='green', marker='o', label='Team B')



plt.title("Cricket Match Score: India vs. Pakistan")
plt.xlabel("Overs")
plt.ylabel("Scores")
plt.xticks(overs)
plt.yticks(np.arange(0, max(max(team_a_scores), max(team_b_scores)) + 50, 25))
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()
