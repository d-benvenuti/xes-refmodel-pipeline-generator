# xes-refmodel-pipeline-generator
Simple collection of Python scripts to generate an XES log following the Big Data Pipeline reference model.

To run it, use first:
```
pip install PyQt5
```

Then, run the script:
```
python refmodel_generator.py
```

# Debug button

The "debug" button in the main window simply creates a pre-fixed set of objects that can be used to generate a simple XES really fast.

# Info about xes generation

- If more than one resource is linked to the same step, each entry related to that step in the xes file will contain all the linked resources.
- If more than one data sources is linked to the same step, only one will be chosen at random while writing in the xes an entry related to that step. The same goes for the link between step phases and technologies, and for the link between technologies and cpus, gpus, rams, storages and networks.
- The order in which steps and step phases are written in the xes is the order in which they are created.
- Each step will have in each trace one entry for each step phases linked to it.

# TO-DO

- Increase feedback from the app when something has been done succesfully.
- Implement the possibility to de-link objects.
- Implement data loading functionality from a JSON input.