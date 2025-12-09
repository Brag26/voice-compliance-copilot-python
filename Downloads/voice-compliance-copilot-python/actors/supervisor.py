import os,sys
mode='demo'
if len(sys.argv)>2 and sys.argv[1]=='--mode': mode=sys.argv[2]
print(f'Starting in {mode} mode')
if mode=='audio': os.system('python actors/audio_transcriber/main.py')
else: os.system('python actors/prompt_response_loader/main.py')
os.system('python actors/quality_judge/main.py')
os.system('python actors/report_generator/main.py')
print('Pipeline completed')