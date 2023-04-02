from datetime import datetime
import time
import sys
import numpy as np
sys.path.append('src/')
import classes
import utils
#------------------------------------------------------------------------------
f = open("DSL/Example.txt", "r")
dsl = f.read().split("steps:")
f.close()
pipeline_details = dsl[0]
steps_details = dsl[1].split("\n\n")
#----------------------------- CLASSES RECAP ----------------------------------
#Step(id, name, continuumLayer, type) + dataSources
#Step Phases(id, name) + technologies[] and environmentVariables[]
#DataSource(id, name, volume, type)
#DataStream(id, name, volume, type, velocity)
#Technology(id, name, os) + cpus[], gpus[], rams[], storages[] and networks[]
#CPU(id, cores, speed, producer)
#GPU(id, cores, speed, memory, producer)
#RAM(id, volume, speed, type, producer)
#Storage(id, volume, speed, type, producer)
#Network(id, bandwidth, latency)
#------------------------------------------------------------------------------
pipeline_name = pipeline_details.split(" ")[1]
pipeline_medium = pipeline_details.split(" ")[4].split("\n")[0]
step_phases = []
step_phases.append(classes.StepPhase("1", "End"))
i = 0
steps = []
step_name = ""
step_type = ""
for item in steps_details:
    step_type = (item.split("\n\t\t")[1].split(" step ")[0])
    step_type = step_type.replace("- ", "")
    step_name = (item.split("\n\t\t")[1].split(" step ")[1])
    steps.append(classes.Step(str(i), step_name, "", step_type))
    i += 1
#NOW THAT WE TRANSLATED THE DSL INTO ALL THE REQUIRED OBJECTS WE CAN GENERATE THE XES    
print(pipeline_name)
print(pipeline_medium)
for i in steps:
    print(i)
for i in step_phases:
    print(i)
utils.generateXES("1", pipeline_name, pipeline_medium, 1, 1, steps, step_phases)
