from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("\n" + "=" * 50)
print("        IRIS CLASSIFICATION MODEL")
print("=" * 50)

print("\n[ DATASET INFORMATION ]")
print("-" * 30)
print("Features       :")
for feature in iris.feature_names:
    print(f"                 - {feature}")

print(f"Target Classes : {', '.join(iris.target_names)}")
print(f"Total Samples  : {len(iris.data)}")

print("\n[ MODEL RESULTS ]")
print("-" * 30)
print(f"Algorithm      : K-Nearest Neighbors (KNN)")
print(f"Training Data  : {len(X_train)} samples")
print(f"Testing Data   : {len(X_test)} samples")
print(f"Accuracy       : {accuracy * 100:.2f}%")

print("\n" + "=" * 50)
# Predict a new flower

print("\n[ NEW FLOWER PREDICTION ]")
print("-" * 30)

new_flower = [[
    5.1,  # Sepal length
    3.5,  # Sepal width
    1.4,  # Petal length
    0.2   # Petal width
]]

new_flower_scaled = scaler.transform(new_flower)

prediction = model.predict(new_flower_scaled)

predicted_species = iris.target_names[prediction[0]]

print(f"Predicted Species : {predicted_species}")