from animepy import Anigamer
from loguru import logger

anime = Anigamer()

keyword = "86"
search_anime  = anime.anisearch(keywords=keyword)

anime_name = search_anime.sani['name'][0]
anime_watch = search_anime.sani['watch'][0]
anime_episode = search_anime.sani['episode'][0]
anime_date = search_anime.sani['date'][0]
anime_href = search_anime.sani['href'][0]
anime_pict = search_anime.sani['pict'][0]

logger.info(anime_name)
logger.info(anime_watch)
logger.info(anime_episode)
logger.info(anime_date)
logger.info(anime_href)
logger.info(anime_pict)