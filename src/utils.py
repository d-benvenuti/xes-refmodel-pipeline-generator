import classes
import sys
import random
from datetime import datetime
import time
import json
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
                print('\t\t<string key="StorageProducer" value="string"/>')
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
                        if len(step.resources) >= 1:
                            i = random.randint(0, len(step.resources)-1)
                            for resource in step.resources:
                                print('\t\t\t<string key="ResourceID" value="' + resource.id + '"/>')
                                print('\t\t\t<string key="org:resource" value="' + resource.name + '"/>')
                        if presence_of_continuum_layer == 1:
                            print('\t\t\t<string key="StepContinuumLayer" value="' + step.continuumLayer + '"/>')
                            print('\t\t\t<string key="StepType" value="' + step.type + '"/>')
                        #data sources
                        if len(step.dataSources) >= 1:
                            i = random.randint(0, len(step.dataSources)-1)
                            print('\t\t\t<string key="DataSourceID" value="' + step.dataSources[i].id + '"/>')
                            print('\t\t\t<string key="DataSourceName" value="' + step.dataSources[i].name + '"/>')
                            print('\t\t\t<string key="DataSourceVolume" value="' + step.dataSources[i].volume + '"/>')
                            if type(step.dataSources[i]) == type(classes.DataStream):
                                print('\t\t\t<string key="DataSourceVelocity" value="' + step.dataSources[i].velocity + '"/>')
                            else:
                                print('\t\t\t<string key="DataSourceVelocity" value="None"/>')
                            print('\t\t\t<string key="DataSourceType" value="' + step.dataSources[i].type + '"/>')
                        #technologies
                        if len(step_phase.technologies) >= 1:
                            i = random.randint(0, len(step_phase.technologies)-1)
                            print('\t\t\t<string key="TechnologyID" value="' + step_phase.technologies[i].id + '"/>')
                            print('\t\t\t<string key="TechnologyName" value="' + step_phase.technologies[i].name + '"/>')
                            print('\t\t\t<string key="TechnologyOS" value="' + step_phase.technologies[i].os + '"/>')
                            #cpus
                            if len(step_phase.technologies[i].cpus) >= 1:
                                j = random.randint(0, len(step_phase.technologies[i].cpus)-1)
                                print('\t\t\t<string key="CPUID" value="' + step_phase.technologies[i].cpus[j].id + '"/>')
                                print('\t\t\t<string key="CPUCores" value="' + step_phase.technologies[i].cpus[j].cores + '"/>')
                                print('\t\t\t<string key="CPUSpeed" value="' + step_phase.technologies[i].cpus[j].speed + '"/>')
                                print('\t\t\t<string key="CPUProducer" value="' + step_phase.technologies[i].cpus[j].producer + '"/>')
                            #gpus
                            if len(step_phase.technologies[i].gpus) >= 1:
                                j = random.randint(0, len(step_phase.technologies[i].gpus)-1)
                                print('\t\t\t<string key="GPUID" value="' + step_phase.technologies[i].gpus[j].id + '"/>')
                                print('\t\t\t<string key="GPUCores" value="' + step_phase.technologies[i].gpus[j].cores + '"/>')
                                print('\t\t\t<string key="GPUSpeed" value="' + step_phase.technologies[i].gpus[j].speed + '"/>')
                                print('\t\t\t<string key="GPUMemory" value="' + step_phase.technologies[i].gpus[j].memory + '"/>')
                                print('\t\t\t<string key="GPUProducer" value="' + step_phase.technologies[i].gpus[j].producer + '"/>')
                            #rams
                            if len(step_phase.technologies[i].rams) >= 1:
                                j = random.randint(0, len(step_phase.technologies[i].rams)-1)
                                print('\t\t\t<string key="RAMID" value="' + step_phase.technologies[i].rams[j].id + '"/>')
                                print('\t\t\t<string key="RAMVolume" value="' + step_phase.technologies[i].rams[j].volume + '"/>')
                                print('\t\t\t<string key="RAMSpeed" value="' + step_phase.technologies[i].rams[j].speed + '"/>')
                                print('\t\t\t<string key="RAMProducer" value="' + step_phase.technologies[i].rams[j].producer + '"/>')
                                print('\t\t\t<string key="RAMType" value="' + step_phase.technologies[i].rams[j].type + '"/>')
                            #storages
                            if len(step_phase.technologies[i].storages) >= 1:
                                j = random.randint(0, len(step_phase.technologies[i].storages)-1)
                                print('\t\t\t<string key="StorageID" value="' + step_phase.technologies[i].storages[j].id + '"/>')
                                print('\t\t\t<string key="StorageVolume" value="' + step_phase.technologies[i].storages[j].volume + '"/>')
                                print('\t\t\t<string key="StorageSpeed" value="' + step_phase.technologies[i].storages[j].speed + '"/>')
                                print('\t\t\t<string key="Storageroducer" value="' + step_phase.technologies[i].storages[j].producer + '"/>')
                                print('\t\t\t<string key="StorageType" value="' + step_phase.technologies[i].storages[j].type + '"/>')
                            #networks
                            if len(step_phase.technologies[i].networks) >= 1:
                                j = random.randint(0, len(step_phase.technologies[i].networks)-1)
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
        s = '\t"Steps":{\n'
        n = 0
        while n < len(steps):
            s += '\t\t' + steps[n].__str__().replace('\n\t','\n\t\t\t').replace('\n}','\n\t}')
            n += 1
            if n < len(steps):
                s += ','
            s += '\n'
        s += '\t},\n\t"StepPhases":{\n'
        n = 0
        while n < len(step_phases):
            s += '\t\t' + step_phases[n].__str__().replace('\n\t','\n\t\t\t').replace('\n}','\n\t}')
            n += 1
            if n < len(step_phases):
                s += ','
            s += '\n'
        s += '\t}'
        if len(data_sources) > 0:
            n = 0
            s += ',\n\t"DataSources":{\n'
            while n < len(data_sources):
                s += '\t\t' + data_sources[n].__str__().replace('\n\t','\n\t\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(data_sources):
                    s += ','
                s += '\n'
            s += '\t}'
        if len(environment_variables) > 0:
            n = 0
            s += ',\n\t"EnvironmentVariables":{\n'
            while n < len(environment_variables):
                s += '\t\t' + environment_variables[n].__str__().replace('\n\t','\n\t\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(environment_variables):
                    s += ','
                s += '\n'
            s += '\t}'
        if len(technologies) > 0:
            n = 0
            s += ',\n\t"Technologies":{\n'
            while n < len(technologies):
                s += '\t\t' + technologies[n].__str__().replace('\n\t','\n\t\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(technologies):
                    s += ','
                s += '\n'
            s += '\t}'
        if len(cpus) > 0:
            n = 0
            s += ',\n\t"CPUS":{\n'
            while n < len(cpus):
                s += '\t\t' + cpus[n].__str__().replace('\n\t','\n\t\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(cpus):
                    s += ','
                s += '\n'
            s += '\t}'
        if len(gpus) > 0:
            n = 0
            s += ',\n\t"GPUS":{\n'
            while n < len(gpus):
                s += '\t\t' + gpus[n].__str__().replace('\n\t','\n\t\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(gpus):
                    s += ','
                s += '\n'
            s += '\t}'
        if len(rams) > 0:
            n = 0
            s += ',\n\t"RAMS":{\n'
            while n < len(rams):
                s += '\t\t' + rams[n].__str__().replace('\n\t\t','\n\t\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(rams):
                    s += ','
                s += '\n'
            s += '\t}'
        if len(storages) > 0:
            n = 0
            s += ',\n\t"Storages":{\n'
            while n < len(storages):
                s += '\t\t' + storages[n].__str__().replace('\n\t','\n\t\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(storages):
                    s += ','
                s += '\n'
            s += '\t}'
        if len(networks) > 0:
            n = 0
            s += ',\n\t"Networks":{\n'
            while n < len(networks):
                s += '\t\t' + networks[n].__str__().replace('\n\t','\n\t\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(networks):
                    s += ','
                s += '\n'
            s += '\t}'
        if len(resources) > 0:
            n = 0
            s += ',\n\t"Resources":{\n'
            while n < len(resources):
                s += '\t\t' + resources[n].__str__().replace('\n\t','\n\t\t\t').replace('\n}','\n\t}')
                n += 1
                if n < len(resources):
                    s += ','
                s += '\n'
            s += '\t}'
        s += '\n}'
        print(s)
    sys.stdout = original_stdout # Reset the standard output to its original value
#--------------------------------------------------------------------
#function to import the data sources from JSON file
#--------------------------------------------------------------------
def importJSON(filename, steps, step_phases, data_sources, technologies, resources, environment_variables, cpus,  gpus, rams, storages, networks ):
    print("Importing from: " + filename)
    # OPEN THE FILE
    f = open(filename)
    # LOAD THE JSON DICT
    data = json.load(f)
    # CLOSE THE FILE
    f.close()
    pipeline_details = []
    info_found = 0
    #PARSE ALL THE KEYS
    for i in data.keys():
        # PARSE PIPELINE DETAILS
        if 'PipelineID' in i:
            info_found += 1
            pipeline_details.append(data[i])
        if 'PipelineName' in i:
            info_found += 1
            pipeline_details.append(data[i])
        if 'PipelineCommunicationMedium' in i:
            info_found += 1
            pipeline_details.append(data[i])
        if 'NumberOfTraces' in i:
            info_found += 1
            pipeline_details.append(data[i])
        # PARSE ALL THE CLASSES
        if 'Steps' in i:
            for j in data[i].keys():
                info_found += 1
                step_j = data[i][j]
                new_step = classes.Step(step_j['ID'], step_j['Name'], step_j['Continuum Layer'], step_j['Type'])
                # PARSE THE RELATIONS BETWEEN STEPS AND OTHER CLASSES
                for z in data[i][j].keys():
                    if 'StepPhase' in z:
                        info_found += 1
                        new_step.stepPhases.append(classes.StepPhase(data[i][j][z]['ID'], data[i][j][z]['Name']))
                    if 'DataSource' in z:
                        info_found += 1
                        new_step.dataSources.append( classes.DataSource(data[i][j][z]['ID'], data[i][j][z]['Name'], data[i][j][z]['Volume'], data[i][j][z]['Type']))
                    if 'DataStream' in z:
                        info_found += 1
                        new_step.dataSources.append(classes.DataStream(data[i][j][z]['ID'],data[i][j][z]['Name'], data[i][j][z]['Volume'], data[i][j][z]['Type'], data[i][j][z]['Velocity']))
                    if 'Resource' in z:
                        info_found += 1
                        new_step.resources.append(classes.Resource(data[i][j][z]['ID'],data[i][j][z]['Name']))
                steps.append(new_step)
        if 'StepPhases' in i:
            for j in data[i].keys():
                info_found += 1
                step_phase_j = data[i][j]
                new_step_phase = classes.StepPhase(step_phase_j['ID'], step_phase_j['Name'])
                # PARSE THE RELATIONS BETWEEN STEP PHASES AND OTHER CLASSES
                for z in data[i][j].keys():
                    if 'Technology' in z:
                        info_found += 1
                        new_step_phase.technologies.append(classes.Technology(data[i][j][z]['ID'], data[i][j][z]['Name'], data[i][j][z]['OS']))
                    if 'EnvironmentVariable' in z:
                        info_found += 1
                        new_step_phase.environmentVariables.append(classes.EnvironmentVariable(data[i][j][z]['Key'], data[i][j][z]['Value']))
                step_phases.append(new_step_phase)
        if 'DataSources' in i:
            for j in data[i].keys():
                info_found += 1
                data_source_j = data[i][j]
                if 'Velocity' in data[i][j].keys():
                    new_data_source = classes.DataStream(data_source_j['ID'], data_source_j['Name'], data_source_j['Volume'], data_source_j['Type'], data_source_j['Velocity'])
                    data_sources.append(new_data_source)           
                else:
                    new_data_stream = classes.DataSource(data_source_j['ID'], data_source_j['Name'], data_source_j['Volume'], data_source_j['Type'])
                    data_sources.append(new_data_stream)
        if 'EnvironmentVariables' in i:
            for j in data[i].keys():
                info_found += 1
                environment_variable_j = data[i][j]
                new_environment_variable = classes.EnvironmentVariable(environment_variable_j['Key'], environment_variable_j['Value'])
                environment_variables.append(new_environment_variable)
        if 'Technologies' in i:
            for j in data[i].keys():
                info_found += 1
                technology_j = data[i][j]
                new_technology = classes.Technology(technology_j['ID'], technology_j['Name'], technology_j['OS'])
                # PARSE THE RELATIONS BETWEEN TECHNOLOGIES AND OTHER CLASSES
                for z in data[i][j].keys():
                    if 'CPU' in z:
                        info_found += 1
                        new_technology.cpus.append(classes.CPU(data[i][j][z]['ID'], data[i][j][z]['Cores'], data[i][j][z]['Speed'], data[i][j][z]['Producer']))
                    if 'GPU' in z:
                        info_found += 1
                        new_technology.gpus.append(classes.GPU(data[i][j][z]['ID'], data[i][j][z]['Cores'], data[i][j][z]['Speed'], data[i][j][z]['Memory'], data[i][j][z]['Producer']))
                    if 'RAM' in z:
                        info_found += 1
                        new_technology.rams.append(classes.RAM(data[i][j][z]['ID'], data[i][j][z]['Volume'], data[i][j][z]['Speed'], data[i][j][z]['Type'], data[i][j][z]['Producer']))
                    if 'Storage' in z:
                        info_found += 1
                        new_technology.storages.append(classes.Storage(data[i][j][z]['ID'], data[i][j][z]['Volume'], data[i][j][z]['Speed'], data[i][j][z]['Type'], data[i][j][z]['Producer']))
                    if 'Network' in z:
                        info_found += 1
                        new_technology.networks.append(classes.Network(data[i][j][z]['ID'], data[i][j][z]['Bandwidth'], data[i][j][z]['Latency']))
                technologies.append(new_technology)
        if 'CPUS' in i:
            for j in data[i].keys():
                info_found += 1
                cpu_j = data[i][j]
                new_cpu = classes.CPU(cpu_j['ID'], cpu_j['Cores'], cpu_j['Speed'], cpu_j['Producer'])
                cpus.append(new_cpu)
        if 'GPUS' in i:
            for j in data[i].keys():
                info_found += 1
                gpu_j = data[i][j]
                new_gpu = classes.GPU(gpu_j['ID'], gpu_j['Cores'], gpu_j['Speed'], gpu_j['Memory'], gpu_j['Producer'])
                gpus.append(new_gpu)
        if 'RAMS' in i:
            for j in data[i].keys():
                info_found += 1
                ram_j = data[i][j]
                new_ram = classes.RAM(ram_j['ID'], ram_j['Volume'], ram_j['Speed'], ram_j['Type'], ram_j['Producer'])
                rams.append(new_ram)
        if 'Storages' in i:
            for j in data[i].keys():
                info_found += 1
                storage_j = data[i][j]
                new_storage = classes.Storage(storage_j['ID'], storage_j['Volume'], storage_j['Speed'], storage_j['Type'], storage_j['Producer'])
                storages.append(new_storage)
        if 'Networks' in i:
            for j in data[i].keys():
                info_found += 1
                network_j = data[i][j]
                new_network = classes.Network(network_j['ID'], network_j['Bandwidth'], network_j['Latency'])
                networks.append(new_network)
        if 'Resources' in i:
            for j in data[i].keys():
                info_found += 1
                resource_j = data[i][j]
                new_resource = classes.Resource(resource_j['ID'], resource_j['Name'])
                resources.append(new_resource)
    # END and return details
    if info_found == 0:
        return -1
    else: 
        pipeline_details.append(info_found)
        return pipeline_details