FROM python:3.6
RUN pip install torchvision
RUN pip install jieba
RUN python -m pip install -U pip
RUN python -m pip install -U matplotlib
ADD seq2seq_translation.py /
ADD format_sub.py /
ADD my_attn_decoder.pt /
ADD my_encoder.pt /
ADD data/eng-chi.txt /
CMD ["python", "./seq2seq_translation.py"]