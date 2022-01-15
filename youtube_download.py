"""
Para criar o virtualEnv
pip install virtualenv  (se nao tiver instalado ainda)
cria o diretorio onde irá ficar o seu virtualenv. 
p.ex. mkdir meuvirtualenv
entra nesse diretorio p.ex. cd meuvirtualenv
entao roda este comando
virtualenv .

(beleza, criou o virtualenv)

Para fazer rodar no sublime:
ir em Tools > Build System > New Build System
daí voce cola este texto:

{
    "cmd": ["C:/@git/whatsapp_video.py/minhavenv/Scripts/python.exe", "-u", "$file"],
    "selector": "source.python",
    "file_regex": "^\\s*File \"(...*?)\", line ([0-9]*)"
}

fazendo as alterações necessárias de acordo com o seu
diretorio virtualenv

OBjetivo deste APP:
Interface GUI
Exibir as opções disponíveis para download
Setar uma configuração padrao para download. p.ex.360p

https://pypi.org/project/pytube/

Streams onde progressive = true tem o audio e o video no mesmo arquivo
"""

def cria_lista_de_opcoes(video_obj):
	yt_videos = video_obj.streams.filter(progressive=True)
	yt_videos_dict = {}; count = 0; video_options = []
	for item in yt_videos:
		yt_videos_dict[item.resolution] = item.itag
	for option in yt_videos_dict.keys():
		count+=1
		video_options.append(option)
	return video_options, yt_videos_dict


def escolher_resolucao(video_obj):
	print("Resoluções disponíveis para download :")
	print('Escolha sua resolução: ')
	#choice=input('?')
	#return choice
	return 0

from pytube import YouTube
DOWNLOAD_FOLDER = "./downloads"
# Israel com Aline
# QUAIS OS NOMES MAIS POPULARES EM ISRAEL? Atualizado 2022
video_url = "https://www.youtube.com/watch?v=U6brR0LGo8A"
video_obj = YouTube(video_url)
#stream = video_obj.streams.get_highest_resolution()
#stream.download(DOWNLOAD_FOLDER)
video_options, yt_videos_dict = cria_lista_de_opcoes(video_obj)
choice = escolher_resolucao(video_obj)

try:
  print('==> ',video_options[int(choice)])
  itag = (yt_videos_dict[video_options[int(choice)]])
  print("Iniciando download")

  print('Título...: ',video_obj.title)
  selected_stream = video_obj.streams.get_by_itag(itag)
  selected_stream.download()
  print("Download concluído com sucesso")
  
except Exception as error:
  print('Opção inválida!')
  print(str(error))

print("Encerrado com sucesso")



