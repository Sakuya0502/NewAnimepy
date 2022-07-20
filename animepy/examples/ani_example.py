from animepy import Anigamer
from loguru import logger

anime = Anigamer()
new_anime  = anime.homepage()

anime_name = new_anime.ani['name'][0]
anime_watch = new_anime.ani['watch'][0]
anime_episode = new_anime.ani['episode'][0]
anime_href = new_anime.ani['href'][0]
anime_pict = new_anime.ani['pict'][0]

logger.info(anime_name)
logger.info(anime_watch)
logger.info(anime_episode)
logger.info(anime_href)
logger.info(anime_pict)