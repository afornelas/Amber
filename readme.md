# Amber

Amber is a voice assistant written almost entirely in python, with the goal of being able to create a fully fledged voice assistant that runs entirely locally on any device without a network. Amber is able to easily expanded through python modules that "plug-in" to their natural language processor to provide more functionality.

## Features

Amber is a expandable voice assistant that leverages open source technologies in order to fulfill its functions.

Amber's core feature set includes:

- Modular expandable natural language processing and intention recognition
- Hot word detection ("Hey Amber", or alternatively "Computer")
- Local speech recognition and transcription

Through modules, Amber's functionality grows to be far more useful, some current working modules are:

- Weather
- Scientific Calculator
- Media Controls

With many more in the works as it makes sense to implement in my life. In the future I hope to implement:

- Deep music player integration with YouTube Music and Spotify
- Deep Windows integration
- Traditional assistant features
  - Reminders, Timers, Search Engine fall back, personality quirks
- Calendar integration
- Context aware responses

## Requirements

As I've written the majority of the program, Amber does not have many requirements outside of a valid python installation.

However, voice recognition is handled through the [VOSK open source speech recognition API](https://alphacephei.com/vosk/)

You can install it in most python installations through the following:

```python
pip3 install vosk
```

Individual modules can be toggled on and off, and while most are functional off of the python standard library, some leverage other libraries (For example the media module relies on the Windows RunTime in order to read the song name and pause music globally).

## Background

Amber is a voice assistant that I've worked on and off for years now (Since June 29, 2019). Back then, I had ambitions to create an entire smart home ecosystem that worked together to make my digital life easier. I thought to myself then, if Big Tech could create a voice assistant with millions of dollars of funding and multiple years of work, what was stopping me? Admittedly, I may have been over my head, but if theres one thing I do great, it's persevere and grow. As such, I've been able to create great things across many different fields.
