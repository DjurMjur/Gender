import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
final_df = pd.read_csv("final_df")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Explanation"])

# Dashboard Page
if page == "Dashboard":
    # Sidebar: Select countries to compare
    st.sidebar.title("Country Comparison")
    selected_countries = st.sidebar.multiselect(
        "Select up to 3 countries to compare:",
        options=final_df["COUNTRY"].unique(),
        default=final_df["COUNTRY"].unique()[:3]
    )

    # Sidebar: Select visualizations to display
    st.sidebar.title("Visualization Options")
    show_scatter = st.sidebar.checkbox("Show Scatter Plot", value=True)
    show_choropleth = st.sidebar.checkbox("Show Choropleth Map", value=True)
    show_bar_chart = st.sidebar.checkbox("Show Bar Chart", value=True)
    show_images = st.sidebar.checkbox("Show Images", value=True)

    # Display the filtered data
    st.title("Country Comparison Dashboard")
    st.write("Explore and compare metrics for different countries.")
    st.write("Selected Countries Data:")
    filtered_data = final_df[final_df["COUNTRY"].isin(selected_countries)]
    st.dataframe(filtered_data)

    # Bar Chart: Comparison of Metrics
    if show_bar_chart and len(selected_countries) > 0:
        st.subheader("Comparison of All Metrics Across Selected Countries (not scaled lol)")
        melted_data = filtered_data.melt(
            id_vars=["COUNTRY"], 
            var_name="Metric", 
            value_name="Value"
        )
        bar_fig = px.bar(
            melted_data,
            x="Metric",
            y="Value",
            color="COUNTRY",
            barmode="group",
            title="Comparison of All Metrics Across Selected Countries",
            labels={"Value": "Metric Value", "Metric": "Metrics"},
            height=600
        )
        st.plotly_chart(bar_fig)

    # Scatter Plot: Urban Population vs. GDI
    if show_scatter:
        st.subheader("Urban Population vs GDI, Colored by Employment Protection")
        custom_colorscale = [[0, 'red'], [1, 'green']]
        scatter_fig = px.scatter(
            final_df,
            x='Urban population (% of total population)',
            y='Gender Development Index',
            color='EMPLOY.', 
            hover_data=['COUNTRY', 'CONST.', 'BROAD PROT.'],  
            color_continuous_scale=custom_colorscale, 
            title='Urban Population vs GDI, Colored by Employment Protection'
        )
        scatter_fig.update_layout(
            coloraxis_colorbar=dict(
                title="Employment Protection",
                tickvals=[0, 1], 
                ticktext=['Bad (0)', 'Good (1)']
            ),
            xaxis_title="Urban Population (% of total population)",
            yaxis_title="Gender Development Index"
        )
        st.plotly_chart(scatter_fig)

    # Choropleth Map: Employment Protection by Country
    if show_choropleth:
        st.subheader("Employment Protection for LGBT Individuals by Country")
        choropleth_fig = px.choropleth(
            final_df,
            locations="COUNTRY",
            locationmode="country names",
            color="EMPLOY.",
            hover_name="COUNTRY",
            hover_data={
                "BROAD PROT.": True,
                "HATE CRIME": True,
                "INCITEMENT": True,
                "Gender Development Index": True,
                "Urban population (% of total population)": True
            },
            title="Employment Protection for LGBT Individuals by Country",
            color_continuous_scale=[[0, 'red'], [1, 'green']]
        )
        choropleth_fig.update_layout(
            coloraxis_colorbar=dict(
                title="Employment Protection",
                tickvals=[0, 1],
                ticktext=["Bad (0)", "Good (1)"]
            )
        )
        st.plotly_chart(choropleth_fig)

    # Add Images
    if show_images:
        st.subheader("Relevant Images")
        st.image("./CorrHeatmap.png", caption="Correlation Heatmap", use_column_width=True)
        st.image("FeatureImportance.png", caption="Feature Importance", use_column_width=True)

# Explanation Page
elif page == "Explanation":
    st.title("Explanation and Resources")
    st.write("""
    This dashboard is designed to explore employment protection and related metrics for LGBT individuals across different countries. Since our project is about sexual-orientation
    in the labour market we had to use the data we could find.         
    
    ### Data:
    Data collected in State-Sponsored Homophobia 2020: Global Legislation Overview Update (published in December 2020).
    https://ilga.org/maps-sexual-orientation-laws
    https://ilga.org/wp-content/uploads/2023/11/ILGA_World_State_Sponsored_Homophobia_report_global_legislation_overview_update_December_2020.pdf
    
             

    ### GDI:

    The Gender Development Index (GDI) measures gender inequalities in the achievement of key dimensions of human development: a long and healthy life, a good education, and a decent
    standard of living. Values close to 1 indicate higher gender equality. The Gender Development Index (GDI) measures gender inequalities in achievement in three basic dimensions of human development: health, measured by female and male life expectancy at birth; education, measured by female and male expected years of schooling for children and female and male mean years of schooling for adults ages 25 years and older; and command over economic resources, measured by female and male estimated earned income.
    https://ourworldindata.org/grapher/gender-development-index?time=2020


    ### URBAN:
    https://ourworldindata.org/urbanization                  
    """)

