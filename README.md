# ING Kedro Code Breakfast

## Overview


## Prerequisites
1. Make sure you can clone from GitHub
2. Install docker 3.x on your computer


## Steps to set up your local environment
1. Fork and clone this github repository: https://github.com/MuradKhalil/ing_kedro_code_breakfast
2. Navigate to the cloned repo: `$ cd ing_kedro_code_breakfast`
3. Build a docker image: `$ docker build -t ing_kedro_code_breakfast:v1 .`
4. Spin up a container: `$ docker run -p=4141:4141 -it ing_kedro_code_breakfast:v1`
5. Navigate to the kedro project folder inside the container: `$ cd kedro_tutorial`


## Tasks:
### Data processing pipeline
1. Run `$ kedro viz --host=0.0.0.0` and inspect the data pipeline
2. Inspect *src/ing_kedro_code_breakfast/pipelines/data_processing/pipeline.py* and *conf/base/catalog.yml* files
3. Run `$ kedro run` and inspect contents of the *data* folder
4. Register the output of the final node of the data_processing pipeline as a csv file in *catalog.yml*. Store the csv file in *data/03_primary*
    - You can open the file by running `$ nano conf/base/catalog.yml`
    - Save by pressing *^s* and exit via *^x*
5. Repeat task 3 (you should see *model_input_table.csv* among the data files)

### Data science pipeline
6. Open up *src/ing_kedro_code_breakfast/pipelines/data_science/pipeline.py* and add two more nodes to the pipeline
    - node to train a model
    - node to evaluate the model on the test set
7. The model training node should output a model, make it persist by registering in *conf/base/catalog.yml*. Specify the path to be *data/06_models*
    - More info on how to regsiter a model: https://kedro.readthedocs.io/en/latest/kedro.extras.datasets.pickle.PickleDataSet.html
8. Register the data_science pipeline in *src/ing_kedro_code_breakfast/pipeline_registry*
9. Run all the pipelines: `$ kedro run`
10. Inspect contents of the *data* folder (you should be able to see the model saved among the data files)
11. Visualize the extended data pipeline: `$ kedro viz --host=0.0.0.0`
