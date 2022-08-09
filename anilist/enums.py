from __future__ import annotations

from enum import Enum
from typing import Optional
import re


class BaseEnum(Enum):
    @classmethod
    def get(cls: BaseEnum, name: str) -> Optional[BaseEnum]:
        try:
            return cls(name)
        except:
            return cls._member_map_.get(re.sub(r'[ -]', '_', name.lower()), None)

    
    def __repr__(self) -> str:
        return self.name.replace('_', ' ').title()



class MediaType(BaseEnum):

    # Japanese Anime
    anime = 0

    # Asian comic
    manga = 1

class MediaFormat(BaseEnum):

    # Anime broadcast on television
    tv = 0
    
    # Anime which are under 15 minutes in length and broadcast on television
    tv_short = 1

    # Anime movies with a theatrical release
    movie = 2

    # Special episodes that have been included in DVD/Blu-ray releases, picture dramas, pilots, etc
    special = 3 

    # (Original Video Animation) Anime that have been released directly on DVD/Blu-ray without originally going through a theatrical release or television broadcast
    ova = 4

    # (Original Net Animation) Anime that have been originally released online or are only available through streaming services.
    ona = 5

    # Short anime released as a music video
    music = 6

    # Professionally published manga with more than one chapter
    manga = 7

    # Written books released as a series of light novels
    novel = 8
    
    # Manga with just one chapter
    one_shot = 9


class MediaStatus(BaseEnum):

    # Has completed and is no longer being released
    finished = 0

    # Currently releasing
    releasing = 1

    # To be released at a later date
    not_yet_released = 2

    # Ended before the work could be finished
    cancelled = 3

    # Version 2 only. Is currently paused from releasing and will resume at a later date
    hiatus = 4


class MediaSeason(BaseEnum):

    # Months December to February [12, 2]
    winter = 0

    # Months March to May [3, 5]
    spring = 1

    # Months June to August [6, 8]
    summer = 2

    # Months September to November [9, 11]
    fall = 3


class MediaSource(BaseEnum):
    # An original production not based of another work
    original = 0

    # Asian comic book
    manga = 1

    # Written work published in volumes
    light_novel = 2

    # Video game driven primary by text and narrative
    visual_novel = 3

    # Video game
    video_game = 4

    # Other
    other = 5


    # Version 2+ only. Written works not published in volumes
    novel = 6

    # Version 2+ only. Self-published works
    doujinshi = 7

    # Version 2+ only. Japanese Anime
    anime = 8


    # Version 3 only. Written works published online
    web_novel = 9

    # Version 3 only. Live action media such as movies or TV show
    live_action = 10 

    # Version 3 only. Games excluding video games
    game = 11

    # Version 3 only. Comics excluding manga    
    comic = 13

    # Version 3 only. Multimedia project
    multimedia_project = 14

    # Version 3 only. Picture book
    picture_book = 15


class Genre(Enum):
    action = 'Action'
    adventure = 'Adventure'
    comedy = 'Comedy'
    drama = 'Drama'
    ecchi = 'Ecchi'
    fantasy = 'Fantasy'
    horror = 'Horror'
    mahou_shoujo = 'Mahou Shoujo'
    mecha = 'Mecha'
    music = 'Music'
    mystery = 'Mystery'
    psychological = 'Psychological'
    romance = 'Romance'
    sci_fi = 'Sci-Fi'
    slice_of_life = 'Slice Of Life'
    sports = 'Sports'
    supernatural = 'Supernatural'
    thriller = 'Thriller'


class Language(BaseEnum):
    japanese = 0
    english = 1
    korean = 2
    italian = 3
    spanish = 4
    portuguese = 5
    french = 6
    german = 7
    hebrew = 8
    hungarian = 9
    chinese = 10
    arabic = 11
    filipino = 12
    catalan = 13
    finnish = 14
    turkish = 15
    dutch = 16
    swedish = 17
    thai = 18
    tagalog = 19
    malaysian = 20
    indonesian = 21
    vietnamese = 22
    nepali = 23
    hindi = 24
    urdu = 25


class Gender(Enum):
    male = 0
    female = 1