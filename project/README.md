# Programming For Data Analytics

By: Daniel Finnerty

## Introduction

This project is an anlaysis of solar generation potential, and comparing that against energy usage, with a view to determine if a quoted solar install makes financial sense.

This is done using learnings gained both from the programming for data analytics module, and through additional research performed as a suplement to these learnings.

The code, explanations, and information sources can be found in the `solar_assessment.ipynb` notebook.

To run this, the following Python packages are required.

- pandas
- numpy
- datetime
- matplotlib.pyplot
- seaborn

### Running the Notebook locally
The notebook can be ran locally however, prior to doing so the repository must be cloned to your local machine through the following steps:

#### _Using cmder_

1. Download and install full version of cmder from:  
https://cmder.app/ 

2. In cmder, clone the repository

```
git clone https://github.com/danielfinnerty/PFDA
```

3. On your local machine, set new repository as directory

4. Configure git pull rebase

```
git config pull.rebase false
```

5. Open repository

```
python -m notebook
```

6. Select the `solar_assessment.ipynb` file within the `project` folder.

7. Click on the double-arrow icon at the top to 'restart the kernell and run all cells'.


### Output
From running the notebook through the above steps, plots can be seen showing the daily, weekly, and monthly usage, along with potential daily, weekly, and monthly solar generation. In addition to this, the estimated savings are calculated and reviewed, for supporting an overall decision.

# End
