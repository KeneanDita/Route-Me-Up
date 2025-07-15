import pycaret as pc

def setup_environment():
    """
    Initializes the PyCaret environment for machine learning tasks.
    """
    pc.setup(
        data=None,  # Placeholder for dataset, to be set later
        target=None,  # Placeholder for target variable, to be set later
        session_id=123,  # Random seed for reproducibility
        silent=True,  # Suppress setup messages
        html=False  # Disable HTML output
    ) 