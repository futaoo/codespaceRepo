import csv

from rdflib import URIRef, BNode, Literal
from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, \
                           PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, \
                           VOID, XMLNS, XSD
from rdflib import Namespace
from rdflib import Graph

wgs84 = Namespace("http://example.org/people/")
qudt = Namespace("http://qudt.org/1.1/schema/qudt#")
unit = Namespace("http://qudt.org/1.1/vocab/unit#")
dul = Namespace("http://www.loa-cnr.it/ontologies/DUL.owl#")
eca = Namespace("http://example.org/eca/ont/")
cf =  Namespace("http://purl.oclc.org/NET/ssnx/cf/cf-feature")


eca_str = "http://example.org/eca/ont/"

eca_tprtSensor = URIRef(eca_str + "Class/TemperatureSensor")
eca_prcpSensor = URIRef(eca_str + "Class/PrecipitationSensor")
eca_tprtObservation = URIRef(eca_str + "Class/TemperatureObservation")
eca_prcpObservation = URIRef(eca_str + "Class/PrecipitationObservation")
eca_tprtResult = URIRef(eca_str + "Class/TemperatureResult")
eca_prcpResult = URIRef(eca_str + "Class/PrecipitationResult")

triples_classes = [(eca_tprtSensor, RDFS.subClassOf, SOSA.Sensor), (eca_prcpSensor, RDFS.subClassOf, SOSA.Sensor), 
(eca_tprtObservation, RDFS.subClassOf, SOSA.Observation), (eca_prcpObservation, RDFS.subClassOf, SOSA.Observation), 
(eca_tprtResult, RDFS.subClassOf, SOSA.Result), (eca_prcpResult, RDFS.subClassOf, SOSA.Result)]




csvpath = './datasets/shanghaifull.csv'
with open(csvpath) as f:
    csvreader =  csv.reader(f)
    record_head = list(next(csvreader))
    record_rows = list(csvreader)

numof_rowitems = len(record_head)

#print(record_head)

triples_lst = list()

for row in record_rows:
    iri_station =  URIRef(eca_str + row[0])
    iri_station_location = URIRef(eca_str + row[0] + "/" + "location")
    iri_station_sensor_prcp =  URIRef(eca_str + "sensor/" + row[0] + "/" + "prcp")
    iri_station_sensor_tprt =  URIRef(eca_str + "sensor/" + row[0] + "/" + "tprt")
    bn_station_sensor_prcp_observation = URIRef(eca_str + "obsv/" + row[0] + "/"+ "sensor/" + "prcp/" + row[5])
    bn_station_sensor_tprt_observation = URIRef(eca_str + "obsv/" + row[0] + "/"+ "sensor/" + "tprt/" + row[5])

    bn_prcp_result = URIRef(eca_str + row[0] + "/" + "result/" + "sensor/" + "prcp/" + row[5]) #BNode() 
    bn_tprt_result_avg = URIRef(eca_str + row[0] + "/" + "result/" + "sensor/" + "tprt/" + "avg/" + row[5]) #BNode()
    bn_tprt_result_max = URIRef(eca_str + row[0] + "/" + "result/" + "sensor/" + "tprt/" + "max/" + row[5]) #BNode()
    bn_tprt_result_min = URIRef(eca_str + row[0] + "/" + "result/" + "sensor/" + "tprt/" + "min/" + row[5]) #BNode()

    triples_station = [(iri_station, RDF.type, SOSA.Platform),(iri_station, RDFS.label, Literal(row[1])),(iri_station, dul.hasLocation, iri_station_location)]

    triples_station_location = [(iri_station_location, eca.locationID, Literal(row[0])),(iri_station_location, wgs84.lat, Literal(row[2])),(iri_station_location, wgs84.lon, Literal(row[3])),(iri_station_location, wgs84.alt, Literal(row[4]))]
    
    triples_sensor = [(iri_station_sensor_prcp, RDF.type, eca_prcpSensor),(iri_station_sensor_prcp, SOSA.isHostedby, iri_station),
    (iri_station_sensor_prcp, SOSA.observes, cf.precipitation_amount)]
    
    triples_sensor.extend([(iri_station_sensor_tprt, RDF.type, eca_tprtSensor),(iri_station_sensor_tprt, SOSA.isHostedby, iri_station),
    (iri_station_sensor_tprt, SOSA.observes, cf.air_temperature)])

    triples_result = []
    
    triples_abservation = [(bn_station_sensor_prcp_observation, RDF.type, eca_prcpObservation),(bn_station_sensor_prcp_observation, SOSA.resultTime,Literal(row[5],datatype=XSD.date)),
    (bn_station_sensor_prcp_observation, SOSA.observedProperty, cf.precipitation_amount),(bn_station_sensor_prcp_observation, SOSA.madeBySensor, iri_station_sensor_prcp)]

    triples_abservation.extend([(bn_station_sensor_tprt_observation, RDF.type, eca_tprtObservation), (bn_station_sensor_tprt_observation, SOSA.resultTime, Literal(row[5],datatype=XSD.date)),
    (bn_station_sensor_tprt_observation, SOSA.observedProperty, cf.air_temperature),(bn_station_sensor_tprt_observation, SOSA.madeBySensor, iri_station_sensor_tprt)])

    if row[record_head.index("PRCP")] != "" :
        triples_abservation.extend([(bn_station_sensor_prcp_observation, SOSA.hasResult, bn_prcp_result)])
        triples_result.extend([(bn_prcp_result, RDF.type, eca_prcpResult),(bn_prcp_result, RDF.type, qudt.QuantityValue),(bn_prcp_result, qudt.unit, unit.Inch),(bn_prcp_result, qudt.numericValue, Literal(row[record_head.index("PRCP")],datatype=XSD.float))])

    if row[record_head.index("TAVG")] != "" :
        triples_abservation.extend([(bn_station_sensor_tprt_observation, SOSA.hasResult, bn_tprt_result_avg)])
        triples_result.extend([(bn_tprt_result_avg, RDFS.label, Literal("avg")), (bn_tprt_result_avg, RDF.type, eca_tprtResult), (bn_tprt_result_avg, RDF.type, qudt.QuantityValue), (bn_tprt_result_avg, qudt.unit, unit.DegreeFahrenheit),(bn_tprt_result_avg, qudt.numericValue, Literal(row[record_head.index("TAVG")],datatype=XSD.float))])
    if row[record_head.index("TMIN")] != "" :
        triples_abservation.extend([(bn_station_sensor_tprt_observation, SOSA.hasResult, bn_tprt_result_min)])
        triples_result.extend([(bn_tprt_result_min, RDFS.label, Literal("min")), (bn_tprt_result_min, RDF.type, eca_tprtResult), (bn_tprt_result_min, RDF.type, qudt.QuantityValue), (bn_tprt_result_min, qudt.unit, unit.DegreeFahrenheit),(bn_tprt_result_min, qudt.numericValue, Literal(row[record_head.index("TMIN")],datatype=XSD.float))])
    if row[record_head.index("TMAX")] != "" :
        triples_abservation.extend([(bn_station_sensor_tprt_observation, SOSA.hasResult, bn_tprt_result_max)])
        triples_result.extend([(bn_tprt_result_max, RDFS.label, Literal("max")), (bn_tprt_result_max, RDF.type, eca_tprtResult), (bn_tprt_result_max, RDF.type, qudt.QuantityValue), (bn_tprt_result_max, qudt.unit, unit.DegreeFahrenheit),(bn_tprt_result_max, qudt.numericValue, Literal(row[record_head.index("TMAX")],datatype=XSD.float))])

    triples_temp = triples_station+triples_station_location + triples_sensor + triples_abservation + triples_result

    triples_lst += triples_temp

triples_lst += triples_classes
g = Graph()
g.bind("wgs84", wgs84)
g.bind("qudt", qudt)
g.bind("dul", dul)
g.bind("cf", cf)
g.bind("unit",unit)
g.bind("eca", eca)
g.bind("ssn", SSN)
g.bind("sosa", SOSA)
g.bind("rdfs", RDFS)
g.bind("rdf", RDF)



for triple in triples_lst:
    g.add(triple)


print(g.serialize(format="turtle").decode("utf-8"))





