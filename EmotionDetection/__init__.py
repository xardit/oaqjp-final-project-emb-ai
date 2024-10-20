# emotion_detection/__init__.py

"""
Emotion Detection Package

This package provides functionality to detect emotions in text using
the Watson NLP API. You can use the `emotion_detector` function to
analyze text for various emotions.
"""

from .emotion_detection import emotion_detector

__all__ = ["emotion_detector"]
