#import library yang dibutuhkan
import pandas as pd
import numpy as np
from scipy.stats import stats
import streamlit as st
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

#judul website
st.title('UJI HIPOTESIS RATA-RATA DUA POPULASI')

st.header('Input Data')
# Memasukkan data variabel 1
var1_input = st.text_input('Variabel 1 (pisahkan dengan koma)', '1,3,5,7')
var1 = [float(var1.strip()) for var1 in var1_input.split(',')]
# Memasukkan data variabel 2
var2_input = st.text_input('Variabel 2 (pisahkan dengan koma)', '2,4,6,8')
var2 = [float(var2.strip()) for var2 in var2_input.split(',')]
# Memasukan alpha sebagai taraf  signifikan
alpha = st.number_input('Alpha :', 0.000)
# Menampilkan data sebagai tabel
df = pd.DataFrame({'Variabel 1': var1, 'Variabel 2': var2})
st.write(df)

#uji hipotesis rata-rata
st.header('Hasil Uji Hipotesis')
st.write('Hipotesis :')
st.write('H0 : Rata-rata populasi satu sama dengan rata-rata populasi dua')
st.write('H1 : Rata-rata populasi satu tidak sama dengan rata-rata populasi dua')

# Calculate statistics
mean1 = np.mean(var1)
mean2 = np.mean(var2)
varians1 = np.var(var1, ddof=1)
varians2 = np.var(var2, ddof=1)
st.write('Mean 1:', mean1)
st.write('Mean 2:', mean2)
st.write('Varians 1:', varians1)
st.write('Varians 2:', varians2)

#menghitung nilai t-statistik
t_stat, p_val = stats.ttest_ind(var1, var2)
st.write('Nilai t-statistik :', t_stat)
st.write('Nilai p-value :', p_val)

#menentukan hipotesis nol diterima atau ditolak
st.write('Keputusan :')
if p_val < alpha:
  st.write('H0 ditolak, artinya rata-rata kedua populasi berbeda.')
else:
  st.write('H0 diterima, artinya rata-rata kedua populasi sama.')

