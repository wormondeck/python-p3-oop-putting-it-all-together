#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self.current_page = 1

    def turn_page(self):
        self.current_page += 1
        print("Flipping the page...wow, you read fast!")
    
    @property
    def page_count(self):
        return self._page_count
            
    @page_count.setter
    def page_count(self, page_count):
        if not isinstance(page_count, int):
            print('page_count must be an integer')
        else:
            self._page_count = page_count