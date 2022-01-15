# https://stackoverflow.com/questions/55735775/how-do-i-add-a-progress-bar-to-my-pytube-code


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


def main():
	stream_options = cria_lista_de_opcoes(video_obj)
	show_user_option(stream_options)
	user_choice_itag = get_user_option(stream_options)
	selected_stream = video_obj.streams.get_by_itag(user_choice_itag)
	selected_stream.download()
	print("Encerrado com sucesso")

def on_progress_func(stream, chunk, bytes_remaining):
	total_size = stream.filesize
	bytes_downloaded = total_size - bytes_remaining
	percentage_of_completion = int (bytes_downloaded / total_size * 100)
	print(percentage_of_completion,' % Completed')

def on_complete_func(stream, file_path):
	print('Download complete')

from pytube import YouTube
import sys
DOWNLOAD_FOLDER = "./downloads"
# Israel com Aline
# QUAIS OS NOMES MAIS POPULARES EM ISRAEL? Atualizado 2022
video_url = "https://www.youtube.com/watch?v=U6brR0LGo8A"
video_obj = YouTube(video_url,
			on_progress_callback = on_progress_func,
			on_complete_callback = on_complete_func )

stream_options = cria_lista_de_opcoes(video_obj)
show_user_option(stream_options)
user_choice_itag = get_user_option(stream_options)
stream = video_obj.streams.get_by_itag(user_choice_itag)
stream.download(DOWNLOAD_FOLDER)
print('End.')
