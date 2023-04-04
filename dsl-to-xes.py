from datetime import datetime
import time
import sys
import numpy as np
sys.path.append('src/')
import classes
import utils
#------------------------------------------------------------------------------
f = open("DSL/Example(withEnvVar).txt", "r")
dsl = f.read().split("steps:\n\t\t- ")
f.close()
pipeline_details = dsl[0]
steps_details = dsl[1].split("\n\t\t-")
#debug ----------------
print(pipeline_details)
for i in steps_details:
    print("----------------------")
    print(i)
    print("----------------------")
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
pipeline_name = pipeline_details.split(" {")[0].replace("Pipeline ", "").replace(" ", "")
pipeline_medium = pipeline_details.split(":")[1].replace(" ", "")
#DEBUG-----------------
print(pipeline_name)
print(pipeline_medium)
#----------------------
step_phases = []
step_phases.append(classes.StepPhase("1", "End"))
i = 0
steps = []
environmentVariables = []
step_name = ""
step_type = ""
for item in steps_details:
    step_type = (item.split(" step ")[0])
    step_name = (item.split(" step ")[1].split('\n')[0])
    new_step = classes.Step(str(i), step_name, "", step_type)
    #take env par if there are
    env_vars = item.split("environmentParameters: {\n")[1].replace("\t", "").split("\n}")[0].split(",\n")
    for env in env_vars:
        env = env.split(":")
        newEnvVar = classes.EnvironmentVariable(env[0], env[1].replace(" ", "").replace("'", ""))
        print(newEnvVar)
    #debug---------------
    print(new_step)
    steps.append(new_step)
    i += 1
#NOW THAT WE TRANSLATED THE DSL INTO ALL THE REQUIRED OBJECTS WE CAN GENERATE THE XES    
for i in step_phases:
    print(i)
utils.generateXES("1", pipeline_name, pipeline_medium, 1, 1, steps, step_phases)
