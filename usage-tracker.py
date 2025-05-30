

class Event:
    def __init__(self,event_date,event_type,machine_name,user,cpu,memory):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user
        self.cpu = cpu
        self.memory = memory

def get_date(event):
    return event.date

def track_usage(events):
    events.sort(key = get_date)

    usage_data = {}

    for event in events:

        key = (event.user, event.machine)  #user,machine pair (unique tuple)

        if key not in usage_data:
            usage_data[key] = {'cpu':0,'memory':0}

        usage_data[key]['cpu'] += event.cpu
        usage_data[key]['memory'] += event.memory

    return usage_data

def generate_report(usage_data):
    
    for (user,machine),usage in usage_data.items():
        print("User: {} , Machine: {}".format(user,machine))
        print("    Total CPU Usage: {}% /    Total Memory Usage: {}MB\n".format(usage['cpu'],usage['memory']))        


events = [
    Event('2020-01-21 12:45:46', 'usage', 'machine1', 'Brian', cpu=25, memory=1024),
    Event('2020-01-21 14:25:30', 'usage', 'machine1', 'Brian', cpu=30, memory=1100),
    Event('2020-01-21 15:45:00', 'usage', 'machine2', 'Caleb', cpu=40, memory=2048),
    Event('2020-01-21 18:30:15', 'usage', 'machine2', 'Brian', cpu=50, memory=1500),
    Event('2020-01-22 10:15:00', 'usage', 'machine1', 'Caleb', cpu=20, memory=1024),
    Event('2020-01-22 11:30:00', 'usage', 'machine3', 'Natasha', cpu=15, memory=512)
]

usage_data = track_usage(events)

# Generate report
generate_report(usage_data)