
# inspired from https://github.com/indigo-lab/geonamesjp_vs_dbpedia/blob/master/2015-07-17.ttl


print """
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix grddl: <http://www.w3.org/2003/g/data-view#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix void: <http://rdfs.org/ns/void#>.

@prefix wds: <http://www.wikidata.org/entity/statement/>.
@prefix p: <http://www.wikidata.org/prop/>.
@prefix wdt: <http://www.wikidata.org/prop/direct/>.
@prefix wd: <http://www.wikidata.org/entity/>.
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .
@prefix enmap: <enmap.ttl#>.

<>      a                   void:Linkset ;
        dcterms:created     "2017-07-02"^^xsd:date ;
        dcterms:creator     "James Michael DuPont" ;
        dcterms:license     <http://unlicense.org> ;
        dcterms:modified    "2017-07-02"^^xsd:date ;
        void:linkPredicate  owl:sameAs ;
        void:target         [ a              void:Dataset ;
                              rdfs:label     "Wikidata" ;
                              foaf:homepage  <www.wikidata.org/>
                            ] .


"""

#print "http://www.wikidata.org/prop/direct/P149"

o= open("wikidata_english_predicate_names.tsv")
for x in o.readlines():
    (p,n)=x.split("\t")
    if p == 'pred':
        continue
    n = n.strip()
    #print n
    n = n.encode('ascii', 'replace')
    
    print "\tenmap:{0} owl:sameAs wdt:{1}.".format(n,p)
