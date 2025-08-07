Warehouse Layout Designer
Overview
This is a Streamlit web application for designing warehouse layouts. It allows users to define MODs/Areas and AISLEs with purposes, display the layout in a table, and save/load designs as JSON files.
Features

Dynamic input for MODs and AISLEs.
Table-based layout display.
Save and load layouts using JSON files.
Error handling for robustness.

Installation

Clone the repository:git clone <your-repo-url>
cd warehouse_layout


Create a virtual environment and activate it:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install -r requirements.txt


Run the app locally:streamlit run main.py



Deployment

Connect this repository to Streamlit Community Cloud.
Set the Python version to 3.11 in the deployment settings.
Ensure the main module is main.py.

Usage

Use the sidebar to switch between designing a new layout or loading a saved one.
Input the number of MODs and configure AISLE details.
Save or download the layout as a JSON file.

Dependencies

streamlit==1.30.0
pandas==2.2.2

License
MIT License
