import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(
    page_title="Iris Dataset Explorer 🌸",
    layout="wide",
)

# Custom CSS for background image
st.markdown(
    """
    <style>
    body {
        background-image: url('file:///C:/Users/divya/OneDrive/Documents/App/Notebook%20dataset/blue-canvas-abstract-texture-background-260nw-486963931.webp');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        color: #fff;
    }
    .main {
        background: rgba(255, 255, 255, 0.8); 
        border-radius: 10px;
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the Iris dataset
iris = pd.read_csv(r'C:\Users\divya\OneDrive\Documents\App\Notebook dataset\Iris.csv')

# Sidebar for user inputs
st.sidebar.title("🌸 Iris Dataset Explorer ")
st.sidebar.write("👋 Select your preferences below to explore the Iris dataset!")

# Visualization options
visualization = st.sidebar.selectbox(
    "📊 Choose a Visualization",
    ("🌟 JointPlot", "📦 BoxPlot", "✨ StripPlot", "🎻 ViolinPlot", "🌈 PairPlot")
)

# Filter options
species_filter = st.sidebar.multiselect(
    "🔍 Filter by Species",
    iris['Species'].unique(),
    default=iris['Species'].unique()
)

# Filter the data
filtered_data = iris[iris['Species'].isin(species_filter)]

# Display dataset
st.write("## 🌺 Iris Dataset")
st.write("Here is a preview of the Iris dataset after applying your filters 👇:")
st.dataframe(filtered_data)

# Create visualizations based on user selection
st.write(f"## {visualization} Visualization 🎨")

if visualization == "🌟 JointPlot":
    fig = sns.jointplot(x='SepalLengthCm', y='SepalWidthCm', data=filtered_data, kind="scatter")
    st.pyplot(fig)

elif visualization == "📦 BoxPlot":
    fig, ax = plt.subplots()
    sns.boxplot(x='Species', y='SepalLengthCm', data=filtered_data, ax=ax)
    st.pyplot(fig)

elif visualization == "✨ StripPlot":
    fig, ax = plt.subplots()
    sns.stripplot(x='Species', y='SepalLengthCm', data=filtered_data, jitter=True, ax=ax)
    st.pyplot(fig)

elif visualization == "🎻 ViolinPlot":
    fig, ax = plt.subplots()
    sns.violinplot(x='Species', y='PetalLengthCm', data=filtered_data, ax=ax)
    st.pyplot(fig)

elif visualization == "🌈 PairPlot":
    fig = sns.pairplot(data=filtered_data, hue='Species')
    st.pyplot(fig)

# Additional histogram feature
st.write("## 📊 Histogram of Sepal Length 📏")
fig, ax = plt.subplots()
filtered_data['SepalLengthCm'].hist(ax=ax, edgecolor='black', linewidth=1.2)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length')
st.pyplot(fig)

# Footer
st.sidebar.write("💡 Tip: Combine filters and visualizations to discover patterns!")
st.write("### 🛠 Built with Streamlit |😊 Happy Exploring!")
