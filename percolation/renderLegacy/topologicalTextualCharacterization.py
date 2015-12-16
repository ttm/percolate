import percolation as P, os
c=P.utils.check
class Bootstrap:
    def __init__(self,endpoint_url,data_dir="/disco/data/",fdir="/root/r/repos/documentation/"):
        """If fdir=None, don't render latex tables"""
        self.res=[]
        metafiles=P.utils.getFiles(data_dir)[:3]
        metagnames=[P.utils.urifyFilename(i) for i in metafiles]
        #foo=P.utils.addToEndpoint(endpoint_url,metafiles)
        oi=self.getOverallInfos(endpoint_url,metagnames)
        dirnames=[os.path.dirname(i) for i in metafiles]
        self.metagnames=metagnames
        self.d={"metafiles":metafiles}
        self.writeOverallTable()
    def writeOverallTable(self):
        labels=[self.odict[i]["label"].split(" ")[-1] for i in self.metagnames]
        labelsh="label","participants","iparticipants","interactions","relations","from","ego","friendship","anon","interaction","anon"
        data=[[self.odict[i][avar] for avar in ("nf","nfi","ni","nfs","ca","ego","f","fa","i","ia")] for i in self.metagnames]
        caption="overview of social datasets"
        P.tableHelpers.lTable(labels,labelsh,data,caption,"tryMe2TT.tex",ttype="strings")
        P.tableHelpers.doubleColumn("tryMe2TT.tex")

    def extra(self):
        # escrita de resumo no grafo de discovery principal
        self.writeOverallEndpoint(oi)
        # carrega translates nos grafos de nomes apropriados (tentar usar uris de snapshots)
        translates=self.loadTranslates(oi)
        # análise geral dos grafos, quais atributos, datas, etc
        analysis=self.overallAnalysis(translates)
        # ESCREVE TABELA
        self.writeOverallTable2(analysis)
        self.oi=oi
        self.translates=translates
        self.analysis=analysis
    def getOverallInfos(self,endpoint_url,metagnames):
        """analisa com os nomes, quantidades, proveniencias e demais infos do Meta"""
        self.odict={}
        for gname in metagnames:
            # faz query para saber a proveniencia
            # pega alguns dados basicos
            # pega endereco dos translates
            qq="SELECT ?{}  WHERE {{ GRAPH <"+ gname +"> {{ ?s <"+str(P.rdf.ns.po.socialProtocol)+"> ?n . }} }}"
            plat=P.utils.mQuery(endpoint_url,qq,("n",))[0][0]
            if plat.endswith("Facebook"):
                qq="SELECT "+"?{} "*13+"WHERE \
                 {{ GRAPH <"+ gname +"> {{            \
                        ?s <"+str(P.rdf.ns.po.createdAt)+">  ?ca .        \
                        ?s <"+str(P.rdf.ns.fb.ego)+">  ?ego .        \
                        ?s <"+str(P.rdf.ns.fb.friendship)+">  ?f .        \
                        ?s <"+str(P.rdf.ns.fb.fAnon)+">  ?fa .        \
                        ?s <"+str(P.rdf.ns.fb.interaction)+">  ?i .        \
                        ?s <"+str(P.rdf.ns.fb.iAnon)+">  ?ia .        \
                        ?s <"+str(P.rdf.ns.rdfs.label)+">  ?label .        \
               OPTIONAL {{ ?s <"+str(P.rdf.ns.fb.nFriends)+"> ?nf .            }} . \
               OPTIONAL {{ ?s <"+str(P.rdf.ns.fb.nFriendships)+">  ?nfs .      }} . \
               OPTIONAL {{ ?s <"+str(P.rdf.ns.fb.nInteractions)+">  ?ni .     }} . \
               OPTIONAL {{ ?s <"+str(P.rdf.ns.fb.nFriendsInteracted)+">  ?nfi .}} . \
               OPTIONAL {{ ?s <"+str(P.rdf.ns.fb.nFriendsInteracted)+">  ?nfi .}} . \
               OPTIONAL {{ ?s <"+str(P.rdf.ns.po.friendshipXMLFile)+">  ?ffile .}} . \
               OPTIONAL {{ ?s <"+str(P.rdf.ns.po.interactionXMLFile)+">  ?ifile .}} . \
                 }} }}"
                keys="nf","nfs","ni","nfi","ca","ego","f","fa","i","ia","ffile","ifile","label"
                vals=P.utils.mQuery(endpoint_url,qq,keys)[0]
                bdict={i:j for i,j in zip(keys,vals)}
                self.odict[gname]=bdict
    def overallAnalysis(self,translates):
        qq="SELECT "+"(COUNT(?s) as ?{}) (COUNT(DISTINCT ?s) as ?{}) (COUNT(DISTINCT ?p) as ?{}) (COUNT(DISTINCT ?o) as ?{}) WHERE \
         {{ GRAPH <"+ gname +"> {{            \
                ?s ?p ?o .        \
         }} }}"
        keys="ntrip","nsubj","npred","nobj"
        vals=P.utils.mQuery(endpoint_url,qq,keys)[0]
        bdict={i:j for i,j in zip(keys,vals)}
        pass
    def writeOverallTable2(self,analysis,fdir):
        pass
class Analyses:
    def __init__(self,bootstrap_instance,graphids=[]):
        aa=[]
        for gid in graphids:
            aa+=Analysis(bootstrap,gid)
        self.aa=aa
    def overallMeasures(self,graphids):
        pass
class Analysis:
    def __init__(self,bootstrap_instance,graphid=None):
        self.boot=bootstrap_instance
        # tudo para as estruturas totais:
        general_info=self.detailedGeneral()
        self.network=self.makeNetwork()
        self.users_sectors=self.getErdosSectorsUsers()
        topological_info=self.topologicalMeasures()
        textual_info=self.textualMeasures()
        temporal_info=self.temporalMeasures()
        scalefree_info=self.scaleFreeTest()
        # explore different scales
    def makeNetwork(self): pass
    def getErdosSectorsUsers(self): pass
    def detailedGeneral(self): pass
    def topologicalMeasures(self): pass
    def textualMeasures(self): pass
    def temporalMeasures(self): pass
    def scaleFreeTest(self): pass
class TimelineAnalysis(Analyses):
    # make Analyses with input graphids
    # plot timelines
    # calculate unitary roots
    # make tables
    def init():
        unitary_info=self.unitaryRoot()
    def unitaryRoot(self): pass
class MultiscaleAnalysis(Analyses):
    # make Analyses with input graphids
    # find bet fit to scale free
    # plot some variables with respect to graphsize
    # render tables
    def init():
        multiscale_info=self.multiScale()
    def multiScale(self): pass

def rdfUnitsTable(end_url,fdir="./tables/",fname="rdfUnits.tex",nrows=None):
    fname_=fdir+fname
    q="SELECT DISTINCT ?{} WHERE {{ GRAPH ?g {{ }} }}"; v="g"
    graphs=[i[0] for i in P.utils.mQuery(end_url,q,v)]
    if nrows:
        graphs=graphs[:nrows]
    graphs=sorted(graphs)
    mres=[]
    mress=[]
    mresp=[]
    mreso=[]
    mresc=[]
    mresi=[]
    for graph in graphs:
        c("check: " +graph)
        q='''SELECT (COUNT(?s) as ?{{}}) (COUNT(DISTINCT ?s) as ?{{}})
                    (COUNT(DISTINCT ?p) as ?{{}}) (COUNT(DISTINCT ?o) as ?{{}})
                    WHERE {{{{ GRAPH <{}> {{{{ ?s ?p ?o }}}} }}}}'''.format(graph)
        mres_,mress_,mresp_,mreso_=P.utils.mQuery(end_url,q,("cs","ds","dp","do"))[0]
        q='''SELECT  (COUNT(DISTINCT ?c) as ?{{}}) (COUNT(DISTINCT ?i) as ?{{}})
                    WHERE {{{{ GRAPH <{}> {{{{ ?i a ?c }}}} }}}}'''.format(graph)
        mresc_,mresi_=P.utils.mQuery(end_url,q,("dc","di"))[0]
        mres+=[mres_]
        mress+=[mress_]
        mresp+=[mresp_]
        mreso+=[mreso_]
        mresc+=[mresc_]
        mresi+=[mresi_]
        #q='SELECT (COUNT(?s) as ?{{}})  WHERE {{{{ GRAPH <{}> {{{{ ?s ?p ?o }}}} }}}}'.format(graph)
        #mres+=P.utils.mQuery(end_url,q,("cs",))[0]
        #q='SELECT (COUNT(DISTINCT ?s) as ?{{}})  WHERE {{{{ GRAPH <{}> {{{{ ?s ?p ?o }}}} }}}}'.format(graph)
        #mress+=P.utils.mQuery(end_url,q,("cs",))[0]
        #q='SELECT (COUNT(DISTINCT ?p) as ?{{}})  WHERE {{{{ GRAPH <{}> {{{{ ?s ?p ?o }}}} }}}}'.format(graph)
        #mresp+=P.utils.mQuery(end_url,q,("cs",))[0]
        #q='SELECT (COUNT(DISTINCT ?o) as ?{{}})  WHERE {{{{ GRAPH <{}> {{{{ ?s ?p ?o }}}} }}}}'.format(graph)
        #mreso+=P.utils.mQuery(end_url,q,("cs",))[0]
    labels=[i.split("http://")[1][:-4] for i in graphs]
    labelsh="graph id","triples","subjects","predicates","objects", "classes","individuals"
    data=[[int(ii) for ii in [i,j,k,l,m,n]] for i,j,k,l,m,n in zip(mres,mress,mresp,mreso,mresc,mresi)]
    caption="count of RDF basic units"
    P.tableHelpers.lTable(labels,labelsh,data,caption,fname_,ttype="textGeral__")
    P.tableHelpers.doubleColumn(fname_)

