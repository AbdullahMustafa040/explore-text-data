import pandas as pd
from nomic import atlas

# Load the data from the CSV file
data = pd.read_csv('bquxjob_1d3a5b39_18a19aa3081.csv').to_dict('records')

# Create a Nomic Atlas project to visualize the text data
project = atlas.map_text(
    data=data,
    id_field='id',  # The name of the column that contains the unique ID for each row
    indexed_field='transcription',  # The name of the column that contains the text data
    name='Your Project Name',
    description='A description of your project'
)
