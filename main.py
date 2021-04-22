import re
import subprocess
import sys

import requests


def get_cdn_url(cdn_video_id):
    try:
        response = requests.get(
            url=f"https://api.flograppling.com/api/right-rail/videos/{cdn_video_id}",
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

    return response.json()['data']['source_video']['playlist']


if __name__ == '__main__':
    url = sys.argv[1]
    location_to_save = url.split('/')[4]
    video_id = re.findall('\d+', url)[0]
    cdn_url = get_cdn_url(video_id)

    command = f'ffmpeg -i {cdn_url} -bsf:a aac_adtstoasc -c copy {location_to_save}.mp4'
    subprocess.call(command, shell=True)

    print('Successfully saved FloGrappling video as', location_to_save, '.mp4')
