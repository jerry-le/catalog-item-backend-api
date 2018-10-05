import re


def extract_video_thumbnail(link):
    """Get a link and return its thumbnail image
    :param link: a string
    :return:
        If `link` is a youtube video's url, extract video id and return
        youtube video thumbnail url. Unless return default image for
        non-exist thumbnail.
    """
    regex = r"(youtu\.be\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v)\/))([" \
            r"^\?&\"'>]+) "
    matches = re.search(regex, link)
    try:
        video_id = matches.group(5)
        img_link = "https://img.youtube.com/vi/{}/2.jpg".format(video_id)
    except:
        return "https://img.youtube.com/vi/notexisted/2.jpg"

    return img_link
