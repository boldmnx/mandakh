# neg huvisagchid olon utga ugch bolno Dict
# Tuple tus tusdn huvisagchid ugnu

class TaskManager:
    def __init__(self):
        self.taskList = []

    def insert(self, priority, task):
        self.taskList.append((priority, task))
        self.min_task(len(self.taskList)-1)

    def swap(self, i, j):
        self.taskList[i], self.taskList[j] = self.taskList[j], self.taskList[i]

    def min_task(self, i):
        while i != 0 and self.taskList[i][0] <= self.taskList[(i-1)//2][0]:
            self.swap(i, (i-1)//2)
            i = (i-1)//2

    def extract_min(self):
        if len(self.taskList) == 0:
            return None
        elif len(self.taskList) == 1:
            return self.taskList.pop()

        minTask = self.taskList[0]
        self.taskList[0] = self.taskList.pop()
        self.medehgui(0)
        return minTask

    def medehgui(self, i):
        smallest = i

        if i*2+1 < len(self.taskList) and self.taskList[i*2+1][0] < self.taskList[smallest][0]:
            smallest = i*2+1
        if i*2+2 < len(self.taskList) and self.taskList[i*2+2][0] < self.taskList[smallest][0]:
            smallest = i*2+2

        if smallest != i:
            self.swap(i, smallest)
            self.medehgui(smallest)

    def print_task(self, i=0, level=0, prefix='Root: '):
        if len(self.taskList) > i:
            print(' '*(level*4)+prefix + str(self.taskList[i]))
            self.print_task(i*2+1, level+1, 'L-- ')
            self.print_task(i*2+2, level+1, 'R-- ')


task = TaskManager()
task.insert(3, 'task5')
task.insert(4, 'task4')
task.insert(6, 'task2')
task.insert(2, 'task1')
task.insert(1, 'task3')

print('Одоогийн таскуудын эрэмбэ')
task.print_task()
print(task.extract_min())
# print(task.extract_min())
print('Хамгийн чухал таскын авсны дараах эрэмбэ')
task.print_task()
