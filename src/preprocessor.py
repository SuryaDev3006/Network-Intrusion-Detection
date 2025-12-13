import os 
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from src.utils import print_header,ensure_artifact_dir

def preprocess_data(df,target_col,test_size,random_state,scaler_path):
    """
    Preprocess the data by handling missing values, encoding categorical variables,
    scaling features, and splitting into training and testing sets.
    Args:
        df (pd.DataFrame): The input dataframe.
        target_col (str): The name of the target column.
        test_size (float): Proportion of the dataset to include in the test split.
        random_state (int): Random seed for reproducibility.
        scaler_path (str): Path to save the fitted scaler.
    """

    X=df.drop(columns=[target_col])
    y=df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y)
    
    scaler=StandardScaler()
    X_train_scaled=scaler.fit_transform(X_train)
    X_test_scaled=scaler.transform(X_test)

    #create artifact directory properly
    ensure_artifact_dir(os.path.dirname(scaler_path))

    #Save scaler
    joblib.dump(scaler,scaler_path)
    print_header(f"Scaler saved at {scaler_path}")