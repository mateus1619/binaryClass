from bs4 import BeautifulSoup
from requests import get
import re
from pytube import YouTube
from config import VIDEO_URL




class Model:

    def __init__(self) -> None:
        pass


    def get_modules_aulas(self, url, cookies=None, headers=None):
        response = get(url, cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        all_module = soup.find_all('div', class_='section-group')

        info_aulas = {
            "binary": []
        }

        for module in all_module:
            all_aulas = []
            module_title = module.find('div', class_='item-titulo').text.split('\n')[1]

            aulas = module.find_all('a', class_='layer-link')
            for aula in aulas:
                aula_title = aula.find('div', class_='item-titulo').text
                aula_title = re.sub(r'\d+\.?\s*', '', aula_title).strip()
                aula_id = re.sub(r'\D', '', aula['href']) 

                all_aulas.append([aula_title, int(aula_id)])

            info_aulas['binary'].append(dict(module_title=module_title, aulas=all_aulas))
        return info_aulas


    def get_video(self, video_id: str | int, url=VIDEO_URL, cookies=None, headers=None):
        video_info = {"title": None,"videos": []}
        
        response = get(url+str(video_id), cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        youtube_link = soup.find('iframe', class_='video-iframe').get('src')
        youtube_link = re.sub(r'\?.*', '', youtube_link)

        youtube = YouTube(youtube_link)

        videos = youtube.streams.filter(type='video', file_extension='mp4')
        for video in videos:
            itag = video.itag
            reso = video.resolution
            fps = video.fps
            progressive = video.is_progressive
            video_link = youtube.streams.get_by_itag(itag).url

            video_info['videos'].append(dict(url=video_link, resolution=reso, fps=fps, progressive=progressive))

        video_info['title'] = youtube.title

        return video_info