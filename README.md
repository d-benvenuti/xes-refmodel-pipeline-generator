# xes-refmodel-pipeline-generator
Simple collection of Python scripts to generate a log following the Big Data Pipeline reference model. The output can be either in JSON or in XES.

To run it, use first:
...
pip install PyQt5
...

Then, run the scrypt:
...
python refmodel_generator.py
...

# TO-DO

1. Fix generateJSON function to handle printing correctly the final "," when some classes are not present.
2. Increase feedback from the app when something has been done succesfully.
3. Implement the possibility to de-link objects.
4. Fix the link between StepPhase and Technology to add Step in it.
5. Implement loading functionality from JSON.