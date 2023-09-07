#!/bin/bash
#This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATHS=$(echo $DATA | jq '.[0].negative')
HOSPITALIZED=$(echo $DATA | jq '.[0].death')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE postive COVID cases, $NEGATIVE negative tests, $DEATHS deaths and $HOSPITALIZED hospitalized"
