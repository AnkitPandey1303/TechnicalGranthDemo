import streamlit as st

def render():
    st.title("AI Development Learning Material")
    st.markdown("""
    ### Topics Covered:
    1. **Introduction to Artificial Intelligence**
    2. **Foundations of Neural Networks**
    3. **Deep Learning Basics: TensorFlow, PyTorch**
    4. **Natural Language Processing (NLP)**
    5. **Computer Vision Applications**
    6. **Reinforcement Learning Overview**
    7. **Generative Adversarial Networks (GANs)**
    8. **Transfer Learning Techniques**
    9. **Building AI-Powered Applications**
    10. **AI Ethics and Best Practices**
    """)

    # List of topics and their content
    content = {
        "Introduction to Artificial Intelligence": """
        Artificial Intelligence (AI) is the simulation of human intelligence in machines. It enables systems to perform tasks like learning, reasoning, and problem-solving.

        **Key AI Types:**
        - **Narrow AI**: Focused on specific tasks (e.g., Siri, recommendation systems).
        - **General AI**: Mimics human intelligence (still theoretical).
        - **Super AI**: Surpasses human intelligence (future potential).

        **Applications:**
        - Healthcare, autonomous vehicles, robotics, and more.
        """,

        "Foundations of Neural Networks": """
        Neural networks are inspired by the human brain and consist of layers of interconnected nodes (neurons).

        **Components:**
        - **Input Layer**: Receives data.
        - **Hidden Layers**: Processes data using weights and activation functions.
        - **Output Layer**: Produces predictions.

        **Example:**
        ```python
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import Dense

        model = Sequential([
            Dense(32, activation='relu', input_shape=(10,)),
            Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        ```
        """,

        "Deep Learning Basics: TensorFlow, PyTorch": """
        Deep Learning uses neural networks with multiple layers to learn complex patterns.

        **Popular Frameworks:**
        - **TensorFlow**: A powerful open-source library by Google.
        - **PyTorch**: A dynamic computation graph library by Facebook.

        **Example: TensorFlow**
        ```python
        import tensorflow as tf

        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(10)
        ])
        model.compile(optimizer='adam', loss='mse')
        ```

        **Example: PyTorch**
        ```python
        import torch
        import torch.nn as nn

        class NeuralNetwork(nn.Module):
            def __init__(self):
                super(NeuralNetwork, self).__init__()
                self.linear = nn.Linear(10, 1)

            def forward(self, x):
                return self.linear(x)

        model = NeuralNetwork()
        ```
        """,

        "Natural Language Processing (NLP)": """
        NLP focuses on enabling machines to understand and process human language.

        **Common Tasks:**
        - Text preprocessing, sentiment analysis, translation, and text generation.

        **Example: Preprocessing with NLTK**
        ```python
        import nltk
        from nltk.tokenize import word_tokenize

        nltk.download('punkt')
        text = "Streamlit is great for building AI applications!"
        tokens = word_tokenize(text)
        print(tokens)
        ```

        **Example: Sentiment Analysis with Hugging Face**
        ```python
        from transformers import pipeline
        sentiment_model = pipeline('sentiment-analysis')
        result = sentiment_model("I love learning AI!")
        print(result)
        ```
        """,

        "Computer Vision Applications": """
        Computer Vision enables machines to interpret and process images and videos.

        **Applications:**
        - Object detection, facial recognition, image classification, etc.

        **Example: Image Classification with OpenCV**
        ```python
        import cv2

        image = cv2.imread('example.jpg')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Gray Image', gray)
        cv2.waitKey(0)
        ```

        **Example: Using TensorFlow**
        ```python
        from tensorflow.keras.applications import ResNet50

        model = ResNet50(weights='imagenet')
        ```
        """,

        "Reinforcement Learning Overview": """
        Reinforcement Learning (RL) involves training agents to make decisions by rewarding desired actions.

        **Key Concepts:**
        - **Agent**: Learns to interact with the environment.
        - **Environment**: Provides feedback in the form of rewards or penalties.

        **Example: Gym Environment**
        ```python
        import gym

        env = gym.make("CartPole-v1")
        state = env.reset()
        for _ in range(1000):
            action = env.action_space.sample()  # Random action
            state, reward, done, _ = env.step(action)
            if done:
                break
        env.close()
        ```
        """,

        "Generative Adversarial Networks (GANs)": """
        GANs consist of two neural networks:
        - **Generator**: Creates fake data.
        - **Discriminator**: Differentiates between real and fake data.

        **Example: Simple GAN**
        ```python
        import tensorflow as tf
        from tensorflow.keras.layers import Dense

        # Generator
        generator = tf.keras.Sequential([
            Dense(128, activation='relu', input_shape=(100,)),
            Dense(784, activation='sigmoid')
        ])

        # Discriminator
        discriminator = tf.keras.Sequential([
            Dense(128, activation='relu', input_shape=(784,)),
            Dense(1, activation='sigmoid')
        ])
        ```
        """,

        "Transfer Learning Techniques": """
        Transfer learning involves leveraging pre-trained models for new tasks.

        **Steps:**
        1. Load a pre-trained model (e.g., ResNet, VGG).
        2. Fine-tune on your dataset.

        **Example: Transfer Learning with TensorFlow**
        ```python
        from tensorflow.keras.applications import VGG16
        model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
        ```
        """,

        "Building AI-Powered Applications": """
        AI applications integrate AI models into real-world systems.

        **Example: Flask App**
        ```python
        from flask import Flask, request, jsonify

        app = Flask(__name__)

        @app.route('/predict', methods=['POST'])
        def predict():
            data = request.json
            prediction = model.predict(data['features'])
            return jsonify({'prediction': prediction.tolist()})

        app.run()
        ```
        """,

        "AI Ethics and Best Practices": """
        **Ethics in AI** ensures that AI systems are fair, transparent, and non-discriminatory.

        **Key Principles:**
        - Avoid bias in training data.
        - Ensure model interpretability.
        - Respect user privacy.

        **Example: Evaluating Fairness**
        ```python
        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(y_true, y_pred)
        print(cm)
        ```
        """
    }

    # Display content for each topic
    for topic, text in content.items():
        st.subheader(topic)
        st.markdown(text)
