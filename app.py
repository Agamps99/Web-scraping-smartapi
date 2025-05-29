import streamlit as st
from scraper import scrape_remoteok_jobs

st.title("🔍 Remote Job Listings (Scraped Live!)")
st.write("Showing remote jobs scraped from remoteok.com")

jobs = scrape_remoteok_jobs()

if not jobs:
    st.error("No jobs found.")
else:
    for job in jobs:
        st.subheader(job['title'])
        st.write(f"**Company:** {job['company']}")
        st.markdown(f"[🌐 View Job Posting]({job['link']})")
        st.markdown("---")
