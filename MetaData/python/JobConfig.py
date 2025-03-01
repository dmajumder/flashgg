import FWCore.ParameterSet.VarParsing as VarParsing
from flashgg.MetaData.samples_utils import SamplesManager
import FWCore.ParameterSet.Config as cms


class JobConfig(object):
    
    def __init__(self,*args,**kwargs):
        
        super(JobConfig,self).__init__()

#        self.metaDataSrc=kwargs.get("metaDataSrc","flashgg")
        self.crossSections=kwargs.get("crossSections",["$CMSSW_BASE/src/flashgg/MetaData/data/cross_sections.json"])
        self.tfileOut=kwargs.get("tfileOut",None)

        self.processIdMap = {}

        self.options = VarParsing.VarParsing("analysis")
        ## self.options.setDefault ('maxEvents',100)
        self.options.register ('metaDataSrc',
                               'flashgg', # default value
                               VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                               VarParsing.VarParsing.varType.string,          # string, int, or float
                               "metaDataSrc")
        self.options.register ('dataset',
                       "", # default value
                       VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                       VarParsing.VarParsing.varType.string,          # string, int, or float
                       "dataset")
        self.options.register ('processId',
                       "", # default value
                       VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                       VarParsing.VarParsing.varType.string,          # string, int, or float
                       "processId")
        self.options.register ('processIdMap',
                       "", # default value
                       VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                       VarParsing.VarParsing.varType.string,          # string, int, or float
                       "processIdMap")
        self.options.register ('processIndex',
                       None, # default value
                       VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                       VarParsing.VarParsing.varType.int,          # string, int, or float
                       "processIndex")
        self.options.register ('secondaryDatasetInProcId',
                       False, # default value
                       VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                       VarParsing.VarParsing.varType.bool,          # string, int, or float
                       "secondaryDatasetInProcId")
        self.options.register ('campaign',
                       "", # default value
                       VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                       VarParsing.VarParsing.varType.string,          # string, int, or float
                       "campaign")
        self.options.register ('useAAA',
                       False, # default value
                       VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                       VarParsing.VarParsing.varType.bool,          # string, int, or float
                       "useAAA")
        self.options.register ('useEOS',
                       True, # default value
                       VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                       VarParsing.VarParsing.varType.bool,          # string, int, or float
                       "useEOS")
        self.options.register ('targetLumi',
                       1.e+3, # default value
                       VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                       VarParsing.VarParsing.varType.float,          # string, int, or float
                       "targetLumi")
        self.options.register ('nJobs',
                       0, # default value
                       VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                       VarParsing.VarParsing.varType.int,          # string, int, or float
                       "nJobs")
        self.options.register ('jobId',
                               -1, # default value
                               VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                               VarParsing.VarParsing.varType.int,          # string, int, or float
                               "jobId")
        self.options.register ('lastAttempt',
                       False, # default value
                       VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                       VarParsing.VarParsing.varType.bool,          # string, int, or float
                       "lastAttempt")
        self.options.register ('lumiMask',
                       "", # default value
                       VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                       VarParsing.VarParsing.varType.string,          # string, int, or float
                       "lumiMask")
        self.options.register ('dryRun',
                       False, # default value
                       VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                       VarParsing.VarParsing.varType.bool,          # string, int, or float
                       "dryRun")
        self.options.register ('dumpPython',
                       "", # default value
                       VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                       VarParsing.VarParsing.varType.string,          # string, int, or float
                       "dumpPython")
        self.options.register ('getMaxJobs',
                       False, # default value
                       VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                       VarParsing.VarParsing.varType.bool,          # string, int, or float
                       "getMaxJobs")
        self.options.register ('processType',
                               "", # default value
                               VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                               VarParsing.VarParsing.varType.string,          # string, int, or float
                               "processType")
        self.options.register ('puTarget',
                               "", # default value
                               VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                               VarParsing.VarParsing.varType.string,          # string, int, or float
                               "puTarget")

        
        self.parsed = False
        
        
        from SimGeneral.MixingModule.mix_2015_25ns_Startup_PoissonOOTPU_cfi import mix as mix_2015_25ns
        from SimGeneral.MixingModule.mix_2015_50ns_Startup_PoissonOOTPU_cfi import mix as mix_2015_50ns
        self.pu_distribs = { "74X_mcRun2_asymptotic_v2" : mix_2015_25ns.input.nbPileupEvents }
        try:
            from SimGeneral.MixingModule.mix_2015_25ns_FallMC_matchData_PoissonOOTPU_cfi import mix as mix_2015_76_25ns
            self.pu_distribs["PU25nsData2015v1"] = mix_2015_76_25ns.input.nbPileupEvents
        except Exception:
            print "Failed to load 76X mixing, this is expected in 74X!"
            
        try:
            from SimGeneral.MixingModule.mix_2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU_cfi import mix as mix_2016_80_25ns
            self.pu_distribs["PUSpring16"] = mix_2016_80_25ns.input.nbPileupEvents
        except Exception:
            print "Failed to load 80X mixing, this is expected in 7X!"

        try:
            from SimGeneral.MixingModule.mix_2016_25ns_Moriond17MC_PoissonOOTPU_cfi import mix as mix_Moriond17
            self.pu_distribs["Summer16"] = mix_Moriond17.input.nbPileupEvents
            self.pu_distribs["PUMoriond17"] = mix_Moriond17.input.nbPileupEvents
            self.pu_distribs["upgrade2017"] = mix_Moriond17.input.nbPileupEvents
        except Exception:
            print "Failed to load Moriond17 mixing, this is expected in earlier releases"

            
    def __getattr__(self,name):
        ## did not manage to inherit from VarParsing, because of some issues in __init__
        ## this allows to use VarParsing methods on JobConfig
        if hasattr(self.options,name):
            return getattr(self.options,name)
        
        raise AttributeError
    
    def __call__(self,process):
        self.customize(process)
 
    # process customization
    def customize(self,process):
        self.parse()

        isFwlite = False
        hasOutput = False
        hasTFile = False
        sp_unused = ""
        if hasattr(process,"fwliteInput"):
            isFwlite = True
        if not isFwlite:
            hasOutput = hasattr(process,"out")            
            hasTFile = hasattr(process,"TFileService")
        
        if hasOutput and hasTFile:
            tfile = self.outputFile.replace(".root","_histos.root")
        else:
            tfile = self.outputFile
            
        if self.dryRun:
            import sys
            if self.dataset and self.dataset != "":
                name,xsec,totEvents,files,maxEvents,sp_unused = self.dataset
                if self.getMaxJobs:
                    print "maxJobs:%d" % ( min(len(files),self.nJobs) )                    
                if len(files) != 0:
                    if isFwlite:
                        print "hadd:%s" % self.outputFile
                    else:
                        if hasOutput:
                            print "edm:%s" % self.outputFile
                        if hasTFile or self.tfileOut:
                            print "hadd:%s" % tfile
                    ## sys.exit(0)
            else:
                sys.exit(1)
            
        files = self.inputFiles
        if self.dataset and self.dataset != "":
            dsetname,xsec,totEvents,files,maxEvents,sp_unused = self.dataset
            if type(xsec) == float or xsec == None:
                print 
                print "Error: cross section not found for dataset %s" % dsetname
                print
                
            self.maxEvents = int(maxEvents)
            
            putarget = None
            samplepu = None
            if self.puTarget != "":
                putarget = map(float, self.puTarget.split(","))
                
            processId = self.getProcessId(dsetname)
            self.processId = processId

            #----------

            if self.options.processIndex != None:
                self.processIndex = self.options.processIndex
            else:
                # not specified on the command line, try to take it 
                # from the cross section file, otherwise use smallest int32 as default value
                # in order not to confuse it with data (index 0)

                if isinstance(xsec, dict):
                    self.processIndex = xsec.get('itype', -0x7FFFFFFF)
                else:
                    # note that in some cases (process not defined in cross_sections.json ?)
                    # this can still be a float
                    self.processIndex = -0x7FFFFFFF

            #----------

            if isinstance(xsec, dict) and "itype" in xsec:
                for name,obj in process.__dict__.iteritems():
                    if hasattr(obj, "sampleIndex"):
                        obj.sampleIndex = xsec["itype"]

            
            isdata = self.processType == "data"
            if isdata or self.targetLumi > 0. or putarget:
                ## look for analyzers which have lumiWeight as attribute
                for name,obj in process.__dict__.iteritems():
                    
                    if hasattr(obj,"lumiWeight"):
                        if  isdata:
                            obj.lumiWeight = 1.
                        else:
                            wei = xsec["xs"]/float(totEvents)*self.targetLumi
                            wei *= xsec.get("br",1.)
                            wei *= xsec.get("kf",1.)
                            obj.lumiWeight = wei

                    if hasattr(obj,"intLumi"):
                        if isdata:
                            obj.intLumi= 0 # should not be used in final fits.
                            # setting to 0 will cause error if someone tries to use
                            #it for normalization downsteram
                        else:
                            obj.intLumi=self.targetLumi

                    if putarget and not isdata:
                        puObj = None
                        if hasattr(obj,"puReWeight"):
                            puObj = obj
                        elif hasattr(obj,"globalVariables") and hasattr(obj.globalVariables,"puReWeight"):
                            puObj = obj.globalVariables
                        if puObj:
                            if not samplepu:
                                matches = filter(lambda x: x in dsetname, self.pu_distribs.keys() )
                                print matches
                                if len(matches) > 1:
                                    print "Multiple matches, check if they're all the same"
                                    allsame = True
                                    for i in range(1,len(matches)):
                                        if self.pu_distribs[matches[0]] != self.pu_distribs[matches[i]]:
                                            allsame = False
                                    if allsame:
                                        print "They're all the same so we just take the 0th one:",matches[0]
                                        matches = [matches[0]]
                                    else:
                                        print "Not all the same... so we return to the old behavior and take an exact match, otherwise leave empty..."
                                        matches = filter(lambda x: x == dsetname, matches)
                                if len(matches) != 1:
                                    raise Exception("Could not determine sample pu distribution for reweighting. Possible matches are [%s]. Selected [%s]\n dataset: %s" % 
                                                ( ",".join(self.pu_distribs.keys()), ",".join(matches), dsetname ) )
                                samplepu = self.pu_distribs[matches[0]]
                            puObj.puReWeight = True
                            puObj.puBins = cms.vdouble( map(float, samplepu.probFunctionVariable) )
                            puObj.mcPu   = samplepu.probValue
                            puObj.dataPu = cms.vdouble(putarget)
                            puObj.useTruePu = cms.bool(True)
                        
                    
            for name,obj in process.__dict__.iteritems():
                if hasattr(obj,"processId"):
                    obj.processId = str(processId)

            for name,obj in process.__dict__.iteritems():
                if hasattr(obj,"processIndex"):
                    obj.processIndex = int(self.processIndex)
                    
            lumisToSkip = None
            if isdata:
                lumisToSkip = self.samplesMan.getLumisToSkip(dsetname)
                process.source.lumisToSkip = lumisToSkip.getVLuminosityBlockRange()

            if isdata and self.lumiMask != "":
                if isFwlite:
                    sys.exit("Lumi mask not supported in FWlite",-1)

                import FWCore.PythonUtilities.LumiList as LumiList
                target = LumiList.LumiList(filename = self.lumiMask)
                if lumisToSkip: 
                    target = target.__sub__(lumisToSkip)                    
                process.source.lumisToProcess = target.getVLuminosityBlockRange()

            if isdata:    
                print process.source.lumisToProcess
            
        flist = []
        for f in files:
            if len(f.split(":",1))>1:
                flist.append(str(f))
            else:
                flist.append(str("%s%s" % (self.filePrepend,f)))
        if len(flist) > 0:
            ## fwlite
            if isFwlite:
                ## process.fwliteInput.fileNames.extend([ str("%s%s" % (self.filePrepend,f)) for f in  files])
                process.fwliteInput.fileNames = flist
            ## full framework
            else:
                ## process.source.fileNames.extend([ str("%s%s" % (self.filePrepend,f)) for f in  files])
                process.source.fileNames = flist
 
        ## fwlite
        if isFwlite:
            process.fwliteInput.maxEvents = self.maxEvents
            process.fwliteOutput.fileName = self.outputFile
        ## full framework
        else:
            process.maxEvents.input = self.maxEvents
            
            if hasOutput:
                process.out.fileName = self.outputFile

            if hasTFile:
                process.TFileService.fileName = tfile
    
        if self.tfileOut:
            if hasTFile:
                print "Could not run with both TFileService and custom tfileOut"
                sys.exit(-1)
            name,attr = self.tfileOut
            setattr( getattr( process, name ), attr, tfile )
            

        if self.dumpPython != "":
            from gzip import open
            pyout = open("%s.gz" % self.dumpPython,"w+")
            pyout.write( process.dumpPython() )
            pyout.close()

    # parse command line and do post-processing
    def parse(self):

        if self.parsed:
            return

        self.options.parseArguments()
#        print "parsing arguments, processIdnex is "+str(self.options.processIndex)
        self.processIndex = self.options.processIndex
        if self.options.processIdMap != "":
            self.readProcessIdMap(self.options.processIdMap)
        
        if self.useAAA:
            self.filePrepend = "root://xrootd-cms.infn.it/"
        elif self.useEOS:
            self.filePrepend = "root://eoscms.cern.ch//eos/cms"
        
        self.samplesMan = None
        dataset = None
        if self.dataset != "":
            print "Reading dataset (%s) %s" % ( self.campaign, self.dataset)
            self.samplesMan = SamplesManager("$CMSSW_BASE/src/%s/MetaData/data/%s/datasets*.json" % (self.metaDataSrc, self.campaign),
                                         self.crossSections,
                                         )
            if self.dryRun and self.getMaxJobs:
                dataset = self.samplesMan.getDatasetMetaData(self.maxEvents,self.dataset,jobId=-1,nJobs=self.nJobs)
            else:
                dataset = self.samplesMan.getDatasetMetaData(self.maxEvents,self.dataset,jobId=self.jobId,nJobs=self.nJobs)
            if not dataset: 
                print "Could not find dataset %s in campaing %s/%s" % (self.dataset,self.metaDataSrc,self.campaing)
                sys.exit(-1)
                
        self.dataset = dataset
        # auto-detect data from xsec = 0
        if self.dataset:
            name,xsec,totEvents,files,maxEvents,specialPrepend = self.dataset
            if len(specialPrepend) > 0 and not self.useAAA:
                self.filePrepend = specialPrepend
            if type(xsec) != dict or type(xsec.get("xs",None)) != float:
                print "Warning: you are running on a dataset for which you specified no cross section: \n %s " % name
            else:
                if self.processType == "" and xsec["xs"] == 0.:
                    self.processType = "data"
                    
            self.processId = self.getProcessId(name)
            
        outputFile=self.outputFile
        if self.jobId != -1:
            outputFile = "%s_%d.root" % ( outputFile.replace(".root",""), self.jobId )
        self.setType ("outputFile", VarParsing.VarParsing.varType.string)
        self.outputFile = outputFile

        self.parsed=True

    def datasetName(self):
        if type(self.dataset) == tuple:
            return self.dataset[0]
        return self.dataset
    
    def getProcessId(self,name):
        return self.getProcessId_(name).replace("/","").replace("-","_")
    
    def getProcessId_(self,name):
        if self.processId != "":
            return self.processId
        
        ## print name, self.processIdMap
        if name in self.processIdMap:
            return self.processIdMap[name]

        primSet,secSet = name.rsplit("/")[1:3]
        if primSet in self.processIdMap:
            return self.processIdMap[primSet]

        primSet = "/"+primSet
        if primSet in self.processIdMap:
            return self.processIdMap[primSet]
        
        if self.secondaryDatasetInProcId:
            return primSet + "_" + secSet
        return primSet

    def readProcessIdMap(self,fname):
        
        with open(fname) as fin:
            import json

            cfg = json.loads(fin.read())
            
            processes = cfg["processes"]
            for key,val in processes.iteritems():
                for dst in val:
                    if type(dst) == list:
                        name = dst[0]
                    else:
                        name = dst
                    self.processIdMap[name] = key
            
            fin.close()

        
# customization object
customize = JobConfig()
