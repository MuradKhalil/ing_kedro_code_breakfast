# ING Kedro Code Breakfast

## Overview


## Steps to set up your local environment

1. Fork and clone this github repository: https://github.com/MuradKhalil/ing_kedro_code_breakfast
2. Navigate to the cloned repo: *$ cd ing_kedro_code_breakfast*
3. Build a docker container: *$ docker build -t ing_kedro_code_breakfast:v1 .*
4. Spin up the container and start a bash session: *$ docker run -p=4141:4141 -it ing_kedro_code_breakfast:v1  /bin/bash*
5. Navigate to the kedro project folder inside the container: *$ cd kedro_tutorial*

## Tasks:
- Data
1. Run *$ kedro run --node=preprocess_companies_node*
2. Run *$ kedro run --node=preprocess_shuttles_node*. This should give an error
3. Open up conf/base/catalog.yml and register the data/01_raw/shuttles.csv file
    - Specify ";" as the delimeter
4. Repeat task 2

- Data processing pipeline
5. Open up src/ing_kedro_code_breakfast/pipelines/data_processing/pipeline.py and add one more node to the pipeline
    - Node takes the create_model_input_table function as the func argument
    - Node takes 3 input files: outputs of the previous two nodes and the reviews.csv files
    - Node outputs 1 table
    - Specify a name for the node as well
6. Register the output of the newly added node as a csv file in catalog.yml. Store the csv file in data/03_primary
7. Run the data processing pipeline: *$ kedro run --pipeline=dp*. You should see the output of the newly added node stored in data/03_primary

- Data science pipeline
8. Open up src/ing_kedro_code_breakfast/pipelines/data_science/pipeline.py and complete the code
    - Pass the newly created csv file as one of the inputs to the split data node
9. train_model_node outputs a regressor, make it persist by registering in catalog.yml. Specify the path to be data/06_models
10. Run all the pipelines: *$ kedro run*
11. Visualize the pipelines: *$ kedro viz --host=0.0.0.0*