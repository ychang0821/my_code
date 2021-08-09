#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def getname(got_dj):
    if got_dj.get("name") != "":
        name = got_dj.get("name")
        return name
    else:
        name = got_dj.get("aliases")[0]
        return name


def listbooks(books, name):
    bookslist = []
    if len(books) == 0:
        print(f"{name} not appear in any book")
    else:
        for book in books:
            bookresp = requests.get(book).json()
            book_name = bookresp.get("name")
            bookslist.append(book_name)
        print(f"{name} is appear in {bookslist}")

def listhouse(allegiances, name):
    if len(allegiances) == 0:
        print(f"{name} is not belong to any house")
    else:
        for allegency in allegiances:
            allegencyresp = requests.get(allegency).json()
            house_name = allegencyresp.get("name")
            print(f"{name} is belong to {house_name}")
def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        name = getname(got_dj)

        allegiances = got_dj.get("allegiances")
        listhouse(allegiances, name)
        
        books = got_dj.get("books")
        povBooks = got_dj.get("povBooks")
        books.extend(povBooks)
        listbooks(books, name)

        # pprint.pprint(got_dj)

if __name__ == "__main__":
        main()

