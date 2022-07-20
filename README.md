[![CI](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/workflows/Sheet2RDF/badge.svg)](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/actions?query=workflow%3ASheet2RDF)

# Wind lidar ontology
This repository provides the source file for a wind lidar ontology. The Task 32 wind lidar ontology is a controlled vocabulary about wind lidar that also includes a hierarchy, synonyms, and interrelationships. It can be used to help organise and explore data, publications and software.

[**Check out a human-friendly version of the ontology**](http://vocab.ieawindtask32.org/wind-lidar-ontology/).


## Based on the OpenLidar module definitions
This ontology includes terms used to describe the design of a wind lidar. These are structured according to the modular layout proposed in [the OpenLidar project](https://doi.org/10.5281/zenodo.3414197) and described in detail [here](https://github.com/e-WindLidar/OpenLidarModuleDefinitions/).

![The OpenLidar modular wind lidar architecture](https://github.com/e-WindLidar/OpenLidarModuleDefinitions/blob/master/OpenLidarModules.png)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3414197.svg)](https://doi.org/10.5281/zenodo.3414197)

## Developed using sheet2df and OntoStack
We use [sheet2rdf](https://github.com/fair-data-collective/sheet2rdf) to build wind lidar ontology, while DTU Wind Energy instance of OntoStack to serve the ontology. `sheet2rdf` and `OntoStack` are developed by [FAIR Data Collective](https://dk.linkedin.com/company/fair-data-collective).


## How to use this ontology
There are several ways the ontology.

### As a glossary
If you just want to know what a certain lidar-related term means, [check out a human-friendly version of the ontology**](http://vocab.ieawindtask32.org/ontolidar/en/).

### To define the inputs for simulations
The ontology defines a structure for the data that describe the design of a wind lidar and how it is used. This could be encoded in a YAML file and used as the input to a lidar simulation.

### To define a reference lidar device
The ontology defines a structure for the data that describe the design of a wind lidar. A very incomplete example of how this could be used is included as [`reference-designs/staring_lidar.yaml`](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/blob/main/reference-designs/staring_lidar.yml).

## Implementation

### The ontology file
The actual ontology is contained in ontology.ttl.

### Syntax
The file is written using the [Simple Knowledge Organisation System (skos) schema](https://www.w3.org/2009/08/skos-reference/skos.html). It can be checked for conformance to the skos schema using e.g. the [SPARNA skos verification tool](https://labs.sparna.fr/skos-testing-tool/test?url=https://raw.githubusercontent.com/IEA-Wind-Task-32/wind-lidar-glossary/main/glossary.ttl&rules=anr,chr,dcc,dlv,el,hr,husv,ilc,ipl,ml,mri,ncl,oc,oilt,ol,otc,rc,rrc,strc,tchbc,uc,ucil,urc,usr&format=html).

### Building the ontology files
The ontology is created by from a google sheet using sheet2rdf

# To contribute
The data in the ontology can only be changed by the repository maintainers. The ontology data is protected to ensure availability and avoid misuse or abuse.

The data is entered via a [google sheet](https://docs.google.com/spreadsheets/d/1rC2bugsJzRpuINqbVKR7GO1xNHPvzUvrKEz-75MNdXY/edit?usp=sharing). To request access, please [raise an issue](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/issues/).

## NEW: Discussions
Not familiar with GitHub? Don't know the difference between an issue and a hole in the ground? Jump in to the discussion at https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/discussions/ instead, and we'll help.

## Raise an issue
GitHub issues are used to provide an open and auditable way for modifying the data in the ontology
- [Suggest a new definition](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/issues/new?assignees=&labels=&template=new-definition.md&title=%5BNew+definition%5D).
- [Change a definition](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/issues/new?assignees=&labels=&template=change-definition.md&title=%5BChange+a+definition%5D).

For any other feedback please [raise an issue](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/issues/new?assignees=&labels=&template=new-definition.md&title=%5BNew+definition%5D).

Contributions will become part of this repository according to the terms of the contributor agreement.

# Resources
- [A human-friendly version of the ontology](http://vocab.ieawindtask32.org/ontolidar/en/).
- [The difference between a glossary and ontology](https://asistdl.onlinelibrary.wiley.com/doi/epdf/10.1002/bult.2013.1720390211).


# Maintainers
This repository is maintained by
- [Andy Clifton](https://github.com/andyclifton), IEA Wind Task 32 Operating Agent
- [Nikola Vasiljevic](https://github.com/niva83), DTU Wind Energy.

... and uses contributions from
- [Francisco Costa](https://github.com/pacocosta)
- [Peter Clive]()


# Contact
Questions, comments, and feedback about the ontology should be [shared as an issue](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/issues/new/choose) or sent to ieawind.task32@ifb.uni-stuttgart.de.
