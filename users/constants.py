from enum import StrEnum

USER_NAME_MAX_LENGTH = 124
USER_PHONE_MAX_LENGTH = 12
USER_ABOUT_MAX_LENGTH = 256

AVATAR_SIZE = 200
AVATAR_FONT_SIZE = 80
AVATAR_FONT_PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
AVATAR_TEXT_COLOR = 'white'


class AvatarColor(StrEnum):
    TEAL = '#01696f'
    GREEN = '#4f98a3'
    OLIVE = '#6daa45'
    ORANGE = '#da7101'
    PURPLE = '#a86fdf'
    RED = '#d19900'
    YELLOW = '#dd6974'
    DARK_TEAL = '#006494'


AVATAR_PALETTE = list(AvatarColor)
