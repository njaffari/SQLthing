import pandas as pd

# Simulated dataframe (you’d fetch from Supabase in real case)
data = {
    "title": ["BOTW", "Odyssey", "MK8 Deluxe", "Pokemon R/B", "SSBU"],
    "platform": ["Switch", "Switch", "Switch", "Game Boy", "Switch"],
    "release_year": [2017, 2017, 2017, 1996, 2018],
    "sales_millions": [31.15, 27.65, 60.58, 31.38, 34.22],
    "genre": ["Action-Adventure", "Platformer", "Racing", "RPG", "Fighting"]
}
df = pd.DataFrame(data)

# Example pandas query
print(df[df["platform"] == "Switch"][["title", "release_year"]])
