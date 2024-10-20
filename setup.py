from setuptools import setup, find_packages

setup(
    name="emotion_detection",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "emotion_detector=emotion_detection.emotion_detection:emotion_detector",
        ],
    },
    author="Ardit",
    author_email="ardit@example.com",
    description="A simple application for emotion detection using Watson NLP.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/xardit/oaqjp-final-project-emb-ai",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
