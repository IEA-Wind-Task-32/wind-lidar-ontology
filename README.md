[![CI](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/workflows/CI/badge.svg)](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/actions?query=workflow%3ACI)

# Wind lidar glossary
This repository provides the source file for a glossary of terms for wind lidar (see the file, `glossary.ttl`). This glossary can be used to help organise and explore data, publications and software.

For a human-friendly version of the repository, see the [the online viewer](https://data.windenergy.dtu.dk/ontologies/view/IEATask32Glossary/en/).

## Glossary, ontology, taxonomy, ...
The Task 32 wind lidar glossary is a controlled vocabulary about wind lidar that includes a hierarchy, synonyms, and interrelationships. This is often called an [_ontology_](https://asistdl.onlinelibrary.wiley.com/doi/epdf/10.1002/bult.2013.1720390211).

## Implementation
The glossary is built from information contained in the text files in this repository.

Each branch of the glossary - e.g., `applications`, `devices`, or `measurement principles` - has its own file. These files are then automatically concatenated with the headers needed for the glossary (in `00_headers.txt`), and imported in to the viewer.

The file is written using the [Simple Knowledge Organisation System (skos) schema](https://www.w3.org/2009/08/skos-reference/skos.html). It can be checked for conformance to the skos schema using e.g. the [SPARNA skos verification tool](http://labs.sparna.fr/skos-testing-tool/test?url=https://raw.githubusercontent.com/IEA-Wind-Task-32/wind-lidar-glossary/main/glossary.ttl&rules=anr,chr,dcc,dlv,el,hr,husv,ilc,ipl,ml,mri,ncl,oc,oilt,ol,otc,rc,rrc,strc,tchbc,uc,ucil,urc,usr&format=html).

# To contribute
The data in the glossary can only be changed by the repository maintainers. The glossary data is protected to avoid misuse or abuse, and to help provide a clear way for modifying the data in the repository
- [Suggest a new definition](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/issues/new?assignees=&labels=&template=new-definition.md&title=%5BNew+definition%5D).
- [Change a definition](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/issues/new?assignees=&labels=&template=change-definition.md&title=%5BChange+a+definition%5D).

For any other feedback please [raise an issue](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/issues/new?assignees=&labels=&template=new-definition.md&title=%5BNew+definition%5D).

Contributions will become part of this repository according to the terms of the contributor agreement.

# Maintainers
This repository is maintained by
- Andy Clifton as IEA Wind Task 32 Operating Agent
- Nikola Vasiljevic at the Danish Technical University.

# Contact
Questions, comments, and feedback about the glossary should be [shared as an issue](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/issues/new/choose) or sent to ieawind.task32@ifb.uni-stuttgart.de.
