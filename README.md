This Streamlit application is designed to predict the status and selling price of copper sales using classification and regression models. The application allows users to input various features related to copper sales and get predictions based on pre-trained machine learning models.

Table of Contents
Installation
Usage
Features
Model Details
Encoding Mappings
Contributing
License
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/ArovincyJenifer/CopperModel-ML-Algorithms.git
Navigate to the project directory:
bash
Copy code
cd copper-sales-prediction
Create a virtual environment and activate it:
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Ensure you have the pre-trained models (model.pkl, scaler.pkl, modellgbm.pkl, scalerlgb.pkl) in the project directory.
Usage
Run the Streamlit application:
bash
Copy code
streamlit run app.py
Open your web browser and navigate to http://localhost:8501 to view the application.
Features
Classification Tab:

Input fields for item date, country, selling price, application, quantity (tons), thickness, and customer.
Predict the status of a copper sale using a pre-trained classification model.
Display the status encoding mapping.
Regression Tab:

Input fields for item type, status, time since item order, application, quantity (tons), thickness, width, and customer.
Predict the selling price of copper using a pre-trained regression model.
Display the item type and status encoding mappings in the sidebar.
Model Details
The application uses two pre-trained machine learning models:

Classification Model: Used to predict the status of copper sales.
Regression Model: Used to predict the selling price of copper sales.
Both models are loaded from serialized files (.pkl files) using joblib.

Encoding Mappings
The application uses LabelEncoder to encode categorical features. 


Contributing
Contributions are welcome! Please feel free to submit a Pull Request.



