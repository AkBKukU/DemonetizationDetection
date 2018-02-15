#!/usr/bin/python

class VideoData(object):
    
    def __init__(self):
        # Standard Data
        self._video_id = None
        self._title = None
        self._description = None
        self._published = None

        # Metrics
        self._date_start = None
        self._date_end = None
        self._views = None
        self._monetizedPlaybacks = None
        self._estimatedRevenue = None
        self._estimatedMinutesWatched = None
        self._percent = None
   

    @property
    def id(self):
        return self._video_id

    @id.setter
    def id(self,value):
        self._video_id = value
 
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,value):
        self._title = value
   
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self,value):
        self._descrioption = value
    
    @property
    def published(self):
        return self._published

    @published.setter
    def published(self,value):
        self._published = value
    
    @property
    def date_start(self):
        return self._date_start

    @date_start.setter
    def date_start(self,value):
        self._date_start = value

    @property
    def date_end(self):
        return self._date_end

    @date_end.setter
    def date_end(self,value):
        self._date_end = value

    @property
    def views(self):
        return self._views

    @views.setter
    def views(self,value):
        self._views = value
 
    @property
    def monetizedPlaybacks(self):
        return self._monetizedPlaybacks

    @monetizedPlaybacks.setter
    def monetizedPlaybacks(self,value):
        self._monetizedPlaybacks = value

    @property
    def estimatedRevenue(self):
        return self._estimatedRevenue

    @estimatedRevenue.setter
    def estimatedRevenue(self,value):
        self._estimatedRevenue = value

    @property
    def estimatedMinutesWatched(self):
        return self._estimatedMinutesWatched

    @estimatedMinutesWatched.setter
    def estimatedMinutesWatched(self,value):
        self._estimatedMinutesWatched = value

    @property
    def percent(self):
        if self._percent == None and self.views > 0:
            self._percent = self._monetizedPlaybacks / self._views
        else:
            self._percent = 0
        return self._percent

    @percent.setter
    def percent(self,value):
        return self._percent


