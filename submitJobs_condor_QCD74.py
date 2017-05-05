#!/usr/bin/python
import os, sys
import shlex, subprocess
from datetime import datetime, date
import time
#sys.path.append(os.path.abspath(os.path.curdir))

JobTime = datetime.now()
fTag = JobTime.strftime("%Y%m%d_%H%M%S")
dirname = "jobs/QCD74_%s"%fTag

try:
    os.makedirs(dirname)
except:
    pass

OutDirTag = "QCD74_v3p3"
outDir = "/data/users/jengbou/output/"+OutDirTag

try:
    os.makedirs(outDir)
except:
    pass


## note if nFilesPerJob changed remember to change accordingly for submitJobs afterward
nFilesPerJob = 1

QCDsets = [
##    '1000to1500',
##    '1500to2000',
    '2000toInf',
##    '700to1000',
##    '500to700',
    ]

for sName in QCDsets:

    fin=open('QCD74_HT%s.txt'%sName,'r')

    fout = open('%s/QCD74_HT%s_1.txt'%(dirname,sName),'w')
    fidx = 1
    idx = 0

    for line in fin:
        if idx!= 0 and idx % nFilesPerJob == 0:
            fout.close()
            fout = open('%s/QCD74_HT%s_%i.txt'%(dirname,sName,fidx+1),'w')
            fidx+=1

        fout.write(line)

        idx+=1

    print "# of files = ",fidx
    fin.close()
    fout.close()

    condor_script_template = """
    universe = vanilla
    Executable = condor-executable.sh
    +IsLocalJob = true
    Should_transfer_files = NO
    Requirements = TARGET.FileSystemDomain == "privnet"
    Output = /data/users/jengbou/output/%(OUTSUBDIR)s/%(MYPREFIX)s_sce_$(cluster)_$(process).stdout
    Error  = /data/users/jengbou/output/%(OUTSUBDIR)s/%(MYPREFIX)s_sce_$(cluster)_$(process).stderr
    Log    = /data/users/jengbou/output/%(OUTSUBDIR)s/%(MYPREFIX)s_sce_$(cluster)_$(process).condor
    Arguments = %(MYPREFIX)s $(process) /data/users/jengbou/output/%(OUTSUBDIR)s/  /data/users/jengbou/workspace/CMSSW_7_6_3/src/EmergingJetAnalysis  Configuration/test/condor_cfg.py 1234567 10000 %(MYFILENAME)s
    Queue 1
    """

    for j in xrange(1,fidx+1):
        kw = {}

        kw["MYFILENAME"] = "%s/QCD74_HT%s_%i.txt"%(dirname,sName,j)
        kw["MYPREFIX"] = "QCD74_HT%s_%i"%(sName,j)
        kw["OUTSUBDIR"] = OutDirTag

        script_str = condor_script_template % kw
        f = open("%s/condor_jobs_QCD74_HT%s_%i.jdl"%(dirname,sName,j), 'w')
        f.write(script_str)
        f.close()

        condorcmd = "condor_submit %s/condor_jobs_QCD74_HT%s_%i.jdl"%(dirname,sName,j)
        print 'condorcmd: ', condorcmd
        print 'Executing condorcmd'

        p=subprocess.Popen(condorcmd, shell=True)
        p.wait()
        if j % 100 == 0: time.sleep(600)
