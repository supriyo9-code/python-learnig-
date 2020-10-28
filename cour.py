def Searcher():
    import time
    #Some 4 Seconds time consuming task
    book = "This is a book on harry and code harry and good"
    time.sleep(4)
    while True:
        text = (yield)
        if text in book:
            print("Your text in the book")
        else:
            print("Text is not in the book")

search = Searcher()
print("search started")
next(search)
print("Next method run")
search.send("harry")

search.close()
# search.send("harry")