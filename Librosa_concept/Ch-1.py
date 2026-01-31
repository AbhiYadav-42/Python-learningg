"""What is librosa?? """
# Librosa is a python library designed for audio and music analysis 
# uses the extracting features like MFCC , visulaizing waveforms and perfrominng stretching or pitch shifting. 

# Loading an Audio File!!

import librosa
import matplotlib.pyplot as plt 
import librosa.display
import numpy as np

audio = '/media/alchemax/New Volume/Programming_Files/python_GIT/Librosa_concept/sample_voice.mp3'

#Load
y,sr = librosa.load(audio, sr =None)        
# load file and returns the waveform(y) and sample rate (sr) = none , so that it load at its orginal sampling rate

#Display
print(f'Sampling rate: {sr}')
print(f'waveform Length: {len(y)}')


# Visualize the waveform
plt.figure(figsize=(10,4))
librosa.display.waveshow(y, sr=sr)
plt.title('waveform')
plt.xlabel('Time (Seconds)')
plt.ylabel('(Amplitude)')


plt.savefig('waveform.png')
plt.close()




# Extracting Audio featuress 
#  LibROSA allows you to extract features such as spectrograms and MFCC (Mel-Frequency Cepstral Coefficients).


# Display Spectrograms
# --->> Generate a spectogram using Short-Time Fourier Transform (STFT)

D= librosa.stft(y)
s_db =  librosa.amplitude_to_db(abs(D))

plt.figure (figsize=(10,4))
librosa.display.specshow(s_db, sr=sr, x_axis = 'time', y_axis='log')
plt.colorbar(format = '%+2.0f dB')

plt.title('Spectogram')
plt.savefig('spectogram.png')


# Now on Spectogram we will extract the MFCC (mel-frequency cepstral Coefficients)

# Extract
mfccs = librosa.feature.mfcc(y=y , sr=sr, n_mfcc=13)

mfcc_var = np.var(mfccs, axis=1)
print(mfcc_var)
# Display the MFCCs
plt.figure(figsize = (10,4))
librosa.display.specshow(mfccs , sr=sr, x_axis ='time')
plt.colorbar()
plt.title('MFCC')
plt.xlabel('Time(seconds)')
plt.ylabel('MFCC coefficients')
plt.savefig('Mfcc_extraction.png')





# Extract  and plot the ZCR ( zero crossing rate )

zcr =  librosa.feature.zero_crossing_rate(y)

avg_zcr = np.mean(zcr)
print(f'Avg zcr: {avg_zcr}')
