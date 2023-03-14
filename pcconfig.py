import pynecone as pc


config = pc.Config(
    app_name="voice_reader",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    frontend_packages=[
        "react-speech",
    ],
)
