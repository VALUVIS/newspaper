import streamlit as st
from newspaper import Article
import nltk

nltk.download("punkt_tab")


def main():
    st.title("Valuvis News Article Extractor")

    # Input for the user to enter the article URL
    url = st.text_input("Enter a news URL:")

    if st.button("Extract"):
        if url:
            # Create an Article object
            article = Article(url)
            try:
                # Download and parse the article
                article.download()
                article.parse()

                # Display basic metadata
                st.subheader("Title")
                st.write(article.title)

                st.subheader("Authors")
                st.write(article.authors)

                st.subheader("Publication Date")
                st.write(article.publish_date)

                st.subheader("Top Image")
                if article.top_image:
                    st.image(article.top_image, width=600)
                else:
                    st.write("No top image found.")

                st.subheader("Article Text")
                st.write(article.text)

                # Perform NLP (keyword extraction, summary, etc.)
                article.nlp()

                st.subheader("Keywords")
                st.write(article.keywords)

                st.subheader("Summary")
                st.write(article.summary)

            except Exception as e:
                st.error(f"An error occurred while processing the article: {str(e)}")
        else:
            st.warning("Please enter a valid URL.")


if __name__ == "__main__":
    main()
