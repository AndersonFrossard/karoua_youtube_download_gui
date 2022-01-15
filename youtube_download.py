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
  yt_stream_list = video_obj.streams.filter(progressive=True)
  stream_options =[]
  for item in yt_stream_list:
    stream_options.append([item.itag, item.resolution])
  return stream_options

def show_user_option(stream_options):
  i=0
  print("Resoluções disponíveis para download : ")
  for item in stream_options:
    print(i, '- ', item[1])
    i+=1
  print('Escolha sua resolução: ')

def get_user_option(stream_options):
  try:
    choice = input( " ? " )
    int_choice = int(choice)
    itag = stream_options[int_choice][0] 
    return itag
  except Exception as error:
    exception_routine(error)

def exception_routine(error):
  print("Opção inválida !!!")
  print("Erro: ", str(error))
  raise SystemExit

from pytube import YouTube
DOWNLOAD_FOLDER = "./downloads"
# Israel com Aline
# QUAIS OS NOMES MAIS POPULARES EM ISRAEL? Atualizado 2022
video_url = "https://www.youtube.com/watch?v=U6brR0LGo8A"
video_obj = YouTube(video_url)
#stream = video_obj.streams.get_highest_resolution()
#stream.download(DOWNLOAD_FOLDER)

stream_options = cria_lista_de_opcoes(video_obj)
show_user_option(stream_options)
user_choice_itag = get_user_option(stream_options)
selected_stream = video_obj.streams.get_by_itag(user_choice_itag)
selected_stream.download()
print("Encerrado com sucesso")



