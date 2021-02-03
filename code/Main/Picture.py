class Picture:
    """
    This class hold the deets of a picture file. I haven't really used this yet. This may be useful if we implemented some kind of sign 
    recognition module (identifying what type of sign it is).
    """

    def __init__(self, pic_id, long, lat, alt):
        self.picture_id = pic_id
        self.longitude = long
        self.latitude = lat
        self.altitude = alt


