# https://stackoverflow.com/questions/55735775/how-do-i-add-a-progress-bar-to-my-pytube-code
#Use this option to run under google colab:
#from pytube import exceptions 

# https://stackoverflow.com/questions/42422139/how-to-easily-avoid-tkinter-freezing


def exception_routine(error):
  if type(error) == IndexError:
    print('Opção inválida !! ')
  elif type(error) == KeyError:
  	print('Noob User did not choose a resolution and clicked on DOWNLOAD button. Afff.')
  elif type(error) == ValueError:
    print('Opção inválida. Somente números são permitidos.')
  elif type(error) == pytube.exceptions.VideoUnavailable:
    print('Erro: Vídeo não disponível.')
    print('Você entrou com a URL correta? Utilizar conforme o exemplo :')
    print('https://www.youtube.com/watch?v=NNNNNNNNNNN')
  elif type(error) == pytube.exceptions.VideoPrivate:
      print('Erro: Vídeo é privado. Download não disponível.')
  elif type(error) == pytube.exceptions.LiveStreamError:
      print('Erro: Vídeo é uma live. Download não disponível.')
  elif type(error) == pytube.exceptions.AgeRestrictedError:
      print('Video is age restricted, and cannot be accessed without OAuth.')
  elif type(error) == pytube.exceptions.MaxRetriesExceeded:
      print('Maximum number of retries exceeded.')
  elif type(error) == pytube.exceptions.MembersOnly:
      print('Error: Video is members-only.')
      print('YouTube has special videos that  are only viewable to users who')
      print('have subscribed to a content creator')
  elif type(error) == pytube.exceptions.VideoRegionBlocked:
      print('Error: Video is blocked to your region. Try using a VPN.')
  else:
    print(str(error))
  print('Program Terminated.')
  raise SystemExit

def on_progress_func(stream, chunk, bytes_remaining):
	total_size = stream.filesize
	bytes_downloaded = total_size - bytes_remaining
	percentage_of_completion = int (bytes_downloaded / total_size * 100)
	print("\r Downloading ...... %d%%" % percentage_of_completion,end="")
	try:
		gui_lbl_information.set("Downloading ...... %d%%" % percentage_of_completion)
	except Exception as e:
		pass
	finally:
		pass

def on_complete_func(stream, file_path):
	try:
		message = "Download complete."
		print("\n"+message)
		gui_lbl_information.set(message)
	except Exception as e:
		pass

def clear_combo_box():
	tk_mycombox['values'] = ""

def on_btn_load_cliked():
	global video_obj
	global stream_options_dict
	try:
		gui_lbl_information.set("...Loading...")
		if tk_entry_url_text.get() == 'teste':
			video_url = 'https://www.youtube.com/watch?v=U6brR0LGo8A'
		else:
			video_url = tk_entry_url_text.get()
		video_obj = YouTube(video_url,
			on_progress_callback = on_progress_func,
			on_complete_callback = on_complete_func)
		print(video_obj.title)
		str_var_movie_title.set(video_obj.title)
		create_stream_options(video_obj, stream_options_dict)
		gui_populate_combox()
		gui_lbl_information.set("...Options Loaded...")
	except Exception as error:
		exception_routine(error)

def thread_on_btn_load_clicked():
	threading.Thread(target = on_btn_load_cliked).start()

def create_stream_options(video_obj, stream_options_dict):
	try:
		yt_stream_list_video = video_obj.streams.filter(progressive = True)
		yt_stream_list_audio = video_obj.streams.filter(only_audio = True)
		for item in yt_stream_list_video:
			stream_options_dict[item.resolution] = item.itag
		for item in yt_stream_list_audio:
			stream_options_dict[item.abr + ' only audio'] = item.itag
	except Exception as e:
		exception_routine(e)
	return stream_options_dict

def gui_populate_combox():
	global stream_options_dict
	clear_combo_box()
	for resolution in stream_options_dict.keys():
		tk_mycombox['values'] = tuple (list(tk_mycombox['values'])
			+ [str(resolution)])
	#tk_mycombox.current(1)

def gui_on_btn_download_clicked():
	global stream_options_dict
	global video_obj
	global DOWNLOAD_FOLDER
	gui_lbl_information.set("Starting download..")
	try:
		user_choice_itag = stream_options_dict[tk_mycombox.get()]
		stream = video_obj.streams.get_by_itag(user_choice_itag)
		new_filename = create_filename(stream)
		stream.download(DOWNLOAD_FOLDER, filename = new_filename)
	except Exception as e:
		exception_routine(e)
	finally:
		pass

def thread_gui_on_btn_download_clicked():
	threading.Thread(target = gui_on_btn_download_clicked).start()
	
def create_filename(stream):
	if is_stream_audio_only(stream):
		return stream.default_filename[0:-4]+'.mp3'
	return stream.default_filename

def is_stream_audio_only(stream):
	return not stream.includes_video_track



def is_cli():
	for item in sys.argv:
		if 'nogui' in item.lower():
			return True
	return False

def show_user_option(stream_options):
  i=0
  print("Resoluções disponíveis para download : ")
  for item in stream_options.keys():
    print(i, '- ', item)
    i+=1
  print('Escolha sua resolução: ')

def get_user_url():
## TODO: throw exception if user enters a number.	
	try:
	  print('Exemplo: https://www.youtube.com/watch?v=U6brR0LGo8A')
	  print('Insira a URL do vídeo :')
	  video_url = input(' ==> ')
	  if video_url == 'teste': video_url = 'https://www.youtube.com/watch?v=U6brR0LGo8A'
	  return video_url
	except Exception as error:
	  print('erro')
	  SystemExit

def get_user_option(stream_options_dict):
  try:
  	stream_options_list = list(stream_options_dict)
  	choice = input( " ? " )
  	int_choice = int(choice)
  	itag = stream_options_dict[stream_options_list[int_choice]]
  	return itag
  except Exception as error:
    exception_routine(error)


def run_terminal():
	try:
		print(' -=-=-=-=-= Running on Terminal =-=-=-=-=-')
		DOWNLOAD_FOLDER = "./downloads"
		url_test = "https://www.youtube.com/watch?v=U6brR0LGo8A"
		video_url = get_user_url()
		if video_url == 'teste' : video_url = url_test

		video_obj = YouTube(video_url,
				on_progress_callback = on_progress_func,
				on_complete_callback = on_complete_func )
		
		stream_options = create_stream_options(video_obj, dict())
		show_user_option(stream_options)
		user_choice_itag = get_user_option(stream_options)
		stream = video_obj.streams.get_by_itag(user_choice_itag)
		new_filename = create_filename(stream)
		stream.download(DOWNLOAD_FOLDER, filename = new_filename)
	except Exception as error:
		exception_routine(error)
	
#/-==============================================================
#/-
#/-  Here begins the main module
#/-
#/-==============================================================
from pytube import YouTube
import pytube.exceptions 
import sys
import tkinter
from tkinter import ttk
import threading

#/-====================
#/- Here begins the GUI
#/-====================


if is_cli():
	run_terminal()
	raise SystemExit

example_url = 'https://www.youtube.com/watch?v=U6brR0LGo8A'
program_name = 'Karoua YouTube Downloader'
program_icon_path = './img/Graphics-Vibe-Classic-3d-Social-Youtube.ico'
global stream_options
global stream_options_dict
global video_obj
global DOWNLOAD_FOLDER
global gui_lbl_information
WIDTH = 504
HEIGHT = 326

stream_options = []
stream_options_dict = dict()
DOWNLOAD_FOLDER = "./downloads"

root = tkinter.Tk()
root.geometry(str(WIDTH)+"x"+str(HEIGHT))

gui_lbl_information = tkinter.StringVar()
gui_lbl_information.set("=[Load your URL]=")

root_color = "#58babf"
lblframe_a_color = "#ffe39f"
lblframe_b_color = "#b3dca0"
lblframe_c_color = "#008080"
root.configure(bg = root_color)
root.title(program_name)
root.iconbitmap(program_icon_path)
labelframe_a = tkinter.LabelFrame(root, text="Example",
				bg=root_color)
labelframe_a.pack(side = tkinter.TOP, 
				fill="both", expand="yes",
				padx = 12, pady = 12)

labelframe_b = tkinter.LabelFrame(root, text = "Enter URL",
				bg=root_color, bd = 3)
labelframe_b.pack(side = tkinter.TOP,
				 fill="both", expand="yes",
				 padx = 12, pady = 12)

labelframe_b2 = tkinter.LabelFrame(root, text = "Movie Title",
				bg=root_color, bd = 3)
labelframe_b2.pack(side = tkinter.TOP,
				 fill="both", expand="yes",
				 padx = 12, pady = 12)



labelframe_c = tkinter.LabelFrame(root,
				 text = "Choose your resolution", bg = root_color)
labelframe_c.pack(side = tkinter.BOTTOM,
				fill = "both", expand = "yes",
				padx = 12, pady = 12)



tk_lbl_example_txt = tkinter.Label(labelframe_a, text = example_url,
				 bg=root_color, bd=5)
tk_lbl_example_txt.pack(side = tkinter.LEFT, padx = 5, pady = 5)
	
tk_entry_url_text = tkinter.Entry(labelframe_b, width = 50)#,
				#bg = lblframe_b_color, bd=3)
tk_entry_url_text.pack(side = tkinter.LEFT, padx = 5, pady = 5)
tk_btn_load = tkinter.Button(labelframe_b, text='LOAD',
			 command= 
			 lambda : thread_on_btn_load_clicked())
tk_btn_load.pack(side = tkinter.BOTTOM, expand=True, padx = 5, pady = 5)

str_var_movie_title = tkinter.StringVar()
str_var_movie_title.set("Not yet loaded")
tk_lbl_movie_title = tkinter.Label(labelframe_b2, textvariable = str_var_movie_title,
				 bg=root_color, bd=5)
tk_lbl_movie_title.pack(side = tkinter.LEFT, padx = 5, pady = 5)



tk_mycombox = tkinter.ttk.Combobox(labelframe_c,
				textvariable= tkinter.IntVar(),
				values=["----Download Type----"],
				state = 'readonly')
tk_mycombox.current(0)
tk_mycombox.pack(side = tkinter.LEFT, fill = tkinter.X,  padx = 16, pady = 5)
tk_mycombox.propagate(False)

tk_btn_download = tkinter.Button(labelframe_c, text = 'DOWNLOAD',
		command = lambda: thread_gui_on_btn_download_clicked())
tk_btn_download.pack(side = tkinter.LEFT, fill = tkinter.X, padx = 16, pady = 5)
tk_btn_download.propagate(False)

tk_lbl_info = tkinter.Label(labelframe_c, 
		textvariable = gui_lbl_information,
		font = ("Bm437 Trident 8x16", 11, "normal"), bg=root_color, fg = "red")
tk_lbl_info.pack(side = tkinter.LEFT, fill = tkinter.X,  padx = 5, pady = 5)
tk_lbl_info.propagate(False)

root.mainloop()	


#/-======
#/- End of the GUI
#/-======


print('End.')
