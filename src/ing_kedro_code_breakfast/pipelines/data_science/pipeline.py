from kedro.pipeline import Pipeline, node
from .nodes import evaluate_model, split_data, train_model

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=split_data,
                inputs=['model_input_table', "parameters"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            # Task 6: add 2 more nodes. One for training a model and another for evaluating it
            ####
            # your code here
            ####
        ]
    )