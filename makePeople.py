#!/bin/python3

import yaml
import json
def addTitleAndBottom(htmlBlock):
    title = 'The SubjuGator project team members are comprised from undergraduate and graduate students from the Department of Electrical and Computer Engineering, the Department of Mechanical and Aerospace Engineering, and the Department of Computer and Information Sciences Engineering at the University of Florida.\n'\
    '\n'\
    '<table id="report">\n'\
    '<tbody>\n'\
    '<tr>\n'\
    '<th>Name</th>\n'\
    '<th>Position</th>\n'\
    '<th>Major</th>\n'\
    '<th>Email</th>\n'\
    '</tr>\n'

    bottom = '</tbody>\n'\
    '</table>\n'
    return title + htmlBlock + '\n' + bottom
    
"""
lst = []
lst.append({
    "name": "Jarrod Sanders",
    "position": "Software-Hardware crossover dev",
    "major": "CSE",
    "email": "jarrod.sanders@ufl.edu"
})
lst.append({
    "name": "Alex Perez",
    "position": "Software team lead",
    "major": "CPE",
    "email": "alex.perez@ufl.edu"
})
print(yaml.dump(lst))

with open("testFile.yaml", "w") as fh:
    fh.write(yaml.dump(lst))
    fh.close()
"""

with open("people.yaml", "r") as fh:
    struct = yaml.full_load(fh)
    fh.close()

htmlblock = ''
for p in struct:
    email    = p.get("email") 
    name     = p.get("name") 
    major    = p.get("major") 
    position = p.get("position") 
    imageURL = p.get("imageurl") 
    degreeLevel = p.get("degreelevel") 
    concentration = p.get("concentration") 
    resume = p.get("resume") 
    teamContributions = p.get("teamcontributions") 

    if(name != 'Allie Gator'):
        htmlblock +='\n<tr>\n'\
        '<td>{name}</td>\n'\
        '<td>{position}</td>\n'\
        '<td>{major}</td>\n'\
        '<td>{email}</td>\n'\
        '</tr>\n'\
        '<tr>\n'\
        '<td colspan="5">\n'\
        '<div class="picture"><img class="alignleft" src="{imageURL}" width="91" height="100"></div>\n'\
        '<div class="details">\n'\
        '<label>Degree Pursuing:</label>{degreeLevel}\n'\
        '<label>Concentration:</label>{concentration}\n'\
        '<label>Resume:</label>{resume}\n'\
        '<label>Team Contributions:</label>{teamContributions}\n'\
        '</div></td>\n'\
        '</tr>\n'.format( email = email, name = name, major = major, position = position, imageURL = imageURL, degreeLevel = degreeLevel, concentration = concentration, resume = resume, teamContributions = teamContributions)

output = addTitleAndBottom(htmlblock)

with open('out.html', 'w') as fh:
    fh.write(output)
    fh.close()



