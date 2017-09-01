"""Updates json for extraction progress using the extraction excel sheet."""

import pandas as pd
import json

data = pd.read_excel(
    '/Users/komalali/Desktop/updated_diet_cooper_project.xlsx', 'viz_data')

with open('/Users/komalali/Documents/development_dump/work_dump/' +
          'extraction_tree/src/extraction_hierarchy.json', 'r') as f:
    output = json.load(f)

dr_numSources = int(data.numSources[0])
dr_numExtracted = int(data.numExtracted[0])
dr_numRejected = int(data.numRejected[0])
dr_numRemaining = int(data.numRemaining[0])
ffq_numSources = int(data.numSources[1])
ffq_numExtracted = int(data.numExtracted[1])
ffq_numRejected = int(data.numRejected[1])
ffq_numRemaining = int(data.numRemaining[1])
hhbs_numSources = int(data.numSources[2])
hhbs_numExtracted = int(data.numExtracted[2])
hhbs_numRejected = int(data.numRejected[2])
hhbs_numRemaining = int(data.numRemaining[2])
other = int(data.numSources[3])

microdata_sources = output['children'][0]['children'][0]['children']

microdata_sources[0]['numExtracted'] = dr_numExtracted
microdata_sources[0]['numRemaining'] = dr_numRemaining
microdata_sources[0]['numRejected'] = dr_numRejected
microdata_sources[0]['numSources'] = dr_numSources
microdata_sources[0]['text'] = (
    str(dr_numExtracted) + ' out of ' +
    str(dr_numSources) + ' dietary recalls have been extracted. ' +
    str(dr_numRejected) + ' have been rejected. ' +
    str(dr_numRemaining) + ' remain.')

microdata_sources[1]['numExtracted'] = ffq_numExtracted
microdata_sources[1]['numRemaining'] = ffq_numRemaining
microdata_sources[1]['numRejected'] = ffq_numRejected
microdata_sources[1]['numSources'] = ffq_numSources
microdata_sources[1]['text'] = (
    str(ffq_numExtracted) + ' out of ' +
    str(ffq_numSources) + ' dietary recalls have been extracted. ' +
    str(ffq_numRejected) + ' have been rejected. ' +
    str(ffq_numRemaining) + ' remain.')

microdata_sources[2]['numExtracted'] = hhbs_numExtracted
microdata_sources[2]['numRemaining'] = hhbs_numRemaining
microdata_sources[2]['numRejected'] = hhbs_numRejected
microdata_sources[2]['numSources'] = hhbs_numSources
microdata_sources[2]['text'] = (
    str(hhbs_numExtracted) + ' out of ' +
    str(hhbs_numSources) + ' dietary recalls have been extracted. ' +
    str(hhbs_numRejected) + ' have been rejected. ' +
    str(hhbs_numRemaining) + ' remain.')

microdata_sources[3]['numSources'] = hhbs_numSources
microdata_sources[3]['text'] = (
    str(other) + ' sources do not meet the inclusion criteria (eg. cohorts).')

with open('/Users/komalali/Documents/development_dump/work_dump/' +
          'extraction_tree/src/extraction_hierarchy_.json', 'w') as f:
    json.dump(output, f)
