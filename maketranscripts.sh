#!/bin/bash

for filename in /data/shared-task/test; do
    echo $filename
    deepspeech --model "/data/shared-task/output_graph.pb" --alphabet "data/alphabet.txt" --audio $filename
done