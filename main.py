import streamlit as st
from classifier import Classifier
from PIL import Image


def print_results():
    preds = classifier.get_result(user_input)
    if preds[0] > preds[1]:
        info_text = "We are **" + str(int(preds[0] * 100)) + "%** sure that it's real headline"
        st.info(info_text)
    else:
        info_text = "We are **" + str(int(preds[1] * 100)) + "%** sure that it's fake headline"
        st.info(info_text)
        

if __name__ == "__main__":
    classifier = Classifier()
    st.set_page_config("Fake News Detector")
    st.image(Image.open('logo-website.png'), use_column_width=True)
    st.title('Fake News Detector \U0001F4F0')
    user_input = st.text_area("Input your headline here (russian, please!)")
    if st.button("Check it!"):
        print_results()

    with st.expander("Want to know more?"):
        st.markdown('Dataset was taken from SKB Kontur internship test task')
        st.write('It consists of 5758 news headlines marked as fake (1) and real (0)')

