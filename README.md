# This is HW1 for CSE 167

## All normal part work as write up

## All extra credit work as write up

### How to run 
1. build with cmake as debug (using any toolchain, I love CLion
2. using `cd` to change directory to `cmake-build-debug` (or any other build directory if you are using other toolchain)
3. for all normal part, run the code as write up
4. for 1-2 boxing extra credit, it is already implemented in the code
5. prep for 1-4 extra credit, run the python script jsonGen.py as instructed in my comment, to make you easy, I have already generated the json files under `/sun` `/piggy` `/transformation_2`
6. for 1-4 line and curve extra credit, run the code with `.balboa -animation dir"
```shell
./balboa -animation ../sun
./balboa -animation ../piggy
./balboa -animation ../transformation_2
```
7. for 1-7, my own scene is under `scenes/hw1/hw_1_7.json` directory, as `hw_1_7.json`. The generated image is under `output` directory as `hw_1_7.png`. If you want to run yourself, using the command:
```shell
./balboa -hw 1_7 ../scenes/hw1/hw_1_7.json
```
8. for 1-8, line and curve is hard coded. Two lines and Two curve. It is name as hw_1_8.png under `output` directory. If you want to run yourself, using the command:
```shell
./balboa -hw 1_8
```

### How to find already generated output
1. for the normal and 1-2 extra credit, the output is under `/output` directory as write up required
2. for the 1-4 extra credit, the output is under `/output/animation` directory
3. for the 1-4 source img out, the output is under `/cmake-build-debug` directory with `prefix out_[name]`
4. for 1-8 extra credit, the output is under `/output` directory with `hw_1_8.png` name


