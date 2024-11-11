#!/bin/bash

sort custom.txt | uniq > sorted.txt
mv sorted.txt custom.txt
