from collections import deque


class TaskScheduler:
    def __init__(self):
        self.task_queue = deque()

    def add_task(self, task, priority='low'):
        if priority == 'high':
            # Add high priority task to the front
            self.task_queue.appendleft(task)
        else:
            self.task_queue.append(task)  # Add low priority task to the end

    def execute_tasks(self):
        while self.task_queue:
            task = self.task_queue.popleft()  # Get the first task
            print("Executing task:", task)


if __name__ == "__main__":
    scheduler = TaskScheduler()

    # Adding tasks with different priorities
    scheduler.add_task("Task 1", priority='low')
    scheduler.add_task("Task 2", priority='high')
    scheduler.add_task("Task 3", priority='low')
    scheduler.add_task("Task 4", priority='high')

    # Execute tasks
    scheduler.execute_tasks()
