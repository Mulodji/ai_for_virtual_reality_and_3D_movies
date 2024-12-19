import streamlit as st

def main():
    st.set_page_config(
        page_title="Aplicações práticas de IA: VR & Animações 3D",
        layout="wide"
    )

    # Custom CSS for styling (from the previous css)
    st.markdown("""
        <style>
            body {
                font-family: sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                min-height: 100vh;
                background-color: #f4f4f4;
                color: #333;
            }

            header {
                background-color: #2c3e50;
                color: white;
                text-align: center;
                padding: 1.5em 0;
            }

            header h1 {
                font-size: 1.8em;
                margin: 0;
                font-weight: bold;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            }

            main {
                flex: 1;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 1.5em;
            }

           .video-card {
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
                overflow: hidden;
                width: 95%;
                max-width: 100%;
                cursor: pointer;
            }

            .mosaic {
                display: grid;
                grid-template-columns: 1fr;
                gap: 2px;
                padding: 2px;
            }

           .thumb-container {
                overflow: hidden;
                position: relative;
            }

            .thumbnail {
                display: block;
                width: 100%;
                height: auto;
                transition: transform 0.3s ease;
                cursor: pointer;
            }

            .thumb-container:hover .thumbnail {
                transform: scale(1.05);
            }


            .carousel-container {
                position: relative;
                padding-bottom: 56.25%;
                overflow: hidden;
                display: none;
            }

            .carousel-container video {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                object-fit: cover;
            }

            footer {
                background-color: #34495e;
                color: white;
                text-align: center;
                padding: 1em 0;
            }

            footer a {
                color: #f39c12;
                text-decoration: none;
            }

            footer a:hover {
                text-decoration: underline;
            }

            @media (min-width: 768px) {
                header h1 {
                    font-size: 2.5em;
                }

                main {
                     padding: 2em;
                }

               .video-card {
                     width: 90%;
                     max-width: 800px;
                }

               .mosaic {
                    grid-template-columns: repeat(2, 1fr);
                }
             }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("<header><h1>Aplicações práticas de IA: VR & Animações 3D</h1></header>", unsafe_allow_html=True)

    # Video Mosaic
    video_files = ["video1.mp4", "video2.mp4", "video3.mp4", "video4.mp4"]
    thumb_files = ["thumb1.jpg", "thumb2.jpg", "thumb3.jpg", "thumb4.jpg"]

    #Carousel State
    if 'current_video_index' not in st.session_state:
       st.session_state.current_video_index = 0
    if 'is_playing' not in st.session_state:
       st.session_state.is_playing = False
    if 'interval' not in st.session_state:
       st.session_state.interval = None


    def play_carousel():
        if not st.session_state.is_playing:
            st.session_state.is_playing = True
            st.session_state.interval = st.session_state.current_video_index + 1
        else:
            st.session_state.is_playing = False
            st.session_state.interval = None


    with st.container():
        st.markdown('<div class="video-card" id="videoCard">', unsafe_allow_html=True)

        with st.container():
            st.markdown('<div class="mosaic">', unsafe_allow_html=True)
            for idx, (thumb, video) in enumerate(zip(thumb_files, video_files)):
              st.markdown(f'<div class="thumb-container" data-video="{video}"><img src="{thumb}" alt="Thumbnail {idx+1}" class="thumbnail"></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # Carousel container
        if st.session_state.is_playing:
            st.markdown('<div class="carousel-container" id="carouselContainer" style="display: block;">', unsafe_allow_html=True)
            st.video(video_files[st.session_state.current_video_index], controls = True)
            st.markdown('</div>', unsafe_allow_html=True)
            if st.session_state.interval is not None:
                if st.session_state.interval > len(video_files)-1:
                      st.session_state.current_video_index = 0;
                else:
                     st.session_state.current_video_index = st.session_state.interval
            else:
                 st.session_state.current_video_index = 0;

        else:
             st.markdown('<div class="carousel-container" id="carouselContainer" style="display: none;">', unsafe_allow_html=True)
             st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)



    # Footer
    st.markdown("""
        <footer>
            <p>Inscreve-te Já! WhatsApp: +244-953186182, Facebook: <a href="https://www.facebook.com/ticnes">https://www.facebook.com/ticnes</a></p>
        </footer>
    """, unsafe_allow_html=True)

    st.button("Play Carousel", on_click=play_carousel)


if __name__ == "__main__":
    main()