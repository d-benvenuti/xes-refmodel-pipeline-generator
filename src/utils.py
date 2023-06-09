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
    #MAKE SURE THAT THE DATA STRUCTURES ARE EMPTY
    steps.clear()
    step_phases.clear()
    technologies.clear()
    #POPULATE THE DATA STRUCTURES
    steps.append(classes.Step('1','1','edge','processing'))
    steps.append(classes.Step('2','2','edge','processing'))
    step_phases.append(classes.StepPhase('1','1'))
    step_phases.append(classes.StepPhase('2','2'))
    steps[0].stepPhases.append(step_phases[0])
    steps[0].resources.append(classes.Resource('1', '1'))
    steps[1].resources.append(classes.Resource('2', '2'))
    steps[1].stepPhases.append(step_phases[0])
    steps[1].stepPhases.append(step_phases[1])
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
def generateXES(pipeline_id, pipeline_name, pipeline_medium, pipeline_traces, n, steps):
        print("Generating XES file.")
        original_stdout = sys.stdout # Save a reference to the original standard output
        #check for presence of links to avoid printing the attributes of classes that will not be present
        presence_of_resources = 0
        presence_of_continuum_layer = 0
        presence_of_data_sources = 0
        presence_of_step_phases = 0
        presence_of_technologies = 0
        presence_of_cpus = 0
        presence_of_gpus = 0
        presence_of_rams = 0
        presence_of_storages = 0
        presence_of_networks = 0
        for step in steps:
            if len(step.resources) > 0:
                presence_of_resources = 1
            if step.continuumLayer != "":
                presence_of_continuum_layer = 1
            if len(step.dataSources) > 0:
                presence_of_data_sources = 1
            for step_phase in step.stepPhases:
                    if len(step_phase.technologies) > 0:
                        presence_of_technologies = 1
                        for technology in step_phase.technologies:
                            if len(technology.cpus) > 0:
                                presence_of_cpus = 1
                            if len(technology.gpus) > 0:
                                presence_of_gpus = 1
                            if len(technology.rams) > 0:
                                presence_of_rams = 1
                            if len(technology.storages) > 0:
                                presence_of_storages = 1
                            if len(technology.networks) > 0:
                                presence_of_networks = 1
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
            #Step
            print('\t\t<string key="StepID" value="string"/>')
            if presence_of_resources == 1:
                print('\t\t<string key="ResourceID" value="string"/>')
                print('\t\t<string key="org:resource" value="string"/>')
            if presence_of_continuum_layer == 1:
                print('\t\t<string key="StepContinuumLayer" value="string"/>')
            print('\t\t<string key="StepType" value="string"/>')
            #DataSource
            #only if there are DataSources
            if presence_of_data_sources == 1:
                print('\t\t<string key="DataSourceID" value="string"/>')
                print('\t\t<string key="DataSourceName" value="string"/>')
                print('\t\t<string key="DataSourceVolume" value="string"/>')
                print('\t\t<string key="DataSourceVelocity" value="string"/>')
                print('\t\t<string key="DataSourceType" value="string"/>')          
            #technologies
            #only if there are Technologies
            if presence_of_technologies == 1:
                print('\t\t<string key="TechnologyID" value="string"/>')
                print('\t\t<string key="TechnologyName" value="string"/>')
                print('\t\t<string key="TechnologyOS" value="string"/>')
            #cpus
            if presence_of_cpus == 1:
                print('\t\t<string key="CPUID" value="string"/>')
                print('\t\t<string key="CPUCores" value="string"/>')
                print('\t\t<string key="CPUSpeed" value="string"/>')
                print('\t\t<string key="CPUProducer" value="string"/>')
            #gpus
            if presence_of_gpus == 1:
                print('\t\t<string key="GPUID" value="string"/>')
                print('\t\t<string key="GPUCores" value="string"/>')
                print('\t\t<string key="GPUSpeed" value="string"/>')
                print('\t\t<string key="GPUMemory" value="string"/>')
                print('\t\t<string key="GPUProducer" value="string"/>')
            #rams
            if presence_of_rams == 1:
                print('\t\t<string key="RAMID" value="string"/>')
                print('\t\t<string key="RAMVolume" value="string"/>')
                print('\t\t<string key="RAMSpeed" value="string"/>')
                print('\t\t<string key="RAMProducer" value="string"/>')
                print('\t\t<string key="RAMType" value="string"/>')
            #storages
            if presence_of_storages == 1:
                print('\t\t<string key="StorageID" value="string"/>')
                print('\t\t<string key="StorageVolume" value="string"/>')
                print('\t\t<string key="StorageSpeed" value="string"/>')
                print('\t\t<string key="Storageroducer" value="string"/>')
                print('\t\t<string key="StorageType" value="string"/>')
            #networks
            if presence_of_networks == 1:
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
                    for step_phase in step.stepPhases:
                        print('\t\t<event>')
                        print('\t\t\t<string key="concept:name" value="' + step.name + '-' + step_phase.name + '"/>')
                        print('\t\t\t<string key="StepPhaseID" value="' + step_phase.id + '"/>')
                        #timestamp in YYYY-mm-ddTHH:MM:SS.fff+TZD"
                        print('\t\t\t<date key="time:timestamp" value="' + datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f+01:00') + '"/>')
                        #pipeline
                        print('\t\t\t<string key="PipelineID" value="' + pipeline_id + '"/>')
                        print('\t\t\t<string key="PipelineCommunicationMedium" value="' + pipeline_medium + '"/>')
                        print('\t\t\t<string key="PipelineName" value="' + pipeline_name + '"/>')
                        #Step
                        print('\t\t\t<string key="StepID" value="' + step.id + '"/>')
                        print('\t\t\t<string key="StepName" value="' + step.name + '"/>')
                        #resources
                        if presence_of_resources == 1:
                            i = random.randint(0,len(step.resources)-1)
                            for resource in step.resources:
                                print('\t\t\t<string key="ResourceID" value="' + resource.id + '"/>')
                                print('\t\t\t<string key="org:resource" value="' + resource.name + '"/>')
                        if presence_of_continuum_layer == 1:
                            print('\t\t\t<string key="StepContinuumLayer" value="' + step.continuumLayer + '"/>')
                            print('\t\t\t<string key="StepType" value="' + step.type + '"/>')
                        #data sources
                        if presence_of_data_sources == 1:
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
                        if presence_of_technologies == 1:
                            i = random.randint(0,len(step_phase.technologies)-1)
                            print('\t\t\t<string key="TechnologyID" value="' + step_phase.technologies[i].id + '"/>')
                            print('\t\t\t<string key="TechnologyName" value="' + step_phase.technologies[i].name + '"/>')
                            print('\t\t\t<string key="TechnologyOS" value="' + step_phase.technologies[i].os + '"/>')
                        #cpus
                        if presence_of_cpus == 1:
                            j = random.randint(0,len(step_phase.technologies[i].cpus)-1)
                            print('\t\t\t<string key="CPUID" value="' + step_phase.technologies[i].cpus[j].id + '"/>')
                            print('\t\t\t<string key="CPUCores" value="' + step_phase.technologies[i].cpus[j].cores + '"/>')
                            print('\t\t\t<string key="CPUSpeed" value="' + step_phase.technologies[i].cpus[j].speed + '"/>')
                            print('\t\t\t<string key="CPUProducer" value="' + step_phase.technologies[i].cpus[j].producer + '"/>')
                        #gpus
                        if presence_of_gpus == 1:
                            j = random.randint(0,len(step_phase.technologies[i].gpus)-1)
                            print('\t\t\t<string key="GPUID" value="' + step_phase.technologies[i].gpus[j].id + '"/>')
                            print('\t\t\t<string key="GPUCores" value="' + step_phase.technologies[i].gpus[j].cores + '"/>')
                            print('\t\t\t<string key="GPUSpeed" value="' + step_phase.technologies[i].gpus[j].speed + '"/>')
                            print('\t\t\t<string key="GPUMemory" value="' + step_phase.technologies[i].gpus[j].memory + '"/>')
                            print('\t\t\t<string key="GPUProducer" value="' + step_phase.technologies[i].gpus[j].producer + '"/>')
                        #rams
                        if presence_of_rams == 1:
                            j = random.randint(0,len(step_phase.technologies[i].rams)-1)
                            print('\t\t\t<string key="RAMID" value="' + step_phase.technologies[i].rams[j].id + '"/>')
                            print('\t\t\t<string key="RAMVolume" value="' + step_phase.technologies[i].rams[j].volume + '"/>')
                            print('\t\t\t<string key="RAMSpeed" value="' + step_phase.technologies[i].rams[j].speed + '"/>')
                            print('\t\t\t<string key="RAMProducer" value="' + step_phase.technologies[i].rams[j].producer + '"/>')
                            print('\t\t\t<string key="RAMType" value="' + step_phase.technologies[i].rams[j].type + '"/>')
                        #storages
                        if presence_of_storages == 1:
                            j = random.randint(0,len(step_phase.technologies[i].storages)-1)
                            print('\t\t\t<string key="StorageID" value="' + step_phase.technologies[i].storages[j].id + '"/>')
                            print('\t\t\t<string key="StorageVolume" value="' + step_phase.technologies[i].storages[j].volume + '"/>')
                            print('\t\t\t<string key="StorageSpeed" value="' + step_phase.technologies[i].storages[j].speed + '"/>')
                            print('\t\t\t<string key="Storageroducer" value="' + step_phase.technologies[i].storages[j].producer + '"/>')
                            print('\t\t\t<string key="StorageType" value="' + step_phase.technologies[i].storages[j].type + '"/>')
                        #networks
                        if presence_of_networks == 1:
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
def generateJSON(pipeline_id, pipeline_name, pipeline_medium, pipeline_traces, n, steps, step_phases, data_sources, environment_variables, technologies, cpus, gpus, rams, storages, networks, resources):
    print("Generating JSON file.")
    original_stdout = sys.stdout # Save a reference to the original standard output
    with open('data/' + pipeline_name + '.json', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print('{\n\t"PipelineID": "' + pipeline_id + '",\n\t"PipelineName": "' + pipeline_name + '",\n\t"PipelineCommunicationMedium": "' + pipeline_medium + '",\n\t"NumberOfTraces": "' + pipeline_traces + '",')
        s = ""
        for i in steps:
            s += '\t' + i.__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t},')
            s += '\n'
        n = 0
        while n < len(step_phases):
            s += '\t' + step_phases[n].__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t}')
            n += 1
            if n < len(step_phases):
                s += ',\n'
        if len(data_sources) > 0:
            n = 0
            s += ',\n'
            while n < len(data_sources):
                s += '\t' + data_sources[n].__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(data_sources):
                    s += ',\n'
        if len(environment_variables) > 0:
            n = 0
            s += ',\n'
            while n < len(environment_variables):
                s += '\t' + environment_variables[n].__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(environment_variables):
                    s += ',\n'           
        if len(technologies) > 0:
            n = 0
            s += ',\n'
            while n < len(technologies):
                s += '\t' + technologies[n].__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(technologies):
                    s += ',\n'       
        if len(cpus) > 0:
            n = 0
            s += ',\n'
            while n < len(cpus):
                s += '\t' + cpus[n].__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(cpus):
                    s += ',\n'                 
        if len(gpus) > 0:
            n = 0
            s += ',\n'
            while n < len(gpus):
                s += '\t' + gpus[n].__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(gpus):
                    s += ',\n'                  
        if len(rams) > 0:
            n = 0
            s += ',\n'
            while n < len(rams):
                s += '\t' + rams[n].__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(rams):
                    s += ',\n'               
        if len(storages) > 0:
            n = 0
            s += ',\n'
            while n < len(storages):
                s += '\t' + storages[n].__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(storages):
                    s += ',\n'           
        if len(networks) > 0:
            n = 0
            s += ',\n'
            while n < len(networks):
                s += '\t' + networks[n].__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(networks):
                    s += ',\n'
        if len(resources) > 0:
            n = 0
            s += ',\n'
            while n < len(resources):
                s += '\t' + resources[n].__str__().replace('\n\t','\n\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(resources):
                    s += ',\n'
        s += '\n}'
        print(s)
    sys.stdout = original_stdout # Reset the standard output to its original value