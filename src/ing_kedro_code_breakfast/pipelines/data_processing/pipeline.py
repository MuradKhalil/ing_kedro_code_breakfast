from kedro.pipeline import Pipeline, node
from .nodes import preprocess_companies, preprocess_shuttles, create_model_input_table

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=preprocess_companies,
                inputs="companies",
                outputs="preprocessed_companies",
                name="preprocess_companies_node",
            ),
            node(
                func=preprocess_shuttles,
                inputs="shuttles",
                outputs="preprocessed_shuttles",
                name="preprocess_shuttles_node",
            ),
            # Task 5: Create a new node
            ####
            # your code here
            ####
        ]
    )