import os
import sox
import sys

sample_folder = "/home/sourya4/pro/columbia/spring22/fund_sp_rec/datasets/microsoftspeechcorpusindianlanguages/te-in-Train/Audios/"
def computer_folder_statistics(folder_name):
    # sample_path = "/home/sourya4/pro/columbia/spring22/fund_sp_rec/datasets/microsoftspeechcorpusindianlanguages/te-in-Train/Audios/000010013.wav"
    folder_name = sample_folder
    #Iterate through all files in the folder that have .wav extension
    duration_seconds_list = []
    counter_files = 0
    for file in os.listdir(folder_name):
        if file.endswith(".wav"):
            file_path = os.path.join(folder_name, file)
            #Get the total time of the file
            dur_sec = sox.file_info.duration(file_path)
            duration_seconds_list.append(dur_sec)
            counter_files += 1
            if(counter_files%1000 == 0):
                print(f"{counter_files} files processed")
            if(counter_files>=5000):
                break

    num_files = len(duration_seconds_list)
    total_time = sum(duration_seconds_list)
    minimum_time = min(duration_seconds_list)
    maximum_time = max(duration_seconds_list)
    average_time = total_time/len(duration_seconds_list)
    print(f"Total number of files: {num_files}")
    print(f"Total time in seconds: {total_time}")
    print(f"Total time in minutes: {total_time/60}")
    print(f"Total time in hours: {total_time/(60*60)}")
    print(f"Minimum time: {minimum_time}")
    print(f"Maximum time: {maximum_time}")
    print(f"Average time: {average_time}")
    return total_time

if(len(sys.argv)>1):
    computer_folder_statistics(sys.argv[1])
else:
    computer_folder_statistics(sample_folder)

