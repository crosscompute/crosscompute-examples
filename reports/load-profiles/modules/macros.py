import re


UPPER_LOWER_PATTERN = re.compile(r'(.)([A-Z][a-z]+)')
LOWER_UPPER_PATTERN = re.compile(r'([a-z0-9])([A-Z])')


def get_title_case_from_camel_case(key):
    """
    Normalize key using a variation of the method described in
    http://stackoverflow.com/a/1176023/192092

    ONETwo   One Two
    OneTwo   One Two
    """
    key = UPPER_LOWER_PATTERN.sub(r'\1 \2', key)
    key = LOWER_UPPER_PATTERN.sub(r'\1 \2', key)
    return key.title()
