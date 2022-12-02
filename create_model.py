# # Import libraries
# import pandas as pd
# import pickle

# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor

# df = pd.read_csv('data/crimedata.csv')

# # Create a column for the sum of all crimes
# df["total_crime"] = df["murders"] + df["rapes"] + df["robberies"] + df["assaults"] + df["burglaries"] + df["larcenies"] + df["autoTheft"] + df["arsons"]

# selected_features = ['numbUrban', 'numUnderPov', 'population', 'numKidsBornNeverMar', 'numStreet']

# X = df[selected_features]
# y = df["total_crime"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
# model = RandomForestRegressor(random_state=2)
# model.fit(X_train, y_train)

# pickle.dump(model, open('models/model.pkl', 'wb'))
