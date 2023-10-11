#------------------------------------------------------------------
#------------------------------------------------------------------
#DEFINE ALL THE CLASSES IN THE UML
#------------------------------------------------------------------
#------------------------------------------------------------------
class Resource():
    #CONSTRUCTOR
    def __init__(self, id, name):
        self.id = id
        self.name = name
    #TO STRING
    def __str__(self):
        return '"Resource_' + self.id + '": {\n\t"ID": "' + self.id + '",\n\t"Name": "' + self.name + '"\n}'
class Step():
    #CONSTRUCTOR
    def __init__(self, id, name, continuumLayer, type):
        self.id = id
        self.name = name
        self.continuumLayer = continuumLayer
        self.type = type
        self.dataSources = []
        self.stepPhases = []
        self.resources = []
    #TO STRING
    def __str__(self):
        s = '"Step_' + self.id + '": {\n\t"ID": "' + self.id + '",\n\t"Name": "' + self.name + '",\n\t"Continuum Layer": "' + self.continuumLayer + '",\n\t"Type": "' + self.type + '",'
        n = 0
        while n < len(self.stepPhases):
            s += '\n\t' + self.stepPhases[n].__str__().replace('\n\t', '\n\t\t').replace('}','\t}')
            n += 1
            if n < len(self.stepPhases):
                s += ','
        if len(self.dataSources) > 0 :
            s += ','
            n = 0
            while n < len(self.dataSources):
                s += '\n\t' + self.dataSources[n].__str__().replace('\n\t', '\n\t\t').replace('}','\t}')
                n += 1
                if n < len(self.dataSources):
                    s += ','
        if len(self.resources) > 0:
            s += ','
            n = 0
            while n < len(self.resources):
                s += '\n\t' + self.resources[n].__str__().replace('\n\t', '\n\t\t').replace('}','\t}')
                n += 1
                if n < len(self.resources):
                    s += ','
        s += '\n}'
        return s
#STEP PHASE
class StepPhase():
    #CONSTRUCTOR
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.technologies = []
        self.environmentVariables = []
    #TO STRING
    def __str__(self):
        s = '"StepPhase_' + self.id + '": {\n\t"ID": "' + self.id + '",\n\t"Name": "' + self.name + '"'
        if len(self.technologies) > 0:
            s += ','
            n = 0
            while n < len(self.technologies):
                s += '\n\t' + self.technologies[n].__str__().replace('\n\t', '\n\t\t').replace('}','\t}')
                n += 1
                if n < len(self.technologies):
                    s += ','
        if len(self.environmentVariables) > 0 :
            s += ','
            n = 0
            while n < len(self.environmentVariables):
                s += '\n\t' + self.environmentVariables[n].__str__().replace('\n\t', '\n\t\t').replace('}','\t}')
                n += 1
                if n < len(self.environmentVariables):
                    s += ','
        s += '\n}'
        return s        
#ENVIRONMENT VARIABLE
class EnvironmentVariable():
    #CONSTRUCTOR
    def __init__(self, key, value):
        self.key = key
        self.value = value
    #TO STRING
    def __str__(self):
        return '"EnvironmentVariable_' + self.key + '": {\n\t"Key": "' + self.key + '",\n\t"Value": "' + self.value + '"\n}'       
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
        return '"DataSource_' + self.id + '": {\n\t"ID": "' + self.id + '",\n\t"Name": "' + self.name + '",\n\t"Volume": "' + self.volume + '",\n\t"Type": "' + self.type + '"\n}'
#DATA STREAM   
class DataStream(DataSource):
   #CONSTRUCTOR
    def __init__(self, id, name, volume, type, velocity):
        super().__init__(id, name, volume, type)
        self.velocity = velocity
    #TO STRING
    def __str__(self):
        return '"DataStream_' + self.id + '": {\n\t"ID": "' + self.id + '",\n\t"Name": "' + self.name + '",\n\t"Volume": "' + self.volume + '",\n\t"Type": "' + self.type + '",\n\t"Velocity": "' + self.velocity + '"\n}'
#TECHNOLOGY
class Technology():
#CONSTRUCTOR
    def __init__(self, id, name, os):
        self.id = id
        self.name = name
        self.os = os
        self.cpus = []
        self.gpus = []
        self.rams = []
        self.storages = []
        self.networks = []
    #TO STRING
    def __str__(self):
        s = '"Technology_' + self.id + '": {\n\t"ID": "' + self.id + '",\n\t"Name": "' + self.name + '",\n\t"OS": "' + self.os + '",'
        n = 0
        while n < len(self.cpus):
            s += '\n\t' + self.cpus[n].__str__().replace('\n\t', '\n\t\t').replace('}','\t}')
            n += 1
            if n < len(self.cpus):
                s += ','
        if len(self.gpus) > 0 :
            s += ','
            n = 0
            while n < len(self.gpus):
                s += '\n\t' + self.gpus[n].__str__().replace('\n\t', '\n\t\t').replace('}','\t}')
                n += 1
                if n < len(self.gpus):
                    s += ','
        if len(self.rams) > 0 :
            s += ','
            n = 0
            while n < len(self.rams):
                s += '\n\t' + self.rams[n].__str__().replace('\n\t', '\n\t\t').replace('}','\t}')
                n += 1
                if n < len(self.rams):
                    s += ','
        if len(self.storages) > 0 :
            s += ','
            n = 0
            while n < len(self.storages):
                s += '\n\t' + self.storages[n].__str__().replace('\n\t', '\n\t\t').replace('}','\t}')
                n += 1
                if n < len(self.storages):
                    s += ','
        if len(self.networks) > 0 :
            s += ','
            n = 0
            while n < len(self.networks):
                s += '\n\t' + self.networks[n].__str__().replace('\n\t', '\n\t\t').replace('}','\t}')
                n += 1
                if n < len(self.networks):
                    s += ','
        s += '\n}'
        return s
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
        return '"RAM_' + self.id + '": {\n\t"ID": "' + self.id + '",\n\t"Volume": "' + self.volume + '",\n\t"Speed": "' + self.speed + '",\n\t"Type": "' + self.type + '",\n\t"Producer": "' + self.producer + '"\n}'    
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
        return '"GPU_' + self.id + '": {\n\t"ID": "' + self.id + '",\n\t"Cores": "' + self.cores + '",\n\t"Speed": "' + self.speed + '",\n\t"Memory": "' + self.memory + '",\n\t"Producer": "' + self.producer + '"\n}'
#CPU
class CPU():
    def __init__(self, id, cores, speed, producer):
        self.id = id
        self.cores = cores
        self.speed = speed
        self.producer = producer
    #TO STRING
    def __str__(self):
        return '"CPU_' + self.id + '": {\n\t"ID": "' + self.id + '",\n\t"Cores": "' + self.cores + '",\n\t"Speed": "' + self.speed + '",\n\t"Producer": "' + self.producer + '"\n}'       
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
        return '"Storage_' + self.id + '": {\n\t"ID": "' + self.id + '",\n\t"Volume": "' + self.volume + '",\n\t"Speed": "' + self.speed + '",\n\t"Type": "' + self.type + '",\n\t"Producer": "' +self.producer + '"\n}'
#NETWORK
class Network():
    def __init__(self, id, bandwidth, latency):
        self.id = id
        self.bandwidth = bandwidth
        self.latency = latency
    #TO STRING
    def __str__(self):
        return '"Network_' + self.id + '": {\n\t"ID": "' + self.id + '",\n\t"Bandwidth": "' + self.bandwidth + '",\n\t"Latency": "' + self.latency + '"\n}' 
