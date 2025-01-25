import streamlit as st

def render():
    st.title("Machine Learning Learning Material")
    st.markdown("""
    ### Topics Covered:
    1. **Introduction to Machine Learning**
    2. **Supervised Learning: Regression, Classification**
    3. **Unsupervised Learning: Clustering, Dimensionality Reduction**
    4. **Evaluation Metrics: Accuracy, Precision, Recall**
    5. **Working with Scikit-Learn**
    6. **Feature Scaling and Selection**
    7. **Overfitting and Regularization**
    8. **Hyperparameter Tuning**
    9. **Working with Real-World Datasets**
    10. **Deploying ML Models**
    """)

    # List of topics and their content
    content = {
        "Introduction to Machine Learning": """
        Machine Learning (ML) is a branch of artificial intelligence where machines are trained to learn patterns from data to make predictions or decisions.

        **Key Points:**
        - **Types of ML**: Supervised, Unsupervised, and Reinforcement Learning.
        - **Applications**: Image recognition, Natural language processing, Recommender systems, etc.

        **Example:**
        ```python
        # Simple pseudo-code for ML workflow
        1. Collect data
        2. Preprocess data
        3. Train the model
        4. Evaluate the model
        5. Deploy the model
        ```
        """,

        "Supervised Learning: Regression, Classification": """
        **Supervised Learning** involves training a model on labeled data.

        - **Regression**: Predict continuous values (e.g., house prices).
        - **Classification**: Predict categories (e.g., spam detection).

        **Example: Regression**
        ```python
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        ```

        **Example: Classification**
        ```python
        from sklearn.tree import DecisionTreeClassifier
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        ```
        """,

        "Unsupervised Learning: Clustering, Dimensionality Reduction": """
        **Unsupervised Learning** involves working with unlabeled data.

        - **Clustering**: Group data points (e.g., customer segmentation).
        - **Dimensionality Reduction**: Reduce the number of features (e.g., PCA).

        **Example: Clustering**
        ```python
        from sklearn.cluster import KMeans
        model = KMeans(n_clusters=3)
        model.fit(data)
        labels = model.predict(data)
        ```

        **Example: Dimensionality Reduction**
        ```python
        from sklearn.decomposition import PCA
        pca = PCA(n_components=2)
        reduced_data = pca.fit_transform(data)
        ```
        """,

        "Evaluation Metrics: Accuracy, Precision, Recall": """
        Evaluation metrics help measure the performance of ML models.

        **Key Metrics:**
        - **Accuracy**: Ratio of correct predictions to total predictions.
        - **Precision**: Ratio of true positives to predicted positives.
        - **Recall**: Ratio of true positives to actual positives.

        **Example: Classification Metrics**
        ```python
        from sklearn.metrics import accuracy_score, precision_score, recall_score
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        print(accuracy, precision, recall)
        ```
        """,

        "Working with Scikit-Learn": """
        Scikit-Learn is a popular ML library in Python. It provides tools for data preprocessing, model building, and evaluation.

        **Key Functions:**
        - **Data Preprocessing**: `StandardScaler`, `LabelEncoder`.
        - **Model Building**: Regression, Classification, Clustering.
        - **Model Evaluation**: Cross-validation, Grid Search.

        **Example:**
        ```python
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        ```
        """,

        "Feature Scaling and Selection": """
        Feature scaling and selection improve model performance and reduce training time.

        **Feature Scaling**: Normalizes feature values to a similar range.
        - **Standardization**: `StandardScaler()`
        - **Normalization**: `MinMaxScaler()`

        **Feature Selection**: Picks the most important features for training.

        **Example:**
        ```python
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        ```
        """,

        "Overfitting and Regularization": """
        Overfitting occurs when a model learns the training data too well, including noise.

        **Regularization** helps prevent overfitting by adding a penalty to the loss function.
        - **L1 Regularization (Lasso)**: Encourages sparsity.
        - **L2 Regularization (Ridge)**: Penalizes large coefficients.

        **Example: Ridge Regression**
        ```python
        from sklearn.linear_model import Ridge
        model = Ridge(alpha=1.0)
        model.fit(X_train, y_train)
        ```
        """,

        "Hyperparameter Tuning": """
        Hyperparameter tuning optimizes a model's parameters for better performance.

        **Methods:**
        - **Grid Search**: Tries all combinations of parameters.
        - **Random Search**: Tries a random set of parameters.

        **Example: Grid Search**
        ```python
        from sklearn.model_selection import GridSearchCV
        param_grid = {'C': [0.1, 1, 10]}
        grid = GridSearchCV(SVC(), param_grid, refit=True)
        grid.fit(X_train, y_train)
        ```
        """,

        "Working with Real-World Datasets": """
        Real-world datasets often require cleaning and preprocessing.

        **Steps:**
        1. Handle missing values.
        2. Encode categorical features.
        3. Scale numerical features.

        **Example: Handling Missing Values**
        ```python
        df.fillna(df.mean(), inplace=True)
        ```
        """,

        "Deploying ML Models": """
        Deploying ML models involves making them available in production.

        **Steps:**
        1. Serialize the model using `joblib` or `pickle`.
        2. Create an API using Flask or FastAPI.
        3. Monitor the model's performance post-deployment.

        **Example: Saving a Model**
        ```python
        import joblib
        joblib.dump(model, 'model.pkl')
        ```

        **Example: Flask API**
        ```python
        from flask import Flask, request, jsonify
        app = Flask(__name__)

        @app.route('/predict', methods=['POST'])
        def predict():
            data = request.json
            prediction = model.predict([data['features']])
            return jsonify({'prediction': prediction.tolist()})

        app.run()
        ```
        """
    }

    # Display content for each topic
    for topic, text in content.items():
        st.subheader(topic)
        st.markdown(text)
