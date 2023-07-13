from py2neo import Graph
# docs https://py2neo.org/2021.1/workflow.html#graph-objects

'''
from py2neo import Graph
sales = Graph("bolt+s://g.example.com:7687", name="sales")
sales.run("MATCH (c:Customer) RETURN c.name")
 c.name
---------------
 John Smith
 Amy Pond
 Rory Williams
 '''

# Connect to the Neo4j database
graph = Graph("bolt://localhost:7687", 
              name="autogroup",
              auth=("neo4j", "87654321"))

# Define the query to retrieve person nodes
query = """
MATCH (p:person)
RETURN p.name AS name, p.POB AS place_of_birth, p.YOB AS year_of_birth
"""

# Execute the query
result = graph.run(query)

# Process the result
for record in result:
    name = record["name"]
    place_of_birth = record["place_of_birth"]
    year_of_birth = record["year_of_birth"]
    
    print(f"Name: {name}")
    print(f"Place of Birth: {place_of_birth}")
    print(f"Year of Birth: {year_of_birth}")
    print("---")
