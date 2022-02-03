# ING Kedro Code Breakfast

## Overview
Kedro is a python framework that makes it easy to build data pipelines and run those via terminal. Some concepts important to this session:
- *conf/base/catalog.yml* - a yaml file where data (raw input, processed data, models, etc.) is registered
- *src/ing_kedro_code_breakfast/pipelines* - a directory where pipelines are created. Each pipeline will have its own subdirectory here
- *src/ing_kedro_code_breakfast/pipelines/data_processing/nodes.py* - each pipeline will have a nodes.py file that contains different functions to be applied on the data
- *src/ing_kedro_code_breakfast/pipelines/data_processing/pipeline.py* - functions from the nodes.py file are used in pipeline.py to construct a pipeline
- *src/ing_kedro_code_breakfast/pipeline_registry.py* - once pipelines are created, they need to be registered here. Once registered they can be executed via terminal


## Prerequisites
1. Make sure you can clone from GitHub
2. Install docker 3.x on your computer


## Steps to set up your local environment
1. Fork and clone this github repository: https://github.com/MuradKhalil/ing_kedro_code_breakfast
2. Navigate to the cloned repo: `$ cd ing_kedro_code_breakfast`
3. Build a docker image: `$ docker build -t ing_kedro_code_breakfast:v1 .`
    - this will create a container image from a Dockerfile
    - this process will go through 6 steps and take a couple of minutes to complete
4. Spin up a container: `$ docker run -p=4141:4141 -it ing_kedro_code_breakfast:v1`
    - this will start the container and access bash inside it
5. Navigate to the kedro project folder inside the container: `$ cd kedro_tutorial`


## Tasks:
### Data processing pipeline
1. Run `$ kedro viz --host=0.0.0.0`. This will start a web app with interactive visualization of the pipeline. Inspect the data pipeline. Once finished, shut down the app by pressing *ctrl C*.
2. Inspect *src/ing_kedro_code_breakfast/pipelines/data_processing/pipeline.py* and *conf/base/catalog.yml* files
3. Run `$ kedro run` and inspect contents of the *data/03_primary* folder
4. Register the output of the final node of the data_processing pipeline as a csv file in *catalog.yml*. Store the csv file in *data/03_primary*
    - You can open the file by running `$ nano conf/base/catalog.yml`
    - Save by pressing `^s` and exit via `^x`
5. Repeat task 3 (you should see *model_input_table.csv* among the data files)

### Data science pipeline
6. Open up *src/ing_kedro_code_breakfast/pipelines/data_science/pipeline.py* and add two more nodes to the pipeline (nodes are available in nodes.py within the same directory)
    - node to train a model
    - node to evaluate the model on the test set
7. The model training node should output a model, make it persist by registering in *conf/base/catalog.yml*. Specify the path to be *data/06_models*
    - More info on how to regsiter a model: https://kedro.readthedocs.io/en/latest/kedro.extras.datasets.pickle.PickleDataSet.html
8. Register the data_science pipeline in *src/ing_kedro_code_breakfast/pipeline_registry.py*
9. Run all the pipelines: `$ kedro run`
10. Inspect contents of the *data/06_models* folder (you should be able to see the model saved there)
11. Visualize the extended data pipeline: `$ kedro viz --host=0.0.0.0`