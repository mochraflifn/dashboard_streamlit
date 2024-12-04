import streamlit as st
import pandas as pd
import plotly.express as px

# Memuat dataset
data = pd.read_csv('dbd_jabar.csv')

# Menetapkan judul dan subjudul
st.title("Dashboard Kasus DBD di Jawa Barat")
st.subheader("Analisis Kasus DBD berdasarkan Wilayah dan Jenis Kelamin")

# Sidebar untuk input pengguna
st.sidebar.header("Menu")
province = st.sidebar.selectbox("Pilih Provinsi", data['nama_provinsi'].unique())
year = st.sidebar.slider("Pilih Tahun", min_value=2014, max_value=2023, value=2016)
show_male = st.sidebar.checkbox("Tampilkan Kasus Laki-Laki", value=True)
show_female = st.sidebar.checkbox("Tampilkan Kasus Perempuan", value=True)

# Menyaring data berdasarkan input pengguna
filtered_data = data[(data['nama_provinsi'] == province) & (data['tahun'] == year)]

# Diagram Batang: Total kasus berdasarkan jenis kelamin
gender_counts = filtered_data.groupby('jenis_kelamin')['jumlah_kasus'].sum()
gender_counts = gender_counts[gender_counts.index.isin(['LAKI-LAKI' if show_male else '', 'PEREMPUAN' if show_female else ''])]

st.subheader("Total Kasus berdasarkan Jenis Kelamin")
fig_bar = px.bar(gender_counts.reset_index(), x='jenis_kelamin', y='jumlah_kasus', color='jenis_kelamin',
                 title="Total Kasus Berdasarkan Jenis Kelamin", labels={'jumlah_kasus': 'Jumlah Kasus', 'jenis_kelamin': 'Jenis Kelamin'})
st.plotly_chart(fig_bar)

# Insight dari diagram batang
st.write("Diagram ini menunjukkan jumlah total kasus berdasarkan jenis kelamin di provinsi yang dipilih. "
         "Anda dapat memilih untuk menampilkan kasus untuk laki-laki, perempuan, atau keduanya.")

# Diagram Garis: Tren kasus selama beberapa tahun untuk provinsi yang dipilih
trend_data = data[data['nama_provinsi'] == province].groupby(['tahun', 'jenis_kelamin'])['jumlah_kasus'].sum().reset_index()
st.subheader("Jumlah Kasus Selama Beberapa Tahun")
fig_line = px.line(trend_data, x='tahun', y='jumlah_kasus', color='jenis_kelamin', markers=True,
                    title=f"Tren Kasus di {province}", labels={'jumlah_kasus': 'Jumlah Kasus', 'tahun': 'Tahun'})
st.plotly_chart(fig_line)

# Insight dari diagram garis
st.write("Grafik garis ini menunjukkan tren jumlah kasus selama beberapa tahun untuk provinsi yang dipilih, "
         "dengan membandingkan jumlah kasus berdasarkan jenis kelamin.")

# Diagram Lingkaran: Distribusi kasus berdasarkan jenis kelamin untuk tahun yang dipilih
st.subheader("Distribusi Kasus berdasarkan Jenis Kelamin")
gender_distribution = filtered_data.groupby('jenis_kelamin')['jumlah_kasus'].sum()
gender_distribution = gender_distribution[gender_distribution.index.isin(['LAKI-LAKI' if show_male else '', 'PEREMPUAN' if show_female else ''])]

fig_pie = px.pie(gender_distribution.reset_index(), values='jumlah_kasus', names='jenis_kelamin',
                 title="Distribusi Kasus Berdasarkan Jenis Kelamin", hole=0.3)
st.plotly_chart(fig_pie)

# Insight dari diagram lingkaran
st.write("Diagram lingkaran ini menggambarkan distribusi kasus DBD berdasarkan jenis kelamin pada tahun yang dipilih. "
         "Grafik ini memberikan gambaran yang jelas tentang proporsi antara kasus laki-laki dan perempuan.")

# Identitas Kelompok
st.sidebar.subheader("Anggota Kelompok")
st.sidebar.write("""
- Aldi Aldiansyah
- Alwa Putri Roosyidah
- Faunita Raihan Dzahirah
- M Rafli Fadilla Nugraha
- Dwipandra Juldan
""")
