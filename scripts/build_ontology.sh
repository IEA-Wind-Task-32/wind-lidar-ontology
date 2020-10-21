#!/bin/bash

cat 00_header.ttl 01_properties.ttl *.txt >| ontology.ttl
