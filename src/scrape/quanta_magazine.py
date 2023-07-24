import asyncio
from typing import List, Tuple
from bs4 import BeautifulSoup

import requests

from src.scrape.scraped_data import ScrappedData


async def extractLinks(url: str) -> Tuple[str, str] | None:
    """Gather the content and date from a url to a QuantaMagazine article

    Args:
        url (str): url to QuantaMagazine article

    Returns:
        Tuple[str, str] | None: (content, date) pair if successful
        None in the case of an error
    """
    print("started request")
    loop = asyncio.get_running_loop()
    r = await loop.run_in_executor(
        None, requests.get, url)
    print("ended request, got", r.status_code)
    if not r.ok:
        return None
    parsedHTML = BeautifulSoup(r.text, "html.parser")
    content: str = ""
    for element in parsedHTML.find_all(['p', 'h3'], attrs={'style': 'font-weight: 400;'}):
        content += element.getText() + '\n'
    date: str = url[-9: -1]
    return (content, date)


async def gatherCollectionOfArticle(n: int) -> List[ScrappedData]:
    r = requests.post("https://www.quantamagazine.org/graphql", json={
        "operationName": "getPopular",
        "variables": {
            "cat": "189",
            "limit": n,
        },
        "query": """query getPopular($cat: String, $author : Int, $post_type : String, $limit : Int, $range : String, $exclude_ids : String) {
    popular: getPopular(cat: $cat , author: $author , post_type: $post_type , limit: $limit , range: $range , exclude_ids: $exclude_ids ) {
        ... on Post {
        id
        title
        link
        content
        authors {
            name
            link
        }
        acf {
            featured_block_title
            featured_image_default {
            ...ImageFields
            }
            featured_image_square {
            ...ImageFields
            }
        }
        }
    }
    }

    fragment ImageFields on Image {
    alt
    caption
    url
    width
    height
    sizes {
        thumbnail
        square_small
        square_large
        medium
        medium_large
        large
    }
    }"""
    })
    if not r.ok:
        return []
    articles: List[ScrappedData] = []
    results = await asyncio.gather( *map(lambda element : extractLinks(element["link"]),  r.json()["data"]["popular"]) )
    for i, element in enumerate(r.json()["data"]["popular"]):
        match results[i]:
            case content, date:
                authors = list(map(lambda author: author["name"], element["authors"]))
                articles.append(ScrappedData(element["title"],
                                             authors, date, element["acf"]["featured_image_default"]["url"],content))
            case None:
                pass
    return articles