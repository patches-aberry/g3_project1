# g3_project1

## At a very high level, here are the questions and the findings of said questions: 
Does CO2 emissions correlate with increased energy production?
 - There is not a positive correlation. For the time frame measured which was limited to the United States, CO2 emissions were on a downward trend as energy output increased. Both datasets were found to be significant, but the research returned a slight negative correlation value. More research is needed as to what impact energy production has on CO2 emissions in the U.S., and the specifics of how.
 
Does increased energy output overall correlate with higher average temperatures?
 - There is a correlation. For every One Trillion Megawatt Hours of energy output, the temperature increased by about 3.18 degrees in the dataset provided. The P-Value of both datasets is 0.003, suggesting the data was significant. For every percentage point increase in the percentage change of Energy Output, the percentage change of Temperature is expected to increase by 0.03 percentage points if the trend remains the same. States that saw the highest increase in energy output also saw the highest change in temperature.
 
Is the climate reported by news proportionally to the emissions of CO2?
 - There was not a positive correlation between reporting and CO2 emissions. Quantity of articles published overall increased while CO2 Emissions decreased in the US. However, quantity of articles increase as Energy Output increased. Percentage of change year over year for articles varied dramatically whereas with CO2 Emissions and Energy Output the % change was small. The sharing and publishing of articles relating to environmental information may be highly influenced by public interest, media trends and other factors, rather than statistical increase or decrease in CO2 Emissions or Energy Output.

An outline and working collaborative document showing vetting of potential data sources, formulation of central ideas, and several data sources that would be potentially interesting to explore in parallel with the data already outlined in this presentation: 
https://docs.google.com/document/d/1jxufqlucvoshEl477thof0f_lB-NITqpWuxfDlUUids/edit#heading=h.rt5lo1do1kso

All data was sourced from:
- Kaggle.com - an open-source free repository of data sets intended to be used in educational settings
- NYT Article search api - https://developer.nytimes.com/
- NOAA weather data provided by weather.gov

All contributions to code and project were agreed upon by the team members of this project: 
- Jennifer Vincent
- Alex Heilman
- Emily Notaro 
- Evan Cromwell
- Patrick Aubry
- Denise Froning

#Notebook Navigation
## Data cleanup and investigation
The "Data Input and Cleanup.ipynb" notebook contains code to pull in, clean, and export several data sets from Kaggle and the NYT. The resultant CSVs were passed into the corresponding question notebooks, designated with "Question_#" in the notbook names.
