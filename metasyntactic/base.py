from collections import defaultdict

def autovivi():
    return defaultdict(autovivi)


class addlist(list):

    def add(self, item):
        return self.append(item)


def parse_data(data):
    acc = autovivi()
    section = None
    for line in data.splitlines():
        if line.startswith("#"):
            parts = line.split()
            type = parts[1]
            if type == "names":
                section = acc[type][" ".join(parts[2:]) or "en"] = set()
            else:
                section = acc[type] = addlist()
        else:
            for item in line.split():
                section.add(item)
    return acc

