import datetime

class Incident:
    """docstring for Incident."""

    incidentId = 1

    def __init__(self, createdOn, createdBy, type, location, comment,images,videos):
        self.createdOn = datetime.datetime.now()
        self.createdBy = createdBy
        self.type = type
        self.location_long = location['location_long']
        self.location_lat = location['location_lat']
        self.comment = comment
        self.images = images
        self.videos = videos
        self.status = 'draft'
        self.incidentId = Incident.incidentId
        Incident.incidentId += 1

    def get_location(self):
        return " ".join([self.location_long, self.location_lat])

    def get_incident_details(self):
        return {
            "location": self.get_location(),
            "createdOn":self.createdOn,
            "createdBy":self.createdBy,
            "type":self.type,
            "status":self.status,
            "images":self.images,
            "videos":self.videos,
            "comment":self.comment
            }

# if __name__ == '__main__':
    # inc1 = Incident(
    #     location={"location_long":"0.39737", "location_lat":"9.38974"},
    #     createdOn="2018-11-25 22:41:14",
    #     createdBy="2",
    #     type='redflag',
    #     videos="1.gif",
    #     comment="Arnold was caught stilling jack fruit in hassan's Garden"
    #     )
    # # inc1.status="under_Investigation"
    # print(inc1.get_incident_details())
