#!/bin/bash
echo "CRHM path: $1"
echo "Iteration count: $2"
cd $1
for ((i=1; i<=$2; i++)); do
    echo "************************* $i ***********************"
    time ./crhm prj/smithcreek.prj 
     mv CRHM_output_1.obs sc$i.obs     
done