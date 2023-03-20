from PyQt5 import QtWidgets, uic, QtCore, QtGui
import sys
import numpy as np
from PyQt5.QtWidgets import QMessageBox, QDialog
import random
from datetime import datetime
import time
#------------------------------------------------------------------
#------------------------------------------------------------------
#DEFINE ALL THE CLASSES IN THE UML
#------------------------------------------------------------------
#------------------------------------------------------------------

#STEP
class Step():
    #CONSTRUCTOR
    def __init__(self, id, name, continuumLayer, type):
        self.id = id
        self.name = name
        self.continuumLayer = continuumLayer
        self.type = type
    #TO STRING
    def __str__(self):
        return '"Step": {\n\t"ID": "' + self.id + '",\n\t"Name": "' + self.name + '",\n\t"Continuum Layer": "' + self.continuumLayer + '",\n\t"Type": "' + self.type + '"\n}'
     
#STEP PHASE
class StepPhase():
    #CONSTRUCTOR
    def __init__(self, id, name):
        self.id = id
        self.name = name
    #TO STRING
    def __str__(self):
        return '"StepPhase": {\n\t"ID": "' + self.id + '",\n\t"Name": "' + self.name + '"\n}'
        
#ENVIRONMENT VARIABLE
class EnvironmentVariable():
    #CONSTRUCTOR
    def __init__(self, key, value):
        self.key = key
        self.value = value
    #TO STRING
    def __str__(self):
        return '"EnvironmentVariable": {\n\t"Key": "' + self.key + '",\n\t"Value": "' + self.value + '"\n}'
        
#DATA SOURCE
class DataSource():
    #CONSTRUCTOR
    def __init__(self, id, name, volume, type):
        self.id = id
        self.name = name
        self.volume = volume
        self.type = type
    #TO STRING
    def __str__(self):
        return '"DataSource": {\n\t"ID": "' + self.id + '",\n\t"Name": "' + self.name + '",\n\t"Volume": "' + self.volume + '",\n\t"Type": "' + self.type + '"\n}'

#DATA STREAM   
class DataStream(DataSource):
   #CONSTRUCTOR
    def __init__(self, id, name, volume, type, velocity):
        super().__init__(id, name, volume, type)
        self.velocity = velocity
    #TO STRING
    def __str__(self):
        return '"DataStream": {\n\t"ID": "' + self.id + '",\n\t"Name": "' + self.name + '",\n\t"Volume": "' + self.volume + '",\n\t"Type": "' + self.type + '",\n\t"Velocity": "' + self.velocity + '"\n}'

#TECHNOLOGY
class Technology():
#CONSTRUCTOR
    def __init__(self, id, name, os):
        self.id = id
        self.name = name
        self.os = os
    #TO STRING
    def __str__(self):
        return '"Technology": {\n\t"ID": "' + self.id + '",\n\t"Name": "' + self.name + '",\n\t"OS": "' + self.os + '"\n}'

#RAM
class RAM():
    def __init__(self, id, volume, speed, type, producer):
        self.id = id
        self.volume = volume
        self.speed = speed
        self.type = type
        self.producer = producer
    #TO STRING
    def __str__(self):
        return '"RAM": {\n\t"ID": "' + self.id + '",\n\t"Volume": "' + self.volume + '",\n\t"Speed": "' + self.speed + '",\n\t"Type": "' + self.type + '",\n\t"Producer": "' + self.producer + '"\n}'
    
#GPU
class GPU():
    def __init__(self, id, cores, speed, memory, producer):
        self.id = id
        self.cores = cores
        self.speed = speed
        self.memory = memory
        self.producer = producer
    #TO STRING
    def __str__(self):
        return '"GPU": {\n\t"ID": "' + self.id + '",\n\t"Cores": "' + self.cores + '",\n\t"Speed": "' + self.speed + '",\n\t"Memory": "' + self.memory + '",\n\t"Producer": "' + self.producer + '"\n}'

#CPU
class CPU():
    def __init__(self, id, cores, speed, producer):
        self.id = id
        self.cores = cores
        self.speed = speed
        self.producer = producer
    #TO STRING
    def __str__(self):
        return '"CPU": {\n\t"ID": "' + self.id + '",\n\t"Cores": "' + self.cores + '",\n\t"Speed": "' + self.speed + '",\n\t"Producer": "' + self.producer + '"\n}'
        
#STORAGE
class Storage():
    def __init__(self, id, volume, speed, type, producer):
        self.id = id
        self.volume = volume
        self.speed = speed
        self.type = type
        self.producer = producer
    #TO STRING
    def __str__(self):
        return '"Storage": {\n\t"ID": "' + self.id + '",\n\t"Volume": "' + self.volume + '",\n\t"Speed": "' + self.speed + '",\n\t"Type": "' + self.type + '",\n\t"Producer": "' +self.producer + '"\n}'

#NETWORK
class Network():
    def __init__(self, id, bandwidth, latency):
        self.id = id
        self.bandwidth = bandwidth
        self.latency = latency
    #TO STRING
    def __str__(self):
        return '"Network": {\n\t"ID": "' + self.id + '",\n\t"Bandwidth": "' + self.bandwidth + '",\n\t"Latency": "' + self.latency + '"\n}' 

#------------------------------------------------------------------          
#------------------------------------------------------------------       
#DEFINE AND CREATE ALL THE WINDOWS
#------------------------------------------------------------------
#------------------------------------------------------------------  

#DEFINITION OF THE MAIN WINDOW
class UiMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiMainWindow, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ui/main_window.ui', self) # Load the .ui file
        self.w = None  # No external window yet.
        self.show() # Show the GUI
        #CONNECT BUTTONS AND ACTIONS
        self.generateButton.clicked.connect(self.generateLog)
        #------------------------ ADD ------------------------
        self.actionAddStep.triggered.connect(self.addStep) # Remember to pass the definition/method, not the return value!
        self.actionAddStepPhase.triggered.connect(self.addStepPhase)
        self.actionAddEnvironmentVariable.triggered.connect(self.addEnvironmentVariable)
        self.actionAddDataSource.triggered.connect(self.addDataSource)
        self.actionAddTechnology.triggered.connect(self.addTechnology)
        self.actionAddCPU.triggered.connect(self.addCPU)
        self.actionAddGPU.triggered.connect(self.addGPU)
        self.actionAddRAM.triggered.connect(self.addRAM)
        self.actionAddStorage.triggered.connect(self.addStorage)
        self.actionAddNetwork.triggered.connect(self.addNetwork)
        #------------------------ VIEW ------------------------
        self.actionViewSteps.triggered.connect(self.printSteps)
        self.actionViewStepPhases.triggered.connect(self.printStepPhases)
        self.actionViewEnvironmentVariables.triggered.connect(self.printEnvironmentVariables)
        self.actionViewDataSources.triggered.connect(self.printDataSources)
        self.actionViewTechnologies.triggered.connect(self.printTechnologies)
        self.actionViewCPUs.triggered.connect(self.printCPUs)
        self.actionViewGPUs.triggered.connect(self.printGPUs)
        self.actionViewRAMs.triggered.connect(self.printRAMs)
        self.actionViewStorages.triggered.connect(self.printStorages)
        self.actionViewNetworks.triggered.connect(self.printNetworks)
        self.actionViewAll.triggered.connect(self.printAll)
        #------------------------ DELETE -----------------------
        self.actionDeleteStep.triggered.connect(self.deleteStep)
        self.actionDeleteStepPhase.triggered.connect(self.deleteStepPhase)
        self.actionDeleteDataSource.triggered.connect(self.deleteDataSource)
        self.actionDeleteEnvironmentVariable.triggered.connect(self.deleteEnvironmentVariable)
        self.actionDeleteTechnology.triggered.connect(self.deleteTechnology)
        self.actionDeleteCPU.triggered.connect(self.deleteCPU)
        self.actionDeleteGPU.triggered.connect(self.deleteGPU)
        self.actionDeleteRAM.triggered.connect(self.deleteRAM)
        self.actionDeleteStorage.triggered.connect(self.deleteStorage)
        self.actionDeleteNetwork.triggered.connect(self.deleteNetwork)
    #CLOSE EVENT
    def closeEvent(self, event):
        if self.w is not None:
            self.w.close()
    #------------------------------------------------------------------
    #FUNCTIONS
    def generateXES(self, pipeline_id, pipeline_name, pipeline_medium, pipeline_traces, n):
        print("Generating XES file.")
    def generateJSON(self, pipeline_id, pipeline_name, pipeline_medium, pipeline_traces, n):
        print("Generating JSON file.")
        original_stdout = sys.stdout # Save a reference to the original standard output
        with open(pipeline_name + '.json', 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print('{\n\t"PipelineID": "' + pipeline_id + '",\n\t"PipelineName": "' + pipeline_name + '",\n\t"PipelineCommunicationMedium": "' + pipeline_medium + '",')
            while n > 0:
                print('\t"Trace' + str(n) + '": {')
                i = 0
                while i < len(steps):
                    #print the step    
                    print('\t\t' + steps[i].__str__().replace('\n','\n\t\t').replace('"\n\t\t}','"').replace('Step','Step'+str(i+1)) + ',')
                    j = 0
                    while j < len(step_phases):
                        #print the step phase
                        print('\t\t\t"StepPhase' + str(j+1) + '": {\n\t\t\t\t"Timestamp": "' + datetime.now().strftime('%m/%d/%Y, %H:%M:%S:%f') + '",\n\t\t\t\t"ID": "' + step_phases[j].id + '",\n\t\t\t\t"Name": "' + step_phases[j].name + '"')
                        #see how many objects we have
                        num_datasources = len(data_sources)
                        num_technologies = len(technologies)
                        num_envvar = len(environment_variables)
                        num_cpu = len(cpus)
                        num_gpu = len(gpus)
                        num_ram = len(rams)
                        num_storage = len(storages)
                        num_network = len(networks)
                        #for each object, if the array is not null
                        if num_datasources > 0:
                            #get a random number between 0 and length of the array-1 and print
                            print('\t\t\t\t,' + data_sources[random.randint(0, num_datasources-1)].__str__().replace('\n', '\n\t\t\t\t'))
                        if num_technologies > 0:
                            print('\t\t\t\t,' + technologies[random.randint(0, num_technologies-1)].__str__().replace('\n', '\n\t\t\t\t'))
                        if num_envvar > 0:
                            print('\t\t\t\t,' + environment_variables[random.randint(0, num_envvar-1)].__str__().replace('\n', '\n\t\t\t\t'))
                        if num_cpu > 0:
                            print('\t\t\t\t,' + cpus[random.randint(0, num_cpu-1)].__str__().replace('\n', '\n\t\t\t\t'))
                        if num_gpu > 0:
                            print('\t\t\t\t,' + gpus[random.randint(0, num_gpu-1)].__str__().replace('\n', '\n\t\t\t\t'))
                        if num_storage > 0:
                            print('\t\t\t\t,' + storages[random.randint(0, num_storage-1)].__str__().replace('\n', '\n\t\t\t\t'))
                        if num_network > 0:
                            print('\t\t\t\t,' + networks[random.randint(0, num_network-1)].__str__().replace('\n', '\n\t\t\t\t'))
                        if num_ram > 0:
                            print('\t\t\t\t,' + rams[random.randint(0, num_ram-1)].__str__().replace('\n', '\n\t\t\t\t'))
                        #close stepphase
                        j += 1
                        if j == len(step_phases):
                            print('\t\t\t}')
                        else:    
                            print('\t\t\t},')
                    #close step
                    i  += 1
                    if i == len(steps):
                        print('\t\t}')
                    else:
                        print('\t\t},')
                #close trace and go to the next and reset firstStep
                if (n != 0):
                    print('\t},')
                else:
                    print('\t}')
                n -= 1
            #close root
            print('}')
        sys.stdout = original_stdout # Reset the standard output to its original value
    #------------------------------------------------------------------
    #FUNCTION TO GENERATE BOTH XES AND JSON FILES
    def generateLog(self):
        print('XES button clicked.')
        #READ VALUES FROM lineEdit
        pipeline_id = self.lineEdit_id.text()
        pipeline_medium = self.lineEdit_medium.text()
        pipeline_name = self.lineEdit_name.text()
        pipeline_traces = self.lineEdit_traces.text()
        #CHECK FOR MISSING INPUTS
        if len(steps) == 0:
            print('At least 1 Step is needed.')
            msg.setText('At least 1 Step is needed.')
            msg.exec()
            return -1
        elif len(step_phases) == 0:
            print('At least 1 Step Phase is needed.')
            msg.setText('At least 1 Step Phase is needed.')
            msg.exec()
            return -1
        elif pipeline_id == "":
            print("Big Data Pipeline ID can not be null.")
            msg.setText("Big Data Pipeline ID can not be null.")
            msg.exec()
            return -1
        elif pipeline_medium == "":
            print("Big Data Pipeline Communication Medium can not be null.")
            msg.setText("Big Data Pipeline Communication Medium can not be null.")
            msg.exec()
            return -1
        elif pipeline_name == "":  
            print("Big Data Pipeline Name can not be null.")
            msg.setText("Big Data Pipeline Name can not be null.")
            msg.exec()
            return -1
        elif pipeline_traces == "":
            print("Big Data Pipeline Number of Traces can not be null.")
            msg.setText("Big Data Pipeline Number of Traces can not be null.")
            msg.exec()
            return -1
        else:
            #---------- CHECK FOR ERRORS IN NUMBER OF TRACES
            try:
                n = int(pipeline_traces)
            except ValueError as ve:
                print('Number of Traces must be a number.')
                msg.setText('Number of Traces must be a number.')
                msg.exec()
                return -2
            if n <= 0:
                print('Number of Traces must be positive.')
                msg.setText('Number of Traces must be positive.')
                msg.exec()
                return -3
            #GENERATE THE LOG IN XES AND JSON
            self.generateJSON(pipeline_id, pipeline_name, pipeline_medium, pipeline_traces, n)
            self.generateXES(pipeline_id, pipeline_name, pipeline_medium, pipeline_traces, n)
            #-------------------------------------- CLOSE THE APP
            self.close()
            return 1
    #FUNCTION TO ADD A NEW STEP
    def addStep(self):
        self.setEnabled(0)
        print("Add-Step action clicked.")
        self.w = UiStepWindow()
        self.w.show()
    #FUNCTION TO ADD A NEW STEP PHASE
    def addStepPhase(self):
        self.setEnabled(0)
        print("Add-StepPhase action clicked.")
        self.w = UiStepPhaseWindow()
        self.w.show()
    #FUNCTION TO ADD A NEW ENVIRONMENT VARIABLE
    def addEnvironmentVariable(self):
        self.setEnabled(0)
        print("Add-EnvironmentVariable action clicked.")
        self.w = UiEnvironmentVariableWindow()
        self.w.show()
    #FUNCTION TO ADD A NEW DATA SOURCE
    def addDataSource(self):
        self.setEnabled(0)
        print("Add-DataSource action clicked.")
        self.w = UiDataSourceWindow()
        self.w.show()
    #FUNCTION TO ADD A NEW TECHNOLOGY
    def addTechnology(self):
        self.setEnabled(0)
        print("Add-Technology action clicked.")
        self.w = UiTechnologyWindow()
        self.w.show()
    #FUNCTION TO ADD A NEW CPU
    def addCPU(self):
        self.setEnabled(0)
        print("Add-CPU action clicked.")
        self.w = UiCPUWindow()
        self.w.show()
    #FUNCTION TO ADD A NEW GPU
    def addGPU(self):
        self.setEnabled(0)
        print("Add-GPU action clicked.")
        self.w =UiGPUWindow()
        self.w.show()
    #FUNCTION TO ADD A NEW RAM
    def addRAM(self):
        self.setEnabled(0)
        print("Add-RAM action clicked.")
        self.w = UiRAMWindow()
        self.w.show()
    #FUNCTION TO ADD A NEW STORAGE
    def addStorage(self):
        self.setEnabled(0)
        print("Add-Storage action clicked.")
        self.w = UiStorageWindow()
        self.w.show()
    #FUNCTION TO ADD A NEW NETWORK 
    def addNetwork(self):
        self.setEnabled(0)
        print("Add-Network action clicked.")
        self.w = UiNetworkWindow()
        self.w.show()
    
    #------------------------------------------------------------------
    #FUNCTIONS TO PRINT OBJECTS
    #------------------------------------------------------------------ 
    
    #FUNCTION TO PRINT THE LIST OF STEPS
    def printSteps(self):
        print("View-Step action clicked.")
        to_print = ""
        for i in steps:
            print(i)
            to_print = to_print + i.__str__() + '\n'
        self.setEnabled(0)
        self.w = UiViewerWindow()
        self.w.textBox.setText(to_print)
        self.w.show()
    #FUNCTION TO PRINT THE LIST OF STEP PHASES
    def printStepPhases(self):
        print("View-StepPhases action clicked.")
        to_print = ""
        for i in step_phases:
            print(i)
            to_print = to_print + i.__str__() + '\n'
        self.setEnabled(0)
        self.w = UiViewerWindow()
        self.w.textBox.setText(to_print)
        self.w.show()
    #FUNCTION TO PRINT THE LIST OF ENVIRONMENT VARIABLES
    def printEnvironmentVariables(self):
        print("View-EnvironmentVariables action clicked.")
        to_print = ""
        for i in environment_variables:
            print(i)
            to_print = to_print + i.__str__() + '\n'
        self.setEnabled(0)
        self.w = UiViewerWindow()
        self.w.textBox.setText(to_print)
        self.w.show()
    #FUNCTION TO PRINT THE LIST OF DATA SOURCES
    def printDataSources(self):
        print("View-DataSources action clicked.")
        to_print = ""
        for i in data_sources:
            print(i)
            to_print = to_print + i.__str__() + '\n'
        self.setEnabled(0)
        self.w = UiViewerWindow()
        self.w.textBox.setText(to_print)
        self.w.show()
    #FUNCTION TO PRINT THE LIST OF TECHNOLOGIES
    def printTechnologies(self):
        print("View-Technologies action clicked.")
        to_print = ""
        for i in technologies:
            print(i)
            to_print = to_print + i.__str__() + '\n'
        self.setEnabled(0)
        self.w = UiViewerWindow()
        self.w.textBox.setText(to_print)
        self.w.show()
    #FUNCTION TO PRINT THE LIST OF CPUS
    def printCPUs(self):
        print("View-CPUs action clicked.")
        to_print = ""
        for i in cpus:
            print(i)
            to_print = to_print + i.__str__() + '\n'
        self.setEnabled(0)
        self.w = UiViewerWindow()
        self.w.textBox.setText(to_print)
        self.w.show()
    #FUNCTION TO PRINT THE LIST OF GPUS
    def printGPUs(self):
        print("View-GPUs action clicked.")
        to_print = ""
        for i in gpus:
            print(i)
            to_print = to_print + i.__str__() + '\n'
        self.setEnabled(0)
        self.w = UiViewerWindow()
        self.w.textBox.setText(to_print)
        self.w.show()
    #FUNCTION TO PRINT THE LIST OF RAMS
    def printRAMs(self):
        print("View-RAMs action clicked.")
        to_print = ""
        for i in rams:
            print(i)
            to_print = to_print + i.__str__() + '\n'
        self.setEnabled(0)
        self.w = UiViewerWindow()
        self.w.textBox.setText(to_print)
        self.w.show()
    #FUNCTION TO PRINT THE LIST OF STORAGES
    def printStorages(self):
        print("View-Storages action clicked.")
        to_print = ""
        for i in storages:
            print(i)
            to_print = to_print + i.__str__() + '\n'
        self.setEnabled(0)
        self.w = UiViewerWindow()
        self.w.textBox.setText(to_print)
        self.w.show()
    #FUNCTION TO PRINT THE LIST OF NETWORKS
    def printNetworks(self):
        print("View-Networks action clicked.")
        to_print = ""
        for i in networks:
            print(i)
            to_print = to_print + i.__str__() + '\n'
        self.setEnabled(0)
        self.w = UiViewerWindow()
        self.w.textBox.setText(to_print)
        self.w.show()
    #FUNCTION TO PRINT ALL
    def printAll(self):
        print("View-All action clicked")
        to_print = np.concatenate((steps, step_phases, data_sources, environment_variables, technologies, cpus, gpus, rams, storages, networks))
        to_print_str = ""
        for i in to_print:
            print(i)
            to_print_str = to_print_str + '\n' + i.__str__()
        self.setEnabled(0)
        self.w = UiViewerWindow()
        self.w.textBox.setText(to_print_str)
        self.w.show()
    
    #------------------------------------------------------------------
    #FUNCTIONS TO PRINT OBJECTS
    #------------------------------------------------------------------ 
    
    #FUNCTION TO DELETE STEP
    def deleteStep(self):
        print("Delete-Step action clicked")
        #CHECK IF THERE IS AT LEAST ONE
        if len(steps) == 0:
            msg.setText("There is no Step to delete.")
            msg.exec()
            return -2
        #ASK FOR ID
        dialog.exec()
        for i in steps:
            if dialog.id == i.id:
                #IF IT IS IN THE DATA STRUCTURE DELETE IT
                steps.remove(i)
                print("Step removed.")
                return 1
        #IF THERE IS NO MATCH
        print("There is no Step with the given ID.")
        msg.setText("There is no Step with the given ID.")
        msg.exec()
        return -1
           
    #FUNCTION TO DELETE STEP PHASE
    def deleteStepPhase(self):
        print("Delete-StepPhase action clicked")
        #CHECK IF THERE IS AT LEAST ONE
        if len(step_phases) == 0:
            msg.setText("There is no Step Phase to delete.")
            msg.exec()
            return -2
        #ASK FOR ID
        dialog.exec()
        for i in step_phases:
            if dialog.id == i.id:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    step_phases.remove(i)
                    print("Step Phase removed.")
                    return 1
        #IF THERE IS NO MATCH
        print("There is no Step Phase with the given ID.")
        msg.setText("There is no Step Phase with the given ID.")
        msg.exec()
        return -1  
        
    #FUNCTION TO DELETE DATA SOURCE
    def deleteDataSource(self):
        print("Delete-DataSource action clicked")
        #CHECK IF THERE IS AT LEAST ONE
        if len(data_sources) == 0:
            msg.setText("There is no Data Source to delete.")
            msg.exec()
            return -2
        #ASK FOR ID
        dialog.exec()
        for i in data_sources:
            if dialog.id == i.id:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    data_sources.remove(i)
                    print("Data Source removed.")
                    return 1
        #IF THERE IS NO MATCH
        print("There is no Data Source with the given ID.")
        msg.setText("There is no Data Source with the given ID.")
        msg.exec()
        return -1   
        
    #FUNCTION TO DELETE ENVIRONMENT VARIABLE
    def deleteEnvironmentVariable(self):
        print("Delete-EnvironmentVariable action clicked")
        #CHECK IF THERE IS AT LEAST ONE
        if len(environment_variables) == 0:
            msg.setText("There is no Environment Variable to delete.")
            msg.exec()
            return -2
        #ASK FOR ID
        dialog.exec()
        for i in environment_variables:
            if dialog.id == i.key:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    environment_variables.remove(i)
                    print("Environment Variable removed.")
                    return 1
        #IF THERE IS NO MATCH
        print("There is no Environment Variable with the given key.")
        msg.setText("There is no Environment Variable with the given key.")
        msg.exec()
        return -1
        
    #FUNCTION TO DELETE TECHNOLOGY
    def deleteTechnology(self):
        print("Delete-Technology action clicked")
        #CHECK IF THERE IS AT LEAST ONE
        if len(technologies) == 0:
            msg.setText("There is no Technology to delete.")
            msg.exec()
            return -2
        #ASK FOR ID
        dialog.exec()
        for i in technologies:
            if dialog.id == i.id:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    technologies.remove(i)
                    print("Technology removed.")
                    return 1
        #IF THERE IS NO MATCH
        print("There is no Technology with the given ID.")
        msg.setText("There is no Technology with the given ID.")
        msg.exec()
        return -1
        
    #FUNCTION TO DELETE CPU
    def deleteCPU(self):
        print("Delete-CPU action clicked")
        #CHECK IF THERE IS AT LEAST ONE
        if len(cpus) == 0:
            msg.setText("There is no CPU to delete.")
            msg.exec()
            return -2
        #ASK FOR ID
        dialog.exec()
        for i in cpus:
            if dialog.id == i.id:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    cpus.remove(i)
                    print("CPU removed.")
                    return 1
        #IF THERE IS NO MATCH
        print("There is no CPU with the given ID.")
        msg.setText("There is no CPU with the given ID.")
        msg.exec()
        return -1
        
    #FUNCTION TO DELETE GPU
    def deleteGPU(self):
        print("Delete-GPU action clicked")
        #CHECK IF THERE IS AT LEAST ONE
        if len(gpus) == 0:
            msg.setText("There is no GPU to delete.")
            msg.exec()
            return -2
        #ASK FOR ID
        dialog.exec()
        for i in gpus:
            if dialog.id == i.id:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    gpus.remove(i)
                    print("GPU removed.")
                    return 1
        #IF THERE IS NO MATCH
        print("There is no GPU with the given ID.")
        msg.setText("There is no GPU with the given ID.")
        msg.exec()
        return -1
        
    #FUNCTION TO DELETE RAM
    def deleteRAM(self):
        print("Delete-RAM action clicked")
        #CHECK IF THERE IS AT LEAST ONE
        if len(rams) == 0:
            msg.setText("There is no RAM to delete.")
            msg.exec()
            return -2
        #ASK FOR ID
        dialog.exec()
        for i in rams:
            if dialog.id == i.id:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    rams.remove(i)
                    print("RAM removed.")
                    return 1
        #IF THERE IS NO MATCH
        print("There is no RAM with the given ID.")
        msg.setText("There is no RAM with the given ID.")
        msg.exec()
        return -1
        
    #FUNCTION TO DELETE STORAGE
    def deleteStorage(self):
        print("Delete-STORAGE action clicked")
        #CHECK IF THERE IS AT LEAST ONE
        if len(storages) == 0:
            msg.setText("There is no Storage to delete.")
            msg.exec()
            return -2
        #ASK FOR ID
        dialog.exec()
        for i in storages:
            if dialog.id == i.id:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    storages.remove(i)
                    print("Storage removed.")
                    return 1
        #IF THERE IS NO MATCH
        print("There is no Storage with the given ID.")
        msg.setText("There is no Storage with the given ID.")
        msg.exec()
        return -1
    #FUNCTION TO DELETE NETWORK
    def deleteNetwork(self):
        print("Delete-Network action clicked")
        #CHECK IF THERE IS AT LEAST ONE
        if len(networks) == 0:
            msg.setText("There is no Network to delete.")
            msg.exec()
            return -2
        #ASK FOR ID
        dialog.exec()
        for i in networks:
            if dialog.id == i.id:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    networks.remove(i)
                    print("Network removed.")
                    return 1
        #IF THERE IS NO MATCH
        print("There is no Network with the given ID.")
        msg.setText("There is no Network with the given ID.")
        msg.exec()
        return -1
        
#DEFINITION OF THE VIEWER WINDOW
class UiViewerWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiViewerWindow, self).__init__()
        uic.loadUi('ui/viewer.ui', self)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1)

#DEFINITION OF THE DIALOG WINDOW
class UiDialogWindow(QtWidgets.QDialog):
    def __init__(self):
        super(UiDialogWindow, self).__init__()
        uic.loadUi('ui/dialog.ui', self)
        #VARIABLE TO STORE THE RESULT
        self.id = ''
        #CONNECT BUTTONS AND ACTIONS
        self.delete_button.clicked.connect(self.delete)
    
    def delete(self):
        print("Delete button pressed in dialog window.")
        self.id = self.lineEdit_id.text()
        self.close()

#DEFINITION OF THE STEP WINDOW
class UiStepWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiStepWindow, self).__init__()
        uic.loadUi('ui/add_step.ui', self)
        #CONNECT BUTTONS AND ACTIONS
        self.add_button.clicked.connect(self.add)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1) 
    #FUNCTION TO APPEND THE NEW STEP
    def add(self):
        print("Add button pressed in add_step window.")
        #READ VALUES FROM lineEdit
        step_id = self.lineEdit_id.text() 
        step_name = self.lineEdit_name.text()
        #READ VALUES FROM RADIOBUTTONS
        if self.radioButtonEdge.isChecked():
            step_continuum = "Edge"
        elif self.radioButtonCloud.isChecked():
            step_continuum = "Cloud"
        elif self.radioButtonFog.isChecked():
            step_continuum = "Fog"
        if self.radioButtonProcessing.isChecked():
            step_type = "Processing"
        elif self.radioButtonProducer.isChecked():
            step_type = "Producer"
        elif self.radioButtonConsumer.isChecked():
            step_type = "Consumer"
        #CHECK FOR MISSING INPUT
        if step_id == "":
            print("Step ID can not be null.")
            msg.setText("Step ID can not be null.")
            msg.exec()
            return -1
        if step_name == "":
            print("Step Name can not be null.")
            msg.setText("Step Name can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ALREADY USED ID
        for i in steps:
            if step_id == i.id:
                print("Step ID already used.")
                msg.setText("Step ID already used.")
                msg.exec()
                return -2
        #CREATE NEW STEP AND ADD IT TO THE LIST
        new_step = Step(step_id, step_name, step_continuum, step_type)
        steps.append(new_step)
        self.close()
        window.setEnabled(1)
        return 1
        
#DEFINITION OF THE STEP PHASE WINDOW
class UiStepPhaseWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiStepPhaseWindow, self).__init__()
        uic.loadUi('ui/add_step_phase.ui', self)
        #CONNECT BUTTONS AND ACTIONS
        self.add_button.clicked.connect(self.add)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1)   
    #FUNCTION TO APPEND THE NEW STEP PHASE   
    def add(self):
        print("Add button pressed in add_step_phase window.")
        #READ VALUES FROM lineEdit
        step_phase_id = self.lineEdit_id.text() 
        step_phase_name = self.lineEdit_name.text()
        #CHECK FOR MISSING INPUT
        if step_phase_id == "":
            print("Step Phase ID can not be null.")
            msg.setText("Step Phase ID can not be null.")
            msg.exec()
            return -1
        if step_phase_name == "":
            print("Step Phase name can not be null.")
            msg.setText("Step Phase Name can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ALREADY USED ID
        for i in step_phases:
            if step_phase_id == i.id:
                print("Step Phase ID already used.")
                msg.setText("Step Phase ID already used.")
                msg.exec()
                return -2
        #CREATE NEW STEP PHASE AND ADD IT TO THE LIST
        new_step_phase = StepPhase(step_phase_id, step_phase_name)
        step_phases.append(new_step_phase)
        self.close()
        window.setEnabled(1)
        return 1

#DEFINITION OF THE ENVIRONMENT VARIABLE WINDOW
class UiEnvironmentVariableWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiEnvironmentVariableWindow, self).__init__()
        uic.loadUi('ui/add_environment_variable.ui', self)
        #CONNECT BUTTONS AND ACTIONS
        self.add_button.clicked.connect(self.add)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1)    
    #FUNCTION TO APPEND THE NEW ENVIRONMENT VARIABLE    
    def add(self):
        print("Add button pressed in add_environment_variable window.")
        #READ VALUES FROM lineEdit
        environment_variable_key = self.lineEdit_key.text() 
        environment_variable_value = self.lineEdit_value.text()
        #CHECK FOR MISSING INPUT
        if environment_variable_key == "":
            print("Environment Variable Key can not be null.")
            msg.setText("Environment Variable Key can not be null.")
            msg.exec()
            return -1
        if environment_variable_value == "":
            print("Environment Variable Value can not be null.")
            msg.setText("Environment Variable Value can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ALREADY USED ID
        for i in environment_variables:
            if environment_variable_key == i.key:
                print("Environment Variable key already used.")
                msg.setText("Environment Variable key already used.")
                msg.exec()
                return -2
        #CREATE NEW ENVIRONMENT VARIABLE AND ADD IT TO THE LIST
        new_environment_variable = EnvironmentVariable(environment_variable_key, environment_variable_value)
        environment_variables.append(new_environment_variable)
        self.close()
        window.setEnabled(1)
        return 1

#DEFINITION OF THE DATA SOURCE WINDOW
class UiDataSourceWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiDataSourceWindow, self).__init__()
        uic.loadUi('ui/add_data_source.ui', self)
        #CONNECT BUTTONS AND ACTIONS
        self.add_button.clicked.connect(self.add)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1)   
    #FUNCTION TO APPEND THE NEW DATA SOURCE    
    def add(self):
        print("Add button pressed in add_data_source window.")
        #READ VALUES FROM lineEdit
        data_source_id = self.lineEdit_id.text() 
        data_source_name = self.lineEdit_name.text()
        data_source_volume = self.lineEdit_volume.text()
        #CHECK FOR MISSING INPUT
        if data_source_id == "":
            print("Data Source ID can not be null.")
            msg.setText("Data Source ID can not be null.")
            msg.exec()
            return -1
        if data_source_name == "":
            print("Data Source Name can not be null.")
            msg.setText("Data Source Name can not be null.")
            msg.exec()
            return -1
        if data_source_volume == "":
            print("Data Source Volume can not be null.")
            msg.setText("Data Source Volume can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ALREADY USED ID
        for i in data_sources:
            if data_source_id == i.id:
                print("Data Source ID already used.")
                msg.setText("Data Source ID already used.")
                msg.exec()
                return -2
        #READ VALUES FROM RADIOBUTTONS
        if self.radioButtonInput.isChecked():
            data_source_type = "Input"
        elif self.radioButtonOutput.isChecked():
            data_source_type = "Output"
        elif self.radioButtonIO.isChecked():
            data_source_type = "IO"
        #CHECK FOR SUBCLASS
        data_source_velocity = self.lineEdit_velocity.text()
        if data_source_velocity != "":
            data_stream = 1
        else:
            data_stream = 0
        #CREATE NEW ENVIRONMENT VARIABLE AND ADD IT TO THE LIST
        if data_stream == 0:
            new_data_source = DataSource(data_source_id, data_source_name, data_source_volume, data_source_type)
        else:
            new_data_source = DataStream(data_source_id, data_source_name, data_source_volume, data_source_type, data_source_velocity)
        data_sources.append(new_data_source)
        self.close()
        window.setEnabled(1)
        return 1
        
#DEFINITION OF THE TECHNOLOGY WINDOW
class UiTechnologyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiTechnologyWindow, self).__init__()
        uic.loadUi('ui/add_technology.ui', self)
        #CONNECT BUTTONS AND ACTIONS
        self.add_button.clicked.connect(self.add)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1)   
    #FUNCTION TO APPEND THE NEW TECHNOLOGY    
    def add(self):
        print("Add button pressed in add_technology window.")
        #READ VALUES FROM lineEdit
        technology_id = self.lineEdit_id.text() 
        technology_name = self.lineEdit_name.text()
        #CHECK FOR MISSING INPUT
        if technology_id == "":
            print("Technology ID can not be null.")
            msg.setText("Technology ID can not be null.")
            msg.exec()
            return -1
        if technology_name == "":
            print("Technology Name can not be null.")
            msg.setText("Technology Name can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ALREADY USED ID
        for i in technologies:
            if technology_id == i.id:
                print("Technology ID already used.")
                msg.setText("Technology ID already used.")
                msg.exec()
                return -2
        #READ VALUES FROM RADIOBUTTONS
        if self.radioButtonWindows.isChecked():
            technology_os = "Windows"
        elif self.radioButtonMac.isChecked():
            technology_os = "Mac"
        elif self.radioButtonLinux.isChecked():
            technology_os = "Linux"
        else:
            technology_os = ""
        #CREATE NEW TECHNOLOGY AND ADD IT TO THE LIST
        new_technology = Technology(technology_id, technology_name, technology_os)
        technologies.append(new_technology)
        self.close()
        window.setEnabled(1)
        return 1
    
#DEFINITION OF THE CPU WINDOW
class UiCPUWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiCPUWindow, self).__init__()
        uic.loadUi('ui/add_cpu.ui', self)
        #CONNECT BUTTONS AND ACTIONS
        self.add_button.clicked.connect(self.add)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1)    
    #FUNCTION TO APPEND THE NEW CPU   
    def add(self):
        print("Add button pressed in add_cpu window.")
        #READ VALUES FROM lineEdit
        cpu_id = self.lineEdit_id.text()
        cpu_cores = self.lineEdit_cores.text()
        cpu_speed = self.lineEdit_speed.text()
        cpu_producer = self.lineEdit_producer.text()
        #CHECK FOR MISSING INPUT
        if cpu_id == "":
            print("CPU ID can not be null.")
            msg.setText("CPU ID can not be null.")
            msg.exec()
            return -1
        if cpu_cores == "":
            print("CPU Cores can not be null.")
            msg.setText("CPU Cores can not be null.")
            msg.exec()
            return -1
        if cpu_speed == "":
            print("CPU Speed can not be null.")
            msg.setText("CPU Speed can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ALREADY USED ID
        for i in cpus:
            if cpu_id == i.id:
                print("CPU ID already used.")
                msg.setText("CPU ID already used.")
                msg.exec()
                return -2
        #CREATE NEW CPU AND ADD IT TO THE LIST
        new_cpu = CPU(cpu_id, cpu_cores, cpu_speed, cpu_producer)
        cpus.append(new_cpu)
        self.close()
        window.setEnabled(1)
        return 1

#DEFINITION OF THE RAM WINDOW
class UiRAMWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiRAMWindow, self).__init__()
        uic.loadUi('ui/add_ram.ui', self)
        #CONNECT BUTTONS AND ACTIONS
        self.add_button.clicked.connect(self.add)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1)   
    #FUNCTION TO APPEND THE NEW RAM  
    def add(self):
        print("Add button pressed in add_ram window.")
        #READ VALUES FROM lineEdit
        ram_id = self.lineEdit_id.text()
        ram_volume = self.lineEdit_volume.text()
        ram_speed = self.lineEdit_speed.text()
        ram_producer = self.lineEdit_producer.text()
        #CHECK FOR MISSING INPUT
        if ram_id == "":
            print("RAM ID can not be null.")
            msg.setText("RAM ID can not be null.")
            msg.exec()
            return -1
        if ram_volume == "":
            print("RAM Volume can not be null.")
            msg.setText("RAM Volume can not be null.")
            msg.exec()
            return -1
        if ram_speed == "":
            print("RAM Speed can not be null.")
            msg.setText("Ram Speed can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ALREADY USED ID
        for i in rams:
            if ram_id == i.id:
                print("RAM ID already used.")
                msg.setText("RAM ID already used.")
                msg.exec()
                return -2
        #READ VALUES FROM RADIOBUTTONS
        if self.radioButtonDDR3.isChecked():
            ram_type = "DDR3"
        elif self.radioButtonDDR4.isChecked():
            ram_type = "DDR4" 
        else:
            ram_type = "DDR5"
        #CREATE NEW RAM AND ADD IT TO THE LIST
        new_ram = RAM(ram_id, ram_volume, ram_speed, ram_type, ram_producer)
        rams.append(new_ram)
        self.close()
        window.setEnabled(1)
        return 1
       
#DEFINITION OF THE GPU WINDOW
class UiGPUWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiGPUWindow, self).__init__()
        uic.loadUi('ui/add_gpu.ui', self)
        #CONNECT BUTTONS AND ACTIONS
        self.add_button.clicked.connect(self.add)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1)   
    #FUNCTION TO APPEND THE NEW GPU   
    def add(self):
        print("Add button pressed in add_gpu window.")
        #READ VALUES FROM lineEdit
        gpu_id = self.lineEdit_id.text()
        gpu_cores = self.lineEdit_cores.text()
        gpu_speed = self.lineEdit_speed.text()
        gpu_memory = self.lineEdit_memory.text()
        gpu_producer = self.lineEdit_producer.text()
        #CHECK FOR MISSING INPUT
        if gpu_id == "":
            print("GPU ID can not be null.")
            msg.setText("GPU ID can not be null.")
            msg.exec()
            return -1
        if gpu_cores == "":
            print("GPU Cores can not be null.")
            msg.setText("GPU Cores can not be null.")
            msg.exec()
            return -1
        if gpu_speed == "":
            print("GPU Speed can not be null.")
            msg.setText("GPU Speed can not be null.")
            msg.exec()
            return -1
        if gpu_memory == "":
            print("GPU Memory can not be null.")
            msg.setText("GPU Memory can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ALREADY USED ID
        for i in gpus:
            if gpu_id == i.id:
                print("GPU ID already used.")
                msg.setText("GPU ID already used.")
                msg.exec()
                return -2
        #CREATE NEW GPU AND ADD IT TO THE LIST
        new_gpu = GPU(gpu_id, gpu_cores, gpu_speed, gpu_memory, gpu_producer)
        gpus.append(new_gpu)
        self.close()
        window.setEnabled(1)
        return 1
        
#DEFINITION OF THE STORAGE WINDOW 
class UiStorageWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiStorageWindow, self).__init__()
        uic.loadUi('ui/add_storage.ui', self)
        #CONNECT BUTTONS AND ACTIONS
        self.add_button.clicked.connect(self.add)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1)   
    #FUNCTION TO APPEND THE NEW STORAGE   
    def add(self):
        print("Add button pressed in add_storage window.")
        #READ VALUES FROM lineEdit
        storage_id = self.lineEdit_id.text()
        storage_volume = self.lineEdit_volume.text()
        storage_speed = self.lineEdit_speed.text()
        storage_producer = self.lineEdit_producer.text()
        #CHECK FOR MISSING INPUT
        if storage_id == "":
            print("Storage ID can not be null.")
            msg.setText("Storage ID can not be null.")
            msg.exec()
            return -1
        if storage_volume == "":
            print("Storage Volume can not be null.")
            msg.setText("Storage Volume can not be null.")
            msg.exec()
            return -1
        if storage_speed == "":
            print("Storage Speed can not be null.")
            msg.setText("Storage Speed can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ALREADY USED ID
        for i in storages:
            if storage_id == i.id:
                print("Storage ID already used.")
                msg.setText("Storage ID already used.")
                msg.exec()
                return -2
        #READ VALUES FROM RADIOBUTTONS
        if self.radioButtonHD.isChecked():
            storage_type = "HD"
        elif self.radioButtonSSD.isChecked():
            storage_type = "SSD" 
        else:
            storage_type = "SD"
        #CREATE NEW STORAGE AND ADD IT TO THE LIST
        new_storage = Storage(storage_id, storage_volume, storage_speed, storage_type, storage_producer)
        storages.append(new_storage)
        self.close()
        window.setEnabled(1)
        return 1

#DEFINITION OF THE NETWORK WINDOW
class UiNetworkWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiNetworkWindow, self).__init__()
        uic.loadUi('ui/add_network.ui', self)
        #CONNECT BUTTONS AND ACTIONS
        self.add_button.clicked.connect(self.add)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1)   
    #FUNCTION TO APPEND THE NEW NETWORK  
    def add(self):
        print("Add button pressed in add_network window.")
        #READ VALUES FROM lineEdit
        network_id = self.lineEdit_id.text()
        network_bandwidth = self.lineEdit_bandwidth.text()
        network_latency = self.lineEdit_latency.text()
        #CHECK FOR MISSING INPUT
        if network_id == "":
            print("Network ID can not be null.")
            msg.setText("Network ID can not be null.")
            msg.exec()
            return -1
        if network_bandwidth == "":
            print("Network Bandwidth can not be null.")
            msg.setText("Network Bandwidth can not be null.")
            msg.exec()
            return -1
        if network_latency == "":
            print("Network Latency can not be null.")
            msg.setText("Network Latency can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ALREADY USED ID
        for i in networks:
            if network_id == i.id:
                print("Network ID already used.")
                msg.setText("Network ID already used.")
                msg.exec()
                return -2
        #CREATE NEW NETWORK AND ADD IT TO THE LIST
        new_network = Network(network_id, network_bandwidth, network_latency)
        networks.append(new_network)
        self.close()
        window.setEnabled(1)
        return 1

#------------------------------------------------------------------
#------------------------------------------------------------------
#DATA STRUCTURES
#------------------------------------------------------------------
#------------------------------------------------------------------
steps = []
step_phases = []
environment_variables = []
data_sources = []
technologies = []
cpus = []
gpus = []
rams = []
storages = []
networks = []
#------------------------------------------------------------------
#------------------------------------------------------------------
#RUN THE MAIN WINDOW
#------------------------------------------------------------------
#------------------------------------------------------------------
app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = UiMainWindow() # Create an instance of our class
#------------------------------------------------------------------
#ERROR MESSAGE
#------------------------------------------------------------------
msg = QMessageBox()
dialog = UiDialogWindow()
dialog.setWindowTitle("Deletion")
#msg.setIcon(QMessageBox.Warning)
msg.setText("Error")
msg.setWindowTitle("Error")
#------------------------------------------------------------------
#RUN THE APP
#------------------------------------------------------------------
app.exec() # Start the application