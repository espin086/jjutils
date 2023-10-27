import streamlit as st

class StreamlitAppBuilder:
    def __init__(self, app_title='Streamlit App'):
        self.app_title = app_title

    def set_title(self, title):
        st.title(title)

    def set_subtitle(self, subtitle):
        st.subheader(subtitle)

    def set_text(self, text):
        st.write(text)

    def create_input(self, label, input_type='text', default_value=None):
        if input_type == 'text':
            return st.text_input(label, default_value)
        elif input_type == 'number':
            return st.number_input(label, value=default_value)
        elif input_type == 'slider':
            return st.slider(label, min_value=0, max_value=100, value=default_value)
        elif input_type == 'selectbox':
            options = st.selectbox(label, options=default_value)
            return options

    def create_button(self, label, key=None):
        return st.button(label, key=key)

    def create_checkbox(self, label, default_value=False):
        return st.checkbox(label, value=default_value)

    def create_radio_buttons(self, label, options, default_value=None):
        return st.radio(label, options, index=default_value)

    def create_selectbox(self, label, options, default_value=None):
        return st.selectbox(label, options, index=default_value)

    def create_multiselect(self, label, options, default_values=None):
        return st.multiselect(label, options, default=default_values)

    def create_file_uploader(self, label):
        return st.file_uploader(label)

    def create_dataframe(self, dataframe):
        st.dataframe(dataframe)

    def create_plot(self, plot_func):
        plot_func()

    def create_image(self, image, caption=None):
        st.image(image, caption=caption)

    def create_expander(self, label):
        return st.expander(label)

    def create_columns(self, num_columns):
        return st.columns(num_columns)

    def create_sidebar(self, content_func):
        st.sidebar.title("Sidebar")
        content_func()

    def run(self):
        st.set_page_config(page_title=self.app_title)
        self.create_sidebar(self._sidebar)
        self._main()

    def _sidebar(self):
        # Define the app's sidebar content here
        pass

    def _main(self):
        # Define the main content of the app here
        pass