from PyQt5 import QtWidgets, uic, QtCore, QtGui
import numpy as np
from PyQt5.QtWidgets import QMessageBox, QDialog
import random
from datetime import datetime
import time
import sys
sys.path.append('src/')
import classes
import utils
#------------------------------------------------------------------          
#------------------------------------------------------------------       
#DEFINE ALL THE UI WINDOWS
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
        self.actionAddResource.triggered.connect(self.addResource)
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
        self.actionViewResources.triggered.connect(self.printResources)
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
        self.actionDeleteResource.triggered.connect(self.deleteResource)
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
        #------------------------ LINK -----------------------
        self.actionLinkStepResource.triggered.connect(self.linkStepResource)
        self.actionLinkStepDataSource.triggered.connect(self.linkStepDataSource)
        self.actionLinkStepStepPhase.triggered.connect(self.linkStepStepPhase)
        self.actionLinkStepPhaseTechnology.triggered.connect(self.linkStepPhaseTechnology)
        self.actionLinkStepPhaseEnvironmentVariable.triggered.connect(self.linkStepPhaseEnvironmentVariable)
        self.actionLinkTechnologyCPU.triggered.connect(self.linkTechnologyCPU)
        self.actionLinkTechnologyGPU.triggered.connect(self.linkTechnologyGPU)
        self.actionLinkTechnologyRAM.triggered.connect(self.linkTechnologyRAM)
        self.actionLinkTechnologyStorage.triggered.connect(self.linkTechnologyStorage)
        self.actionLinkTechnologyNetwork.triggered.connect(self.linkTechnologyNetwork)
        #----------------------- DEBUG -----------------------
        self.debugButton.clicked.connect(self.debug)
        #----------------------- IMPORT ----------------------
        self.importButton.clicked.connect(self.importJSON)
    #----------------------- CLOSE EVENT -----------------------
    def closeEvent(self, event):
        if self.w is not None:
            self.w.close()
    #------------------------------------------------------------------
    #FUNCTIONS
    #------------------------ DEBUG -----------------------
    def debug(self):
        self.lineEdit_id.setText("1")
        self.lineEdit_name.setText("new")
        self.lineEdit_medium.setText("cloud")
        self.lineEdit_traces.setText("10")
        utils.debug(steps, step_phases, technologies)
    #------------------------ IMPORT -----------------------
    def importJSON(self):
        # get the data from the file
        pipeline_details = utils.importJSON( "data/test.json", steps, step_phases, technologies)
        # populate pipeline detailes boxes
        self.lineEdit_id.setText(pipeline_details[0])
        self.lineEdit_name.setText(pipeline_details[1])
        self.lineEdit_medium.setText(pipeline_details[2])
        self.lineEdit_traces.setText(pipeline_details[3])
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
            msg.setText('At least 1 Step is needed.')
            msg.exec()
            return -1
        elif len(step_phases) == 0:
            msg.setText('At least 1 Step Phase is needed.')
            msg.exec()
            return -1
        elif pipeline_id == "":
            msg.setText("Big Data Pipeline ID can not be null.")
            msg.exec()
            return -1
        elif pipeline_medium == "":
            msg.setText("Big Data Pipeline Communication Medium can not be null.")
            msg.exec()
            return -1
        elif pipeline_name == "":  
            msg.setText("Big Data Pipeline Name can not be null.")
            msg.exec()
            return -1
        elif pipeline_traces == "":
            msg.setText("Big Data Pipeline Number of Traces can not be null.")
            msg.exec()
            return -1
        else:
            #---------- CHECK FOR ERRORS IN NUMBER OF TRACES
            try:
                n = int(pipeline_traces)
            except ValueError as ve:
                msg.setText('Number of Traces must be a number.')
                msg.exec()
                return -2
            if n <= 0:
                msg.setText('Number of Traces must be positive.')
                msg.exec()
                return -2
            #CHECK FOR MISSING LINKS
            for step in steps:
                if len(step.stepPhases) == 0:
                    msg.setText('Step ' + step.id + ' needs to be linked with at least one Step Phase.')
                    msg.exec()
                    return-3
            #GENERATE THE LOG IN XES AND JSON
            utils.generateJSON(pipeline_id, pipeline_name, pipeline_medium, pipeline_traces, n, steps, step_phases, data_sources, environment_variables, technologies, cpus, gpus, rams, storages, networks, resources)
            utils.generateXES(pipeline_id, pipeline_name, pipeline_medium, pipeline_traces, n, steps)
            #-------------------------------------- CLOSE THE APP
            self.close()
            return 1
    #FUNCTION TO ADD A NEW Resource
    def addResource(self):
        self.setEnabled(0)
        print("Add-Resource action clicked.")
        self.w = UiResourceWindow()
        self.w.show()
    #FUNCTION TO ADD A NEW Step
    def addStep(self):
        self.setEnabled(0)
        print("Add-Step action clicked.")
        self.w = UiStepWindow()
        self.w.show()
    #FUNCTION TO ADD A NEW Step PHASE
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
    #FUNCTION TO ADD A NEW Technology
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
    #FUNCTION TO ADD A NEW Storage
    def addStorage(self):
        self.setEnabled(0)
        print("Add-Storage action clicked.")
        self.w = UiStorageWindow()
        self.w.show()
    #FUNCTION TO ADD A NEW Network 
    def addNetwork(self):
        self.setEnabled(0)
        print("Add-Network action clicked.")
        self.w = UiNetworkWindow()
        self.w.show() 
    #------------------------------------------------------------------
    #FUNCTIONS TO PRINT OBJECTS
    #------------------------------------------------------------------ 
    #FUNCTION TO PRINT THE LIST OF RESOURCES
    def printResources(self):
        print("View-Resource action clicked.")
        to_print = ""
        for i in resources:
            to_print = to_print + i.__str__() + '\n'
        self.setEnabled(0)
        self.w = UiViewerWindow()
        self.w.textBox.setText(to_print)
        self.w.show()
    #FUNCTION TO PRINT THE LIST OF STEPS
    def printSteps(self):
        print("View-Step action clicked.")
        to_print = ""
        for i in steps:
            to_print = to_print + i.__str__() + '\n'
        self.setEnabled(0)
        self.w = UiViewerWindow()
        self.w.textBox.setText(to_print)
        self.w.show()
    #FUNCTION TO PRINT THE LIST OF Step PHASES
    def printStepPhases(self):
        print("View-StepPhases action clicked.")
        to_print = ""
        for i in step_phases:
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
            to_print = to_print + i.__str__() + '\n'
        self.setEnabled(0)
        self.w = UiViewerWindow()
        self.w.textBox.setText(to_print)
        self.w.show()
    #FUNCTION TO PRINT ALL
    def printAll(self):
        print("View-All action clicked")
        to_print = np.concatenate((steps, step_phases, data_sources, environment_variables, technologies, cpus, gpus, rams, storages, networks, resources))
        to_print_str = ""
        for i in to_print:
            to_print_str = to_print_str + '\n' + i.__str__()
        self.setEnabled(0)
        self.w = UiViewerWindow()
        self.w.textBox.setText(to_print_str)
        self.w.show()
    #------------------------------------------------------------------
    #FUNCTIONS TO DELETE OBJECTS
    #------------------------------------------------------------------ 
    #FUNCTION TO DELETE RESOURCE
    def deleteResource(self):
        print("Delete-Resource action clicked")
        #CHECK IF THERE IS AT LEAST ONE
        if len(resources) == 0:
            msg.setText("There is no Resource to delete.")
            msg.exec()
            return -2
        #ASK FOR ID
        dialog.exec()
        #CHECK IF THE DIALOG WAS CLOSED
        if dialog.closed == 1:
            dialog.closed = 0
            return -3
        for i in resources:
            if dialog.id == i.id:
                #IF IT IS IN THE DATA STRUCTURE DELETE IT
                resources.remove(i)
                print("Resource removed.")
                return 1
        #IF THERE IS NO MATCH
        msg.setText("There is no Resource with the given ID.")
        msg.exec()
        return -1   
    #FUNCTION TO DELETE Step
    def deleteStep(self):
        print("Delete-Step action clicked")
        #CHECK IF THERE IS AT LEAST ONE
        if len(steps) == 0:
            msg.setText("There is no Step to delete.")
            msg.exec()
            return -2
        #ASK FOR ID
        dialog.exec()
        #CHECK IF THE DIALOG WAS CLOSED
        if dialog.closed == 1:
            dialog.closed = 0
            return -3
        for i in steps:
            if dialog.id == i.id:
                #IF IT IS IN THE DATA STRUCTURE DELETE IT
                steps.remove(i)
                print("Step removed.")
                return 1
        #IF THERE IS NO MATCH
        msg.setText("There is no Step with the given ID.")
        msg.exec()
        return -1          
    #FUNCTION TO DELETE Step PHASE
    def deleteStepPhase(self):
        print("Delete-StepPhase action clicked")
        #CHECK IF THERE IS AT LEAST ONE
        if len(step_phases) == 0:
            msg.setText("There is no Step Phase to delete.")
            msg.exec()
            return -2
        #ASK FOR ID
        dialog.exec()
        #CHECK IF THE DIALOG WAS CLOSED
        if dialog.closed == 1:
            dialog.closed = 0
            return -3
        for i in step_phases:
            if dialog.id == i.id:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    step_phases.remove(i)
                    print("Step Phase removed.")
                    return 1
        #IF THERE IS NO MATCH
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
        #CHECK IF THE DIALOG WAS CLOSED
        if dialog.closed == "1":
            dialog.closed = 0
            return -3
        for i in data_sources:
            if dialog.id == i.id:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    data_sources.remove(i)
                    print("Data Source removed.")
                    return 1
        #IF THERE IS NO MATCH
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
        #CHECK IF THE DIALOG WAS CLOSED
        if dialog.closed == 1:
            dialog.closed = 0
            return -3
        for i in environment_variables:
            if dialog.id == i.key:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    environment_variables.remove(i)
                    print("Environment Variable removed.")
                    return 1
        #IF THERE IS NO MATCH
        msg.setText("There is no Environment Variable with the given key.")
        msg.exec()
        return -1       
    #FUNCTION TO DELETE Technology
    def deleteTechnology(self):
        print("Delete-Technology action clicked")
        #CHECK IF THERE IS AT LEAST ONE
        if len(technologies) == 0:
            msg.setText("There is no Technology to delete.")
            msg.exec()
            return -2
        #ASK FOR ID
        dialog.exec()
        #CHECK IF THE DIALOG WAS CLOSED
        if dialog.closed == 1:
            dialog.closed = 0
            return -3
        for i in technologies:
            if dialog.id == i.id:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    technologies.remove(i)
                    print("Technology removed.")
                    return 1
        #IF THERE IS NO MATCH
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
        #CHECK IF THE DIALOG WAS CLOSED
        if dialog.closed == 1:
            dialog.closed = 0
            return -3
        for i in cpus:
            if dialog.id == i.id:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    cpus.remove(i)
                    print("CPU removed.")
                    return 1
        #IF THERE IS NO MATCH
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
        #CHECK IF THE DIALOG WAS CLOSED
        if dialog.closed == 1:
            dialog.closed = 0
            return -3
        for i in gpus:
            if dialog.id == i.id:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    gpus.remove(i)
                    print("GPU removed.")
                    return 1
        #IF THERE IS NO MATCH
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
        #CHECK IF THE DIALOG WAS CLOSED
        if dialog.closed == 1:
            dialog.closed = 0
            return -3
        for i in rams:
            if dialog.id == i.id:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    rams.remove(i)
                    print("RAM removed.")
                    return 1
        #IF THERE IS NO MATCH
        msg.setText("There is no RAM with the given ID.")
        msg.exec()
        return -1      
    #FUNCTION TO DELETE Storage
    def deleteStorage(self):
        print("Delete-Storage action clicked")
        #CHECK IF THERE IS AT LEAST ONE
        if len(storages) == 0:
            msg.setText("There is no Storage to delete.")
            msg.exec()
            return -2
        #ASK FOR ID
        dialog.exec()
        #CHECK IF THE DIALOG WAS CLOSED
        if dialog.closed == 1:
            dialog.closed = 0
            return -3
        for i in storages:
            if dialog.id == i.id:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    storages.remove(i)
                    print("Storage removed.")
                    return 1
        #IF THERE IS NO MATCH
        msg.setText("There is no Storage with the given ID.")
        msg.exec()
        return -1
    #FUNCTION TO DELETE Network
    def deleteNetwork(self):
        print("Delete-Network action clicked")
        #CHECK IF THERE IS AT LEAST ONE
        if len(networks) == 0:
            msg.setText("There is no Network to delete.")
            msg.exec()
            return -2
        #ASK FOR ID
        dialog.exec()
        #CHECK IF THE DIALOG WAS CLOSED
        if dialog.closed == 1:
            dialog.closed = 0
            return -3
        for i in networks:
            if dialog.id == i.id:
                    #IF IT IS IN THE DATA STRUCTURE DELETE IT
                    networks.remove(i)
                    print("Network removed.")
                    return 1
        #IF THERE IS NO MATCH
        msg.setText("There is no Network with the given ID.")
        msg.exec()
        return -1
#------------------------------------------------------------------
#FUNCTIONS TO LINK OBJECTS
#------------------------------------------------------------------    
    def linkStepResource(self):
        print("Link Step to Resource action clicked")
        #CHECK IF THERE IS AT LEAST ONE Step
        if len(steps) == 0:
            msg.setText("There is no Step to link.")
            msg.exec()
            return -2
        #CHECK IF THERE IS AT LEAST ONE RESOURCE
        if len(resources) == 0:
            msg.setText("There is no Resource to link.")
            msg.exec()
            return -2
        #ASK FOR IDs
        link_dialog.exec()
        #CHECK IF THE DIALOG WAS CLOSED
        if link_dialog.closed == 1:
            link_dialog.closed = 0
            return -3
        #CHECK FOR IDS IN THE DATA STRUCTURE
        for i in steps:
            if i.id == link_dialog.id1:
                for j in resources:
                    if j.id == link_dialog.id2:
                        for z in i.resources:
                            if z.id == link_dialog.id2:
                                msg.setText("This Step-Resource pair is already linked.")
                                msg.exec()
                                return -2 
                        i.resources.append(j)
                        print("Succesfully linked Resource to Step")
                        return 1
                msg.setText("There is no Resource with such ID.")
                msg.exec()
                return -2
        msg.setText("There is no Step with such ID.")
        msg.exec()
        return -2   
    def linkStepDataSource(self):
        print("Link Step to Data Source action clicked")
        #CHECK IF THERE IS AT LEAST ONE Step
        if len(steps) == 0:
            msg.setText("There is no Step to link.")
            msg.exec()
            return -2
        #CHECK IF THERE IS AT LEAST ONE DataSource
        if len(data_sources) == 0:
            msg.setText("There is no Data Source to link.")
            msg.exec()
            return -2
        #ASK FOR IDs
        link_dialog.exec()
        #CHECK IF THE DIALOG WAS CLOSED
        if link_dialog.closed == 1:
            link_dialog.closed = 0
            return -3
        #CHECK FOR IDS IN THE DATA STRUCTURE
        for i in steps:
            if i.id == link_dialog.id1:
                for j in data_sources:
                    if j.id == link_dialog.id2:
                        for z in i.dataSources:
                            if z.id == link_dialog.id2:
                                msg.setText("This Step-Data Source pair is already linked.")
                                msg.exec()
                                return -2 
                        i.dataSources.append(j)
                        print("Succesfully linked Data Source to Step")
                        return 1
                msg.setText("There is no Data Source with such ID.")
                msg.exec()
                return -2
        msg.setText("There is no Step with such ID.")
        msg.exec()
        return -2
    def linkStepStepPhase(self):
        print("Link Step to Step Phase action clicked")
        #CHECK IF THERE IS AT LEAST ONE Step
        if len(steps) == 0:
            msg.setText("There is no Step to link.")
            msg.exec()
            return -2
        #CHECK IF THERE IS AT LEAST ONE Step Phase
        if len(step_phases) == 0:
            msg.setText("There is no Step Phase to link.")
            msg.exec()
            return -2
        #ASK FOR IDs
        link_dialog.exec()
        #CHECK IF THE DIALOG WAS CLOSED
        if link_dialog.closed == 1:
            link_dialog.closed = 0
            return -3
        #CHECK FOR IDS IN THE DATA STRUCTURE
        for i in steps:
            if i.id == link_dialog.id1:
                for j in step_phases:
                    if j.id == link_dialog.id2:
                        for z in i.stepPhases:
                            if z.id == link_dialog.id2:
                                msg.setText("This Step-Step Phase pair is already linked.")
                                msg.exec()
                                return -2 
                        i.stepPhases.append(j)
                        print("Succesfully linked Step Phases to Step")
                        return 1
                msg.setText("There is no Step Phase with such ID.")
                msg.exec()
                return -2
        msg.setText("There is no Step with such ID.")
        msg.exec()
        return -2            
    def linkStepPhaseTechnology(self):
        print("Link Step Phase to Technology action clicked")
        #CHECK IF THERE IS AT LEAST ONE Step PHASE
        if len(step_phases) == 0:
            msg.setText("There is no Step Phase to link.")
            msg.exec()
            return -2
        #CHECK IF THERE IS AT LEAST ONE Technology
        if len(technologies) == 0:
            msg.setText("There is no Technology to link.")
            msg.exec()
            return -2
        #ASK FOR IDs
        link_dialog.exec()
        #CHECK IF THE DIALOG WAS CLOSED
        if link_dialog.closed == 1:
            link_dialog.closed = 0
            return -3
        for i in step_phases:
            if i.id == link_dialog.id1:
                for j in technologies:
                    if j.id == link_dialog.id2:
                        for z in i.technologies:
                            if z.id == link_dialog.id2:
                                msg.setText("This Step Phase-Technology pair is already linked.")
                                msg.exec()
                                return -2 
                        i.technologies.append(j)
                        print("Succesfully linked Technology to  Step Phase ")
                        return 1
                msg.setText("There is no Technology with such ID.")
                msg.exec()
                return -2
        msg.setText("There is no Step Phase with such ID.")
        msg.exec()
        return -2  
    def linkStepPhaseEnvironmentVariable(self):
        print("Link StepPhase to Environment Variable action clicked")
        #CHECK IF THERE IS AT LEAST ONE Step PHASE
        if len(step_phases) == 0:
            msg.setText("There is no Step Phase to link.")
            msg.exec()
            return -2
        #CHECK IF THERE IS AT LEAST ONE ENVIRONMENT VARIABLE
        if len(environment_variables) == 0:
            msg.setText("There is no Environment Variable to link.")
            msg.exec()
            return -2
        #ASK FOR IDs
        link_dialog.exec()
        #CHECK IF THE DIALOG WAS CLOSED
        if link_dialog.closed == 1:
            link_dialog.closed = 0
            return -3
        for i in step_phases:
            if i.id == link_dialog.id1:
                for j in environment_variables:
                    if j.key == link_dialog.id2:
                        for z in i.environmentVariables:
                            if z.key == link_dialog.id2:
                                msg.setText("This Step Phase-Environment Variable pair is already linked.")
                                msg.exec()
                                return -2 
                        i.environmentVariables.append(j)
                        print("Succesfully linked Environment Variable to Step Phase")
                        return 1
                msg.setText("There is no Environment Variable with such Key.")
                msg.exec()
                return -2
        msg.setText("There is no Step Phase with such ID.")
        msg.exec()
        return -2       
    def linkTechnologyCPU(self):
        print("Link Technology to CPU action clicked")
        #CHECK IF THERE IS AT LEAST ONE Technology
        if len(technologies) == 0:
            msg.setText("There is no Technology to link.")
            msg.exec()
            return -2
        #CHECK IF THERE IS AT LEAST ONE CPU
        if len(cpus) == 0:
            msg.setText("There is no CPU to link.")
            msg.exec()
            return -2
        #ASK FOR IDs
        link_dialog.exec()
        #CHECK IF THE DIALOG WAS CLOSED
        if link_dialog.closed == 1:
            link_dialog.closed = 0
            return -3
        for i in technologies:
            if i.id == link_dialog.id1:
                for j in cpus:
                    if j.id == link_dialog.id2:
                        for z in i.cpus:
                            if z.id == link_dialog.id2:
                                msg.setText("This Technology-CPU pair is already linked.")
                                msg.exec()
                                return -2 
                        i.cpus.append(j)
                        print("Succesfully linked CPU to Technology")
                        return 1
                msg.setText("There is no CPU with such ID.")
                msg.exec()
                return -2
        msg.setText("There is no Technology with such ID.")
        msg.exec()
        return -2
    def linkTechnologyGPU(self):
        print("Link Technology to GPU action clicked")
        #CHECK IF THERE IS AT LEAST ONE Technology
        if len(technologies) == 0:
            msg.setText("There is no Technology to link.")
            msg.exec()
            return -2
        #CHECK IF THERE IS AT LEAST ONE GPU
        if len(gpus) == 0:
            msg.setText("There is no GPU to link.")
            msg.exec()
            return -2
        #ASK FOR IDs
        link_dialog.exec()
        #CHECK IF THE DIALOG WAS CLOSED
        if link_dialog.closed == 1:
            link_dialog.closed = 0
            return -3
        for i in technologies:
            if i.id == link_dialog.id1:
                for j in gpus:
                    if j.id == link_dialog.id2:
                        for z in i.gpus:
                            if z.id == link_dialog.id2:
                                msg.setText("This Technology-GPU pair is already linked.")
                                msg.exec()
                                return -2 
                        i.gpus.append(j)
                        print("Succesfully linked GPU to Technology")
                        return 1
                msg.setText("There is no GPU with such ID.")
                msg.exec()
                return -2
        msg.setText("There is no Technology with such ID.")
        msg.exec()
        return -2
    def linkTechnologyRAM(self):
        print("Link Technology to RAM clicked")
        #CHECK IF THERE IS AT LEAST ONE Technology
        if len(technologies) == 0:
            msg.setText("There is no Technology to link.")
            msg.exec()
            return -2
        #CHECK IF THERE IS AT LEAST ONE RAM
        if len(rams) == 0:
            msg.setText("There is no RAM to link.")
            msg.exec()
            return -2
        #ASK FOR IDs
        link_dialog.exec()
        #CHECK IF THE DIALOG WAS CLOSED
        if link_dialog.closed == 1:
            link_dialog.closed = 0
            return -3
        for i in technologies:
            if i.id == link_dialog.id1:
                for j in rams:
                    if j.id == link_dialog.id2:
                        for z in i.rams:
                            if z.id == link_dialog.id2:
                                msg.setText("This Technology-RAM pair is already linked.")
                                msg.exec()
                                return -2 
                        i.rams.append(j)
                        print("Succesfully linked RAM to Technology")
                        return 1
                msg.setText("There is no RAM with such ID.")
                msg.exec()
                return -2
        msg.setText("There is no Technology with such ID.")
        msg.exec()
        return -2
    def linkTechnologyStorage(self):
        print("Link Technology to Storage clicked")
        #CHECK IF THERE IS AT LEAST ONE Technology
        if len(technologies) == 0:
            msg.setText("There is no Technology to link.")
            msg.exec()
            return -2
        #CHECK IF THERE IS AT LEAST ONE Storage
        if len(storages) == 0:
            msg.setText("There is no Storage to link.")
            msg.exec()
            return -2
        #ASK FOR IDs
        link_dialog.exec()
        #CHECK IF THE DIALOG WAS CLOSED
        if link_dialog.closed == 1:
            link_dialog.closed = 0
            return -3
        for i in technologies:
            if i.id == link_dialog.id1:
                for j in storages:
                    if j.id == link_dialog.id2:
                        for z in i.storages:
                            if z.id == link_dialog.id2:
                                msg.setText("This Technology-Storage pair is already linked.")
                                msg.exec()
                                return -2 
                        i.storages.append(j)
                        print("Succesfully linked Storage to Technology")
                        return 1
                msg.setText("There is no Storage with such ID.")
                msg.exec()
                return -2
        msg.setText("There is no Technology with such ID.")
        msg.exec()
        return -2
    def linkTechnologyNetwork(self):
        print("Link Technology to Network action clicked")
        #CHECK IF THERE IS AT LEAST ONE Technology
        if len(technologies) == 0:
            msg.setText("There is no Technology to link.")
            msg.exec()
            return -2
        #CHECK IF THERE IS AT LEAST ONE Network
        if len(networks) == 0:
            msg.setText("There is no Network to link.")
            msg.exec()
            return -2
        #ASK FOR IDs
        link_dialog.exec()
        #CHECK IF THE DIALOG WAS CLOSED
        if link_dialog.closed == 1:
            link_dialog.closed = 0
            return -3
        for i in technologies:
            if i.id == link_dialog.id1:
                for j in networks:
                    if j.id == link_dialog.id2:
                        for z in i.networks:
                            if z.id == link_dialog.id2:
                                msg.setText("This Technology-Network pair is already linked.")
                                msg.exec()
                                return -2 
                        i.networks.append(j)
                        print("Succesfully linked Network to Technology")
                        return 1
                msg.setText("There is no Network with such ID.")
                msg.exec()
                return -2
        msg.setText("There is no Technology with such ID.")
        msg.exec()
        return -2
#----------------------------------------------------------------------------------------------    
#DEFINITION OF THE VIEWER WINDOW
class UiViewerWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiViewerWindow, self).__init__()
        uic.loadUi('ui/viewer.ui', self)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1)
#DEFINITION OF THE DELETE DIALOG WINDOW
class UiDialogWindow(QtWidgets.QDialog):
    def __init__(self):
        super(UiDialogWindow, self).__init__()
        uic.loadUi('ui/dialog.ui', self)
        #VARIABLE TO STORE THE RESULT
        self.id = ''
        self.closed = 0
        self.deletePressed = 0
        #CONNECT BUTTONS AND ACTIONS
        self.delete_button.clicked.connect(self.delete)   
    def delete(self):
        print("Delete button pressed in dialog window.")
        self.id = self.lineEdit_id.text()
        self.deletePressed = 1
        self.close()
    def closeEvent(self, event):
        self.lineEdit_id.setText("")
        if self.deletePressed == 0:
            self.closed = 1
        else:
            self.deletePressed = 0
        self.close()
        window.setEnabled(1)
#DEFINITION OF THE LINK DIALOG WINDOW
class UiLinkDialogWindow(QtWidgets.QDialog):
    def __init__(self):
        super(UiLinkDialogWindow, self).__init__()
        uic.loadUi('ui/link_dialog.ui', self)
        #VARIABLE TO STORE THE RESULT
        self.id1 = ''
        self.id2 = ''
        self.closed = 0
        self.linkPressed = 0
        #CONNECT BUTTONS AND ACTIONS
        self.link_button.clicked.connect(self.link)   
    def link(self):
        print("Link button pressed in link_dialog window.")
        self.id1 = self.lineEdit_id_1.text()
        self.id2 = self.lineEdit_id_2.text()
        self.linkPressed = 1
        self.close()
    def closeEvent(self, event):
        self.lineEdit_id_1.setText("")
        self.lineEdit_id_2.setText("")
        if self.linkPressed == 0:
            self.closed = 1
        else:
            self.linkPressed = 0
        self.close()
        window.setEnabled(1)
#DEFINITION OF THE Resource WINDOW
class UiResourceWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiResourceWindow, self).__init__()
        uic.loadUi('ui/add_resource.ui', self)
        #CONNECT BUTTONS AND ACTIONS
        self.add_button.clicked.connect(self.add)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1) 
    #FUNCTION TO APPEND THE NEW Step
    def add(self):
        print("Add button pressed in add_resource window.")
        #READ VALUES FROM lineEdit
        resource_id = self.lineEdit_id.text() 
        resource_name = self.lineEdit_name.text()
        #CHECK FOR MISSING INPUT
        if resource_id == "":
            msg.setText("Resource ID can not be null.")
            msg.exec()
            return -1
        if resource_name == "":
            msg.setText("Resource Name can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ' IN THE FIELDS
        if "'" in resource_id:
            msg.setText("Resource ID can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in resource_name:
            msg.setText("Resource Name can not contain ' in the symbol.")
            msg.exec()
            return -3
        #CHECK FOR ALREADY USED ID
        for i in resources:
            if resource_id == i.id:
                msg.setText("Resource ID already used.")
                msg.exec()
                return -2
        #CREATE NEW Step AND ADD IT TO THE LIST
        new_resource = classes.Resource(resource_id, resource_name)
        resources.append(new_resource)
        print("Resource created.")
        self.close()
        window.setEnabled(1)
        return 1  
#DEFINITION OF THE Step WINDOW
class UiStepWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiStepWindow, self).__init__()
        uic.loadUi('ui/add_step.ui', self)
        #CONNECT BUTTONS AND ACTIONS
        self.add_button.clicked.connect(self.add)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1) 
    #FUNCTION TO APPEND THE NEW Step
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
            msg.setText("Step ID can not be null.")
            msg.exec()
            return -1
        if step_name == "":
            msg.setText("Step Name can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ' IN THE FIELDS
        if "'" in step_id:
            msg.setText("Step ID can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in step_name:
            msg.setText("Step Name can not contain ' in the symbol.")
            msg.exec()
            return -3
        #CHECK FOR ALREADY USED ID
        for i in steps:
            if step_id == i.id:
                msg.setText("Step ID already used.")
                msg.exec()
                return -2
        #CREATE NEW Step AND ADD IT TO THE LIST
        new_step = classes.Step(step_id, step_name, step_continuum, step_type)
        steps.append(new_step)
        print("Step created.")
        self.close()
        window.setEnabled(1)
        return 1       
#DEFINITION OF THE Step PHASE WINDOW
class UiStepPhaseWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiStepPhaseWindow, self).__init__()
        uic.loadUi('ui/add_step_phase.ui', self)
        #CONNECT BUTTONS AND ACTIONS
        self.add_button.clicked.connect(self.add)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1)   
    #FUNCTION TO APPEND THE NEW Step PHASE   
    def add(self):
        print("Add button pressed in add_step_phase window.")
        #READ VALUES FROM lineEdit
        step_phase_id = self.lineEdit_id.text() 
        step_phase_name = self.lineEdit_name.text()
        #CHECK FOR MISSING INPUT
        if step_phase_id == "":
            msg.setText("Step Phase ID can not be null.")
            msg.exec()
            return -1
        if step_phase_name == "":
            msg.setText("Step Phase Name can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ' IN THE FIELDS
        if "'" in step_phase_id:
            msg.setText("Step Phase ID can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in step_phase_name:
            msg.setText("Step Phase Name can not contain the ' symbol.")
            msg.exec()
            return -3
        #CHECK FOR ALREADY USED ID
        for i in step_phases:
            if step_phase_id == i.id:
                msg.setText("Step Phase ID already used.")
                msg.exec()
                return -2
        #CREATE NEW Step PHASE AND ADD IT TO THE LIST
        new_step_phase = classes.StepPhase(step_phase_id, step_phase_name)
        step_phases.append(new_step_phase)
        print("Step Phase created.")
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
            msg.setText("Environment Variable Key can not be null.")
            msg.exec()
            return -1
        if environment_variable_value == "":
            msg.setText("Environment Variable Value can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ' IN THE FIELDS
        if "'" in environment_variable_key:
            msg.setText("Environment Variable Key can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in environment_variable_value:
            msg.setText("Environment Variable Value can not contain the ' symbol.")
            msg.exec()
            return -3
        #CHECK FOR ALREADY USED ID
        for i in environment_variables:
            if environment_variable_key == i.key:
                msg.setText("Environment Variable key already used.")
                msg.exec()
                return -2
        #CREATE NEW ENVIRONMENT VARIABLE AND ADD IT TO THE LIST
        new_environment_variable = classes.EnvironmentVariable(environment_variable_key, environment_variable_value)
        environment_variables.append(new_environment_variable)
        print("Environment Variable created.")
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
            msg.setText("Data Source ID can not be null.")
            msg.exec()
            return -1
        if data_source_name == "":
            msg.setText("Data Source Name can not be null.")
            msg.exec()
            return -1
        if data_source_volume == "":
            msg.setText("Data Source Volume can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ' IN THE FIELDS
        if "'" in data_source_id:
            msg.setText("Data Source ID can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in data_source_name:
            msg.setText("Data Source Name can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in data_source_volume:
            msg.setText("Data Source Volume can not contain the ' symbol.")
            msg.exec()
            return -3
        #CHECK FOR ALREADY USED ID
        for i in data_sources:
            if data_source_id == i.id:
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
            if "'" in data_source_velocity:
                msg.setText("Data Source Velocity can not contain the ' symbol.")
                msg.exec()
                return -3
        else:
            data_stream = 0
        #CREATE NEW DATA SOURCE AND ADD IT TO THE LIST
        if data_stream == 0:
            new_data_source = classes.DataSource(data_source_id, data_source_name, data_source_volume, data_source_type)
        else:
            new_data_source = classes.DataStream(data_source_id, data_source_name, data_source_volume, data_source_type, data_source_velocity)
        data_sources.append(new_data_source)
        print("Data Source created.")
        self.close()
        window.setEnabled(1)
        return 1     
#DEFINITION OF THE Technology WINDOW
class UiTechnologyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiTechnologyWindow, self).__init__()
        uic.loadUi('ui/add_technology.ui', self)
        #CONNECT BUTTONS AND ACTIONS
        self.add_button.clicked.connect(self.add)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1)   
    #FUNCTION TO APPEND THE NEW Technology    
    def add(self):
        print("Add button pressed in add_technology window.")
        #READ VALUES FROM lineEdit
        technology_id = self.lineEdit_id.text() 
        technology_name = self.lineEdit_name.text()
        #CHECK FOR MISSING INPUT
        if technology_id == "":
            msg.setText("Technology ID can not be null.")
            msg.exec()
            return -1
        if technology_name == "":
            msg.setText("Technology Name can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ' IN THE FIELDS
        if "'" in technology_id:
            msg.setText("Technology ID can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in technology_name:
            msg.setText("Technology Name can not contain the ' symbol.")
            msg.exec()
            return -3
        #CHECK FOR ALREADY USED ID
        for i in technologies:
            if technology_id == i.id:
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
        #CREATE NEW Technology AND ADD IT TO THE LIST
        new_technology = classes.Technology(technology_id, technology_name, technology_os)
        technologies.append(new_technology)
        print("Technology created.")
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
            msg.setText("CPU ID can not be null.")
            msg.exec()
            return -1
        if cpu_cores == "":
            msg.setText("CPU #Cores can not be null.")
            msg.exec()
            return -1
        if cpu_speed == "":
            msg.setText("CPU Speed can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ' IN THE FIELDS
        if "'" in cpu_id:
            msg.setText("CPU ID can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in cpu_cores:
            msg.setText("CPU #Cores can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in cpu_speed:
            msg.setText("CPU Speed can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in cpu_producer:
            msg.setText("CPU Producer can not contain the ' symbol.")
            msg.exec()
            return -3
        #CHECK FOR ALREADY USED ID
        for i in cpus:
            if cpu_id == i.id:
                msg.setText("CPU ID already used.")
                msg.exec()
                return -2
        #CREATE NEW CPU AND ADD IT TO THE LIST
        new_cpu = classes.CPU(cpu_id, cpu_cores, cpu_speed, cpu_producer)
        cpus.append(new_cpu)
        print("CPU created.")
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
            msg.setText("RAM ID can not be null.")
            msg.exec()
            return -1
        if ram_volume == "":
            msg.setText("RAM Volume can not be null.")
            msg.exec()
            return -1
        if ram_speed == "":
            msg.setText("RAM Speed can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ' IN THE FIELDS
        if "'" in ram_id:
            msg.setText("RAM ID can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in ram_volume:
            msg.setText("RAM Volume can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in ram_speed:
            msg.setText("RAM Speed can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in ram_producer:
            msg.setText("RAM Producer can not contain the ' symbol.")
            msg.exec()
            return -3
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
        new_ram = classes.RAM(ram_id, ram_volume, ram_speed, ram_type, ram_producer)
        rams.append(new_ram)
        print("RAM created.")
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
            msg.setText("GPU ID can not be null.")
            msg.exec()
            return -1
        if gpu_cores == "":
            msg.setText("GPU Cores can not be null.")
            msg.exec()
            return -1
        if gpu_speed == "":
            msg.setText("GPU Speed can not be null.")
            msg.exec()
            return -1
        if gpu_memory == "":
            msg.setText("GPU Memory can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ' IN THE FIELDS
        if "'" in gpu_id:
            msg.setText("GPU ID can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in gpu_cores:
            msg.setText("GPU #Cores can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in gpu_speed:
            msg.setText("GPU Speed can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in gpu_memory:
            msg.setText("GPU Memory can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in gpu_producer:
            msg.setText("GPU Producer can not contain the ' symbol.")
            msg.exec()
            return -3
        #CHECK FOR ALREADY USED ID
        for i in gpus:
            if gpu_id == i.id:
                msg.setText("GPU ID already used.")
                msg.exec()
                return -2
        #CREATE NEW GPU AND ADD IT TO THE LIST
        new_gpu = classes.GPU(gpu_id, gpu_cores, gpu_speed, gpu_memory, gpu_producer)
        gpus.append(new_gpu)
        print("GPU created.")
        self.close()
        window.setEnabled(1)
        return 1      
#DEFINITION OF THE Storage WINDOW 
class UiStorageWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiStorageWindow, self).__init__()
        uic.loadUi('ui/add_storage.ui', self)
        #CONNECT BUTTONS AND ACTIONS
        self.add_button.clicked.connect(self.add)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1)   
    #FUNCTION TO APPEND THE NEW Storage   
    def add(self):
        print("Add button pressed in add_storage window.")
        #READ VALUES FROM lineEdit
        storage_id = self.lineEdit_id.text()
        storage_volume = self.lineEdit_volume.text()
        storage_speed = self.lineEdit_speed.text()
        storage_producer = self.lineEdit_producer.text()
        #CHECK FOR MISSING INPUT
        if storage_id == "":
            msg.setText("Storage ID can not be null.")
            msg.exec()
            return -1
        if storage_volume == "":
            msg.setText("Storage Volume can not be null.")
            msg.exec()
            return -1
        if storage_speed == "":
            msg.setText("Storage Speed can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ' IN THE FIELDS
        if "'" in storage_id:
            msg.setText("Storage ID can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in storage_volume:
            msg.setText("Storage Volume can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in storage_speed:
            msg.setText("Storage Speed can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in storage_producer:           
            msg.setText("Storage Producer can not contain the ' symbol.")
            msg.exec()
            return -3
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
        #CREATE NEW Storage AND ADD IT TO THE LIST
        new_storage = classes.Storage(storage_id, storage_volume, storage_speed, storage_type, storage_producer)
        storages.append(new_storage)
        print("Storage created.")
        self.close()
        window.setEnabled(1)
        return 1
#DEFINITION OF THE Network WINDOW
class UiNetworkWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiNetworkWindow, self).__init__()
        uic.loadUi('ui/add_network.ui', self)
        #CONNECT BUTTONS AND ACTIONS
        self.add_button.clicked.connect(self.add)
    def closeEvent(self, event):
        self.close()
        window.setEnabled(1)   
    #FUNCTION TO APPEND THE NEW Network  
    def add(self):
        print("Add button pressed in add_network window.")
        #READ VALUES FROM lineEdit
        network_id = self.lineEdit_id.text()
        network_bandwidth = self.lineEdit_bandwidth.text()
        network_latency = self.lineEdit_latency.text()
        #CHECK FOR MISSING INPUT
        if network_id == "":
            msg.setText("Network ID can not be null.")
            msg.exec()
            return -1
        if network_bandwidth == "":
            msg.setText("Network Bandwidth can not be null.")
            msg.exec()
            return -1
        if network_latency == "":
            msg.setText("Network Latency can not be null.")
            msg.exec()
            return -1
        #CHECK FOR ' IN THE FIELDS
        if "'" in network_id:
            msg.setText("Network ID can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in network_bandwidth:
            msg.setText("Network Bandwidth can not contain the ' symbol.")
            msg.exec()
            return -3
        if "'" in network_latency:
            msg.setText("Network Latency can not contain the ' symbol.")
            msg.exec()
            return -3
        #CHECK FOR ALREADY USED ID
        for i in networks:
            if network_id == i.id:
                msg.setText("Network ID already used.")
                msg.exec()
                return -2
        #CREATE NEW Network AND ADD IT TO THE LIST
        new_network = classes.Network(network_id, network_bandwidth, network_latency)
        networks.append(new_network)
        print("Network created.")
        self.close()
        window.setEnabled(1)
        return 1
#------------------------------------------------------------------
#DATA STRUCTURES
#------------------------------------------------------------------
resources = []
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
#RUN THE MAIN WINDOW
#------------------------------------------------------------------
app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = UiMainWindow() # Create an instance of our class
#------------------------------------------------------------------
#ERROR MESSAGE
#------------------------------------------------------------------
msg = QMessageBox()
dialog = UiDialogWindow()
link_dialog = UiLinkDialogWindow()
dialog.setWindowTitle("Deletion")
link_dialog.setWindowTitle("Linking")
#msg.setIcon(QMessageBox.Warning)
msg.setText("Error")
msg.setWindowTitle("Error")
#------------------------------------------------------------------
#RUN THE APP
#------------------------------------------------------------------
app.exec() # Start the application