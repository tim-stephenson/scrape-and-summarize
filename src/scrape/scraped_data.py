
from typing import List


class ScrappedData:
    """The information corresponding to one scrapped textual media
    """

    def __init__(self, title: str, authors : List[str], date : str, image_url : str, content : str ):
        """Initialize an instance of ScrappedData with all required attributes

        Args:
            title (str): title of textual media
            authors (List[str]): list authors of the textual media
            date (str): YYYYMMDD formatted date of initial publication
            image_url (str): url corresponding with a the thumbnail for the textual media
            content (str): string of the content of the textual media
        """
        self.title = title
        self.authors = authors
        self.date = date
        self.image_url = image_url
        self.content = content



