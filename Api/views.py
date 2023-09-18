from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

import json
import pickle
import numpy as np
import random
import os
import ffmpeg
import openai
import os
import openai
import speech_recognition as sr
from pydub.utils import mediainfo
from pathlib import Path

def lec_process(filename, chunk_duration=90):

    record = sr.Recognizer()

    with sr.AudioFile(filename) as source:

        lec_data = mediainfo(filename)

        lec_duration = int(float(lec_data['duration']))

        data_material = ""

        for i in range(0, lec_duration, chunk_duration):

            lec_chunk = record.record(source, duration=chunk_duration)

            data_material += record.recognize_google(lec_chunk) + " "
            
        return data_material
    
#lecturer summarizer part with different option



class Filesummary(APIView):
    def get(self, request):
        Overfilename=request.FILES['video'] 
        output_audio = 'output_audio.wav'  # Specify the output WAV audio file path
      
        file_path = Path(Overfilename.temporary_file_path())

        try:
            (
                ffmpeg.input(file_path)
                .output(output_audio)
                .run(overwrite_output=True)
            )
        except ffmpeg.Error as e:
            print('Error:', e.stderr.decode())

        Text_extraction = lec_process("output_audio.wav")
        



        
        return Response({"Translation":Text_extraction,"status": status.HTTP_200_OK})
