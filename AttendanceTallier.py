import os

def createSectionDict():
    """
    for each row of enrollment sheet, add student name as dict key to value
    of enrolled section
    """
    sectionDict = {}
    sectionCodes = []

    # open membership sheet and skip header line
    f = open(os.path.join('roster', os.listdir('roster')[0]), "r")
    for i in range(len(os.listdir('attendance'))):
        line = next(f)
        if line.startswith('Sect'):
            line = next(f)
        sectionCodes.append(line.split(',')[0])

    # loop through lines with names to assign
    for line in f:
        name = ''
        parts = line.split(",")
        for part in parts:
            if '@' in part: # extract first part of email
                name = part.split("@")[0]
        section = parts[0]
        if name == '':
            continue

        #print(name + " " + section)
        sectionDict[name] = section

    f.close()

    return sectionDict, sectionCodes

# get sectionDict
sectionDict, sectionCodes = createSectionDict()

# uncomment this to create a txt of section membership
'''
#check that dict is correct
roster = open("Section Roster.txt", "w")
for key, value in sectionDict.items():
    roster.write("{key}:{value}\n".format(key = key, value = value))
roster.close()
'''

# from attendance sheets, assign each student to a points tally
pointsDict = {}
for (f, numCode) in zip(os.listdir('attendance'), sectionCodes):
    attendance = open(os.path.join('attendance', f), 'r')

    for line in attendance:
        if line.startswith("Student") or line.startswith("Points"):
            continue

        parts = line.split(",")
        name = parts[4]
        try:
            points = int(float(parts[-1][:-1]))
        except:
            continue

        if name not in pointsDict:
            pointsDict[name] = 0
        if name in sectionDict and sectionDict[name] == str(numCode):
            pointsDict[name] += points
        elif name not in sectionDict:
            pointsDict[name] = max(pointsDict[name], points)

    attendance.close()

# uncomment this to create a txt of point tallies
'''
#check that dict is correct
points = open("Points.txt", "w")
for key, value in pointsDict.items():
    points.write("{key}:{value}\n".format(key = key, value = value))
points.close()
'''

# open file to tally points
if not os.path.exists('assignment_results'):
    os.makedir('assignment_results')
newAssignment = open(os.path.join('assignment_results', 'assignment.csv'), "w")
canvasData = open(os.path.join('gradebook', os.listdir('gradebook')[0]), "r")
newAssignment.write(next(canvasData))

# add each student's info + score to new assignment
for line in canvasData:
    parts = line.split(",")[:-1]
    name = parts[4]

    if name in pointsDict:
        points = pointsDict[name]
    else:
        points = 0

    for part in parts:
        newAssignment.write(str(part) + ",")
    newAssignment.write(str(points) + "\n")

canvasData.close()
newAssignment.close()
