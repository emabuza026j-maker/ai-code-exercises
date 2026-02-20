class Task:
    def __init__(self, title: str, description: str, status: 'TaskStatus', priority: 'TaskPriority'):
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority

class TaskStatus:
    PENDING = 'Pending'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'

class TaskPriority:
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'