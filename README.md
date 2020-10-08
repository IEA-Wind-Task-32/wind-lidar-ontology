# Wind lidar glossary
A glossary of terms for wind lidar.

## What is it?
The Task 32 wind lidar glossary is a controlled terminology that includes a hierarchy, synonyms, and interrelationships. This is often called an _ontology_ (see https://asistdl.onlinelibrary.wiley.com/doi/epdf/10.1002/bult.2013.1720390211).

## Why
This repository provides a human- and machine readable glossary of terms for wind lidar. This can be used as a taxonomy for data, publications and software.

## Implementation
The glossary is created from the .ttl files in this repository, that are imported in to the [DTU Wind Energy Taxonomy](https://data.windenergy.dtu.dk/ontologies/view/wtax/en/).

Each branch of the glossary - e.g., `applications`, `devices`, or `measurement principles` has its own file for simplicity. These files are then concatenated with header.ttl and imported in to the viewer.

## Structure
- header.ttl contains the headers. 
- applications.ttl
- devices.ttl

These files are then appended to create glossary.ttl.

# To contribute

The data in definitions.csv can only be changed by the repository maintainers. To make a sugestion for a change, please raise an [issue](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/issues/new/choose).

To suggest a new glossary entry please [raise an issue](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/issues/new?assignees=&labels=&template=new-definition.md&title=%5BNew+definition%5D).

Contributions will become part of this repository according to the terms of the contributor agreement.

# Maintainers
This repository is maintained by Andy Clifton as IEA Wind Task 32 Operating Agent and Nikola Vasiljevic at the Danish Technical University.

# Contact
Questions, comments, and feedback about the terms should be [shared as an issue](https://github.com/IEA-Wind-Task-32/wind-lidar-glossary/issues/new/choose) or sent to ieawind.task32@ifb.uni-stuttgart.de.
