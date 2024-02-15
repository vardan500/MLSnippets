#LabelEncoder for simple binary encoding
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
LabelEncoder_y = LabelEncoder()
Kyphosis_df['Kyphosis'] = LabelEncoder_y.fit_transform(Kyphosis_df['Kyphosis'])

#All encoding using get_dummies
bike_df = pd.get_dummies(data=bike_df, columns=['Make', 'Model', 'Type', 'Origin', 'DriveTrain'])

#Encoding using one hot encoder
X_cat = creditcard_df[['SEX', 'EDUCATION', 'MARRIAGE']]
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder()
X_cat = onehotencoder.fit_transform(X_cat).toarray()
