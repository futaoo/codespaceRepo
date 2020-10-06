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
ca = Namespace("http://example.org/ca/ont/")
cf =  Namespace("http://purl.oclc.org/NET/ssnx/cf/cf-feature")


ca_str = "http://example.org/ca/ont/"

ca_tprtSensor = URIRef(ca_str + "Class/TemperatureSensor")
ca_prcpSensor = URIRef(ca_str + "Class/PrecipitationSensor")
ca_tprtObservation = URIRef(ca_str + "Class/TemperatureObservation")
ca_prcpObservation = URIRef(ca_str + "Class/PrecipitationObservation")
ca_tprtResult = URIRef(ca_str + "Class/TemperatureResult")
ca_prcpResult = URIRef(ca_str + "Class/PrecipitationResult")

triples_classes = [(ca_tprtSensor, RDFS.subClassOf, SOSA.Sensor), (ca_prcpSensor, RDFS.subClassOf, SOSA.Sensor), 
(ca_tprtObservation, RDFS.subClassOf, SOSA.Observation), (ca_prcpObservation, RDFS.subClassOf, SOSA.Observation), 
(ca_tprtResult, RDFS.subClassOf, SOSA.Result), (ca_prcpResult, RDFS.subClassOf, SOSA.Result)]




csvpath = './datasets/73_78.csv'
with open(csvpath) as f:
    csvreader =  csv.reader(f)
    record_head = list(next(csvreader))
    record_rows = list(csvreader)

numof_rowitems = len(record_head)

#print(record_head)

triples_lst = list()

for row in record_rows:
    iri_station =  URIRef(ca_str + row[record_head.index("STATION")])
    iri_station_location = URIRef(ca_str + row[record_head.index("STATION")] + "/" + "location")
    iri_station_sensor_prcp =  URIRef(ca_str + "sensor/" + row[record_head.index("STATION")] + "/" + "prcp")
    iri_station_sensor_tprt =  URIRef(ca_str + "sensor/" + row[record_head.index("STATION")] + "/" + "tprt")
    bn_station_sensor_prcp_observation = URIRef(ca_str + "obsv/" + row[record_head.index("STATION")] + "/"+ "sensor/" + "prcp/" + row[record_head.index("DATE")])
    bn_station_sensor_tprt_observation = URIRef(ca_str + "obsv/" + row[record_head.index("STATION")] + "/"+ "sensor/" + "tprt/" + row[record_head.index("DATE")])

    bn_prcp_result_prcp = URIRef(ca_str + row[record_head.index("STATION")] + "/" + "result/" + "sensor/" + "prcp/" + "prcp/" + row[record_head.index("DATE")]) #BNode() 
    bn_prcp_result_snwd = URIRef(ca_str + row[record_head.index("STATION")] + "/" + "result/" + "sensor/" + "prcp/" + "snwd/" + row[record_head.index("DATE")]) #BNode()
    bn_tprt_result_avg = URIRef(ca_str + row[record_head.index("STATION")] + "/" + "result/" + "sensor/" + "tprt/" + "avg/" + row[record_head.index("DATE")]) #BNode()
    bn_tprt_result_max = URIRef(ca_str + row[record_head.index("STATION")] + "/" + "result/" + "sensor/" + "tprt/" + "max/" + row[record_head.index("DATE")]) #BNode()
    bn_tprt_result_min = URIRef(ca_str + row[record_head.index("STATION")] + "/" + "result/" + "sensor/" + "tprt/" + "min/" + row[record_head.index("DATE")]) #BNode()

    triples_station = [(iri_station, RDF.type, SOSA.Platform),(iri_station, RDFS.label, Literal(row[record_head.index("NAME")])),(iri_station, dul.hasLocation, iri_station_location)]

    triples_station_location = [(iri_station_location, ca.locationID, Literal(row[record_head.index("STATION")])),(iri_station_location, wgs84.lat, Literal(row[record_head.index("LATITUDE")])),
    (iri_station_location, wgs84.lon, Literal(row[record_head.index("LONGITUDE")])),(iri_station_location, wgs84.alt, Literal(row[record_head.index("ELEVATION")]))]
    
    triples_sensor = [(iri_station_sensor_prcp, RDF.type, ca_prcpSensor),(iri_station_sensor_prcp, SOSA.isHostedby, iri_station),
    (iri_station_sensor_prcp, SOSA.observes, cf.precipitation_amount)]
    
    triples_sensor.extend([(iri_station_sensor_tprt, RDF.type, ca_tprtSensor),(iri_station_sensor_tprt, SOSA.isHostedby, iri_station),
    (iri_station_sensor_tprt, SOSA.observes, cf.air_temperature)])

    triples_result = []
    
    triples_abservation = [(bn_station_sensor_prcp_observation, RDF.type, ca_prcpObservation),(bn_station_sensor_prcp_observation, SOSA.resultTime,Literal(row[record_head.index("DATE")],datatype=XSD.date)),
    (bn_station_sensor_prcp_observation, SOSA.observedProperty, cf.precipitation_amount),(bn_station_sensor_prcp_observation, SOSA.madeBySensor, iri_station_sensor_prcp)]

    triples_abservation.extend([(bn_station_sensor_tprt_observation, RDF.type, ca_tprtObservation), (bn_station_sensor_tprt_observation, SOSA.resultTime, Literal(row[record_head.index("DATE")],datatype=XSD.date)),
    (bn_station_sensor_tprt_observation, SOSA.observedProperty, cf.air_temperature),(bn_station_sensor_tprt_observation, SOSA.madeBySensor, iri_station_sensor_tprt)])

    if row[record_head.index("PRCP")] != "" :
        triples_abservation.extend([(bn_station_sensor_prcp_observation, SOSA.hasResult, bn_prcp_result_prcp)])
        triples_result.extend([(bn_prcp_result_prcp, RDFS.label, Literal("precipitation")), (bn_prcp_result_prcp, RDF.type, ca_prcpResult),(bn_prcp_result_prcp, RDF.type, qudt.QuantityValue),(bn_prcp_result_prcp, qudt.unit, unit.Inch),(bn_prcp_result_prcp, qudt.numericValue, Literal(row[record_head.index("PRCP")],datatype=XSD.float))])
    if row[record_head.index("SNWD")] != "" :
        triples_abservation.extend([(bn_station_sensor_prcp_observation, SOSA.hasResult, bn_prcp_result_snwd)])
        triples_result.extend([(bn_prcp_result_snwd, RDFS.label, Literal("snow_depth")), (bn_prcp_result_snwd, RDF.type, ca_prcpResult),(bn_prcp_result_snwd, RDF.type, qudt.QuantityValue),(bn_prcp_result_snwd, qudt.unit, unit.Inch),(bn_prcp_result_snwd, qudt.numericValue, Literal(row[record_head.index("SNWD")],datatype=XSD.float))])


    if row[record_head.index("TAVG")] != "" :
        triples_abservation.extend([(bn_station_sensor_tprt_observation, SOSA.hasResult, bn_tprt_result_avg)])
        triples_result.extend([(bn_tprt_result_avg, RDFS.label, Literal("avg")), (bn_tprt_result_avg, RDF.type, ca_tprtResult), (bn_tprt_result_avg, RDF.type, qudt.QuantityValue), (bn_tprt_result_avg, qudt.unit, unit.DegreeFahrenheit),(bn_tprt_result_avg, qudt.numericValue, Literal(row[record_head.index("TAVG")],datatype=XSD.float))])
    if row[record_head.index("TMIN")] != "" :
        triples_abservation.extend([(bn_station_sensor_tprt_observation, SOSA.hasResult, bn_tprt_result_min)])
        triples_result.extend([(bn_tprt_result_min, RDFS.label, Literal("min")), (bn_tprt_result_min, RDF.type, ca_tprtResult), (bn_tprt_result_min, RDF.type, qudt.QuantityValue), (bn_tprt_result_min, qudt.unit, unit.DegreeFahrenheit),(bn_tprt_result_min, qudt.numericValue, Literal(row[record_head.index("TMIN")],datatype=XSD.float))])
    if row[record_head.index("TMAX")] != "" :
        triples_abservation.extend([(bn_station_sensor_tprt_observation, SOSA.hasResult, bn_tprt_result_max)])
        triples_result.extend([(bn_tprt_result_max, RDFS.label, Literal("max")), (bn_tprt_result_max, RDF.type, ca_tprtResult), (bn_tprt_result_max, RDF.type, qudt.QuantityValue), (bn_tprt_result_max, qudt.unit, unit.DegreeFahrenheit),(bn_tprt_result_max, qudt.numericValue, Literal(row[record_head.index("TMAX")],datatype=XSD.float))])

    triples_temp = triples_station+triples_station_location + triples_sensor + triples_abservation + triples_result

    triples_lst += triples_temp

triples_lst += triples_classes
g = Graph()
g.bind("wgs84", wgs84)
g.bind("qudt", qudt)
g.bind("dul", dul)
g.bind("cf", cf)
g.bind("unit",unit)
g.bind("ca", ca)
g.bind("ssn", SSN)
g.bind("sosa", SOSA)
g.bind("rdfs", RDFS)
g.bind("rdf", RDF)

 

for triple in triples_lst:
    g.add(triple)


print(g.serialize(format="turtle").decode("utf-8"))





