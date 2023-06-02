# Clicker attendance tallier
Sum up students' attendance over several sections, only awarding attendance in each student's enrolled section.

## How to use
1. Place attendance sheets in `./attendance`
2. Place a single roster csv in `./roster`
3. Place a single gradebook csv in `./gradebook`
4. Run `python AttendanceTallier.py`
5. Review assignment output file, which is placed in `./assignment` upon creation, and upload to Canvas

## File formats
### Attendance sheets:
One attendance sheet for each section. Each one should be a csv with the following format:
```
Student,ID,SIS User ID,SIS Login ID,Section,<AssignmentName>
Points Possible,,,,,<PointNum>
<student data below...>
```
With the following constraints:
- **! Important !** Ensure attendance files are listed in the `attendance` directory in the same order as their codes are listed in the roster. This is a shortcoming of the current approach which requires matching points in attendance to a section code which is not included in the attendance sheets themselves. For example, if the roster lists section 001, then 002, then 003, make sure the attendance file for section 001 is listed before that of 002, which is listed before that of 003. This should mean the attendance sheets' names are ordered lexicographically to achieve this.
- The first two rows are optional.
- Each row after the first two contains the student data described in row 1; i.e., `StudentName,StudentId,SisPid,SisUsername,Section,Points`. Fields may be empty except for SisUsername and Points.

### Roster:
Roster of students enrolled in the class. This should be a csv with the following format:
```
Sect ID
<id for each section on a separate line>

Sec ID,Email
<each student's id and email, comma-separated, on its own line>
```
Additional fields may be included if the downloaded roster includes them. The following MUST be true, however:
- All section data are listed before any student data
- The first field of any section must be its section id code
- The first field of any student must correspond to the student's enrolled section ID
- The student's email must be in some field

### Gradebook:
Canvas gradebook. This can be downloaded from the course page > Grades on Canvas. Delete columns so that the csv has the following format:
```
Student,ID,SIS User ID,SIS Login ID,Section,<AssignmentName>
Points Possible,,,,,<PointNum>
<student data below...>
```
With the following constraints:
- The first two rows must be exactly as described, with <AssignmentName> being replaced by the name of the new attendance assignment and <PointNum> being the total number of possible points
- Each row after the first two contains the student data described in row 1; i.e., `StudentName,StudentId,SisPid,SisUsername,Section,Points`. Points should be 0 to begin and will be updated by the script.
