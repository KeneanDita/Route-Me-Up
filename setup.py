from pycaret.classification import setup

def setup_environment():
    """
    Initializes the PyCaret environment for machine learning tasks.
    """
    setup(
        data=None,
        target='target_column',
        session_id=123,
        html=False,
        log_experiment=True,
        experiment_name='pysco_paralysis',
        log_plots=True,
    )