import classes
import sys
import random
from datetime import datetime
import time
#--------------------------------------------------------------------
#function to debug by populating the data sources
#--------------------------------------------------------------------
def debug(steps, step_phases, technologies):
    print("Debug Button clicked.")
    steps.append(classes.Step('1','1','edge','processing'))
    steps.append(classes.Step('2','2','edge','processing'))
    step_phases.append(classes.StepPhase('1','1'))
    step_phases.append(classes.StepPhase('2','2'))
    technologies.append(classes.Technology('1','1','Windows'))
    technologies.append(classes.Technology('2','2','Linux'))
    steps[0].dataSources.append(classes.DataSource('1','1','1','1'))
    steps[1].dataSources.append(classes.DataStream('2','2','2','2','IO'))
    step_phases[0].environmentVariables.append(classes.EnvironmentVariable('1','1'))
    step_phases[1].environmentVariables.append(classes.EnvironmentVariable('2','2'))
    technologies[0].cpus.append(classes.CPU('1','1','1',""))
    technologies[0].gpus.append(classes.GPU('1','1','1','1',""))
    technologies[0].rams.append(classes.RAM('1','1','1',"",'DDR4'))
    technologies[0].storages.append(classes.Storage('1','1','1',"",'HD'))
    technologies[0].networks.append(classes.Network('1','1','1'))
    technologies[1].cpus.append(classes.CPU('2','2','2','2'))
    technologies[1].gpus.append(classes.GPU('1','1','1','1',""))
    technologies[1].rams.append(classes.RAM('2','2','2','2','DDR5'))
    technologies[1].storages.append(classes.Storage('2','2','2','2','SSD'))
    technologies[1].networks.append(classes.Network('2','2','2'))
    step_phases[0].technologies.append(technologies[0])
    step_phases[1].technologies.append(technologies[1])
#--------------------------------------------------------------------
#function to generate the xes file
#--------------------------------------------------------------------
def generateXES(pipeline_id, pipeline_name, pipeline_medium, pipeline_traces, n, steps, step_phases):
        print("Generating XES file.")
        original_stdout = sys.stdout # Save a reference to the original standard output
        with open('logs/' + pipeline_name + '.xes', 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            #standard header
            print("<?xml version='1.0' encoding='UTF-8'?>\n<log>")
            print('\t<string key="creator" value="RefModel_Generator"/>')
            #extenstions
            print('\t<extension name="Concept" prefix="concept" uri="http://code.deckfour.org/xes/concept.xesext"/>')
            print('\t<extension name="Time" prefix="time" uri="http://code.deckfour.org/xes/time.xesext"/>')
            print('\t<extension name="Organizational" prefix="org" uri="http://code.deckfour.org/xes/org.xesext"/>')
            #attributes definition at log level
            #attributes definition at trace level
            print('\t<global scope="trace">')
            print('\t\t<string key="concept:name" value="name"/>')
            print('\t</global>')
            #attributes definition at event level
            print('\t<global scope="event">')
            print('\t\t<string key="concept:name" value="name"/>')
            print('\t\t<string key="StepPhaseID" value="string"/>')
            print('\t\t<date key="time:timestamp" value="' + datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f+01:00') + '"/>')
            #pipeline
            print('\t\t<string key="PipelineName" value="name"/>')
            print('\t\t<string key="PipelineID" value="string"/>')
            print('\t\t<string key="PipelineCommunicationMedium" value="string"/>')
            #classes.Step
            print('\t\t<string key="StepID" value="string"/>')
            print('\t\t<string key="StepContinuumLayer" value="string"/>')
            print('\t\t<string key="StepType" value="string"/>')
            #classes.DataSource
            print('\t\t<string key="DataSourceID" value="string"/>')
            print('\t\t<string key="DataSourceName" value="string"/>')
            print('\t\t<string key="DataSourceVolume" value="string"/>')
            print('\t\t<string key="DataSourceVelocity" value="string"/>')
            print('\t\t<string key="DataSourceType" value="string"/>')          
            #technologies
            print('\t\t<string key="TechnologyID" value="string"/>')
            print('\t\t<string key="TechnologyName" value="string"/>')
            print('\t\t<string key="TechnologyOS" value="string"/>')
            #cpus
            print('\t\t<string key="CPUID" value="string"/>')
            print('\t\t<string key="CPUCores" value="string"/>')
            print('\t\t<string key="CPUSpeed" value="string"/>')
            print('\t\t<string key="CPUProducer" value="string"/>')
            #gpus
            print('\t\t<string key="GPUID" value="string"/>')
            print('\t\t<string key="GPUCores" value="string"/>')
            print('\t\t<string key="GPUSpeed" value="string"/>')
            print('\t\t<string key="GPUMemory" value="string"/>')
            print('\t\t<string key="GPUProducer" value="string"/>')
            #rams
            print('\t\t<string key="RAMID" value="string"/>')
            print('\t\t<string key="RAMVolume" value="string"/>')
            print('\t\t<string key="RAMSpeed" value="string"/>')
            print('\t\t<string key="RAMProducer" value="string"/>')
            print('\t\t<string key="RAMType" value="string"/>')
            #storages
            print('\t\t<string key="StorageID" value="string"/>')
            print('\t\t<string key="StorageVolume" value="string"/>')
            print('\t\t<string key="StorageSpeed" value="string"/>')
            print('\t\t<string key="Storageroducer" value="string"/>')
            print('\t\t<string key="StorageType" value="string"/>')
            #networks
            print('\t\t<string key="NetworkID" value="string"/>')
            print('\t\t<string key="NetworkBandwidth" value="string"/>')
            print('\t\t<string key="NetworkLatency" value="string"/>')
            print('\t</global>')
            #classifiers
            print('\t<classifier name="Activity" keys="name"/>')
            print('\t<classifier name="activity classifier" keys="Activity"/>')
            #log
            #traces
            while n > 0:
                print('\t<trace>')
                print('\t\t<string key="concept:name" value="' + n.__str__() + '"/>')
                #events
                for step in steps:
                    for step_phase in step_phases:
                        print('\t\t<event>')
                        print('\t\t\t<string key="concept:name" value="' + step.name + '-' + step_phase.name + '"/>')
                        print('\t\t\t<string key="StepPhaseID" value="' + step_phase.id + '"/>')
                        #timestamp in YYYY-mm-ddTHH:MM:SS.fff+TZD"
                        print('\t\t\t<date key="time:timestamp" value="' + datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f+01:00') + '"/>')
                        #pipeline
                        print('\t\t\t<string key="PipelineID" value="' + pipeline_id + '"/>')
                        print('\t\t\t<string key="PipelineCommunicationMedium" value="' + pipeline_medium + '"/>')
                        print('\t\t\t<string key="PipelineName" value="' + pipeline_name + '"/>')
                        #classes.Step
                        print('\t\t\t<string key="StepID" value="' + step.id + '"/>')
                        print('\t\t\t<string key="StepName" value="' + step.name + '"/>')
                        print('\t\t\t<string key="StepContinuumLayer" value="' + step.continuumLayer + '"/>')
                        print('\t\t\t<string key="StepType" value="' + step.type + '"/>')
                        #data sources
                        i = random.randint(0,len(step.dataSources)-1)
                        print('\t\t\t<string key="DataSourceID" value="' + step.dataSources[i].id + '"/>')
                        print('\t\t\t<string key="DataSourceName" value="' + step.dataSources[i].name + '"/>')
                        print('\t\t\t<string key="DataSourceVolume" value="' + step.dataSources[i].volume + '"/>')
                        if type(step.dataSources[i]) == type(classes.DataStream):
                            print('\t\t\t<string key="DataSourceVelocity" value="' + step.dataSources[i].velocity + '"/>')
                        else:
                            print('\t\t\t<string key="DataSourceVelocity" value="None"/>')
                        print('\t\t\t<string key="DataSourceType" value="' + step.dataSources[i].type + '"/>')
                        #technologies
                        i = random.randint(0,len(step_phase.technologies)-1)
                        print('\t\t\t<string key="TechnologyID" value="' + step_phase.technologies[i].id + '"/>')
                        print('\t\t\t<string key="TechnologyName" value="' + step_phase.technologies[i].name + '"/>')
                        print('\t\t\t<string key="TechnologyOS" value="' + step_phase.technologies[i].os + '"/>')
                        #cpus
                        j = random.randint(0,len(step_phase.technologies[i].cpus)-1)
                        print('\t\t\t<string key="CPUID" value="' + step_phase.technologies[i].cpus[j].id + '"/>')
                        print('\t\t\t<string key="CPUCores" value="' + step_phase.technologies[i].cpus[j].cores + '"/>')
                        print('\t\t\t<string key="CPUSpeed" value="' + step_phase.technologies[i].cpus[j].speed + '"/>')
                        print('\t\t\t<string key="CPUProducer" value="' + step_phase.technologies[i].cpus[j].producer + '"/>')
                        #gpus
                        j = random.randint(0,len(step_phase.technologies[i].gpus)-1)
                        print('\t\t\t<string key="GPUID" value="' + step_phase.technologies[i].gpus[j].id + '"/>')
                        print('\t\t\t<string key="GPUCores" value="' + step_phase.technologies[i].gpus[j].cores + '"/>')
                        print('\t\t\t<string key="GPUSpeed" value="' + step_phase.technologies[i].gpus[j].speed + '"/>')
                        print('\t\t\t<string key="GPUMemory" value="' + step_phase.technologies[i].gpus[j].memory + '"/>')
                        print('\t\t\t<string key="GPUProducer" value="' + step_phase.technologies[i].gpus[j].producer + '"/>')
                        #rams
                        j = random.randint(0,len(step_phase.technologies[i].rams)-1)
                        print('\t\t\t<string key="RAMID" value="' + step_phase.technologies[i].rams[j].id + '"/>')
                        print('\t\t\t<string key="RAMVolume" value="' + step_phase.technologies[i].rams[j].volume + '"/>')
                        print('\t\t\t<string key="RAMSpeed" value="' + step_phase.technologies[i].rams[j].speed + '"/>')
                        print('\t\t\t<string key="RAMProducer" value="' + step_phase.technologies[i].rams[j].producer + '"/>')
                        print('\t\t\t<string key="RAMType" value="' + step_phase.technologies[i].rams[j].type + '"/>')
                        #storages
                        j = random.randint(0,len(step_phase.technologies[i].storages)-1)
                        print('\t\t\t<string key="StorageID" value="' + step_phase.technologies[i].storages[j].id + '"/>')
                        print('\t\t\t<string key="StorageVolume" value="' + step_phase.technologies[i].storages[j].volume + '"/>')
                        print('\t\t\t<string key="StorageSpeed" value="' + step_phase.technologies[i].storages[j].speed + '"/>')
                        print('\t\t\t<string key="Storageroducer" value="' + step_phase.technologies[i].storages[j].producer + '"/>')
                        print('\t\t\t<string key="StorageType" value="' + step_phase.technologies[i].storages[j].type + '"/>')
                        #networks
                        j = random.randint(0,len(step_phase.technologies[i].networks)-1)
                        print('\t\t\t<string key="NetworkID" value="' + step_phase.technologies[i].networks[j].id + '"/>')
                        print('\t\t\t<string key="NetworkBandwidth" value="' + step_phase.technologies[i].networks[j].bandwidth + '"/>')
                        print('\t\t\t<string key="NetworkLatency" value="' + step_phase.technologies[i].networks[j].latency + '"/>')
                        #close event
                        print('\t\t</event>')
                #close trace
                print('\t</trace>')
                #little wait to avoid timestamps with the same value
                time.sleep(0.2)
                n -= 1
            #close the log 
            print('</log>')
        sys.stdout = original_stdout # Reset the standard output to its original value       
#--------------------------------------------------------------------
#function to generate the json file
#--------------------------------------------------------------------
def generateJSON(pipeline_id, pipeline_name, pipeline_medium, pipeline_traces, n, steps, step_phases, data_sources, environment_variables, technologies, cpus, gpus, rams, storages, networks):
    print("Generating JSON file.")
    original_stdout = sys.stdout # Save a reference to the original standard output
    with open('data/' + pipeline_name + '.json', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print('{\n\t"PipelineID": "' + pipeline_id + '",\n\t"PipelineName": "' + pipeline_name + '",\n\t"PipelineCommunicationMedium": "' + pipeline_medium + '",\n\t"NumberOfTraces": "' + pipeline_traces + '",')
        for i in steps:
            print('\t' + i.__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t},'))    
        for i in step_phases:
            print('\t' + i.__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t},'))  
        for i in data_sources:
            print('\t' + i.__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t},'))  
        for i in environment_variables:
            print('\t' + i.__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t},'))  
        for i in technologies:
            print('\t' + i.__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t},'))  
        for i in cpus:
            print('\t' + i.__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t},'))  
        for i in gpus:
            print('\t' + i.__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t},'))  
        for i in rams:
            print('\t' + i.__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t},'))  
        for i in storages:
            print('\t' + i.__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t},')) 
        for i in networks:
            print('\t' + i.__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t}')) 
        print('}')
    sys.stdout = original_stdout # Reset the standard output to its original value