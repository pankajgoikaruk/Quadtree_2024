from sklearn.model_selection import train_test_split
import pandas as pd

class Modelling:
    def __init__(self) -> None:
        pass

    # Split data into training and testing sets
    def split_train_test(self, df, test_size=0.2, random_state=None):
            
        # Split the data into features (X) and target variable (y)
        X = df.drop(columns=['Longitude','Latitude', 'Crime_count'])  # Assuming 'Crime_count' is the target variable
        y = df['Crime_count']

        # Split the data into training and testing sets
        train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=test_size, random_state=random_state)

        # Concatenate the features and target variable for training and testing sets
        train_df = pd.concat([train_X, train_y], axis=1)
        test_df = pd.concat([test_X, test_y], axis=1)

        return train_df, test_df