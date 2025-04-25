# PhobiaX - VR-based Phobia Therapy

# PhobiaX - ml Module

PhobiaX is an Android-based application built using React Native, designed to educate and treat various types of phobias using Virtual Reality (VR). The app covers phobias like Aquaphobia (fear of water), Nyctophobia (fear of the dark), and Acrophobia (fear of heights). The project integrates a pre- and post-assessment to evaluate the effectiveness of the VR-based therapy and uses machine learning to predict the user's phobia level.

## Deployed Application

The Streamlit app for this project is deployed and can be accessed here:

[PhobiaX Streamlit App](https://phobiax-ml-1234.streamlit.app/)

This app helps visualize and analyze the effectiveness of the VR-based phobia therapy with interactive graphs for comparing pre- and post-assessment results.

## Features

- **Phobia Education**: Learn about different types of phobias (Aquaphobia, Nyctophobia, Acrophobia).
- **VR-based Therapy**: Immersive VR experiences designed to treat phobias.
- **Pre- and Post-Assessment**: Collect data to assess the user's phobia level before and after therapy.
- **Phobia Level Prediction**: Uses machine learning to predict the level of phobia based on responses to questions.
- **Interactive Graphs**: Visualize pre- and post-therapy results for better understanding.

## Installation and Running Locally

To run the app locally on your machine, follow these steps:

1. **Clone the repository**:
   Open a terminal and clone the project repository:
   ```bash
   git clone https://github.com/anuragyadav04/phobiax-ml.git
2. Navigate to the project directory:

bash
Copy
Edit
cd phobiax-ml
Set up a virtual environment (optional but recommended): If you are using a virtual environment, create one with the following command:

bash
Copy
Edit
python -m venv venv
Then activate the virtual environment:

For Windows:

bash
Copy
Edit
venv\Scripts\activate
For macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
Install the required dependencies: Install all the dependencies listed in the requirements.txt file:

bash
Copy
Edit
pip install -r requirements.txt
Run the application locally: Once all the dependencies are installed, you can start the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Access the application: After running the app, you can access it in your browser at the following address:

arduino
Copy
Edit
http://localhost:8501
Usage
Once the app is running, you can:

Take a pre-assessment to evaluate your initial phobia level.

Experience immersive VR therapy for your selected phobia.

Take a post-assessment to assess any change in your phobia level.

View the interactive graphs that compare your pre- and post-assessment results.

Contributing
If you would like to contribute to the project, follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature-name).

Make your changes.

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin feature-name).

Create a pull request with a description of your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.
