import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer

def GetTargets(df):
    folder = './'

    # Load synthetic data
    synthetic_data_path = os.path.join(folder, 'DATA1.csv')
    synthetic_data = pd.read_csv(synthetic_data_path, encoding='latin-1')

    # Select the feature columns
    features = ['Feed water', 'pH', 'Temp', 'NH4', 'K', 'Na', 'Mg', 'Ca', 'Sr', 'Ba', 'Co3', 'HCo3', 'No3', 'F', 'Cl', 'Br', 'So4', 'Po4', 'SiO2', 'Vessel', 'Elements']

    # Select the target column
    target = ['Energy(kWh/m3)', 'Concentrate flow(m3/h)', 'permeate flow(m3/h)', 'Pressure(bar)', 'NH4.1', 'K.1', 'Na.1', 'Mg.1', 'Ca.1', 'Sr.1', 'Ba.1', 'Co3.1', 'HCo3.1', 'No3.1', 'F.1', 'Cl.1', 'Br.1', 'So4.1', 'Po4.1', 'SiO2.1', 'Active Area(m2)']

    # Now select the features
    synthetic_features = synthetic_data[features]
    synthetic_target = synthetic_data[target]

    # Preprocess synthetic data
    # synthetic_data.dropna()
    synthetic_features = synthetic_features.apply(pd.to_numeric, errors='coerce')
    synthetic_features.replace(r'^\s*$', float('nan'), regex=True, inplace=True)

    # data = {
    #   'Feed water': [90],
    #   'pH': [7],
    #   'Temp': [25],
    #   'NH4': [0],
    #   'K': [395.5],
    #   'Na': [10746],
    #   'Mg': [1295],
    #   'Ca': [407],
    #   'Sr': [0],
    #   'Ba': [0],
    #   'Co3': [0],
    #   'HCo3': [0],
    #   'No3': [0],
    #   'F': [0],
    #   'Cl': [19401],
    #   'Br': [67.14],
    #   'So4': [2708],
    #   'Po4': [0],
    #   'SiO2': [0],
    #   'Vessel': [12],
    #   'Elements': [6]
    # }
    # df = pd.DataFrame(data)
    real_features = df[features]

    imputer = SimpleImputer(strategy='mean')
    synthetic_features_imputed = pd.DataFrame(imputer.fit_transform(synthetic_features), columns=synthetic_features.columns)

    synthetic_target = synthetic_target.fillna(synthetic_target.mean())

    # Create the Random Forest Regressor model
    rf_regressor = RandomForestRegressor()

    # Train the model using synthetic data
    rf_regressor.fit(synthetic_features_imputed, synthetic_target)

    # Perform predictions on the real experimental testing data
    real_predictions_train = rf_regressor.predict(real_features)

    return real_predictions_train

# ans = GetTargets()
# print(ans)

# print(ans[0][0])
# print(ans[0][1])
# print(ans[0][2])
# print(ans[0][3])
