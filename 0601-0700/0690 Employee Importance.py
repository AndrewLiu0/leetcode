
from typing import List
from collections import deque

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates



class Solution:
    

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        myMap = {} # Key: id, entry: list of child ids
        idImportance = {} # Key id, entry: importance
        for employee in employees:
            idImportance[employee.id] = employee.importance
            if(employee.id not in myMap):
                myMap[employee.id] = employee.subordinates

        queue = deque()
        visited = set()
        queue.append(id)
        # starting node is id

        sum = 0

        while(len(queue)!=0):
            curr = queue.popleft()
            sum += idImportance[curr]
            for childId in myMap[curr]:
                if(childId not in visited):
                    visited.add(childId)
                    queue.append(childId)
        return sum

sol = Solution()
testCase = [[1,5,[2,3]],[2,3,[]],[3,3,[]]]
id = 1
employeeList = []

for case in testCase:
    employeeList.append(Employee(case[0], case[1], case[2]))

print(sol.getImportance(employeeList, id))