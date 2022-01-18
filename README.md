# ING Kedro Code Breakfast

## Overview


## Steps to set up your local environment

1. Fork and clone this github repository: https://github.com/MuradKhalil/ing_kedro_code_breakfast
2. Navigate to the cloned repo: *$ cd ing_kedro_code_breakfast*
3. Build a docker container: *$ docker build -t ing_kedro_code_breakfast:v1 .*
4. Spin up the container and start a bash session: *$ docker run -p=4141:4141 -it ing_kedro_code_breakfast:v1  /bin/bash*
5. Navigate to the kedro project folder inside the container: *$ cd kedro_tutorial*

## Kedro command line arguments
$ kedro run
$ kedro viz --host=0.0.0.0