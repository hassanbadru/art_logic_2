# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import math
import os

from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic import TemplateView, View, CreateView
from django.conf import settings

from rest_framework.response import Response
from rest_framework import generics

import json
# from rest_framework import serializers
from django.core.serializers import serialize

from art_logic_app.models import UserAction
from art_logic_app.serializers import UserActionSerializer
from art_logic_app.myfunctions import encoder, decoder, readInstruction, write_instructions


# Create your views here.
class ArtLogicAPI(generics.ListCreateAPIView):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer


class ArtLogicApp(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArtLogicApp, self).get_context_data()

        # user_action = UserAction()

        #Uploaded Text Files
        # if self.request.FILES.get('file_compute'):
        #     print("recognizes file input")
        #     file_compute = self.request.FILES['file_compute'].readlines()
        #     # print(file_compute)
        #     return redirect('art_logic')

        instruction_string = self.request.GET.get('instruction_string')
        if instruction_string:

            context['instruction_string'] = instruction_string

            #get instructions
            instruction_stream = readInstruction(instruction_string)

            # perform instructed operations
            instruction_json = write_instructions(instruction_stream)

            # convert to json
            instruction_json = json.dumps(instruction_json)
            # print(instruction_json)

            context['instruction_stream'] = instruction_json
            # print(instruction_stream)


        to_compute = self.request.GET.get('to_compute')

        if to_compute:
            decode = self.request.GET.get('decode')
            encode = self.request.GET.get('encode')
            # print(to_compute)

            encode_operation = encode == "on"
            # print(encode_operation)

            result = ''
            if encode_operation:
                # print('Encoding')
                encoded_result = encoder(to_compute)
                # context['encoding_result'] = encoding_result
                result = encoded_result
            else:
                # print('Decoding')
                decoded_result = decoder(to_compute)
                result = decoded_result

            context['result'] = str(result)

            #Add to results database for REST API
            if encode_operation:
                operation_type = 'encoding'
            else:
                operation_type = 'decoding'

            # context['operation_type'] = operation_type

            user_action = UserAction(operation=operation_type, input=to_compute, result=result)
            # print(user_action.input)
            all_items = UserAction.objects.all()
            # print([i.pk for i in all_items])
            user_action.save()

        # Get all preloaded inputs from database
        all_items = UserAction.objects.all()
        encoding_stream = []
        decoding_stream = []

        # Categorize inputs
        for i in all_items:
            if i.operation == 'encoding':
                encoding_stream.append(i.input)
            elif i.operation == 'decoding':
                decoding_stream.append(i.input)

            # print(i.input, i.operation)
        # print(encoding_stream, decoding_stream)

        #Test Preloaded Streams
        # encoding_stream = ['6111', '340', '-2628', '-255', '7550']
        # decoding_stream = ['0A0A', '0029', '3F0F', '4400', '5E7F']

        #Write all valid encoded data to text file
        with open(os.path.join(settings.MEDIA_ROOT, 'ConvertedData.txt'), 'w') as f:
            f.write('ENCODED DATA: '+'\n')

            counter = 0 # to count through loop
            for x in encoding_stream:
                encoded = encoder(x)
                counter += 1
                # print(counter)
                if len(encoded) < 6:
                    if counter > 5:
                        f.write('USER ADDED: ' + x + ' is encoded as ' + encoded + '\n')
                    else:
                        f.write(x + ' is encoded as ' + encoded + '\n')
            f.close()


        #Write all valid decoded data to text file
        with open(os.path.join(settings.MEDIA_ROOT, 'ConvertedData.txt'), 'a') as f:
            f.write('\n\n\n'+'DECODED DATA: '+'\n')

            counter = 0 # to count through loop
            for x in decoding_stream:
                decoded = str(decoder(x))
                counter += 1
                if len(decoded) < 6:
                # print(x)
                    if counter > 5:
                        f.write('USER ADDED: ' + x + ' is decoded as ' + decoded + '\n')
                    else:
                        f.write(x + ' is decoded as ' + decoded + '\n')

            f.close()


        return context
