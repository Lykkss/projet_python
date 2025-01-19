# COVID Data Analysis and Visualization

This project provides tools to analyze and visualize COVID-19 data using Streamlit, Pandas, Matplotlib, and Plotly.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Lykkss/projet_python.git
    cd projet_python
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Launch the Project

To start the Streamlit application, run the following command:
```sh
streamlit run app.py
```

## Deploy Project 

https://lykkss-projet-python-app-sczaoz.streamlit.app/

## Diagram

            +----------------+
            |     app.py     |
            +----------------+
                     |
       +---------------------------+
       |        src/               |
       +---------------------------+
       | file_reader.py  analyzer.py|
       | visualizer.py              |
       +---------------------------+
                     |
            +----------------+
            |      data/      |
            +----------------+
