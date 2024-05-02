# Copyright 2021 Sony Group Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np

from neu.tts.hparams import HParams

hparams = HParams(

    corpus_path='LJSpeech-1.1/',
    precomputed_path='ljspeech/',

    output_path='./log/fastspeech2/',

    # data-dependent parameters
    max_len_phone=150,      # maximum length of phonemes
    max_len_mel=871,        # maximum length of Mel-frames

    # optimization
    batch_size=48,          # batch size
    epoch=1000,
    seed=123456,            # random seed
    beta1=0.9,
    beta2=0.98,
    lr=1e-3,
    warmup=4000,
    print_frequency=10,
    epochs_per_checkpoint=25,

    # vocoder
    vocoder='HifiGAN',  # or 'MelGAN'

    # encoder
    encoder_hidden=256,
    encoder_layer=4,
    encoder_dropout=0.2,
    encoder_head=2,
    conv_filter_size=1024,
    conv_kernel_size=9,

    # decoder
    decoder_hidden=256,
    decoder_dropout=0.2,
    decoder_layer=6,
    decoder_head=2,

    # predictor
    predictor_filter_size=256,
    predictor_kernel_size=3,
    predictor_dropout=0.5,
    predictor_blocks=2,

    n_bins=256,             # number of buckets

    # audio parameters
    sr=22050,               # sampling rate
    mel_fmax=8000,          # set to None for MelGAN
    mel_fmin=0,
    n_fft=1024,
    hop_length=256,
    win_length=1024,
    n_mels=80,
    lower_bound=np.log(1e-5),  # change to np.log10(1e-5) for MelGAN
)
