[![CI](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/workflows/CI/badge.svg)](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/actions?query=workflow%3ACI)

# Wind lidar glossary
A glossary of terms for wind lidar.

## What is it?
The Task 32 wind lidar glossary is a controlled terminology for wind lidar that includes a hierarchy, synonyms, and interrelationships. This is often called an [_ontology_](https://asistdl.onlinelibrary.wiley.com/doi/epdf/10.1002/bult.2013.1720390211).

## About the repository
This repository provides a human- and machine readable glossary of terms for wind lidar. This can be used to help organise and explore data, publications and software.

## Implementation
The glossary is created from the .txt files in this repository, that are imported in to the [DTU Wind Energy Taxonomy](https://data.windenergy.dtu.dk/ontologies/view/wtax/en/).

Each branch of the glossary - e.g., `applications`, `devices`, or `measurement principles` - has its own file for simplicity. These files are then automaticaly concatenated with the headers needed for the glossary (in `00_headers.txt`), and imported in to the viewer.

# To contribute
The data in the glossary can only be changed by the repository maintainers.
- [Suggest a new definition](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/issues/new?assignees=&labels=&template=new-definition.md&title=%5BNew+definition%5D).
- [Change a definition](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/issues/new?assignees=&labels=&template=change-definition.md&title=%5BChange+a+definition%5D).

To suggest a new glossary entry please [raise an issue](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/issues/new?assignees=&labels=&template=new-definition.md&title=%5BNew+definition%5D).

Contributions will become part of this repository according to the terms of the contributor agreement.

# Maintainers
This repository is maintained by 
- Andy Clifton as IEA Wind Task 32 Operating Agent 
- Nikola Vasiljevic at the Danish Technical University.

# Contact
Questions, comments, and feedback about the glossary should be [shared as an issue](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/issues/new/choose) or sent to ieawind.task32@ifb.uni-stuttgart.de.
